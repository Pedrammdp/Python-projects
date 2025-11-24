
auction = {}
continue_bidding = True

while(continue_bidding):
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n"))
    auction[name] = price
    ongoing = input("Is there someone else?\n")
    if (ongoing == "no"):
        continue_bidding = False
    print("\n" * 50)

def findHighestBidder(biddingDictionary):
    winner = ""
    highestBid = 0
    for bidder in biddingDictionary:
        bidAmount = biddingDictionary[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of ${highestBid}")

findHighestBidder(auction)