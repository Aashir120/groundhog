# 🦦 Groundhog

Data science meta-harness application for agentic experimentation looping.

Load a dataset, define your target variable and train/test strategy.
Then launch your AI coding agent to run indepdent loops of experimentation.
Each loop reflects on previous experiments and results before devising the
next approach.

## Implementation

Created as a Reflex python web application and managed using the uv package manager.

Refer to the [Design](DESIGN.md) document for outline of the initial idea.

## Usage

For the current version you will need a Claude Code subscription. Log in
once with `claude /login` (or just run `claude` and follow the prompt) so
the `claude` CLI is authenticated against your claude.ai account — Groundhog
launches it headlessly using that login for every experiment run.

1. Install dependencies:
   ```
   uv sync
   ```
2. Start the app:
   ```
   uv run reflex run
   ```
3. Open http://localhost:3000 in your browser.


