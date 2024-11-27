import pandas as pd

class BuyManagement(object):
    def __init__(self):
        self.db = pd.read_csv("./storage/WS2425/bought.csv")

    def save_db(self):
        self.db.to_csv("./storage/WS2425/bought.csv")

    def add_buying(self, chargenr: int, product: str, buying_price: float, selling_price: float, amount: int, mhd: str):
        dct = {"Product": product, "Buying_Price": buying_price, "Selling_Price": selling_price, "Amount": amount, "MHD": mhd}
        self.db.loc[chargenr] = dct
        self.save_db()


class StockManagement(object):
    def __init__(self):
        self.db = pd.read_csv("./storage/WS2425/stock.csv").set_index("Product")

    def save_db(self):
        self.db.to_csv("./storage/db.csv")

    def add_entry(self, name:str, stock:int, buying_price:float, selling_price: float, mhd: str):
        dct = {"Product": name, "Stock": stock, "Buying_price": buying_price, "Selling_price": selling_price, "total_sold": 0, "average_sold": 0, "MHD": mhd}
        self.db.loc[name] = dct
        self.save_db()
    
    def remove_entry(self, name:str):
        self.db.drop(name, inplace=True, axis=0)

    def mod_price(self, name:str, new_price:float):
        self.db.at[name, 'Selling_price']= new_price
    
    def mod_bprice(self, name:str, new_bprice:float):
        self.db.at[name, "Buying_price"] = new_bprice

    def add_stock(self, name:str, amount:int):
        self.db.at[name, "Stock"] += amount

    def sold(self, name:str, amount:int):
        self.db.at[name, "Stock"] -= amount

class TicketManager(object):
    def __init__(self):
        self.db = pd.read_csv("./storage/WS2425/ticket_db.csv").set_index("Date")
    
    def update_database(self):
        self.db = pd.read_csv("./storage/WS2425/ticket_db.csv").set_index("Date")


    def save_db(self):
        self.db.to_csv("./storage/WS2425/ticket_db.csv")

    def save_tickets(self, name:str, date:str, tickets_sold: int, free_tickets:int, clubcards: int, genres:list, goal:int, startnr:int, endnr:int):
        dct = {"Movie": name, "Tickets": tickets_sold, "Free-Tickets": free_tickets, "Club-Cards": clubcards, "Genres": genres, "Visitors": tickets_sold+free_tickets, "Goal": goal, "Start-Nr": startnr, "End-Nr": endnr}
        self.db.loc[date] = dct
        self.add_total()
        self.save_db()
    
    def add_total(self):
        self.db.drop("Total", inplace=True, axis=0)
        dct = {"Date": None, "Tickets": self.db["Tickets"].sum(), "Free-Tickets": self.db["Free-Tickets"].sum(), "Club-Cards": self.db["Club-Cards"].sum(), "Visitors": self.db["Visitors"].sum(), "Goal": self.db["Goal"].sum()}
        self.db.loc["Total"] = dct

    def modify_ticket(self, date:str,ticket: int):
        self.db.at[date, "Tickets"] = ticket
        self.update_db(date=date)
        self.save_db()


    def modify_freeticket(self, date:str, ticket:int):
        self.db.at[date, "Free-Tickets"] = ticket
        self.update_db(date=date)
        self.save_db()

    def modify_clubcards(self, date:str, cards:int):
        self.db.at[date, "Club-Cards"] = cards
        self.save_db()

    def modify_genres(self, date:str, genres:list):
        self.db.at[date, "Genres"] = genres
        self.save_db()

    def modify_goal(self, date:str, goal:int):
        self.db.at[date, "Goal"] = goal
        self.save_db()

    def modify_startnr(self, date:str, startnr:int):
        self.db.at[date, "Start-Nr"] = startnr
        self.save_db()

    def modify_endnr(self, date:str, endnr:int):
        self.db.at[date, "End-Nr"] = endnr
        self.save_db()

    def update_db(self, date:str):
        entry = self.db.loc[date]
        self.db.at[date, "Visitors"] = entry["Tickets"] + entry["Free-Tickets"]

    def plot_goal(self):
        self.db.plot(y=["Goal", "Visitors"])


