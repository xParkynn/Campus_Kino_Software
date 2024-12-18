import reflex as rx
from Program.shared import TiMg, FiMg
from .HomePage import sidebar
from typing import List, Dict

class StatisticsPageState(rx.State):
    """State class for the statistics page."""

    # A list of dictionaries to hold the table data
    table_data: List[Dict] = []

    def on_load(self):
        """Load and prepare table data."""
        data = []

        for idx, ticket in TiMg.db.iterrows():
            # Format money-related items
            money_items = [
                str(FiMg.db.loc[idx]["Sales-Volume"]),
                str(FiMg.db.loc[idx]["Cash"]),
                str(FiMg.db.loc[idx]["Unifilm"]),
                str(FiMg.db.loc[idx]["CK"]),
                str(FiMg.db.loc[idx]["Additional-Costs"]),
            ]
            formatted_money_items = []
            for elem in money_items:
                parts = elem.split(".")
                if len(parts) == 2 and len(parts[1]) < 2:
                    elem = f"{parts[0]}.{parts[1]}0€"
                else:
                    if not elem.endswith("€"):
                        elem += "€"
                formatted_money_items.append(elem)

            # Append row data as a dictionary
            data.append({
                "Datum": idx,
                "Name": ticket["Movie"],
                "Tickets": ticket["Tickets"],
                "Freikarten": ticket["Free-Tickets"],
                "Clubkarten": ticket["Club-Cards"],
                "Besucher": ticket["Visitors"],
                "Goal": ticket["Goal"],
                "Zusatzkosten": formatted_money_items[4],
                "Umsatz": formatted_money_items[0],
                "Cash": formatted_money_items[1],
                "Unifilm-Part": formatted_money_items[2],
                "Campus-Kino": formatted_money_items[3],
            })

        # Update state variable
        self.table_data = data

def statistics_page():
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.box(
                rx.heading("Statistiken", size="xl"),
                width="100%",
                display="flex",
                align_items="center",
                justify_content="center",
                padding="2rem",
                height="4rem",
            ),
            rx.divider(size="4", width="100%"),
            rx.box(
                rx.vstack(
                    rx.heading("Ticket-Finanzen:", size="xl"),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.cell("Datum"),
                                rx.table.cell("Name"),
                                rx.table.cell("Tickets"),
                                rx.table.cell("Freikarten"),
                                rx.table.cell("Clubkarten"),
                                rx.table.cell("Besucher"),
                                rx.table.cell("Goal"),
                                rx.table.cell("Zusatzkosten"),
                                rx.table.cell("Umsatz"),
                                rx.table.cell("Cash"),
                                rx.table.cell("Unifilm-Part"),
                                rx.table.cell("Campus-Kino"),
                            )
                        ),
                        rx.table.body(
                            # Use foreach to dynamically render rows from the table_data
                            rx.foreach(
                                StatisticsPageState.table_data,
                                lambda row: rx.table.row(
                                    rx.table.cell(row["Datum"]),
                                    rx.table.cell(row["Name"]),
                                    rx.table.cell(row["Tickets"]),
                                    rx.table.cell(row["Freikarten"]),
                                    rx.table.cell(row["Clubkarten"]),
                                    rx.table.cell(row["Besucher"]),
                                    rx.table.cell(row["Goal"]),
                                    rx.table.cell(row["Zusatzkosten"]),
                                    rx.table.cell(row["Umsatz"]),
                                    rx.table.cell(row["Cash"]),
                                    rx.table.cell(row["Unifilm-Part"]),
                                    rx.table.cell(row["Campus-Kino"]),
                                )
                            )
                        )
                    ),
                    width="100%",
                ),
                width="100%",
                border="1px solid",
                border_color="white",
                border_radius="5px",
                padding="15px",
            ),
            width="100%",
        )
    )
