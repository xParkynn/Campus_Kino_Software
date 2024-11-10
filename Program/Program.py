import reflex as rx
from backend_pandas import TicketManager
from assets.pages.ModifierPage import modify_page
from assets.pages.AddPage import add_movie

TiMg = TicketManager()
app = rx.App()
for i in TiMg.db.index:
    if i == "Total":
        break
    app.add_page(lambda i=i: modify_page(i, TiMg.db.loc[i]["Movie"]), title=f"Ticket-Management ({TiMg.db.loc[i]["Movie"]})", route=f"/TiMg_{TiMg.db.loc[i]["Movie"]}")
app.add_page(add_movie, title="Add Ticket", route="/add_ticket")
