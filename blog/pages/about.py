import reflex as rx

from .components.navbar import navbar
from .components.sidebar import generate_sidebar_category
poem = """
涉水阔波出四江，山高峻险势难量。
有识乾坤物堪大，仍怜世间草木青。
"""

hobby = """
- **Coding**: Python (for casual work including this website using [Reflex](https://reflex.dev/)), C (System programming), Chisel (Writing hardwares). Know a little Rust though I do not very like it.
- **Reading**: Books about philosophy, history, and science. Recommend *Du contrat social ou Principes du droit politique*, *Journey to the west*, *Siddhartha*.
- **Running**: Passing 5km in 22min30s is just enough :).
- **Music**: Chinese folk music.
- **Game**: *Black Myth: Wukong*, *Forza Horizon 5*.
"""

friends = [
    ["CGH0S7's Blog", "https://blog.hifuu.ink", "Geek in NUDT"],
    ["Wingrew", "https://wingrew.com", "OS lover"]
]
def poem_content() -> rx.Component:
    return rx.vstack(
        rx.heading("Poem"),
        rx.markdown(poem)
    )

def hobby_content() -> rx.Component:
    return rx.vstack(
        rx.heading("Hobby"),
        rx.markdown(hobby)
    )

def friends_content() -> rx.Component:
    return rx.vstack(
        rx.desktop_only(
            rx.vstack(
                rx.heading("Friends"),
                rx.grid(
                    rx.foreach(friends, lambda v: rx.card(rx.vstack(rx.text(v[0]), rx.text(v[2]), rx.link("go", href=v[1])))),
                    columns="4"
                )
            )
        ),
        rx.mobile_and_tablet(
            rx.heading("Friends"),
                rx.grid(
                    rx.foreach(friends, lambda v: rx.card(rx.vstack(rx.text(v[0]), rx.text(v[2]), rx.link("go", href=v[1])), size="2")),
                    columns="2"
                )
        )
        )

@rx.page(route="/about", title="About me | Abnerhexu's Blog")
def about_page() -> rx.Component:
    return rx.container(
        rx.vstack(
            navbar(),
            rx.color_mode.button(position="top-right"),
            rx.button(rx.hstack(rx.icon("arrow-left"), rx.text("Back")), variant="ghost", on_click=rx.redirect("/"), size="4"),
            rx.desktop_only(
                rx.hstack(
                    rx.box(rx.vstack(
                        poem_content(),
                        hobby_content(),
                        friends_content(),
                    ), width="80%"),
                    rx.vstack(rx.heading("Table of contents", size="4"), generate_sidebar_category(["Poem", "Hobby", "Friends"]), width="20%")
                )
            ),
            rx.mobile_and_tablet(
                rx.vstack(
                    rx.box(rx.vstack(rx.heading("Table of contents", size="4"), generate_sidebar_category(["Poem", "Hobby", "Friends"]), width="100%"),),
                    rx.box(
                       rx.vstack(
                        poem_content(),
                        hobby_content(),
                        friends_content(),
                    ), width="100%"),
                    spacing="2em"
                )
            )
        ),
        spacing="5em"
    )