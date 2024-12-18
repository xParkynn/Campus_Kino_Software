import reflex as rx
from Program.shared import FiMg
from .AddPage import FormState
import os

class FinanceState(rx.State):

    date: str = ""

    def submit_form(self, form_data):
        with open("/temp", "r") as file:
            self.date = file.readline()
        os.remove("/temp")
        form_data["ticket_price"] = form_data["ticket_price"].replace(",",".")
        form_data["club_price"] = form_data["club_price"].replace(",",".")
        form_data["addcost"] = form_data["addcost"].replace(",",".")
        if form_data["ticket_price"] == "":
            ticket = 1.5
        else:
            ticket=float(form_data["ticket_price"])
        if form_data["club_price"] == "":
            club=0.5
        else:
            club=float(form_data["club_price"])
        FiMg.save_finances(date=self.date, ticket_price=ticket, club_price=club, addcost=float(form_data["addcost"]))
        return rx.redirect("/TicketManagement")
   

def fin_page():
    return rx.center(
        rx.box(
            rx.form(
                rx.vstack(
                    rx.heading("Finanzen hinzufügen", size='lg'),
                    rx.divider(size='4', width="100%"),
                    rx.box(
                        rx.vstack(
                        rx.heading("Finanzen:"),
                        rx.hstack(
                            rx.input(
                                placeholder = "Ticket-Preis",
                                name="ticket_price",
                                required = False
                            ),
                            rx.input(
                                placeholder = "Clubkartenpreis",
                                name="club_price",
                                required=False
                            ),
                            rx.input(
                                placeholder="Zusatzkosten",
                                name="addcost",
                                required=True
                            ), spacing='5'
                        ),
                        border_radius="5px",
                        padding="15px",
                        border="1px solid",
                        border_color="white"
                        )
                    ),
                    rx.button(
                            "Hinzufügen",
                            type="submit"
                        ),
                    spacing="4"
                ),
                padding="2rem",
                on_submit=FinanceState.submit_form,
                
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