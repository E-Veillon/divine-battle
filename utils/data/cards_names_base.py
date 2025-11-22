"""
Base class for handling card names enum classes.
"""

import typing as tp
from abc import ABC, abstractmethod
from collections.abc import Callable

from names_base import Names


class CardNames(Names):
    """
    Base class for handling families' cards names enum classes.
    In order to implement a new card family language, inherit from this class
    and only define all card names in the family as capitalized enum members.
    Do not call this class directly.
    """
    ...


class CardNamesPack(ABC):
    """
    Abstract base class handling card pack classes for each language.
    In order to implement a new card pack language, inherit from this class.
    Do not call this class directly.
    """
    @abstractmethod
    def __getitem__(self, key: str) -> type[CardNames]:
        """
        Get a family from name query. See the '_getitem_factory()' method
        for more infos on how to implement this method properly in subclasses.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def families(self) -> tuple[type[CardNames], ...]:
        """Tuple of each card family in the pack. The major family must be first."""
        raise NotImplementedError

    @abstractmethod
    def get_all_names(self) -> list[str]:
        """Get list of Enum member names of all cards in the pack."""
        raise NotImplementedError

    @abstractmethod
    def get_all_values(self) -> list[str]:
        """Get list of Enum member values of all cards in the pack."""
        raise NotImplementedError

    def _getitem_factory(self) -> Callable[[tp.Self, str], type[CardNames]]:
        """
        Factory method to get consistent __getitem__ magic method across packs.
        Call this method and call its return when implementing __getitem__ in subclasses.
        """
        def custom_getitem(self: tp.Self, key: str) -> type[CardNames]:
            major_family = self.families[0]
            minor_family_1 = self.families[1]
            minor_family_2 = self.families[2]
            minor_family_3 = self.families[3]
            minor_family_4 = self.families[4]

            match key.lower():
                case major_family.name:
                    return major_family
                case minor_family_1.name:
                    return minor_family_1
                case minor_family_2.name:
                    return minor_family_2
                case minor_family_3.name:
                    return minor_family_3
                case minor_family_4.name:
                    return minor_family_4
                case str():
                    fams_str = ', '.join([f"{family.name!r}" for family in self.families])
                    raise KeyError(
                        f"{self.__class__.__name__}: {key!r} is not a valid key. "
                        f"Supported keys are: {fams_str}."
                    )
                case _:
                    raise TypeError(
                        f"{self.__class__.__name__}: 'key' expected a type 'str', "
                        f"got {type(key).__name__!r} instead."
                    )
        return custom_getitem

    def is_minor(self, name: str | CardNames) -> bool:
        """
        Check whether given name corresponds to any minor card in the pack.
        """
        return any(family.contains(name) for family in self.families[1:])
    
    def is_major(self, name: str | CardNames) -> bool:
        """
        Check whether given name corresponds to any major card in the pack.
        """
        return self.families[0].contains(name)

    def contains(self, name: str | CardNames) -> bool:
        """
        Check whether given name corresponds to any card in the pack.
        """
        return any(family.contains(name) for family in self.families)


if __name__ == "__main__":
    print(CardNames.names())
    print(CardNames.values())
    print(CardNames.contains("ace_of_cups"))