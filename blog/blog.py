"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from .navbar import navbar

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.vstack(
            rx.flex(
                rx.image(
                    src="/profile.jpg",
                    width="120px",
                    height="auto",
                    border_radius="60px 60px",
                    # border="5px solid #555",
                ), justify="center", align="center"),
            rx.heading(config.profiler_name),
            rx.hstack(
                rx.flex(rx.icon("navigation"), rx.text(config.profiler_location)),
                rx.flex(rx.icon("github"), rx.link(rx.text("GitHub"), href="https://github.com/"+config.profiler_github)),
                spacing="5em",
                justify="center"
            ),
            justify="center",
            spacing="2em",
            align="center"
        ),
        rx.vstack(
            rx.hstack(
                rx.box(rx.heading("Introduction"), width="20%"),
                rx.box(
                    rx.vstack(
                        rx.text(config.profiler_role), 
                        rx.text(config.profiler_introduction), 
                        rx.hstack(rx.button(rx.hstack(rx.text("Read more"), rx.icon("arrow-right")), size="2", variant="surface", color_scheme="blue"), justify="center")),
                    width="80%"
                ),
                columns="2", spacing="2em", justify="between", flow="row"
            ),
            rx.hstack(
                rx.box(rx.heading("Education"), width="20%"), 
                rx.box(rx.box(
                    rx.vstack(
                        rx.foreach(config.profiler_education, lambda e: rx.flex(
                            rx.box(
                                rx.vstack(
                                    rx.text(rx.text.strong(e["unit"]), ", "+e["loc"]),
                                    rx.text(e["degree"])
                                ),
                                width="70%"), 
                            rx.box(
                                rx.text(e["year"]),
                                width="20%"), 
                            rx.box(
                                rx.image(e["logo"]),
                                width="10%")))
                    ),
                ), width="80%"), 
                columns="2", spacing="2em", justify="between", flow="row"
            ),
            rx.hstack(
                rx.box(rx.heading("Certifications"), width="20%"), 
                rx.box(
                    rx.vstack(
                        rx.foreach(config.profiler_certifications, lambda e: rx.vstack(
                            rx.text(rx.text.strong(e["title"]), ", by "+e["from"]),
                            rx.text(e["year"]),
                            direction="column",
                            spacing="0em"
                            )
                        ),
                ), width="80%"), 
                columns="2", spacing="2em", justify="between", flow="row", width="100%"
            ),
            spacing="5",
            justify="top",
            min_height="85vh",
        ), spacing="5em", align="center"
        )
    )


app = rx.App()
app.add_page(index)
