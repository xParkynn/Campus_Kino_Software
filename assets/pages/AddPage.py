import reflex as rx
from backend_pandas import TicketManager
import pandas as pd

TiMg = TicketManager()

class FormState(rx.State):

    def submit_form(self, form_data):
        TiMg.save_tickets(name=form_data["name"], date=form_data["date"], tickets_sold=int(form_data["tickets_sold"]), free_tickets=int(form_data["free_tickets"]), clubcards=int(form_data["clubcards"]), genres=[form_data['genre1'], form_data['genre2']], goal=int(form_data["goal"]), startnr=int(form_data["startnr"]), endnr=int(form_data["endnr"]))

    




def add_movie() -> rx.Component:
 
    return rx.center(
            rx.box(
                rx.form(
                    rx.vstack(
                        rx.heading(f"Film hinzufügen", size="lg"),
                        rx.box(
                            rx.vstack(
                                rx.heading("Allgemein:"),
                                rx.hstack(
                                    rx.input(
                                        placeholder="Filmname",
                                        name="name",
                                        required=True
                                    ),
                                    rx.input(
                                        placeholder="Datum",
                                        name="date",
                                        required=True
                                    ), 
                                spacing="5",)
                            ),
                            border_radius="5px",
                            padding="15px",
                            border="1px solid",
                            border_color="white"
                        ),
                        rx.box(
                            rx.vstack(
                                rx.heading("Karten:"),
                                rx.center(
                                    rx.hstack(
                                        rx.input(
                                            placeholder="Verkaufte Tickets",
                                            name="tickets_sold",
                                            required=True
                                            ),
                                        rx.input(
                                            placeholder="Frei-Tickets",
                                            name="free_tickets",
                                            required=True
                                            ),
                                        rx.input(
                                            placeholder="Clubkarten",
                                            name="clubcards",
                                            required=True
                                            )   
                                        )
                                    ),   
                                ),
                            border="1px solid", border_color="white", border_radius="5px", padding="15px"
                        ),
                        rx.box(
                            rx.vstack(
                                rx.heading("Genres:"),
                                rx.hstack(
                                    rx.input(
                                        placeholder="Genre",
                                        name="genre1",
                                        required=True
                                    ),
                                    rx.input(
                                        placeholder="Genre2",
                                        name="genre2",
                                        required=True
                                    )
                                )
                            ), 
                            border="1px solid", border_color="white", border_radius="5px", padding="15px"
                        ),
                        rx.box(
                            rx.vstack(
                                rx.heading("Besucher-Ziel:"),
                                rx.input(
                                    placeholder="Besucher-Ziel",
                                    name="goal",
                                    required=True
                                ),    
                            ),
                            border="1px solid", border_color="white", border_radius="5px", padding="15px"
                        ),
                        rx.box(
                            rx.vstack(
                                rx.heading("Start-/Endnr:"),
                                rx.hstack(
                                    rx.input(
                                        placeholder="Start-Nummer",
                                        name="startnr",
                                        required=True
                                    ),
                                    rx.input(
                                        placeholder="End-Nummer",
                                        name="endnr",
                                        required=True
                                    )
                                )
                            ),
                            border="1px solid", border_color="white", border_radius="5px", padding="15px"
                        ),
                        rx.button(
                            "Hinzufügen",
                            type="submit"
                        ),
                        spacing="4"
                    ),
                    padding="2rem",
                    on_submit=FormState.submit_form,
                ),
                width="100%",                
                max_width="600px",            
                padding="2rem",               
                box_shadow="lg",              
                background_color="gray.900",  
                border_radius="10px",         
            ),
            min_height="100vh"
        )  