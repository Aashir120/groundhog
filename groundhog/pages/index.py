"""Home page: header + projects table."""

from __future__ import annotations

import reflex as rx

from ..components.header import header
from ..components.projects_table import projects_table


def index() -> rx.Component:
    return rx.vstack(
        header(),
        projects_table(),
        width="100%",
        spacing="0",
    )
