import reflex as rx

class ClientIPState(rx.State):
    @rx.var
    def get_client_ip(self):
        return str(self.router.session.client_ip)

def display_user_ip() -> rx.Component:
    return rx.callout(
    rx.text("You are visiting from IP: ", ClientIPState.get_client_ip),
    icon="info",
)