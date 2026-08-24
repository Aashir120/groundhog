"""Project page, stage 3: run the data analysis before any experiments."""

from __future__ import annotations

import reflex as rx

from ..states.project_detail import ProjectState
from .run_log import run_log


def analysis_view() -> rx.Component:
    return rx.vstack(
        rx.heading("Analyse the data", size="6"),
        rx.text(
            f"{ProjectState.dataset_files.join(', ')} — "
            f"{ProjectState.record_count} records",
            color="gray",
        ),
        rx.text(
            "Before running experiments the agent explores the dataset once: "
            "variable distributions, missing values, the nature of the target "
            "variable and univariate relationships. It writes the findings to "
            "ANALYSIS.md, which every later experiment reads as reference.",
            margin_top="0.5em",
        ),
        rx.button(
            "Run Analysis",
            on_click=ProjectState.run_analysis,
            loading=ProjectState.is_running,
            disabled=ProjectState.is_running,
            margin_top="1em",
        ),
        run_log(),
        width="100%",
        max_width="840px",
        margin="0 auto",
        padding="2em 1.5em",
        spacing="2",
        align="start",
    )
