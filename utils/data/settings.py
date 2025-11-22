"""Enum classes for all game settings."""

from enum import auto, IntEnum, StrEnum

from base import Settings, check_type


class GameLanguage(Settings, StrEnum):
    """Supported languages for the game."""
    ENGLISH = auto()
    FRENCH = auto()

    @staticmethod
    def get_error_msg() -> str:
        return "is not a valid supported language"


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


class NBots(Settings, IntEnum):
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()

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
        raise ValueError(f"{setting.name}: {value!r} {setting.get_error_msg()}.")