"""Global application settings (coding agent configuration)."""

from __future__ import annotations

import reflex as rx

AGENT_OPTIONS = ["Claude Code"]


class SettingsState(rx.State):
    show_settings: bool = False
    agent: str = AGENT_OPTIONS[0]

    @rx.event
    def toggle_settings(self):
        self.show_settings = not self.show_settings

    @rx.event
    def set_settings_open(self, value: bool):
        self.show_settings = value

    @rx.event
    def set_agent(self, value: str):
        self.agent = value
