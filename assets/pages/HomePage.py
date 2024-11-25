import reflex as rx

# Sidebar-Components

def sidebar_item(text: str, icon: str, href: str):
    return rx.link(
        rx.hstack(
            #rx.image(icon, width="5em"),
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
        sidebar_item("Ticket_Management", "../icons/ticket_icon.png", "/TicketManagement"),
        rx.divider(),
        sidebar_item("Snack-Management", "../icons/popcorn_icon.png", "/SnackManagement"),
        rx.divider()
    )

def sidebar():
    return rx.box(
        rx.vstack(
            rx.hstack(
                #rx.image("../icons/ck_logo.jpeg", width="2.25rem", height="auto"),
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
            height="100vh",
            width="16em"

        )
    )