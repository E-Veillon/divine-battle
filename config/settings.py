"""Store and change modifiable game settings."""

import typing as tp

try:
    from .supported_settings import GameLanguage, GameMode, NBots
except (ImportError, ModuleNotFoundError):
    from supported_settings import GameLanguage, GameMode, NBots


GAME_SETTINGS: dict[str, tp.Any] = {
    "Language": GameLanguage.ENGLISH,
    "Game_mode": GameMode.SOLO,
    "n_bots": NBots.TWO
}