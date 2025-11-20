"""Store all possible cards names in the game, in several languages."""

try:
    from .cards_names_base import CardName
    from .cards_names_english import EnglishCardNames
    from .cards_names_french import FrenchCardNames

except (ImportError, ModuleNotFoundError):
    from cards_names_base import CardName
    from cards_names_english import EnglishCardNames
    from cards_names_french import FrenchCardNames

__all__ = [
    "CardName", "EnglishCardNames", "FrenchCardNames"
]