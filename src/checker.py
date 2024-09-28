import pandas as pd

_CARDS_INVENTORY = "./my_cards.csv"

ALL_CARDS = pd.read_csv("./all_cards.csv")["Card"].unique().tolist()

def add_card(cardname):

    try:
        df = pd.read_csv(_CARDS_INVENTORY)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Card', 'Quantity'])

    if cardname in df['Card'].values:
        df.loc[df['Card'] == cardname, 'Quantity'] += 1
    else:
        nueva_fila = pd.DataFrame({'Card': [cardname], 'Quantity': [1]})
        df = pd.concat([df, nueva_fila], ignore_index=True)

    df.to_csv(_CARDS_INVENTORY, index=False)

def check_cards(decklist):

    try:
        df = pd.read_csv(_CARDS_INVENTORY)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Card', 'Quantity'])

    df_deck_cards = pd.read_csv("./decks/" + decklist)

    df_my_cards = dict(zip(df_my_cards['Card'], df_my_cards['Quantity']))
    df_deck_cards = dict(zip(df_deck_cards['Card'], df_deck_cards['Quantity']))

    cards_ok = []
    cards_missing = []

    for card_required, quant_required in df_deck_cards.items():
        quant_have = df_my_cards.get(card_required, 0)
        if quant_have >= quant_required:
            cards_ok.append((card_required, quant_required))
        else:
            cards_missing.append((card_required, quant_required - quant_have))

    df_cards_ok = pd.DataFrame(cards_ok, columns=['Card', 'Quantity'])
    df_cards_missing = pd.DataFrame(cards_missing, columns=['Card', 'Quantity'])

    output = "Cards you have\n\n" +  df_cards_ok.to_string() + "\n------------------\n" + "Missing cards\n\n" + df_cards_missing.to_string()
    return output