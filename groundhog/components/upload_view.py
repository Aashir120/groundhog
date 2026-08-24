"""Project page, stage 1: upload a dataset."""

from __future__ import annotations

import reflex as rx

from ..states.project_detail import ProjectState


def upload_view() -> rx.Component:
    return rx.vstack(
        rx.heading("Upload a dataset", size="6"),
        rx.text(
            "Upload the data file for this project. It will be stored in "
            "the project's data directory.",
            color="gray",
        ),
        rx.upload(
            rx.vstack(
                rx.icon("upload", size=28),
                rx.text("Drag and drop a CSV file here, or click to browse"),
                rx.foreach(rx.selected_files("dataset"), rx.text),
                align="center",
                spacing="2",
                padding="2em",
            ),
            id="dataset",
            accept={"text/csv": [".csv"]},
            max_files=1,
            border="1px dashed var(--gray-8)",
            border_radius="0.5em",
            width="100%",
        ),
        rx.button(
            "Upload",
            on_click=ProjectState.handle_upload(rx.upload_files(upload_id="dataset")),
            margin_top="1em",
        ),
        width="100%",
        max_width="640px",
        margin="0 auto",
        padding="2em 1.5em",
        spacing="4",
    )
