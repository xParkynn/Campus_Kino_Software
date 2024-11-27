import reflex as rx
from Program.shared import TiMg
from assets.pages.ModifierPage import modify_page
from assets.pages.AddPage import add_movie
from assets.pages.HomePage import sidebar
from assets.pages.Ticket_Home import Ticket_Home, TicketState
from Program.shared import app





app.add_page(modify_page(), title=f"Ticket-Management", route=f"/TiMg")
app.add_page(add_movie, title="Add Ticket", route="/add_ticket")
app.add_page(sidebar, title="Home", route="/")
app.add_page(Ticket_Home, title="Ticket-Management", route="/TicketManagement", on_load=TicketState.load())


