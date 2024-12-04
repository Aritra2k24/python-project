def winner(total_bid):
    max_bid = 0
    for key in total_bid:
        bid_amount = total_bid[key]
        if bid_amount > max_bid:
            max_bid = bid_amount
    print(f"{key} has won the bid by {max_bid}")



should_continue = True
bidders = {}
while should_continue:
    name = input("Type your name:")
    bid = int(input("How much bid would you want to put ?"))
    bidders[name] = bid
    next = input("to continue, type 'yes' and to stop , type 'no' :").lower()
    if next == 'no':
        should_continue = False
        winner(bidders)