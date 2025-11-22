"""Define Card objects and special rules attached to some cards."""


import typing as tp

from data import (
    CardNames, EnglishCardNames, FrenchCardNames
    )
from effects import CardEffect


class Card:
    """
    Define properties of a card.
    
    Attributes
    ----------

    name: CardName
        The full name of the card, e.g. 'ace_of_cups'.

    face_value: str
        The value one can read on the card ('ace', 'three', 'king', '0', 'XV', ...).

    family: str
        The family ('major', 'cups', 'pentacles', 'wands', 'swords') the card belongs to.

    score_value: int
        The raw score value of the card, i.e. its worth in points regardless of its
        eventual special effects.

    special_effects: list[CardEffect]
        List of all special effects that can be applied by the card.

    partners: tuple[str, ...]
        For the cards having the 'partnership' effect, gives a tuple of the face values
        of the partner cards. For cards that do not have this effect, an empty tuple is
        returned. 
    """
    names_eng: EnglishCardNames = EnglishCardNames()
    names_fr: FrenchCardNames = FrenchCardNames()

    def __init__(self, name: str | CardNames) -> None:
        """
        Parameters
        ----------

        name: str | CardName
            Name of the card to instantiate.
        """
        self.name: CardNames = self._parse_name(name)

    @classmethod
    def _parse_name(cls, name: str | CardNames) -> CardNames:
        """Convert given name into an actual CardName object."""
        if isinstance(name, CardNames):
            return name

        if cls.names_eng.contains(name):
            for family in cls.names_eng.families:
                if family.contains(name):
                    return family(name)

        if cls.names_fr.contains(name):
            for family in cls.names_fr.families:
                if family.contains(name):
                    return family(name)

        raise ValueError(
                f"{cls.__name__}: {name!r} is not a valid card name."
            )

    @property
    def family(self: tp.Self) -> str:
        """
        The family ('major', 'cups', ...) this card belongs to.
        """
        if self.names_eng.is_major(self.name):
            return "major"

        if self.names_fr.is_major(self.name):
            return "majeure"

        return self.name.value.split("_")[-1]

    @property
    def face_value(self: tp.Self) -> str:
        """
        The face value of the card, e.g. 'three', 'king', ...
        for a minor card, or e.g. '0', 'XI', ... for a major card.
        """
        if self.is_minor_any():
            return self.name.value.split("_")[0]

        if self.names_eng.is_major(self.name):
            family_class = self.names_eng[self.family]

        elif self.names_fr.is_major(self.name):
            family_class = self.names_fr[self.family]

        int_value = family_class.values().index(self.name)
        roman_value = to_roman_num(int_value)

        assert roman_value is not None

        return roman_value

    @property
    def score_value(self: tp.Self) -> int:
        """Raw score value of the card, regardless of special effects."""
        if self.has_face_value("XIII"):
            return 0

        if self.names_eng.contains(self.name):
            family_class = self.names_eng[self.family]

        elif self.names_fr.contains(self.name):
            family_class = self.names_fr[self.family]

        assert family_class is not None

        return family_class.values().index(self.name) + int(self.is_minor_any())

    @property
    def special_effects(self: tp.Self) -> list[CardEffect]:
        """Special effects of the card for score calculations."""
        raise NotImplementedError

    def is_major_any(self: tp.Self) -> bool:
        """Whether given name corresponds to a major card name in any supported language."""
        return (
            self.names_fr.is_major(self.name) or
            self.names_eng.is_major(self.name)
        )

    def is_minor_any(self: tp.Self) -> bool:
        """Whether given name corresponds to a minor card name in any supported language."""
        return (
            self.names_eng.is_minor(self.name) or
            self.names_fr.is_minor(self.name)
        )

    def has_face_value(self: tp.Self, face_value: str) -> bool:
        """
        Whether the card has given face value. Face value is the value one can read
        on the card, i.e. 'ace', 'four', 'king', ... for minor cards, or '0', 'III',
        'XXI', ... for major cards. If raw score value in the game scope is what you
        want, use `has_score_value` instead.
        """
        return self.face_value == face_value

    def has_score_value(self: tp.Self, value: int) -> bool:
        """
        Whether the card has given raw score value. Raw score value is the number
        of points one player gets just by winning the card, regardless of any
        special effect. If face value is what you want, use `has_face_value`
        instead.
        """
        return self.score_value == value

    def has_special_effect(self: tp.Self, effect: CardEffect) -> bool:
        """Whether the card possess given special effect."""
        return effect in self.special_effects


def to_roman_num(value: int, contract_big: bool = False) -> str | None:
    """
    Convert any positive integer into Roman numerals (e.g. 12 -> 'XII').

    Parameters
    ----------

    value: int
        Number to convert into Roman numerals.

    contract_big: bool
        If set to `True`, when passed `value` is greater or equal to 11,000,
        the stacking 'M' numerals above the last thousand are contracted
        into 'M...'. Defaults to `False`, as the dots do not respect Roman
        numerals specs.

    Returns
    -------

    str | None
        String representation of the Roman numeral conversion of `value`.
        If wrong type or negative integer is passed, returns `None`.
        If the integer `0` is passed, it is equivalent to calling `str(0)`.
    """
    # Negatives do not exist in Roman numerals
    if not isinstance(value, int) or value < 0:
        return None

    # Trivial case
    if value == 0:
        return str(0)

    total = ""

    # Big numbers case (>= 11_000)
    if contract_big and value >= 11_000:
        value = value // 10_000
        total += "M..."

    # Count each character type
    num_M, int_left = value // 1_000, value % 1_000
    num_D, int_left = int_left // 500, int_left % 500
    num_C, int_left = int_left // 100, int_left % 100
    num_L, int_left = int_left // 50, int_left % 50
    num_X, int_left = int_left // 10, int_left % 10
    num_V, num_I = int_left // 5, int_left % 5

    # Build fully additive format
    M = "" + "M" * num_M
    D = "" + "D" * num_D
    C = "" + "C" * num_C
    L = "" + "L" * num_L
    X = "" + "X" * num_X
    V = "" + "V" * num_V
    I = "" + "I" * num_I
    total += M + D + C + L + X + V + I

    # Find and replace substraction patterns
    substractions = [
        ("IIII", "IV"), # 4
        ("VIV", "IX"), # 9
        ("XXXX", "XL"), # 40
        ("LXL", "XC"), # 90
        ("CCCC", "CD"), # 400
        ("DCD", "CM"), # 900
    ]

    for k, v in substractions:
        if total.find(k) == -1:
            continue
        total.replace(k, v)
    
    return total