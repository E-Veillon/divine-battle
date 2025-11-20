"""
Enum classes listing all possible card names in the game (french names).
"""

import typing as tp
from enum import auto

try:
    from .cards_names_base import CardName
except ImportError:
    from cards_names_base import CardName


class NomsCartesMajeuresFr(CardName):
    MAT = auto()
    BATELEUR = auto()
    PAPESSE = auto()
    IMPERATRICE = auto()
    EMPEREUR = auto()
    PAPE = auto()
    AMOUREUX = auto()
    CHARIOT = auto()
    JUSTICE = auto()
    ERMITE = auto()
    ROUE_DE_FORTUNE = auto()
    FORCE = auto()
    PENDU = auto()
    MORT = auto()
    TEMPERANCE = auto()
    DIABLE = auto()
    MAISON_DIEU = auto()
    ETOILE = auto()
    LUNE = auto()
    SOLEIL = auto()
    JUGEMENT = auto()
    MONDE = auto()


class NomsCartesBatonsFr(CardName):
    AS_DE_BATONS = auto()
    DEUX_DE_BATONS = auto()
    TROIS_DE_BATONS = auto()
    QUATRE_DE_BATONS = auto()
    CINQ_DE_BATONS = auto()
    SIX_DE_BATONS = auto()
    SEPT_DE_BATONS = auto()
    HUIT_DE_BATONS = auto()
    NEUF_DE_BATONS = auto()
    DIX_DE_BATONS = auto()
    VALET_DE_BATONS = auto()
    CAVALIER_DE_BATONS = auto()
    REINE_DE_BATONS = auto()
    ROI_DE_BATONS = auto()


class NomsCartesCoupesFr(CardName):
    AS_DE_COUPES = auto()
    DEUX_DE_COUPES = auto()
    TROIS_DE_COUPES = auto()
    QUATRE_DE_COUPES = auto()
    CINQ_DE_COUPES = auto()
    SIX_DE_COUPES = auto()
    SEPT_DE_COUPES = auto()
    HUIT_DE_COUPES = auto()
    NEUF_DE_COUPES = auto()
    DIX_DE_COUPES = auto()
    VALET_DE_COUPES = auto()
    CAVALIER_DE_COUPES = auto()
    REINE_DE_COUPES = auto()
    ROI_DE_COUPES = auto()


class NomsCartesDeniersFr(CardName):
    AS_DE_DENIERS = auto()
    DEUX_DE_DENIERS = auto()
    TROIS_DE_DENIERS = auto()
    QUATRE_DE_DENIERS = auto()
    CINQ_DE_DENIERS = auto()
    SIX_DE_DENIERS = auto()
    SEPT_DE_DENIERS = auto()
    HUIT_DE_DENIERS = auto()
    NEUF_DE_DENIERS = auto()
    DIX_DE_DENIERS = auto()
    VALET_DE_DENIERS = auto()
    CAVALIER_DE_DENIERS = auto()
    REINE_DE_DENIERS = auto()
    ROI_DE_DENIERS = auto()


class NomsCartesEpeesFr(CardName):
    AS_D_EPEES = auto()
    DEUX_D_EPEES = auto()
    TROIS_D_EPEES = auto()
    QUATRE_D_EPEES = auto()
    CINQ_D_EPEES = auto()
    SIX_D_EPEES = auto()
    SEPT_D_EPEES = auto()
    HUIT_D_EPEES = auto()
    NEUF_D_EPEES = auto()
    DIX_D_EPEES = auto()
    VALET_D_EPEES = auto()
    CAVALIER_D_EPEES = auto()
    REINE_D_EPEES = auto()
    ROI_D_EPEES = auto()


