# 🦦 Groundhog

Data science meta-harness application for agentic experimentation loops.

**The problem**: Solving data science problems often requires many iterations
 of experimentation. Each loop learning from the results of previous iterations.
 These problems are not solved by simply describing a problem and designing
 an appropriate solution.

This project implements a meta-harness for using AI coding agents to perform
those experiments. You define the problem through a dataset, required metric
to optimise and an appropriate testing strategy. Then the groundhog meta-harness
allows you to point one (or more) coding agents at the problem. Each new iteration
can access the previous experimental notes and results to devise an improved approach.




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

* Create a project
* Load a dataset
* Specify your target variable
* Choose a train/test strategy.
* Then start you experiment
 
The AI coding agent runs independent loops of experimentation.
Each loop reflects on previous experiments and results before devising the
next approach.


