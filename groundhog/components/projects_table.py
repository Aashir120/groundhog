"""Home page: the projects table + New Project button."""

from __future__ import annotations

import reflex as rx

from ..states.project_list import ProjectListState
from .new_project_modal import new_project_modal


def _row(project: rx.Var) -> rx.Component:
    return rx.table.row(
        rx.table.cell(
            rx.link(project.name, href=f"/project/{project.name}")
        ),
        rx.table.cell(project.experiment_count),
        rx.table.cell(project.top_result),
    )


def projects_table() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Projects", size="5"),
            rx.spacer(),
            rx.button(
                "New Project",
                on_click=ProjectListState.open_new_project_modal,
            ),
            width="100%",
            align="center",
        ),
        rx.cond(
            ProjectListState.projects.length() == 0,
            rx.text(
                "No projects yet. Click \"New Project\" to create one.",
                color="gray",
                margin_top="2em",
            ),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Project Name"),
                        rx.table.column_header_cell("Experiments"),
                        rx.table.column_header_cell("Top Result"),
                    ),
                ),
                rx.table.body(
                    rx.foreach(ProjectListState.projects, _row),
                ),
                width="100%",
                margin_top="1em",
            ),
        ),
        new_project_modal(),
        width="100%",
        max_width="960px",
        margin="0 auto",
        padding="2em 1.5em",
        on_mount=ProjectListState.load_projects,
    )
