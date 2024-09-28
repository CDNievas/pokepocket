import sys
import os

from simple_term_menu import TerminalMenu
from checker import check_cards, add_card, ALL_CARDS

def render_main_menu():
    options = ["[1] Card Inventory", "[2] Decks", "[q] Exit"]

    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if(menu_entry_index == 0):
        render_inv_menu()
    elif(menu_entry_index == 1):
        render_decks_menu()
    else:
        sys.exit()

def render_inv_menu():
    options = ["[1] Add cards"]

    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if(menu_entry_index == 0):
        print("TO DO")
        render_inv_add_cards_menu()
    else:
        print("TO DO")
        #render_inv_modify_quantity_menu()

def render_inv_add_cards_menu():

    while(True):
        terminal_menu = TerminalMenu(ALL_CARDS, search_key=None, show_search_hint=True)
        menu_entry_index = terminal_menu.show()
        add_card(ALL_CARDS[menu_entry_index])


def render_decks_menu():
    options = ["[1] Check decks"]

    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if(menu_entry_index == 0):
        render_decks_check_menu()
    else:
        print("TO DO")
        #render_decks_create_menu()


def render_decks_check_menu():

    options = (file for file in os.listdir("./decks/") if os.path.isfile(os.path.join("./decks/", file)))
    terminal_menu = TerminalMenu(options, search_key=None, show_search_hint=True, preview_command=check_cards, preview_size=1)
    menu_entry_index = terminal_menu.show()

if __name__ == "__main__":

    while(True):
        render_main_menu()

    check_cards(args.decklist)