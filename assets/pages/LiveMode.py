import reflex as rx
from Program.shared import TiMg, app, LiMg
from .HomePage import sidebar
import pandas as pd




class LiveState(rx.State):
    date: str = ""
    name: str = ""
    tickets: int = 0
    free_tickets: int = 0
    clubcards: int = 0
    db: pd.DataFrame = pd.read_csv("storage/live_db.csv")
    
    def load(self):
        self.db = pd.read_csv("storage/live_db.csv")
        self.date = self.db.iloc[0]["Date"]
        self.name = self.db.iloc[0]["Name"]
        self.tickets = int(TiMg.db.loc[self.date]["Tickets"])  # Ensure tickets is an integer
        self.free_tickets = int(self.db.iloc[0]["Free-Tickets"])
        self.clubcards = int(self.db.iloc[0]["Club-Cards"])

    @rx.event
    def decrement_ticket(self):
        TiMg.db.at[self.date, "Tickets"] -= 1
        self.db.at[0, "Tickets"] -= 1
        TiMg.save_db()
        self.db.to_csv("storage/live_db.csv")
        self.tickets -= 1  # Reactive update

    @rx.event
    def increment_ticket(self):
        TiMg.db.at[self.date, "Tickets"] += 1
        self.db.at[0, "Tickets"] += 1
        TiMg.save_db()
        self.db.to_csv("storage/live_db.csv")
        self.tickets += 1  # Reactive update

    @rx.event
    def decrement_free(self):
        TiMg.db.at[self.date, "Free-Tickets"] -=1
        self.db.at[0, "Free-Tickets"] -= 1
        TiMg.save_db()
        self.db.to_csv("storage/live_db.csv")
        self.free_tickets -=1
    
    @rx.event
    def increment_free(self):
        TiMg.db.at[self.date, "Free-Tickets"] += 1
        self.db.at[0, "Free-Tickets"] += 1
        TiMg.save_db()
        self.db.to_csv("storage/live_db.csv")
        self.free_tickets += 1

    @rx.event
    def decrement_club(self):
        TiMg.db.at[self.date, "Club-Cards"] -=1
        self.db.at[0, "Club-Cards"] -= 1
        TiMg.save_db()
        self.db.to_csv("storage/live_db.csv")
        self.clubcards -=1
    
    @rx.event
    def increment_club(self):
        TiMg.db.at[self.date, "Club-Cards"] +=1
        self.db.at[0, "Club-Cards"] += 1
        TiMg.save_db()
        self.db.to_csv("storage/live_db.csv")
        self.clubcards += 1

    def end_live(self):
        self.db.drop(0)
        self.db.to_csv("storage/live_db.csv")
        return rx.redirect("/")


def live_mode():
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.box(
                rx.box(
                    rx.heading(f"Live-Management for {LiveState.name}", size="xl"),
                    rx.divider(size="4"),
                ),
                rx.center(
                   rx.vstack(
                        rx.heading("Tickets", size="xl"),
                        rx.hstack(
                        rx.button("-", on_click=LiveState.decrement_ticket),
                        rx.text(
                            LiveState.tickets,
                            font_size="2xl",
                            font_weight="bold",
                            color="white",
                            width="4rem",  # Add width for alignment
                            text_align="center",  # Center-align text within its box
                        ),
                        rx.button("+", on_click=LiveState.increment_ticket),
                        spacing="1rem",  # Space between elements
                        align_items="center",  # Vertically align buttons and text
                    ),
                    rx.heading("Free-Tickets", size="xl"),
                    rx.hstack(
                        rx.button("-", on_click=LiveState.decrement_free),
                        rx.text(
                            LiveState.free_tickets,
                            font_size="2xl",
                            font_weight="bold",
                            color="white",
                            width="4rem",  # Add width for alignment
                            text_align="center",  # Center-align text within its box
                        ),
                        rx.button("+", on_click=LiveState.increment_free),
                        spacing="1rem",  # Space between elements
                        align_items="center",  # Vertically align buttons and text
                    ),
                    rx.heading("Clubcards", size="xl"),
                    rx.hstack(
                        rx.button("-", on_click=LiveState.decrement_club),
                        rx.text(
                            LiveState.clubcards,
                            font_size="2xl",
                            font_weight="bold",
                            color="white",
                            width="4rem",  # Add width for alignment
                            text_align="center",  # Center-align text within its box
                        ),
                        rx.button("+", on_click=LiveState.increment_club),
                        spacing="1rem",  # Space between elements
                        align_items="center",  # Vertically align buttons and text
                    ),
                    rx.button("Beenden", on_click=LiveState.end_live),
                    width="100%",
                    height="100vh",
                    justify_content="center",
                    align_items="center",
                    spacing='9'
                   )
                ),
                width="100%",
                height="100vh",
                padding_y="1em",
            ),
            width="100%",
            height="100vh",
            spacing="9",
        ),
    )
