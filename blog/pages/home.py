import reflex as rx

from .components.navbar import navbar
from .components.clientip import display_user_ip
from .components.footer import footer

from .info import blog_name, profiler_name, profiler_location, profiler_github, profiler_role, profiler_introduction, profiler_education, profiler_certifications, profile_image, font_family

def display_posts() -> rx.Component:
    return rx.container(
        rx.card(
            rx.link(
                rx.vstack(
                    rx.blockquote("November 7, 2024", color_scheme="green", font_family="InterVariable"),
                    rx.vstack(
                        rx.heading("Hello, world!", size="4", font_family="InterVariable"),
                        rx.markdown("I built this site using reflex.", font_family="InterVariable"),
                        spacing="-2em"
                    ),
                    spacing="1em"
                ),
            href="", underline="none", size="3", color="black", color_scheme="gray"
            ),
            variant="ghost",
            as_child=True
        )
    )

@rx.page(route="/", title="Abnerhexu | Blog")
def home_page() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),
        rx.color_mode.button(position="top-right"),
        # display_user_ip(),
        rx.desktop_only(rx.vstack(
            rx.vstack(
            rx.flex(
                rx.image(
                    src=profile_image,
                    width="120px",
                    height="auto",
                    border_radius="60px 60px",
                    # border="5px solid #555",
                ), justify="center", align="center"),
            rx.heading(profiler_name, font_family="InterVariable"),
            rx.hstack(
                rx.flex(rx.icon("navigation"), rx.text(profiler_location, font_family="InterVariable")),
                rx.flex(rx.icon("github"), rx.link(rx.text("GitHub", font_family="InterVariable"), href="https://github.com/"+profiler_github)),
                spacing="5em",
                justify="center"
            ),
            justify="center",
            spacing="2em",
            align="center"
        ),
        rx.vstack(
            rx.hstack(
                rx.box(rx.heading("Introduction", font_family="InterVariable"), width="20%"),
                rx.box(
                    rx.vstack(
                        rx.text(profiler_role, font_family="InterVariable"), 
                        rx.text(profiler_introduction, font_family="InterVariable"), 
                        rx.hstack(rx.button(rx.hstack(rx.text("Read more", font_family="InterVariable"), rx.icon("arrow-right")), size="2", variant="ghost", color_scheme="blue", on_click=rx.redirect("/about")), justify="center")),
                    width="80%"
                ),
                columns="2", spacing="2em", justify="between", flow="row"
            ),
            rx.hstack(
                rx.box(rx.heading("Education", font_family="InterVariable"), width="20%"), 
                rx.box(rx.box(
                    rx.vstack(
                        rx.foreach(profiler_education, lambda e: rx.flex(
                            rx.box(
                                rx.vstack(
                                    rx.text(rx.text.strong(e["unit"]), ", "+e["loc"], font_family="InterVariable"),
                                    rx.text(e["degree"], font_family="InterVariable")
                                ),
                                width="70%"), 
                            rx.box(
                                rx.text(e["year"], font_family="InterVariable"),
                                width="20%"), 
                            rx.box(
                                rx.image(e["logo"]),
                                width="10%")))
                    ),
                ), width="80%"), 
                columns="2", spacing="2em", justify="between", flow="row"
            ),
            rx.hstack(
                rx.box(rx.heading("Certifications", font_family="InterVariable"), width="20%"), 
                rx.box(
                    rx.vstack(
                        rx.foreach(profiler_certifications, lambda e: rx.vstack(
                            rx.text(rx.text.strong(e["title"]), ", by "+e["from"], font_family="InterVariable"),
                            rx.text(e["year"], font_family="InterVariable"),
                            direction="column",
                            spacing="0em"
                            )
                        ),
                ), width="80%"), 
                columns="2", spacing="2em", justify="between", flow="row", width="100%"
            ),
            rx.hstack(
                rx.box(rx.heading("Posts", font_family="InterVariable"), width="20%"), 
                rx.box(
                    display_posts(), width="80%"), 
                columns="2", spacing="2em", justify="between", flow="row", width="100%"
            ),
            spacing="5",
            justify="top",
            min_height="85vh",
        ), spacing="5em", align="center"),
        ),
        rx.mobile_and_tablet(
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
            rx.heading(profiler_name),
            rx.hstack(
                rx.flex(rx.icon("navigation"), rx.text(profiler_location)),
                rx.flex(rx.icon("github"), rx.link(rx.text("GitHub"), href="https://github.com/"+profiler_github, underline="none")),
                spacing="5em",
                justify="center"
            ),
            justify="center",
            spacing="2em",
            align="center"
        ),
        rx.vstack(
            rx.vstack(
                rx.box(rx.heading("Introduction")),
                rx.box(
                    rx.vstack(
                        rx.text(profiler_role), 
                        rx.text(profiler_introduction), 
                        rx.hstack(rx.button(rx.hstack(rx.text("Read more"), rx.icon("arrow-right")), size="2", variant="ghost", color_scheme="blue", on_click=rx.redirect("/about")), justify="center"))
                ),
                spacing="2em", justify="between", flow="row"
            ),
            rx.vstack(
                rx.box(rx.heading("Education")), 
                rx.box(rx.box(
                    rx.vstack(
                        rx.foreach(profiler_education, lambda e: rx.flex(
                            rx.box(
                                rx.vstack(
                                    rx.text(rx.text.strong(e["unit"]), ", "+e["loc"]),
                                    rx.text(e["degree"])
                                )), 
                            rx.box(
                                rx.text(e["year"])), 
                            rx.box(
                                rx.image(e["logo"], width="10%")), direction="column"))
                    ),
                )), 
                spacing="2em", justify="between", flow="row"
            ),
            rx.vstack(
                rx.box(rx.heading("Certifications")), 
                rx.box(
                    rx.vstack(
                        rx.foreach(profiler_certifications, lambda e: rx.vstack(
                            rx.text(rx.text.strong(e["title"]), ", by "+e["from"]),
                            rx.text(e["year"]),
                            direction="column",
                            spacing="0em"
                            )
                        ),
                ),), 
                spacing="2em", justify="between", flow="row", width="100%"
            ),
            rx.vstack(
                rx.box(rx.heading("Posts", font_family="InterVariable")), 
                rx.box(
                    display_posts(),), 
                spacing="2em", justify="between", flow="row", width="100%"
            ),
            spacing="5",
            justify="top",
            min_height="85vh",
        ), spacing="5em", align="center")
        ),
        footer()
    )