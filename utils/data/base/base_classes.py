"""Base classes for every data storage classes in the game."""

import typing as tp
from enum import Enum, StrEnum, EnumMeta
from abc import abstractmethod, ABCMeta


class ABCEnumMeta(EnumMeta, ABCMeta):
    """Metaclass to handle both Abstract Base Class and Enum properties."""
    def __new__(mcls, *args, **kw):
        abstract_enum_cls = super().__new__(mcls, *args, **kw)
        # Only check abstractions if members were defined.
        if abstract_enum_cls._member_map_:
            try:  # Handle existence of undefined abstract methods.
                absmethods = list(abstract_enum_cls.__abstractmethods__)
                if absmethods:
                    missing = ', '.join(f'{method!r}' for method in absmethods)
                    plural = 's' if len(absmethods) > 1 else ''
                    raise TypeError(
                       f"cannot instantiate abstract class {abstract_enum_cls.__name__!r}"
                       f" with abstract method{plural} {missing}")
            except AttributeError:
                pass
        return abstract_enum_cls


class GameDataBase(Enum):
    """
    Base class for every data storage subclasses in the game.
    Should not be exported or used directly in higher levels of the project.
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
    def contains(cls, name: int | str | tp.Self) -> bool:
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


class Names(GameDataBase, StrEnum):
    """
    Base class for every list of names to store in the game data.
    Should not be exported or used directly in higher levels of the project.
    """
    ...


class Settings(ABCEnumMeta, GameDataBase):
    """
    Base class for settings classes.
    Should not be called directly in higher levels of the project.
    """
    @staticmethod
    @abstractmethod
    def get_error_msg() -> str:
        """Get error message when a wrong value is passed to the setting."""
        raise NotImplementedError


