import reflex as rx
from .base import MUIBase

class Button(MUIBase):
    variant: rx.Var[str]
    disabled: rx.Var[bool]
    href: rx.Var[str]
    color: rx.Var[str]
    size: rx.Var[str]
    startIcon: rx.Var[rx.Component]
    endIcon: rx.Var[rx.Component]