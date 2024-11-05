import reflex as rx

class User(rx.Model, table=True):
    """A table of Users."""

    username: str
    password: str

class BlogInfo(rx.Model, table=True):
    entity: str
    evalue: str