class FrenchCardNames:
    """Store classes of card families names."""
    def __init__(self) -> None:
        self.MAJEURES = NomsCartesMajeuresFr
        self.BATONS = NomsCartesBatonsFr
        self.COUPES = NomsCartesCoupesFr
        self.DENIERS = NomsCartesDeniersFr
        self.EPEES = NomsCartesEpeesFr
    
    @property
    def families(self) -> tuple[type[CardName], ...]:
        return (
            self.MAJEURES,
            self.BATONS,
            self.COUPES,
            self.DENIERS,
            self.EPEES
        )

    def __getitem__(self, key: str) -> type[CardName]:
        match key.lower():
            case "majeure" | "majeures":
                return self.MAJEURES
            case "batons":
                return self.BATONS
            case "coupes":
                return self.COUPES
            case "deniers":
                return self.DENIERS
            case "epees":
                return self.EPEES
            case str():
                raise KeyError(
                    f"{self.__class__.__name__}: {key!r} is not a valid key. "
                    "Supported keys are: 'majeures', 'batons', 'coupes', 'deniers', 'epees'."
                )
            case _:
                raise TypeError(
                    f"{self.__class__.__name__}: 'key' expected a type 'str', "
                    f"got {type(key).__name__!r} instead."
                )

    def get_all_names(self) -> list[str]:
        """Get list of Enum member names of all cards in the pack."""
        return sum(
            (
                self.MAJEURES.names(),
                self.COUPES.names(),
                self.DENIERS.names(),
                self.BATONS.names(),
                self.EPEES.names()
            ), start=[]
        )
    
    def get_all_values(self) -> list[str]:
        """Get list of Enum member values of all cards in the pack."""
        return sum(
            (
                self.MAJEURES.values(),
                self.COUPES.values(),
                self.DENIERS.values(),
                self.BATONS.values(),
                self.EPEES.values()
            ), start=[]
        )
    
    def is_minor(self, name: str | CardName) -> bool:
        """
        Check whether given name corresponds to any minor card in the pack.
        """
        return any(family.contains(name) for family in self.families[1:])
    
    def is_major(self, name: str | CardName) -> bool:
        """
        Check whether given name corresponds to any major card in the pack.
        """
        return self.MAJEURES.contains(name)

    def contains(self, name: str | CardName) -> bool:
        """
        Check whether given name corresponds to any card in the pack.
        """
        return any(family.contains(name) for family in self.families)


if __name__ == "__main__":
    print(f"{NomsCartesMajeuresFr.names()=}")
    print(f"{NomsCartesMajeuresFr.values()=}")
    print(f"{NomsCartesMajeuresFr.contains('mat')=}")
    print(f"{NomsCartesMajeuresFr.contains('as_de_coupes')=}")

    print(f"{NomsCartesBatonsFr.names()=}")
    print(f"{NomsCartesBatonsFr.values()=}")
    print(f"{NomsCartesBatonsFr.contains('as_de_batons')=}")
    print(f"{NomsCartesBatonsFr.contains('mat')=}")

    print(f"{NomsCartesCoupesFr.names()=}")
    print(f"{NomsCartesCoupesFr.values()=}")
    print(f"{NomsCartesCoupesFr.contains('as_de_coupes')=}")
    print(f"{NomsCartesCoupesFr.contains('mat')=}")

    print(f"{NomsCartesDeniersFr.names()=}")
    print(f"{NomsCartesDeniersFr.values()=}")
    print(f"{NomsCartesDeniersFr.contains('as_de_deniers')=}")
    print(f"{NomsCartesDeniersFr.contains('mat')=}")

    print(f"{NomsCartesEpeesFr.names()=}")
    print(f"{NomsCartesEpeesFr.values()=}")
    print(f"{NomsCartesEpeesFr.contains('as_d_epees')=}")
    print(f"{NomsCartesEpeesFr.contains('mat')=}")

    print(f"{FrenchCardNames().MAJEURES=}")
    print(f"{FrenchCardNames().COUPES=}")
    print(f"{FrenchCardNames().DENIERS=}")
    print(f"{FrenchCardNames().BATONS=}")
    print(f"{FrenchCardNames().EPEES=}")
