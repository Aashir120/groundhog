<!-- reflex managed begin (do not edit inside this block; add custom content outside the markers) -->
# Agents

This project uses the **Reflex agent skills** — up-to-date knowledge for building full-stack Python web apps with [Reflex](https://reflex.dev). Install them first, then use them as described below.

## Installing the Skills

Before working on this project, make sure the Reflex skills are available to you.

### Claude Code

If the skills are not already available, install them yourself by running these shell commands:

```bash
claude plugin marketplace add reflex-dev/agent-skills
claude plugin install reflex@reflex-agent-skills
```

Newly installed plugins load on the next session. After installing, tell the user to restart the session so the skills auto-load; until then, read the skill files directly from `~/.claude/plugins/` when you need them.

### Other agents (Cursor, OpenCode, Codex, Pi)

```
npx skills add reflex-dev/agent-skills
```

Or clone https://github.com/reflex-dev/agent-skills and copy the `skills/` folders into your agent's skill directory (see the repo README for paths).

### Verifying

Before writing or editing any Reflex code, confirm these three skills are available: `reflex-docs`, `setup-python-env`, and `reflex-process-management`. If they are not, STOP and run the install step above — do not proceed without them.

## Using the Skills

### Reflex documentation

For anything about Reflex APIs — components, state management, events, styling, database, routing, authentication — use the **reflex-docs** skill rather than relying on memory. It carries current, version-accurate docs.

### Initializing a new Reflex project

When starting a new Reflex project or setting up a development environment, you **must** follow the **setup-python-env** skill before doing anything else.

Do not skip any steps. Do not assume a virtual environment or Reflex is already available — always verify first by following the skill's instructions in order.

After the environment is ready and Reflex is installed, run:

```bash
reflex init
```

Then proceed with the user's request.

### Managing a Reflex process

When you need to compile, run, reload, or debug a Reflex application, follow the **reflex-process-management** skill for the correct sequence and error investigation steps.
<!-- reflex managed end -->

## Experiment Agent Instructions

The section below is read by Groundhog itself (not by whoever develops the
Groundhog app) and passed as the prompt to the coding agent it launches for
each experiment loop. Your current working directory is one project's
directory: `projects/<project-name>/`.

You are running one iteration of an experimentation loop for a data science
project. Work entirely within the current directory. Do the following, in
order:

1. **Review prior work.** Read `metadata.json` (target variable, train/test
   strategy, evaluation metric). Read `RESULTS.md` for every result achieved
   so far. Read every `experiments/*/README.md` to see what approaches have
   already been tried and what was learned from each.

2. **Plan the next experiment.** Based on what has and hasn't worked so far,
   decide on one concrete, incremental experimental approach to try next
   (a model choice, feature engineering step, hyperparameter change,
   validation strategy, etc). Give it a short, descriptive, filesystem-safe
   name (lowercase, hyphen-separated, e.g. `gradient-boosting-baseline`).

3. **Set up the experiment directory.** Create `experiments/<name>/`.
   Before writing any code, write `experiments/<name>/README.md` documenting:
   - The approach and the reasoning behind trying it now.
   - What prior result (if any) it is trying to improve on.
   - How it will be evaluated (using the metric and split strategy from
     `metadata.json`).

4. **Implement and run the experiment.** Write the experiment code inside
   `experiments/<name>/`, using the dataset in `data/` and respecting the
   target variable, train/test split, and evaluation metric defined in
   `metadata.json`. Execute it.

5. **Record the result.** Append one row to the table in `RESULTS.md`
   (create the row in the same `| Experiment | Date | Metric | Value | Notes |`
   format as the existing rows) with the experiment name, today's date, the
   metric name, the achieved value, and a one-line note. Do this before you
   finish, even if the experiment's result is worse than prior experiments —
   a negative result is still a result.

Do not modify `data/`, `metadata.json`, or any other project's directory.
Do not rewrite history in `RESULTS.md` — only append.
