import reflex as rx
from .components.sidebar import generate_sidebar_category
from .components.navbar import navbar
from .components.footer import footer

network_intro = """
Shaheway education and research network is a network under construction.
- AS number: 215526
"""
def network_info() -> rx.Component:
    return rx.vstack(
        rx.heading("SERN", font_family="InterVariable"),
        rx.markdown(network_intro, font_family="InterVariable")
    )


@rx.page(route="/shahe-network", title="Shaheway education and research network | Abnerhexu's Blog")
def network_page() -> rx.Component:
    return rx.container(
        rx.vstack(
            navbar(),
            rx.color_mode.button(position="top-right"),
            rx.button(rx.hstack(rx.icon("arrow-left"), rx.text("Back", font_family="InterVariable")), variant="ghost", on_click=rx.redirect("/"), size="4"),
            rx.desktop_only(
                rx.hstack(
                    rx.box(rx.vstack(
                        network_info(),
                    ), width="80%"),
                    rx.vstack(rx.heading("Table of contents", size="4", font_family="InterVariable"), generate_sidebar_category(["Introduction"]), width="30%")
                )
            ),
            rx.mobile_and_tablet(
                    rx.box(
                       rx.vstack(
                        network_info()
                    ), width="100%"),
                    spacing="2em"
            ),
            rx.spacer(spacing="5"),
            footer(),
            ),
        spacing="5em",
        min_height="85vh",
    )