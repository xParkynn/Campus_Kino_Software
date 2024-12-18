import reflex as rx
from Program.shared import TiMg, app
from .HomePage import sidebar
from .AddPage import FormState

def live_page():
    return rx.hstack(
        sidebar(),
        
        rx.box(
            # Container für das Heading und den Button
            rx.box(
                rx.heading("Live-Management", size="xl"),
                rx.link(
                    rx.button(
                    "New Movie", 
                    size="md", 
                    color_scheme="blue", 
                    position="absolute",   # Button absolut positionieren
                    top="1rem",            # Abstand von oben
                    right="1rem" 
                    ),
                    href="/add_movie",
                    on_click= lambda: FormState.set_timg(False) 
                ),
                width="100%",
                position="relative",      # Box als relativer Container für den Button
                display="flex",
                align_items="center",     # Heading vertikal zentrieren
                justify_content="center", # Heading horizontal zentrieren
                padding="2rem",
                height="4rem"             # Höhe der Box für das Layout
            ),
            rx.divider(size="4", width="100%"),
            rx.table.root(
                rx.table.body(
                    
                spacing="4",
                padding="2rem"
                ),
            ),
            width="100%",
            height="100vh",
            padding_y="1em"
        )
    )
