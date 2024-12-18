from backend_pandas import TicketManager, FinanceManager
import reflex as rx


TiMg = TicketManager()
FiMg = FinanceManager()
app = rx.App()

def get_nr(lst):
    nr = ""
    for i in range(1, len(lst)-1):
        nr+=lst[i] 
    return nr

def set_nr(nr: str):
    lst = []
    nr = nr.split(",")
    for elem in nr:
        lst.append(int(elem.strip()))
    return lst