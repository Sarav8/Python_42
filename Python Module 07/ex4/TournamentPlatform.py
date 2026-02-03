from ex4 import TournamentCard

class TournamentPlatform ():
    def __init__(self):
        self.cards = {}
        self.matches_played = 0
        self.status = "active"

    
    def register_card(self, card: TournamentCard) -> str:
        self.cards[ card.id ] = card
        return f"{card.id} register satisfully!"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        result = card1.attack(card2)
        self.matches_played += 1
        return result

    def get_leaderboard(self) -> list:
        cards = list(self.cards.values())
        c_ord = sorted(cards, key=lambda c: c.rating, reverse=True)
        leaderboard = []
        for i, cart in enumerate(c_ord, start=1):
            leaderboard.append(f"{i}. {cart.name} - Rating: {cart.rating} ({cart.wins}-{cart.losses})")
        return leaderboard

    def generate_tournament_report(self) -> dict:
        if len(self.cards) > 0:
            avg_rating = sum(c.rating for c in self.cards.values()) // len(self.cards)
        else:
            avg_rating = 0

        result = {
            'total_cards': len(self.cards),
            'matches_played': self.matches_played,
            'avg_rating': avg_rating,
            'platform_status': self.status
        }
        return result
