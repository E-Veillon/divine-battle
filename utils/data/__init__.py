"""All possible cards names in the game, in all supported languages."""

from cards_names_base import CardNames, CardNamesPack
from cards_names_english import EnglishCardNames
from cards_names_french import FrenchCardNames

__all__ = [
    "CardNames", "CardNamesPack",
    "EnglishCardNames",
    "FrenchCardNames"
]