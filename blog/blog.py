import reflex as rx

from .pages.about import about_page
from .pages.home import home_page
from .intro.welcome import welcome_page

app = rx.App(stylesheets = ["https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&family=Noto+Sans+SC:wght@100..900&display=swap", "/fonts.css"])
app.add_page(home_page)
app.add_page(about_page)
app.add_page(welcome_page)