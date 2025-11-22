"""Raw script of the game."""

import random as rdm
from dataclasses import dataclass

from utils.data.base import Settings
from utils.data.settings import check_settings, GameLanguage, NPlayers, NBots
from utils.player import Player
from utils.card import Card
from utils.card_piles import (
    MajorCardsDrawPile, MinorCardsDrawPile,
    MinorCardsDiscardPile, ActionCardsDiscardPile
)


def _interactive_init() -> tuple[str, int, int]:
    """Setup game settings in interactive way."""
    language = input(
        "Which language do you want to play with?\n"
        f"Currently supported languages: {', '.join(GameLanguage.values())}.\n"
    )
    n_players = int(input("How many people are playing (6 max)?\n"))
    assert n_players <= 6, "Too many players."
    if n_players < 6:
        n_bots = int(input(f"How many bots to add (6 - {n_players} = {6 - n_players} max)?\n"))
        assert n_players + n_bots <= 6, "Too many bots."
    else:
        n_bots = 0

    check_settings(GameLanguage, language)
    check_settings(NPlayers, n_players)
    check_settings(NBots, n_bots)

    return language, n_players, n_bots


def play_game(language: str, n_players: int, n_bots: int) -> None:
    """Main script of the game."""
    # 1) Game initialization
    players: list[Player] = []
    for idx in range(1, n_players + 1):
        name = input(f"Enter name for player {idx}:")
        players.append(Player(name, language))

    print("Loading...")
    # 1.1) Generate a full, randomly shuffled card pile for minor cards.
    minor_draw_pile = MinorCardsDrawPile(language)
    minor_discard = MinorCardsDiscardPile(language)
    # 1.2) Generate a full, randomly shuffled card pile for major cards.
    major_draw_pile = MajorCardsDrawPile(language)
    action_discard = ActionCardsDiscardPile(language)
    # 1.3) Distribute 5 minor cards to each player.
    init_hands = minor_draw_pile.distribute(n_players, 5)
    # 1.4) Distribute 1 major card to each player.
    init_majors = major_draw_pile.distribute(n_players, 1)

    for idx, player in enumerate(players):
        player.adds_to_hand(init_hands[idx])
        player.adds_to_major_pile(init_majors[idx])

    print("Game starts !")
    # 2) Game start, phase 1
    active_player_idx = 0
    # 2.6) If all minor cards have been drawn, pass to phase 2, else pass to next player in phase 1
    while len(minor_draw_pile) > 0:
        active_player = players[active_player_idx]
        print(f"It is {active_player.name}'s turn.")
        # 2.1) Turn step 1: Activation of revealed Permanent cards.
        if active_player.has_active_permanents():
            for active_perm in active_player.active_permanents:
                yes_no = input(f"{active_player.name}, do you want to activate {active_perm}? [Y/N]")
                if yes_no.lower() in {"y", "yes"}:
                    active_player.activates_permanent_card(active_perm)
        # 2.2) Turn step 2: Draw a minor card, except if an activated Permanent card said otherwise.
        draw_effects = tuple() # TODO: import from effects module.
        if any(draw_effect in active_player.active_effects for draw_effect in draw_effects):
            raise NotImplementedError
        else:
            active_player.draws_from(minor_draw_pile)
        # 2.3) Turn step 3: Reveal a new major card if wanted.
        if active_player.has_unused_majors():
            yes_no = input(f"{active_player.name}, do you want to reveal a major card? [Y/N]")
            if yes_no.lower() in {"y", "yes"}:
                player_majors = "\n".join(
                    [
                        f"{idx} - {card}" for idx, card
                        in enumerate(active_player.major_pile, start=1)
                    ]
                )
                card_idx = int(input(
                    "Which card do you want to play?\n"
                    f"{player_majors}"
                ))
                major_card = active_player.major_pile[card_idx - 1]
                active_player.reveals_major_card(major_card)
        # 2.4) Turn step 4: Create a new combination or complete an existing one, if possible and wanted.
        yes_no = input(
            f"{active_player.name}, do you want to play a new combination "
            "or complete an existing one? [Y/N]"
        )
        if yes_no.lower() in {"y", "yes"}:
            raise NotImplementedError
        # NOTE: authorized combinations: pair, three/four of a kind, suite of 3+ cards.
        # 2.5) Turn step 5: If a combination has been created or completed, draw a major card.
        if active_player.has_played_combination():
            active_player.draws_from(major_draw_pile)
        
        active_player.ends_turn()
        active_player_idx += 1
        active_player_idx %= len(players)

    # 3) Phase 2
    # 3.0) From now on, any player not having any card left in hand is out of game and doesn't play anymore.
    # No risk of getting Death card anymore, but cannot use any reserved major card, counter attacks, or earn any more points.
    # 3.1) Turn step 1: Activation of revealed Permanent cards (possible alternative drawing effect).
    # 3.2) Turn step 2: Draw a random card in a player hand, except if an activated Permanent card said otherwise.
    # 3.3) Turn step 3: Reveal a new major card if wanted.
    # 3.4) Turn step 4: Create a new combination or complete an existing one, if possible and wanted.
    # 3.5) Turn step 5: If major cards are not depleted yet, and a combination was created or completed, draw a major card.


if __name__ == "__main__":
    settings = _interactive_init()
    play_game(*settings)
