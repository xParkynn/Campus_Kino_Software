import reflex as rx
from Program.shared import TiMg, app
from .HomePage import sidebar

def live_mode():
    return rx.hstack(
        sidebar()
    )