import reflex as rx

class ConfigureState(rx.State):
    configured: bool = False


@rx.page(route="/welcome", title="Welcome blog installation!")
def welcome_page():
    return rx.container(
        rx.vstack(
            rx.heading("Welcome!")
        ),
    )