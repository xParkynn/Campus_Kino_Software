import pandas as pd
import reflex as rx
import math

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
        self.live_date = None
        self.sorted = True
    
    def set_sorted(self, sort: bool):
        self.sorted = sort

    def update_database(self):
        self.db = pd.read_csv("./storage/WS2425/ticket_db.csv").set_index("Date")

    def update_live(self):
        self.live_date = pd.read_csv("./storage/live_db.csv").iloc[0]["Date"]

    def save_db(self):
        self.db.to_csv("./storage/WS2425/ticket_db.csv")

    def save_tickets(self, name:str, date:str, tickets_sold: int, free_tickets:int, clubcards: int, genres:list, goal:int, startnr:int = None, endnr:int=None):
        dct = {"Movie": name, "Tickets": tickets_sold, "Free-Tickets": free_tickets, "Club-Cards": clubcards, "Genres": genres, "Visitors": tickets_sold+free_tickets, "Goal": goal, "Start-Nr": startnr, "End-Nr": endnr}
        self.db.loc[date] = dct
        self.add_total()
        self.save_db()
    
    def add_total(self):
        self.db.drop("Total", inplace=True, axis=0)
        dct = {"Date": '-',"Movie": '-', "Tickets": self.db["Tickets"].sum(), "Free-Tickets": self.db["Free-Tickets"].sum(), "Club-Cards": self.db["Club-Cards"].sum(), "Genres": "-", "Visitors": self.db["Visitors"].sum(), "Goal": self.db["Goal"].sum(), "Additional-Costs": self.db["Additional-Costs"].sum()}
        self.db.loc["Total"] = dct

    def modify_ticket(self, date:str,ticket: int):
        self.db.at[date, "Tickets"] = ticket
        self.update_db(date=date)
        self.save_db()
    
    def sort(self):
        if self.sorted:
            return
        lst = list()
        for i in range(2):
            for elem in filter(lambda x: x!="Total", self.db.index):
                elem = elem.split(".")
                elem[0], elem[-1] = elem[-1], elem[0]
                print(elem)
                lst.append(f"{elem[0]}.{elem[1]}.{elem[2]}")
            lst.append("Total")
            self.db["Date"] = lst
            self.db.set_index("Date", inplace=True)
            if not self.sorted:
                self.db.sort_index(inplace=True)
                self.set_sorted(True)
                lst = []
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

TiMg = TicketManager()
class FinanceManager(object):
    #read csv, set base values
    def __init__(self):
        self.db = pd.read_csv("./storage/WS2425/finance_db.csv").set_index("Date")
        self.uf_fraction = 0.75
        self.get_ticket_data()

    def save_db(self):
        """
        Saves Finance-Database to csv_file

        PARAMETERS:
        None

        Return:
        None
        """
        self.db.to_csv("./storage/WS2425/finance_db.csv")

    def get_ticket_data(self):
        """
        Pulls ticket data out of the ticket database

        PARAMETERS:
        None

        Return:
        None
        """
        TiMg.update_database()
        self.tickets = TiMg.db["Tickets"]
        self.clubcards = TiMg.db["Club-Cards"]
        self.addcosts = TiMg.db["Additional-Costs"]


    def get_uf_fraction(self, date, total, addcost):
        """
        Calculates the amount of money per film going to unifilm

        PARAMETERS:
        - date: date of movie

        RETURN:
        - Unifilm-fraction -> Float
        """
        return round(((total * self.uf_fraction)-addcost),2)
    
    def get_ck_fraction(self, total):

        return round(total * (1-self.uf_fraction), 2)
    
    def get_total_sv(self, tickets, club, price, pricec):
        return tickets*price+club*pricec

    def save_finances(self, date: str, ticket_price: float, club_price: float , addcost: float):
        total = self.get_total_sv(self.tickets[date], self.clubcards[date], ticket_price, club_price)
        dct = {"Ticket-Price": ticket_price, "Club-Price": club_price, "Sales-Volume": total, "Cash": total-addcost, "Unifilm": self.get_uf_fraction(date=date, total=total, addcost=addcost), "CK": self.get_ck_fraction(total=total), "Additional-Costs": addcost}
        self.db.loc[date] = dct
        self.add_total()
        self.save_db()


    def add_total(self):
        self.db.drop("Total", inplace=True, axis=0)
        dct = {"Ticket-Price": "-", "Club-Price": "-", "Sales-Volume": round(self.db["Sales-Volume"].sum(),2), "Cash": round(self.db["Cash"].sum(),2), "Unifilm": round(self.db["Unifilm"].sum(),2), "CK": round(self.db["CK"].sum(),2), "Additional-Costs": round(self.db["Additional-Costs"].sum(),2)}
        self.db.loc["Total"] = dct
        self.save_db()

    def update_database(self):
        self.db = pd.read_csv("./storage/WS2425/finance_db.csv").set_index("Date")
    
    