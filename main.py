from art import logo


print(logo)

bidders_dictionary = {}


def bidder():
    bid_ends = False
    while not bid_ends:
        name = input("What is your name? : ")
        amount = int(input("What's your bid? : $"))
        bidders_dictionary[name] = amount
        bidders_left = input(
            "Are there any other bidders? Type 'yes' or 'no'. ")

        if bidders_left.lower() == 'no':
            bid_ends = True
    max_bid_amount = 0
    for bidder in bidders_dictionary:
        amount = bidders_dictionary[bidder]
        if amount > max_bid_amount:
            max_bid_amount = amount
            winner = bidder
    print(f"{winner} won the bid with a bid of ${max_bid_amount}.")


bidder()
