import reflex as rx
from backend_pandas import TicketManager
import pandas as pd

TiMg = TicketManager()

class FormState(rx.State):

    db: pd.DataFrame = TiMg.db

    name: str = ""
    date: str = ""
    tickets_sold: int = 0
    free_tickets: int = 0
    clubcards: int = 0
    genre1: str = ""
    genre2: str = ""
    genres: list = []
    goal: int = 0
    startnr: int = 0
    endnr: int = 0
    

    def submit_form(self, form_data):
        TiMg.save_tickets(name=form_data["name"], date=form_data["date"], tickets_sold=int(form_data["tickets_sold"]), free_tickets=int(form_data["free_tickets"]), clubcards=int(form_data["clubcards"]), genres=[form_data['genre1'], form_data['genre2']], goal=int(form_data["goal"]), startnr=int(form_data["startnr"]), endnr=int(form_data["endnr"]))

    def get_db(self, date: str) -> pd.DataFrame:
        return str(self.db.loc[date]["Movie"])
    



def modify_page(date: str, name: str) -> rx.Component:
    tickets = ""
    free_tickets = ""
    clubcards = ""
    genre1 = ""
    genre2 = ""
    goal = ""
    startnr = ""
    endnr = ""
    
    if date in TiMg.db.index:
        db = TiMg.db.loc[date]
        tickets = str(db["Tickets"])
        free_tickets = str(db["Free-Tickets"])
        clubcards = str(db["Club-Cards"])
  
        goal = str(db["Goal"])
        startnr = str(int(db["Start-Nr"]))
        endnr = str(int(db["End-Nr"]))

    
    return rx.center(
            rx.box(
                rx.form(
                    rx.vstack(
                        rx.heading(f"Ticket-Management for {name}", size="lg"),
                        rx.box(
                            rx.vstack(
                                rx.heading("Allgemein:"),
                                rx.hstack(
                                    rx.input(
                                        placeholder="Filmname",
                                        name="name",
                                        value = name,
                                        required=True
                                    ),
                                    rx.input(
                                        placeholder="Datum",
                                        name="date",
                                        value=date,
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
                                            value=tickets,
                                            required=True
                                            ),
                                        rx.input(
                                            placeholder="Frei-Tickets",
                                            name="free_tickets",
                                            value=free_tickets,
                                            required=True
                                            ),
                                        rx.input(
                                            placeholder="Clubkarten",
                                            name="clubcards",
                                            value=clubcards,
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
                                        value=genre1,
                                        required=True
                                    ),
                                    rx.input(
                                        placeholder="Genre2",
                                        name="genre2",
                                        value=genre2,
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
                                    value=goal,
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
                                        value=startnr,
                                        required=True
                                    ),
                                    rx.input(
                                        placeholder="End-Nummer",
                                        name="endnr",
                                        value=endnr,
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
                        spacing="1rem"
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