"""Groundhog: a data science experimentation platform for agentic looping."""

import reflex as rx

from .pages.index import index
from .pages.project import project

app = rx.App()

app.add_page(index, route="/")
app.add_page(project, route="/project/[name]")
