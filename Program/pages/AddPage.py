import reflex as rx
from Program.shared import TiMg, FiMg
import pandas as pd
from .ModifierPage import modify_page
from Program.shared import app
from .LiveMode import LiveState

class FormState(rx.State):

    timg: bool = True
    date: str = ""

    def submit_form(self, form_data):
        
        self.date = form_data["date"]
        with open("/temp", "w") as file:
            file.write(self.date)
        
        if self.timg:
            TiMg.save_tickets(name=form_data["name"], date=form_data["date"], tickets_sold=int(form_data["tickets_sold"]), free_tickets=int(form_data["free_tickets"]), clubcards=int(form_data["clubcards"]), genres=[form_data['genre1'], form_data['genre2']], goal=int(form_data["goal"]), startnr=int(form_data["startnr"]), endnr=int(form_data["endnr"]))
            TiMg.update_database()
            TiMg.set_sorted(False)
            FiMg.get_ticket_data()
            return rx.redirect("/FinanceManagement")
        else:
            if not form_data["date"] in TiMg.db.index:
                TiMg.save_tickets(name=form_data["name"], date=form_data["date"], tickets_sold=0, free_tickets=0, clubcards= 0, genres=[form_data["genre1"], form_data["genre2"]], goal=int(form_data["goal"]), startnr=int(form_data["startnr"]), endnr=int(form_data["endnr"]))
                TiMg.set_sorted(False)
                TiMg.update_database()

            ticket, free_ticket, clubcards = 0,0,0
            if(TiMg.db.loc[form_data["date"]]["Tickets"] != 0):
                ticket = TiMg.db.loc[form_data["date"]]["Tickets"]
            if(TiMg.db.loc[form_data["date"]]["Free-Tickets"] != 0):
                free_ticket = TiMg.db.loc[form_data["date"]]["Free-Tickets"]
            if(TiMg.db.loc[form_data["date"]]["Club-Cards"] != 0):
                clubcards = TiMg.db.loc[form_data["date"]]["Club-Cards"]

            dct = {"Date": form_data["date"], "Name": form_data["name"], "Tickets": [ticket], "Free-Tickets": [free_ticket], "Club-Cards": [clubcards]}
            pd.DataFrame.from_dict(dct).set_index("Date", inplace=False).to_csv("storage/live_db.csv")
            TiMg.update_live()
            return rx.redirect("/live_mode")
    
    def get_date(self):
        return self.date
    def set_timg(self, live):
        self.timg = live






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
                        rx.cond(condition=FormState.timg,
                                c1=rx.box(
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
                                )
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
                    on_submit=FormState.submit_form
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