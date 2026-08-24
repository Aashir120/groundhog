"""Project page, stage 2: define target variable, split strategy, metric."""

from __future__ import annotations

import reflex as rx

from ..lib.fs import EVAL_METRICS, SPLIT_MODES
from ..states.project_detail import ProjectState


def configure_view() -> rx.Component:
    return rx.vstack(
        rx.heading("Configure project", size="6"),
        rx.text(
            f"{ProjectState.dataset_files.join(', ')} — "
            f"{ProjectState.record_count} records",
            color="gray",
        ),
        rx.vstack(
            rx.text("Target variable", weight="bold", size="2"),
            rx.select(
                ProjectState.column_names,
                value=ProjectState.target_variable,
                on_change=ProjectState.set_target_variable,
            ),
            align="start",
            width="100%",
        ),
        rx.vstack(
            rx.text("Train / test strategy", weight="bold", size="2"),
            rx.hstack(
                rx.select(
                    SPLIT_MODES,
                    value=ProjectState.split_mode,
                    on_change=ProjectState.set_split_mode,
                ),
                rx.input(
                    placeholder="e.g. 0.8, a column name, or 5 folds",
                    value=ProjectState.split_value,
                    on_change=ProjectState.set_split_value,
                ),
                width="100%",
            ),
            align="start",
            width="100%",
        ),
        rx.vstack(
            rx.text("Evaluation metric", weight="bold", size="2"),
            rx.select(
                EVAL_METRICS,
                value=ProjectState.eval_metric,
                on_change=ProjectState.set_eval_metric,
            ),
            align="start",
            width="100%",
        ),
        rx.cond(
            ProjectState.error != "",
            rx.text(ProjectState.error, color="red", size="2"),
        ),
        rx.button("Save & continue", on_click=ProjectState.save_metadata),
        width="100%",
        max_width="640px",
        margin="0 auto",
        padding="2em 1.5em",
        spacing="4",
    )
