import reflex as rx

# Sidebar-Components



def sidebar_item(text: str, href: str):
    return rx.link(
        rx.hstack(
            rx.text(text),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.5rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium"
    )
def sidebar_items():
    return rx.vstack(
        rx.divider(),
        sidebar_item("LIVE", "/live"),
        rx.divider(),
        sidebar_item("Ticket-Management", "/TicketManagement"),
        rx.divider(),
        sidebar_item("Snack-Management", "/SnackManagement"),
        rx.divider(),
        sidebar_item("Statistiken", "/statistics"),
        rx.divider()
    )

def sidebar():
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading("CampusKino Landshut", side=7, weight="bold"),
                align="center",
                justify="start",
                padding_x="0.5rem",
                width="100%"
            ),
            sidebar_items(),
            spacing="5",
            padding_x="1em",
            padding_y="1.5em",
            bg=rx.color("bronze", 3),
            align="start",
            min_height="100vh",
            width="16em",
            overflow_y = "auto"

        )
        
    )