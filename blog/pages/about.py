import reflex as rx

from .components.navbar import navbar
from .components.sidebar import generate_sidebar_category
poem = """

旧游无处不堪寻，洛阳花落又逢君。
"""

hobby = """
- **Coding**: Python (for casual work including this website using [Reflex](https://reflex.dev/)), C (System programming), Chisel (Writing hardwares). Know a little Rust though I do not very like it.
- **Reading**: Books about philosophy, history, and science. Recommend *Du contrat social ou Principes du droit politique*, *Journey to the west*, *Siddhartha*.
- **Running**: Passing 5km in 22min30s is just enough :).
- **Music**: Chinese folk music.
- **Game**: *Black Myth: Wukong*, *Forza Horizon 5*.
"""

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

@rx.page(route="/about", title="About me | Abnerhexu's Blog")
def about_page() -> rx.Component:
    return rx.container(
        rx.vstack(
            navbar(),
            rx.color_mode.button(position="top-right"),
            rx.button(rx.hstack(rx.icon("arrow-left"), rx.text("Back")), variant="ghost", on_click=rx.redirect("/"), size="4"),
            rx.hstack(
                rx.box(rx.vstack(
                    poem_content(),
                    hobby_content()
                ), width="80%"),
                rx.vstack(rx.heading("Table of contents", size="4"), generate_sidebar_category(["Poem", "Hobby"]), width="20%")
            ),
        ),
        spacing="5em"
    )