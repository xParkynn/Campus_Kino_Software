import reflex as rx
from Program.shared import TiMg, set_nr, get_nr
import pandas as pd

db = TiMg.db
class FormState(rx.State):

    
    name: str = ""
    date: str = ""
    tickets_sold: int = 0
    free_tickets: int = 0
    clubcards: int = 0
    genre1: str = ""
    genre2: str = ""
    goal: int = 0
    startnr: int = 0
    endnr: int = 0
    
    def load(self, date):
        movie_db = db.loc[date]
        self.name = movie_db["Movie"]
        self.date = date
        self.tickets_sold = int(movie_db["Tickets"])
        self.free_tickets = int(movie_db["Free-Tickets"])
        self.clubcards = int(movie_db["Club-Cards"])
        if(type(movie_db["Genres"]) == str):
            self.genre1, self.genre2 = get_genre(movie_db["Genres"])
        else:
            self.genre1, self.genre2 = movie_db["Genres"][0], movie_db["Genres"][1]
        self.goal = int(movie_db["Goal"])
        self.startnr = get_nr(movie_db["Start-Nr"])
        self.endnr = get_nr(movie_db["End-Nr"])

    def change_date(self, date):
        self.date = date

    def submit_form(self, form_data):
        TiMg.save_tickets(
            name=form_data["name"],
            date=form_data["date"],
            tickets_sold=int(form_data["tickets_sold"]),
            free_tickets=int(form_data["free_tickets"]),
            clubcards=int(form_data["clubcards"]),
            genres=[form_data['genre1'], form_data['genre2']],
            goal=int(form_data["goal"]),
            startnr=set_nr(form_data["startnr"]),
            endnr=set_nr(form_data["endnr"])
        )
        return rx.redirect(path="/TicketManagement")
    
    def change_name(self, name):
        self.name = name
    def change_ticket(self, ticket):
        self.tickets_sold = ticket
    def change_free(self, free):
        self.free_tickets = free
    def change_club(self, club):
        self.clubcards = club
    def change_genre1(self, genre):
        self.genre1 = genre
    def change_genre2(self, genre):
        self.genre2 = genre
    def change_goal(self, goal):
        self.goal = goal
    def change_stnr(self, startnr):
        self.startnr = startnr
    def change_endnr(self, endnr):
        self.endnr = endnr

    

def get_genre(genre_str: str):
    
    genre_lst = genre_str.split(",") #split genre string    
    return genre_lst[0][2:len(genre_lst[0])-1], genre_lst[1][2:len(genre_lst[1])-2] if len(genre_lst) == 2 else  genre_lst[0][2:len(genre_lst[0])-1]
    

def modify_page() -> rx.Component:
    
    return rx.center(
            rx.box(
                rx.form(
                    rx.vstack(
                        rx.heading(f"Ticket-Management for {FormState.name}", size="lg"),
                        rx.box(
                            rx.vstack(
                                rx.heading("Allgemein:"),
                                rx.hstack(
                                    rx.input(
                                        placeholder="Filmname",
                                        name="name",
                                        value = FormState.name,
                                        required=True,
                                        on_change = FormState.change_name
                                    ),
                                    rx.input(
                                        placeholder="Datum",
                                        name="date",
                                        value=FormState.date,
                                        required=True,
                                        on_change = FormState.change_date
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
                                            value = FormState.tickets_sold,
                                            required=True,
                                            on_change = FormState.change_ticket
                                            ),
                                        rx.input(
                                            placeholder="Frei-Tickets",
                                            name="free_tickets",
                                            value = FormState.free_tickets,
                                            required=True,
                                            on_change = FormState.change_free
                                            ),
                                        rx.input(
                                            placeholder="Clubkarten",
                                            name="clubcards",
                                            value = FormState.clubcards,
                                            required=True,
                                            on_change = FormState.change_club
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
                                        value = FormState.genre1,
                                        required=True,
                                        on_change = FormState.change_genre1
                                    ),
                                    rx.input(
                                        placeholder="Genre2",
                                        name="genre2",
                                        value = FormState.genre2,                                      
                                        on_change = FormState.change_genre2
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
                                    value = FormState.goal,
                                    required=True,
                                    on_change = FormState.change_goal
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
                                        value = FormState.startnr,
                                        required=True,
                                        on_change = FormState.change_stnr
                                    ),
                                    rx.input(
                                        placeholder="End-Nummer",
                                        name="endnr",
                                        value = FormState.endnr,
                                        required=True,
                                        on_change = FormState.change_endnr
                                    )
                                )
                            ),
                            border="1px solid", border_color="white", border_radius="5px", padding="15px"
                        ),
                        
                        rx.button(
                            "Hinzufügen",
                            type="submit",
                        ),
                        spacing="4"
                    ),
                    padding="2rem",
                    on_submit = FormState.submit_form,
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