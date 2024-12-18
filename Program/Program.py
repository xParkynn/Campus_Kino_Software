import reflex as rx
from Program.shared import TiMg
from .pages.ModifierPage import modify_page
from .pages.AddPage import add_movie
from .pages.HomePage import sidebar
from .pages.Ticket_Home import Ticket_Home, TicketState
from .pages.LivePage import live_page
from .pages.LiveMode import live_mode, LiveState
from .pages.StatisticsPage import statistics_page, StatisticsPageState
from .pages.FinPage import fin_page
from Program.shared import app





app.add_page(modify_page, title=f"Ticket-Management", route=f"/TiMg")
app.add_page(add_movie, title="Add Ticket", route="/add_movie")
app.add_page(sidebar, title="Home", route="/")
app.add_page(Ticket_Home, title="Ticket-Management", route="/TicketManagement", on_load=TicketState.load())
app.add_page(live_page, title="Live-Management", route="/live")
app.add_page(live_mode, title="Live Mode", route="/live_mode", on_load = LiveState.load())
app.add_page(statistics_page, title="Statistiken", route="/statistics", on_load=StatisticsPageState.on_load())
app.add_page(fin_page, title="Finanzen", route="/FinanceManagement")


