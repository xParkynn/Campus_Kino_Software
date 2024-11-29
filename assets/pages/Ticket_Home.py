import reflex as rx
from Program.shared import TiMg
from .HomePage import sidebar
from .ModifierPage import FormState
import pandas as pd
from typing import List, Tuple
from .AddPage import FormState as FormStateAdd

class TicketState(rx.State):

    tickets: List[Tuple[str, str]] = []

    

    def load(self):
        self.tickets = []
        TiMg.sort()
        

        for idx, ticket in TiMg.db.iterrows():
            if idx == "Total":
                break
            self.tickets.append((idx, ticket["Movie"]))

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
                    href="/add_movie",
                    on_click = lambda: FormStateAdd.set_timg(True) 
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
                    
                    

                        rx.foreach(TicketState.tickets, table_row)
                        
                    
                        
                    
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
    idx, ticket = idx[0], idx[1]
    

    return rx.table.row(
        rx.table.cell(idx),
        rx.table.cell(ticket),
        rx.table.cell(
            rx.link(
                rx.text("edit"),
                href=f"/TiMg",
                on_click= lambda: FormState.load(idx)
                    
                
            )
        )
    
    )