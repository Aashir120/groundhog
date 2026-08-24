"""Gear-icon settings modal: coding agent configuration."""

from __future__ import annotations

import reflex as rx

from ..states.settings import AGENT_OPTIONS, SettingsState


def settings_modal() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Settings"),
            rx.dialog.description(
                "Choose the coding agent used to run experiments.",
                margin_bottom="1em",
            ),
            rx.text("Coding agent", size="2", weight="bold", margin_bottom="0.25em"),
            rx.select(
                AGENT_OPTIONS,
                value=SettingsState.agent,
                on_change=SettingsState.set_agent,
            ),
            rx.flex(
                rx.dialog.close(rx.button("Done")),
                justify="end",
                margin_top="1.5em",
            ),
        ),
        open=SettingsState.show_settings,
        on_open_change=SettingsState.set_settings_open,
    )
