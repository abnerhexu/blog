import reflex as rx

class ConfigureState(rx.State):
    configured: bool = False

class FormInputState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        for key, value in form_data.items():
            self.form_data[key] = value

@rx.page(route="/welcome", title="Welcome to a new blog!")
def welcome_page():
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to installation page!", size="9"),
            rx.text(
                "Before we get started, we need some information...",
                size="5",
            ),
            rx.form.root(
                rx.vstack(
                    rx.hstack(rx.text("Blog name"), rx.input(
                        name="blog_name",
                        placeholder="Blog name",
                        type="text",
                        required=True,
                    ), justify="center"),
                    rx.hstack(rx.text("Profiler name"), rx.input(
                        name="profiler_name",
                        placeholder="Profiler name",
                        type="text",
                        required=True,
                    ),),
                    rx.hstack(rx.text("profiler location"), rx.input(
                        name="profiler_location",
                        placeholder="Profiler location",
                        type="text",
                        required=True,
                    ),),
                    rx.hstack(rx.text("Profiler GitHub"), rx.input(
                        name="profiler_github",
                        placeholder="Profiler github",
                        type="text",
                        required=True,
                    ),),
                    rx.hstack(rx.text("Profiler role"), rx.input(
                        name="profiler_role",
                        placeholder="Profiler role",
                        type="text",
                        required=True,
                    ),),
                    rx.hstack(rx.text("Profiler introduction"), rx.input(
                        name="profiler_introduction",
                        placeholder="Profiler introduction",
                        type="text",
                        required=True,
                    ),),
                    rx.button("Confirm", type="submit"),
                    width="100%",
                ),
                on_submit=FormInputState.handle_submit,
                reset_on_submit=True,
            ),
            rx.form.root(
                
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

