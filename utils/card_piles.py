"""Handle the behavior of the card pile in the center of the table."""


import typing as tp
import random as rdm
import warnings

from abc import ABC, abstractmethod

try:
    from .card import Card
except ImportError:
    from card import Card


class DrawPile(ABC):
    """
    Base class to be subclassed to define draw piles.
    Do not call directly.
    """
    def __init__(self, language: str = "french") -> None:
        """
        Parameters
        ----------
        language: str
            Language setting for the cards names.
        """
        self.full_list = self._set_cards_list(language)
        self.n_cards_total = len(self.full_list)
        self.cards_left = self.full_list
        self.retries = 4
    
    @staticmethod
    @abstractmethod
    def _set_cards_list(language: str) -> list[Card]:
        raise NotImplementedError
    
    @property
    def n_cards_left(self) -> int:
        """Number of cards left in the pile."""
        return len(self.cards_left)

    def __len__(self) -> int:
        return self.n_cards_left

    def _draw_one(self) -> Card | None:
        """
        Draw one card. Do not call directly,
        call the draw() method to draw cards properly instead.
        """
        if self.n_cards_left < 1:
            return None

        retries = self.retries

        while retries > 0:
            card = rdm.choice(self.cards_left)

            try:
                self.cards_left.remove(card)
            except ValueError:
                retries -= 1
                warnings.warn(
                    f"{self.__class__.__name__}: "
                    "An error occurred while trying to draw a card: "
                    "the card chosen among the pile does not actually "
                    "exist in said pile anymore. This error should not "
                    "be possible to occur in normal circumstances. "
                    f"Card causing the error: {card.name.value!r}.\n"
                    f"Retries left: {retries}"
                )
                continue
            else:
                break

        else:
            raise ValueError(
                f"{self.__class__.__name__}: "
                "Too many consecutive draw errors occurred, this pile is broken. "
                "Try relaunching the game from the start. If the bug persists, "
                "contact the developper and send the game logs to help debugging."
            )

        return card

    def draw(self, number: int = 1) -> list[Card] | None:
        """
        Draw given number of cards from the pile.
        
        Parameters
        ----------
        number: int
            Number of cards to draw. Defaults to 1.
        
        Returns
        -------
        list[Card] or None:
            Drawn cards in a list or None if `number` is not valid.
        """
        if number < 1:
            warnings.warn(
                f"{self.__class__.__name__}: "
                "Cannot draw a negative or null amount of cards."
            )
            return None

        drawn_cards = []

        while len(drawn_cards) < number:
            card = self._draw_one()

            if card is None:
                warnings.warn(
                    f"{self.__class__.__name__}: "
                    "This pile is empty, impossible to draw from it anymore."
                )
                break

            drawn_cards.append(card)

        return drawn_cards

    def distribute(
        self,
        n_players: int,
        n_cards_per_player: int,
        active_player_idx: int = 0,
        hands: list[list[Card]] | None = None
    ) -> list[list[Card]]:
        """
        Distribute given number of cards to each player, one by one,
        starting with the active player and going in the game order.

        Parameters
        ----------
        n_players: int
            Total number of players.

        n_cards_per_player: int
            Number of cards to distribute to each player.

        active_player_idx: int
            Index of the player hand that should receive the first card.

        hands: list[list[Card]], optional
            Hands of the players in index order in case a distribution occurs
            during a set. If not given, assumes set just began and initializes
            new hands for every player.

        Returns
        -------
        list[list[Card]]:
            Initialized or updated players hands.
        """
        if hands is None:
            hands = [[] for _ in range(n_players)]

        for _ in range(n_cards_per_player):
            for idx in range(n_players):
                true_idx = (idx + active_player_idx) % n_players
                draw = self.draw()
                assert draw is not None, (
                    "type checker assertion, never triggered."
                )
                hands[true_idx] += draw

        return hands

    def reset(self) -> None:
        """Refill the pile with all its cards, keeping other parameters."""
        self.cards_left = self.full_list


class MinorCardsDrawPile(DrawPile):
    """
    Main draw pile for minor cards and the special major card.
    The number of cards left in it can be shown to any player
    at any moment in the game.
    """
    @staticmethod
    def _set_cards_list(language: str) -> list[Card]:
        match language:
            case "french":
                names = []
                for family in Card.names_fr.families:
                    if isinstance(family, Card.names_fr.MAJEURES):
                        names.append(family.MORT)
                    else:
                        names += family.values()

            case "english":
                names = []
                for family in Card.names_eng.families:
                    if isinstance(family, Card.names_eng.MAJORS):
                        names.append(family.DEATH)
                    else:
                        names += family.values()

        return [Card(name) for name in names]


class MajorCardsDrawPile(DrawPile):
    """
    Draw pile for major cards obtained when revealing or
    completing combinations.
    The number of cards left in it can be shown to any player
    at any moment in the game.
    """
    @staticmethod
    def _set_cards_list(language: str) -> list[Card]:
        match language:
            case "french":
                names = Card.names_fr.MAJEURES.values()
                names.remove(Card.names_fr.MAJEURES.MORT.value)

            case "english":
                names = Card.names_eng.MAJORS.values()
                names.remove(Card.names_eng.MAJORS.DEATH.value)

        return [Card(name) for name in names]


class DiscardPile(list):
    """
    Base class to be subclassed to define discard piles.
    Do not call directly.
    """
    def __init__(self, language: str = "french", *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.language = language

    def show_cards(self, **kwargs: str) -> str:
        """Pretty print the list of cards in the pile."""
        cards_type_fr = kwargs.pop("cards_type_fr", "[insérer type]")
        cards_type_eng = kwargs.pop("cards_type_eng", "[insert type]")

        if self.language == "french":
            text = f"Cartes dans la défausse des cartes {cards_type_fr} :\n"
        
        elif self.language == "english":
            text = f"Cards in the {cards_type_eng} cards discard pile:\n"

        else:
            raise NotImplementedError(
                f"{self.__class__.__name__}: Language not recognized."
            )

        for card in self:
            text += f"- {card.name.value.replace('_', ' ')}\n"

        return text


class MinorCardsDiscardPile(DiscardPile):
    """
    Discard pile for destroyed minor cards.
    It can be consulted by any player at any moment in the game.
    """
    def __str__(self):
        return self.show_cards(cards_type_fr="mineures", cards_type_eng="minor")


class ActionCardsDiscardPile(DiscardPile):
    """
    Discard pile for used Action type major cards.
    It can be consulted by any player at any moment in the game.
    """
    def __str__(self):
        return self.show_cards(cards_type_fr="Action", cards_type_eng="Action")
