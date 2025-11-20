"""
Le Jeu du Dragon - main script.
"""


import typing as tp
import argparse as argp

# Robust local importations
try:
    from . import _parse_input_args, _clean_none_values
    from .utils import check_type
    from .config.settings import GAME_SETTINGS
    from .config.supported_settings import GameLanguage, GameMode, NBots
except ImportError:
    from . import _parse_input_args, _clean_none_values
    from utils import check_type
    from config.settings import GAME_SETTINGS
    from config.supported_settings import GameLanguage, GameMode, NBots, check_settings


def _get_command_line_args() -> argp.Namespace:
    """Command Line Interface handling."""
    parser = argp.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--player-name",
        default="Player_1",
        help="Name of the player (default: %(default)s)."
    )
    parser.add_argument(
        "--language",
        type=GameLanguage,
        default=GameLanguage.ENGLISH,
        help="Language used during the game (default: %(default)s)."
    )
    parser.add_argument(
        "--gamemode",
        type=GameMode,
        default=GameMode.SOLO,
        help="The game mode to enable (default: %(default)s)."
    )
    parser.add_argument(
        "--nbots",
        type=NBots,
        default=NBots.TWO,
        help="Number of bots to play with (default: %(default)s)."
    )
    args = parser.parse_args()
    return args


def _process_input_args(args_dict: dict[str, tp.Any]) -> dict[str, tp.Any]:
    """Assert input arguments and setup default values."""
    check_type(args_dict, "args_dict", (dict,))
    args_dict = _clean_none_values(args_dict)

    # Undefined values default setup
    args_dict.setdefault("player_name", "Player_1")
    args_dict.setdefault("language", GameLanguage.ENGLISH)
    args_dict.setdefault("gamemode", GameMode.SOLO)
    args_dict.setdefault("nbots", NBots.TWO)

    # Input values assertions
    check_type(args_dict["player_name"], "--player-name", (str,))
    check_settings(GameLanguage, args_dict["language"])
    check_settings(GameMode, args_dict["gamemode"])
    check_settings(NBots, args_dict["nbots"])

    # Input values conversions
    args_dict["language"] = GameLanguage(args_dict["language"])
    args_dict["gamemode"] = GameMode(args_dict["gamemode"])
    args_dict["nbots"] = NBots(args_dict["nbots"])

    return args_dict


def main(standalone: bool = True, **kwargs) -> None:
    """Main entry point."""
    args = _parse_input_args(_get_command_line_args, _process_input_args, standalone, **kwargs)
    # TODO: Setup settings activation and launch the game.
    

if __name__ == "__main__":
    main()