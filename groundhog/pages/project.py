"""Project detail page, route /project/[name]."""

from __future__ import annotations

import reflex as rx

from ..components.analysis_view import analysis_view
from ..components.configure_view import configure_view
from ..components.header import header
from ..components.summary_view import summary_view
from ..components.upload_view import upload_view
from ..states.project_detail import ProjectState


def project() -> rx.Component:
    return rx.vstack(
        header(),
        rx.match(
            ProjectState.stage,
            ("upload", upload_view()),
            ("configure", configure_view()),
            ("analysis", analysis_view()),
            ("summary", summary_view()),
            ("not_found", rx.center(
                rx.text("Project not found.", color="gray"),
                padding="4em",
            )),
            rx.center(rx.spinner(), padding="4em"),
        ),
        width="100%",
        spacing="0",
        on_mount=ProjectState.load_project,
    )
