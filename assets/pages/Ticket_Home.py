import reflex as rx
from backend_pandas import TicketManager
from .HomePage import sidebar
from .ModifierPage import FormState
import pandas as pd

TiMg = TicketManager()


def Ticket_Home():
    tickets = []
    return rx.hstack(
        sidebar(),
        
        rx.box(
            # Container für das Heading und den Button
            rx.box(
                rx.heading("Ticket-Management", size="xl"),
                rx.link(
                    rx.button(
                    "Add Ticket", 
                    size="md", 
                    color_scheme="blue", 
                    position="absolute",   # Button absolut positionieren
                    top="1rem",            # Abstand von oben
                    right="1rem" 
                    ),
                    href="/add_ticket"  
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
                    *[
                    
                    

                        table_row(idx, ticket)
                        
                    
                        for idx, ticket in TiMg.db.iterrows() if idx != "Total"
                    
                    ]
                    if not tickets else [
                        rx.table.row(
                            rx.table.cell("No data available")
                        )
                    ], 
                spacing="4",
                padding="2rem"
                ),
            ),
            width="100%",
            height="100vh",
            padding_y="1em"
        )
    )

def table_row(idx, ticket):
    
    if(idx != "Total"):
       
        return rx.table.row(
            rx.table.cell(idx),
            rx.table.cell(ticket["Movie"]),
            rx.table.cell(
                rx.link(
                    rx.text("edit"),
                    href=f"/TiMg_{ticket["Movie"]}",
                    on_click= lambda: FormState.load(idx)
                    
                )
            )
        )
    
