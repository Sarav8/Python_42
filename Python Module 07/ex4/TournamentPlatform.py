from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """System to manage card tournaments, matches, and leaderboards."""

    def __init__(self):
        """Initialize the platform with empty card storage and stats."""
        self.cards = {}
        self.matches_played = 0
        self.status = "active"

    def register_card(self, card: TournamentCard) -> str:
        """Register a new card in the tournament system using its ID."""
        self.cards[card.id] = card
        return f"{card.id} registered successfully!"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Execute a match between two registered cards by their IDs."""
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        result = card1.attack(card2)
        self.matches_played += 1
        return result

    def get_leaderboard(self) -> list:
        """Return a list of cards sorted by rating in descending order."""
        cards = list(self.cards.values())
        c_ord = sorted(cards, key=lambda c: c.rating, reverse=True)
        leaderboard = []
        for i, cart in enumerate(c_ord, start=1):
            leaderboard.append(
                f"{i}. {cart.name} - Rating: {cart.rating} "
                f"({cart.wins}-{cart.losses})"
            )
        return leaderboard

    def generate_tournament_report(self) -> dict:
        """Provide a summary of the tournament platform status."""
        if len(self.cards) > 0:
            total_rating = sum(c.rating for c in self.cards.values())
            avg_rating = total_rating // len(self.cards)
        else:
            avg_rating = 0

        return {
            'total_cards': len(self.cards),
            'matches_played': self.matches_played,
            'avg_rating': avg_rating,
            'platform_status': self.status
        }
