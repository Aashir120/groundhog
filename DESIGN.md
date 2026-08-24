# Application Design

Opening the root of the application shows a header with name "🦦-Groundhog" on the left 
and a gear icon on the right. Clicking the gear icon opens a model window for changing 
the coding agent configuration: drop down menu with a single option: Claude Code. 

Below the head is the main application pane containing a list of projects in a table.

The header row contains:  Project Name, Experiments, Top Result

These values are drawn from a meta-data file inside each of the project subdirectories.
They are updated by the coding agents after each experiment. 
The Top Result column contains the best metric achieved (with metric name in brackets).

There should be a single button at the top right of the table called "New Project"

## New Project Flow
 
1. User clicks to create a new project
--- Modal dialogue asks for a project name.
--- User clicks Create
--- Application creates a project folder inside the `projects` directory
--- Also creates the required subdirectories: `data` `experiments`
--- Creates the empty RESULTS.md file inside the project directory
2. User is taken into the project page and asked to upload a dataset
--- Application stores the data inside `data` subdirectory of the project
3. User is asked to define the project details: target variable, train/test split, evaluation metric
--- Application stores these details inside a `metadata.json` file in the project directory
4. Project page displays a summary screen:
--- Name of uploaded dataset files and the total number of records
--- Table containing the metadata fields supplied:
---- Name of the target variable field and summary [data type, number of unique values]
---- Column used for train/test split, OR percentage of train test split, OR Number of cross validation folds
---- Name of evaluation metric: AUC, RMSE, MASE, MAPE
--- A button called "Start Experiment"
5. User clicks start experiment 
--- Application kicks off the configured coding agent to run the first experiment
--- Directions for these coding agents are defined in the file `AGENTS.md`
--- Each experiment should be written into a subdirectory of the `experiments` directory
--- Each experiments results should be appended to a table created inside the RESULTS.md file.
--- Each experiment should be documented inside a README.md file in the experiment directory.

## Configuration

By default the application should be set up to initiate a new Claude Code session 
for each experimental run. It should be instructed to read all of the previous experiments
and their results. Then to plan the next experiment. Give the new experiment a concise name,
created the required directories and plan the experimental approach, write the README file for
the experiment, implement it, execute it and write the results into the root RESULTS.md file
before finshing.


