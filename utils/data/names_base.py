"""Base class for every list of names to store in the game data."""

import typing as tp
from enum import StrEnum


class Names(StrEnum):
    """Base class for every list of names to store in the game data."""
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
        Check whether given name corresponds to one of the members.
        """
        if isinstance(name, cls):
            return True

        try:
            card_name = cls(name)
        except (TypeError, ValueError):
            return False
        else:
            return True