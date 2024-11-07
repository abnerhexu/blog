import reflex as rx


def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3", font_family="InterVariable"), href=href)


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "沙河小分队", size="4", weight="bold", as_="h3"
        ),
        footer_item("沙河教育和科研网", "/shahe-network"),
        footer_item("计算机系统导论", "https://ucomputing.shalicon.org"),
        footer_item("计算机体系结构课程网站", "https://computerarchitecture.shalicon.org"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            "资源", size="4", weight="bold", as_="h3"
        ),
        footer_item("Overleaf toolkit", "https://overleaf.hifuu.ink/login"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("tv", "https://space.bilibili.com/88239270"),
        spacing="3",
        justify="end",
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.image(
                            src="/logo.png",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                        ),
                        rx.heading(
                            "和子煦",
                            size="7",
                            weight="bold",
                        ),
                        align_items="center",
                    ),
                    rx.text(
                        "Last update: Nov. 2024",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        font_family="InterVariable"
                    ),
                    spacing="4",
                    align_items=[
                        "center",
                        "center",
                        "start",
                    ],
                ),
                footer_items_1(),
                footer_items_2(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    footer_item("网站可用性", "/#"),
                    spacing="4",
                    align="center",
                    width="100%",
                ),
                socials(),
                justify="between",
                width="100%",
            ),
            spacing="5",
            width="100%",
        ),
        width="100%",
    )