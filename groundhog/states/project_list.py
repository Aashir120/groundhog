"""State for the home page: the projects table and the New Project modal."""

from __future__ import annotations

import pydantic
import reflex as rx

from ..lib import fs


class ProjectRow(pydantic.BaseModel):
    name: str
    experiment_count: int
    top_result: str


class ProjectListState(rx.State):
    projects: list[ProjectRow] = []

    show_new_project_modal: bool = False
    new_project_name: str = ""
    error: str = ""

    @rx.event
    def load_projects(self):
        rows = []
        for name in fs.list_project_names():
            meta = fs.read_metadata(name)
            results = fs.parse_results(name)
            rows.append(
                ProjectRow(
                    name=name,
                    experiment_count=len(fs.list_experiments(name)),
                    top_result=fs.top_result(
                        name, meta.get("eval_metric") if meta else None, results
                    ),
                )
            )
        self.projects = rows

    @rx.event
    def open_new_project_modal(self):
        self.new_project_name = ""
        self.error = ""
        self.show_new_project_modal = True

    @rx.event
    def set_new_project_modal_open(self, value: bool):
        self.show_new_project_modal = value

    @rx.event
    def set_new_project_name(self, value: str):
        self.new_project_name = value

    @rx.event
    def create_project(self):
        try:
            slug = fs.create_project(self.new_project_name)
        except ValueError as exc:
            self.error = str(exc)
            return None
        self.show_new_project_modal = False
        return rx.redirect(f"/project/{slug}")
