"""Raw script of the game."""

import random as rdm
from dataclasses import dataclass

from utils.card import Card
from utils.card_piles import (
    MajorCardsDrawPile, MinorCardsDrawPile,
    MinorCardsDiscardPile, ActionCardsDiscardPile
)

@dataclass
class Player:
    name: str
    hand: list[Card]
    combinations: list[list[Card]]
    major_pile: list[Card]

    def adds_to_hand(self, cards: list[Card]):
        self.hand.extend(cards)

    def adds_to_major_pile(self, cards: list[Card]):
        self.major_pile.extend(cards)

def main(player_names: list[str], language: str) -> None:
    "Raw script of the game."
    # 1) Game initialization
    player_list = [Player(name, [], [], []) for name in player_names]
    n_players = len(player_names)
    # 1.1) Generate a full, randomly shuffled card pile for minor cards.
    minor_pile = MinorCardsDrawPile(language)
    minor_discard = MinorCardsDiscardPile(language)
    # 1.2) Generate a full, randomly shuffled card pile for major cards.
    major_pile = MajorCardsDrawPile(language)
    action_discard = ActionCardsDiscardPile(language)
    # 1.3) Distribute 5 minor cards to each player.
    init_hands = minor_pile.distribute(n_players, 5)
    # 1.4) Distribute 1 major card to each player.
    init_majors = major_pile.distribute(n_players, 1)

    for idx, player in enumerate(player_list):
        player.adds_to_hand(init_hands[idx])
        player.adds_to_major_pile(init_majors[idx])

    # 2) Game start, phase 1
    active_player_idx = 0
    while len(minor_pile) > 0:
        active_player = player_list[active_player_idx]
    # 2.1) Turn step 1: Activation of revealed Permanent cards.
    # 2.2) Turn step 2: Draw a minor card, except if an activated Permanent card said otherwise.
    # 2.3) Turn step 3: Reveal a new major card if wanted.
    # 2.4) Turn step 4: Create a new combination or complete an existing one, if possible and wanted.
    # NOTE: authorized combinations: pair, three/four of a kind, suite of 3+ cards.
    # 2.5) Turn step 5: If a combination has been created or completed, draw a major card.
    # 2.6) If all minor cards have been drawn, pass to phase 2, else pass to next player in phase 1
    # 3) Phase 2
    # 3.0) From now on, any player not having any card left in hand is out of game and doesn't play anymore.
    # No risk of getting Death card anymore, but cannot use any reserved major card, counter attacks, or earn any more points.
    # 3.1) Turn step 1: Activation of revealed Permanent cards (possible alternative drawing effect).
    # 3.2) Turn step 2: Draw a random card in a player hand, except if an activated Permanent card said otherwise.
    # 3.3) Turn step 3: Reveal a new major card if wanted.
    # 3.4) Turn step 4: Create a new combination or complete an existing one, if possible and wanted.
    # 3.5) Turn step 5: If major cards are not depleted yet, and a combination was created or completed, draw a major card.


if __name__ == "__main__":
    main()
