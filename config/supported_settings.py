"""Enum classes of all supported settings."""

import typing as tp
from enum import Enum, StrEnum, IntEnum, auto
from abc import abstractmethod

try:
    from ..utils import check_type
except (ImportError, ModuleNotFoundError):
    from utils import check_type


class Settings(Enum):
    """
    Base class to extend settings classes functionalities.
    Not to be called directly.
    """
    err_msg: tp.ClassVar[str]

    @classmethod
    def names(cls) -> list[str]:
        """Get the list of all Enum members names."""
        return list(member.name for member in cls)

    @classmethod
    def values(cls) -> list[str]:
        """Get the list of all Enum members values."""
        return list(member.value for member in cls)

    @classmethod
    def contains(cls, value: str | int | tp.Self) -> bool:
        """
        Check whether given value corresponds to one of the members.
        """
        if isinstance(value, cls):
            value = value.value

        try:
            setting_value = cls(value)
        except (TypeError, ValueError):
            return False
        else:
            return True

    @staticmethod
    @abstractmethod
    def get_error_msg() -> str:
        raise NotImplementedError


class NPlayers(Settings, IntEnum):
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()

    @staticmethod
    def get_error_msg() -> str:
        return "is not a supported number of players"


class GameLanguage(Settings, StrEnum):
    """Supported languages for the game."""
    ENGLISH = auto()
    FRENCH = auto()

    @staticmethod
    def get_error_msg() -> str:
        return "is not a valid supported language"


class GameMode(Settings, StrEnum):
    """Supported game modes."""
    SOLO = auto()
    MULTIPLAYER = auto()

    @staticmethod
    def get_error_msg() -> str:
        return "is not a supported game mode"


class NBots(Settings, IntEnum):
    ONE = auto()
    TWO = auto()
    THREE = auto()

    @staticmethod
    def get_error_msg() -> str:
        return "is not a supported number of bots"


def check_settings(setting: type[Settings], value: str | int | Settings) -> None:
    """
    Assert that given value is supported by corresponding setting.

    Parameters
    ----------
    setting: type[Settings]
        Class object inheriting from the Settings class to check.

    value: str | Settings
        Input value to verify.

    Raises
    ------
    TypeError
        If `value` is not of a supported type.

    ValueError
        If `value` is not supported by the `setting` class.
    """
    check_type(value, "value", (str, int, Settings))
    if not setting.contains(value):
        raise ValueError(f"{setting.__name__}: {value!r} {setting.get_error_msg()}.")