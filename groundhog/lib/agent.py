"""Launches the configured coding agent to run one experiment loop.

Currently the only supported agent is Claude Code, invoked headlessly via
its CLI with the project directory as the working directory so it only
ever sees (and touches) that one project's files.
"""

from __future__ import annotations

import asyncio
import os
from collections.abc import AsyncIterator

from . import fs

CLAUDE_COMMAND = "claude"

# Env vars that make the Claude Code CLI authenticate with API-key billing
# instead of the user's claude.ai subscription login. Stripped from the
# subprocess environment so experiment runs always use the subscription,
# regardless of what's set in the parent process (e.g. a developer's shell).
AUTH_ENV_VARS_TO_STRIP = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN")


class AgentRunError(Exception):
    """Raised when the coding agent process exits with a non-zero status."""


def _build_prompt() -> str:
    instructions = fs.experiment_agent_instructions()
    return (
        "Follow the instructions below to run the next experiment for this "
        "data science project. The current working directory is the project "
        "directory.\n\n"
        f"{instructions}"
    )


def _subprocess_env() -> dict[str, str]:
    env = dict(os.environ)
    for var in AUTH_ENV_VARS_TO_STRIP:
        env.pop(var, None)
    return env


async def run_experiment(project_name: str) -> AsyncIterator[str]:
    """Run Claude Code in ``projects/<project_name>`` and stream its output.

    Yields decoded output lines as they are produced. Raises AgentRunError
    if the process exits non-zero, or FileNotFoundError if the CLI isn't
    installed.
    """
    cwd = fs.project_dir(project_name)
    proc = await asyncio.create_subprocess_exec(
        CLAUDE_COMMAND,
        "-p",
        _build_prompt(),
        "--dangerously-skip-permissions",
        cwd=cwd,
        env=_subprocess_env(),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    )
    assert proc.stdout is not None
    async for raw_line in proc.stdout:
        yield raw_line.decode("utf-8", errors="replace").rstrip()
    returncode = await proc.wait()
    if returncode != 0:
        raise AgentRunError(f"Claude Code exited with status {returncode}")
