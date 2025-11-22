"""
Class handling card effects resolution during the game.
"""

import typing as tp

from utils.data.effects_names import EffectNamesPack, EffectNames
from player import Player

class CardEffect:
    """An effect attached to a card."""
    names_pack: EffectNamesPack = EffectNamesPack()

    def __init__(self, name: str | EffectNames) -> None:
        """
        Parameters
        ----------

        name: str | EffectNames
            Name of the effect to instantiate.
        """
        self.name: EffectNames = self._parse_name(name)
        self.description = self.name.value

    @classmethod
    def _parse_name(cls, name: str | EffectNames) -> EffectNames:
        """Convert given name into an actual CardName object."""
        if isinstance(name, EffectNames):
            return name

        if cls.names_pack.contains(name):
            for effect_type in cls.names_pack.effects_types:
                if effect_type.contains(name):
                    return effect_type(name)

        raise ValueError(
                f"{cls.__name__}: {name!r} is not a valid card name."
            )

    def resolve(
        self, player: Player, target: tp.Any | None = None, choice: str | None = None
    ) -> None:
        """
        Apply instructions of the effect.
        
        Parameters
        ----------
        player: Player
            Player activating the effect.
        target: Any, optional
            Target of the effect, if needed.
        choice: str, optional
            Choice between several effect cases, if appliable.
        """