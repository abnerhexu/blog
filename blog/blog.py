import reflex as rx

from .pages.about import about_page
from .pages.home import home_page
from .intro.welcome import welcome_page
from .pages.network import network_page

app = rx.App(stylesheets = ["https://rsms.me/inter/inter.css"])
app.add_page(home_page)
app.add_page(about_page)
# app.add_page(welcome_page)
app.add_page(network_page)