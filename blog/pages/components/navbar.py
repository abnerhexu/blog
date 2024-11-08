import reflex as rx

from ..info import blog_name

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.text(
                        blog_name, size="4", weight="medium", font_family="InterVariable"
                    ),
                    align_items="center",
                ),
                # rx.hstack(
                #     navbar_link("Home", "/#"),
                #     navbar_link("Projects", "/#"),
                #     navbar_link("Links", "/#"),
                #     justify="end",
                #     spacing="5",
                # ),
                justify="between",
                align_items="center",
            ),
        ),
        # rx.mobile_and_tablet(
        #     rx.hstack(
        #         rx.hstack(
        #             rx.text(
        #                 blog_name, size="4", weight="medium"
        #             ),
        #             align_items="center",
        #         ),
        #         rx.menu.root(
        #             rx.menu.trigger(
        #                 rx.icon("menu", size=30)
        #             ),
        #             rx.menu.content(
        #                 rx.menu.item("Home"),
        #                 rx.menu.item("Projects"),
        #                 rx.menu.item("Links"),
        #             ),
        #             justify="end",
        #         ),
        #         justify="between",
        #         align_items="center",
        #     ),
        # ),
        # bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )