import reflex as rx

def generate_sidebar_item(section: str, href="") -> rx.Component:
    return rx.box(
        rx.link(
            rx.text(section, font_family="InterVariable"),
            href=href,
            underline="none"
        ),
        width="100%"
    )

def generate_sidebar_category(
    components: list[str]
) -> rx.Component:
    return rx.vstack(
        rx.foreach(components, lambda e: rx.box(
        rx.text(e, font_family="InterVariable"),
        width="100%"
    ))
    )
