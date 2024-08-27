from models import menuItem

def main_menu():

    menu = [
        menuItem.menuItem(1, "Home", "/"),
        menuItem.menuItem(2, "History", "history"),
        menuItem.menuItem(3, "People", "people"),
        menuItem.menuItem(4, "Areas", "/#areas"),
        menuItem.menuItem(5, "About us", "about"),    
    ]
    return menu
    