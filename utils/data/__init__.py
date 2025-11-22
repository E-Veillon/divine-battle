"""All possible cards names in the game, in all supported languages."""

from base import CardNames, CardNamesPack, EffectNames
from cards_names_english import EnglishCardNames
from cards_names_french import FrenchCardNames

__all__ = [
    "CardNames", "CardNamesPack", "EffectNames",
    "EnglishCardNames",
    "FrenchCardNames"
]