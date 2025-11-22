"""Class representing players, their status and possible actions."""

import random as rdm

from data.settings import check_settings, GameLanguage
from card import Card
from effects import CardEffect
from card_piles import (
    DrawPile, MajorCardsDrawPile, MinorCardsDrawPile,
    ActionCardsDiscardPile, MinorCardsDiscardPile
)

class MajorType:
    ACTION = "action"
    EQUIPMENT = "equipment"
    PERMANENT = "permanent"

class Player:
    name: str
    hand: list[Card]
    combinations: list[list[Card]]
    major_pile: list[Card]
    active_permanents: list[Card]
    inactive_permanents: list[Card]
    active_effects: list[CardEffect]
    _revealed_major_card: bool
    _played_combination: bool

    def __init__(self, name: str, language: str) -> None:
        check_settings(GameLanguage, language)
        self.name = name
        self.language = language
        self.hand = []
        self.combinations = []
        self.major_pile = []
        self.active_permanents = []
        self.inactive_permanents = []
        self.active_effects = []
        self._revealed_major_card = False
        self._played_combination = False

    # 2.1) Turn step 1: Activation of revealed Permanent cards.
    # 3.1) Turn step 1: Activation of revealed Permanent cards (possible alternative drawing effect).
    def activates_permanent_card(self, card: Card) -> None:
        """Player activates the effects of one of the permanent cards in their permanent area."""
        assert card in self.active_permanents, (
            f"The card {card} is not one of {self.name}'s active permanent cards."
        )
        for effect in card.special_effects:
            # player = the one activating the effect
            # target = one or several targeted entities (players, piles, areas, cards)
            # choice = If the effect can be different depending on a choice between alternatives
            effect.resolve(player=self, target=target, choice=(choice | None))

    # 2.2) Turn step 2: Draw a minor card, except if an activated Permanent card said otherwise.
    def adds_to_hand(self, cards: list[Card]):
        """Player adds cards to their hand."""
        self.hand.extend(cards)

    # 2.3) Turn step 3: Reveal a new major card if wanted.
    # 3.3) Turn step 3: Reveal a new major card if wanted.
    def reveals_major_card(self, card: Card) -> None:
        """Player reveals a major card from their major cards pile and activates its effects."""
        assert card in self.major_pile, (
            f"The card {card} is not one of {self.name}'s reserved major cards."
        )
        match card.type:
            case MajorType.ACTION:
                for effect in card.special_effects:
                    # player = the one activating the effect
                    # target = one or several targeted entities (players, piles, areas, cards)
                    # choice = If the effect can be different depending on a choice between alternatives
                    effect.resolve(player=self, target=target, choice=(choice | None))
            case MajorType.EQUIPMENT:
                raise NotImplementedError
            case MajorType.PERMANENT:
                raise NotImplementedError
        self._revealed_major_card = True

    # 2.4) Turn step 4: Create a new combination or complete an existing one, if possible and wanted.
    # NOTE: authorized combinations: two/three/four of a kind, suite of 3+ cards.
    # 3.4) Turn step 4: Create a new combination or complete an existing one, if possible and wanted.
    def plays_combination(self, cards: list[Card]) -> None:
        """Player puts a new combination in their combination area."""
        raise NotImplementedError
        self._played_combination = True

    def adds_to_combination(self, cards: list[Card], combination: list[Card]) -> None:
        """PLayer adds cards from their hand to one of their existing combinations."""
        raise NotImplementedError
        self._played_combination = True

    # 2.5) Turn step 5: If a combination was created or completed and major pile is not empty, draw a major card.
    # 3.5) Turn step 5: If a combination was created or completed and major pile is not empty, draw a major card.
    def adds_to_major_pile(self, cards: list[Card]):
        """Player adds cards to their pile of major cards."""
        self.major_pile.extend(cards)

    # 3.2) Turn step 2: Draw a random card in a player hand, except if an activated Permanent card said otherwise.
    def draws_from(self, source: DrawPile | list[Card], n_cards: int = 1) -> None:
        """Player draws cards from a draw pile or another player's hand."""
        if isinstance(source, DrawPile): # Drawing from a pile
            cards = source.draw(n_cards)
            assert cards is not None, f"The number of drawn cards cannot be negative, got {n_cards}."
            if isinstance(source, MinorCardsDrawPile):
                self.adds_to_hand(cards)
            elif isinstance(source, MajorCardsDrawPile):
                self.adds_to_major_pile(cards)
            else:
                raise NotImplementedError(
                    "Player behavior for given card pile is not implemented."
                )
        else: # Drawing from a player's hand
            drawn_cards = []
            for _ in range(n_cards):
                card = rdm.choice(source)
                source.remove(card)
                drawn_cards.append(card)
            self.adds_to_hand(drawn_cards)

    def count_score(self) -> int:
        """
        Calculate player's current score taking account of their combinations
        and appliable major cards score modification effects.
        """
        raise NotImplementedError

    def ends_turn(self) -> None:
        """Player finishes their turn."""
        self._revealed_major_card = False
        self._played_combination = False

    # ===== Status check methods =====
    def has_death(self) -> bool:
        """Whether the player has the Death (XIII) card in hand."""
        match self.language:
            case "english": return Card(Card.names_eng.MAJORS.DEATH) in self.hand
            case "french": return Card(Card.names_fr.MAJEURES.MORT) in self.hand
            case _: raise ValueError(
                f"Unsupported language {self.language} was set for the player {self.name}, "
                "impossible to check their hand content."
            )

    def has_empty_hand(self) -> bool:
        """Whether the player has any card left in hand."""
        return len(self.hand) == 0

    def has_combinations(self) -> bool:
        """Whether the player has at least one combination in their combination area."""
        return len(self.combinations) > 0

    def has_unused_majors(self) -> bool:
        """Whether the player has at least one major card in their major pile."""
        return len(self.major_pile) > 0

    def has_active_permanents(self) -> bool:
        """Whether the player has at least one active permanent card in their permanent area."""
        return len(self.active_permanents) > 0

    def has_inactive_permanents(self) -> bool:
        """Whether the player has at least one inactive permanent card in their permanent area."""
        return len(self.inactive_permanents) > 0

    def has_active_effects(self) -> bool:
        """Whether the player has at least one active effect ongoing."""
        return len(self.active_effects) > 0

    def has_played_combination(self) -> bool:
        """Whether the player has played or completed a combination this turn."""
        return self._played_combination

    def has_revealed_major(self) -> bool:
        """Whether the player has revealed a new major card this turn."""
        return self._revealed_major_card

    # 3.0) From now on, any player not having any card left in hand is out of game and doesn't play anymore.
    # No risk of getting Death card anymore, but cannot use any reserved major card, counter attacks, or earn any more points.





