

class PlayCard:
    ranks_order = ("Jack", "Queen", "King", "Ace")

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        return PlayCard.ranks_order.index(self.rank) == PlayCard.ranks_order.index(other.rank)

    def __ne__(self, other):
        return PlayCard.ranks_order.index(self.rank) != PlayCard.ranks_order.index(other.rank)

    def __lt__(self, other):
        return PlayCard.ranks_order.index(self.rank) < PlayCard.ranks_order.index(other.rank)

    def __le__(self, other):
        return PlayCard.ranks_order.index(self.rank) <= PlayCard.ranks_order.index(other.rank)

    def __gt__(self, other):
        return PlayCard.ranks_order.index(self.rank) > PlayCard.ranks_order.index(other.rank)

    def __ge__(self, other):
        return PlayCard.ranks_order.index(self.rank) >= PlayCard.ranks_order.index(other.rank)


card1 = PlayCard("Ace", "Spades")
card2 = PlayCard("King", "Diamonds")
card3 = PlayCard("Queen", "Clubs")
card4 = PlayCard("Jack", "Hearts")

print(card4 < card1)
print(card3 > card4)
print(card1 >= card2)
print(card2 != card3)
