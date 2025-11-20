"""
Base class for handling card names enum classes.
"""

import typing as tp
from enum import StrEnum


class CardName(StrEnum):
    """
    Base class for handling card names enum classes.
    """
    @classmethod
    def names(cls) -> list[str]:
        """Get the list of all Enum members names."""
        return list(member.name for member in cls)

    @classmethod
    def values(cls) -> list[str]:
        """Get the list of all Enum members values."""
        return list(member.value for member in cls)

    @classmethod
    def contains(cls, name: str | tp.Self) -> bool:
        """
        Check whether given name corresponds to one of the cards.
        """
        if isinstance(name, cls):
            name = name.value

        try:
            card_name = cls(name)
        except (TypeError, ValueError):
            return False
        else:
            return True


if __name__ == "__main__":
    print(CardName.names())
    print(CardName.values())
    print(CardName.contains("ace_of_cups"))