"""Modal for creating a new project (name -> Create)."""

from __future__ import annotations

import reflex as rx

from ..states.project_list import ProjectListState


def new_project_modal() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("New project"),
            rx.input(
                placeholder="Project name",
                value=ProjectListState.new_project_name,
                on_change=ProjectListState.set_new_project_name,
                width="100%",
                auto_focus=True,
            ),
            rx.cond(
                ProjectListState.error != "",
                rx.text(ProjectListState.error, color="red", size="2", margin_top="0.5em"),
            ),
            rx.flex(
                rx.dialog.close(rx.button("Cancel", variant="soft", color_scheme="gray")),
                rx.button("Create", on_click=ProjectListState.create_project),
                spacing="3",
                justify="end",
                margin_top="1.5em",
            ),
        ),
        open=ProjectListState.show_new_project_modal,
        on_open_change=ProjectListState.set_new_project_modal_open,
    )
