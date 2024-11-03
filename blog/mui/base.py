import reflex as rx

class MUIBase(rx.component):
    library = "@mui/material"
    lib_dependencies: list[str] = ["@emotion/styled"]
    tag = "MUIBase"
    is_default = True
    