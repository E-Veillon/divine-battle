"""
Enum classes listing all possible card names in the game (english names).
"""

import typing as tp
from enum import auto

from cards_names_base import CardNames, CardNamesPack


class MajorCardNamesEng(CardNames):
    FOOL = auto()
    MAGICIAN = auto()
    HIGH_PRIESTESS = auto()
    EMPRESS = auto()
    EMPEROR = auto()
    HIEROPHANT = auto()
    LOVERS = auto()
    CHARIOT = auto()
    JUSTICE = auto()
    HERMIT = auto()
    WHEEL_OF_FORTUNE = auto()
    STRENGTH = auto()
    HANGED_MAN = auto()
    DEATH = auto()
    TEMPERANCE = auto()
    DEVIL = auto()
    TOWER = auto()
    STAR = auto()
    MOON = auto()
    SUN = auto()
    JUDGEMENT = auto()
    WORLD = auto()


class CupsCardNamesEng(CardNames):
    ACE_OF_CUPS = auto()
    TWO_OF_CUPS = auto()
    THREE_OF_CUPS = auto()
    FOUR_OF_CUPS = auto()
    FIVE_OF_CUPS = auto()
    SIX_OF_CUPS = auto()
    SEVEN_OF_CUPS = auto()
    EIGHT_OF_CUPS = auto()
    NINE_OF_CUPS = auto()
    TEN_OF_CUPS = auto()
    PAGE_OF_CUPS = auto()
    KNIGHT_OF_CUPS = auto()
    QUEEN_OF_CUPS = auto()
    KING_OF_CUPS = auto()


class PentaclesCardNamesEng(CardNames):
    ACE_OF_PENTACLES = auto()
    TWO_OF_PENTACLES = auto()
    THREE_OF_PENTACLES = auto()
    FOUR_OF_PENTACLES = auto()
    FIVE_OF_PENTACLES = auto()
    SIX_OF_PENTACLES = auto()
    SEVEN_OF_PENTACLES = auto()
    EIGHT_OF_PENTACLES = auto()
    NINE_OF_PENTACLES = auto()
    TEN_OF_PENTACLES = auto()
    PAGE_OF_PENTACLES = auto()
    KNIGHT_OF_PENTACLES = auto()
    QUEEN_OF_PENTACLES = auto()
    KING_OF_PENTACLES = auto()


class WandsCardNamesEng(CardNames):
    ACE_OF_WANDS = auto()
    TWO_OF_WANDS = auto()
    THREE_OF_WANDS = auto()
    FOUR_OF_WANDS = auto()
    FIVE_OF_WANDS = auto()
    SIX_OF_WANDS = auto()
    SEVEN_OF_WANDS = auto()
    EIGHT_OF_WANDS = auto()
    NINE_OF_WANDS = auto()
    TEN_OF_WANDS = auto()
    PAGE_OF_WANDS = auto()
    KNIGHT_OF_WANDS = auto()
    QUEEN_OF_WANDS = auto()
    KING_OF_WANDS = auto()


class SwordsCardNamesEng(CardNames):
    ACE_OF_SWORDS = auto()
    TWO_OF_SWORDS = auto()
    THREE_OF_SWORDS = auto()
    FOUR_OF_SWORDS = auto()
    FIVE_OF_SWORDS = auto()
    SIX_OF_SWORDS = auto()
    SEVEN_OF_SWORDS = auto()
    EIGHT_OF_SWORDS = auto()
    NINE_OF_SWORDS = auto()
    TEN_OF_SWORDS = auto()
    PAGE_OF_SWORDS = auto()
    KNIGHT_OF_SWORDS = auto()
    QUEEN_OF_SWORDS = auto()
    KING_OF_SWORDS = auto()


class EnglishCardNames(CardNamesPack):
    """English card names pack."""
    def __init__(self) -> None:
        self.MAJORS = MajorCardNamesEng
        self.WANDS = WandsCardNamesEng
        self.CUPS = CupsCardNamesEng
        self.PENTACLES = PentaclesCardNamesEng
        self.SWORDS = SwordsCardNamesEng

    def __getitem__(self, key: str) -> type[CardNames]:
        return self._getitem_factory()(self, key)

    @property
    def families(self) -> tuple[type[CardNames], ...]:
        """Tuple of each card family in the pack. The major family must be first."""
        return (
            self.MAJORS,
            self.WANDS,
            self.CUPS,
            self.PENTACLES,
            self.SWORDS
        )

    def get_all_names(self) -> list[str]:
        """Get list of Enum member names of all cards in the pack."""
        return sum(
            (
                self.MAJORS.names(),
                self.CUPS.names(),
                self.PENTACLES.names(),
                self.WANDS.names(),
                self.SWORDS.names()
            ), start=[]
        )

    def get_all_values(self) -> list[str]:
        """Get list of Enum member values of all cards in the pack."""
        return sum(
            (
                self.MAJORS.values(),
                self.CUPS.values(),
                self.PENTACLES.values(),
                self.WANDS.values(),
                self.SWORDS.values()
            ), start=[]
        )


if __name__ == "__main__":
    """Test routine for the pack and its families."""
    print(f"{MajorCardNamesEng.names()=}")
    print(f"{MajorCardNamesEng.values()=}")
    print(f"{MajorCardNamesEng.contains('fool')=}")
    print(f"{MajorCardNamesEng.contains('ace_of_cups')=}")

    print(f"{WandsCardNamesEng.names()=}")
    print(f"{WandsCardNamesEng.values()=}")
    print(f"{WandsCardNamesEng.contains('ace_of_wands')=}")
    print(f"{WandsCardNamesEng.contains('fool')=}")

    print(f"{CupsCardNamesEng.names()=}")
    print(f"{CupsCardNamesEng.values()=}")
    print(f"{CupsCardNamesEng.contains('ace_of_cups')=}")
    print(f"{CupsCardNamesEng.contains('fool')=}")

    print(f"{PentaclesCardNamesEng.names()=}")
    print(f"{PentaclesCardNamesEng.values()=}")
    print(f"{PentaclesCardNamesEng.contains('ace_of_pentacles')=}")
    print(f"{PentaclesCardNamesEng.contains('fool')=}")

    print(f"{SwordsCardNamesEng.names()=}")
    print(f"{SwordsCardNamesEng.values()=}")
    print(f"{SwordsCardNamesEng.contains('ace_of_swords')=}")
    print(f"{SwordsCardNamesEng.contains('fool')=}")

    print(f"{EnglishCardNames().MAJORS=}")
    print(f"{EnglishCardNames().WANDS=}")
    print(f"{EnglishCardNames().CUPS=}")
    print(f"{EnglishCardNames().PENTACLES=}")
    print(f"{EnglishCardNames().SWORDS=}")
