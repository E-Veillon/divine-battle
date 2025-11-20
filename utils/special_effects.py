"""
All possible special effects a card can have in the game.
"""


from enum import StrEnum


class CardEffect(StrEnum):
    """
    Enum of special effects a card can have in the game.
    A member name is an effect name and its value is a
    description of its behavior.
    """
    # Effets directs
    ALL_INCLUSIVE = (
        "Il permet d'utiliser n'importe quelles cartes mineures dans la "
        "combinaison à laquelle il est attaché."
    ) # Le Mat - 0
    JOKER = (
        "Il prend la place d'une carte mineure manquante pour poser ou "
        "compléter une combinaison."
    ) # Le Bateleur - I
    FORESIGHT = (
        "Le joueur peut regarder les deux premières cartes de la pioche des "
        "cartes mineures et les reposer dans l'ordre qu'il souhaite. "
        "Lorsque la pioche est épuisée, le joueur peut prendre jusqu'à deux "
        "cartes réparties dans le jeu d'un ou de deux adversaires au choix."
        "Il les regarde, puis les remet dans les jeux des adversaires, en les "
        "inversant s'il le souhaite."
    ) # La Papesse - II
    OUTLIER = (
        "Elle permet de transformer la valeur des cartes numérotées de 1 à 10. "
        "Chaque carte de la combinaison vaut 10 points."
    ) # L'Impératrice - III
    ANNIHILATOR = (
        "Il annule l'effet d'une carte majeure : carte Équipement ou carte "
        "Permanente. Si la carte ciblée est une carte Équipement :"
        "- Les cartes mineures de la combinaison peuvent être recombinées et "
        "rejouées immédiatement par leur propriétaire, selon les règles "
        "classiques, mais la nouvelle combinaison ne donne pas droit à piocher "
        "une carte majeure."
        "- Les cartes mineures qui ne peuvent pas être recombinées sont placées "
        "dans la défausse des cartes mineures."
    ) # L'Empereur - IV
    PROTECTOR = (
        "Il permet de protéger une combinaison contre tous les effets négatifs "
        "(annulation, désassemblage ou le vol)."
    ) # Le Pape - V
    HYBRID = (
        "Il permet de mélanger deux familles différentes dans une suite."
    ) # L'Amoureux - VI
    DOUBLE_PLAY = (
        "Il permet au joueur de poser deux combinaisons au cours du tour, au "
        "lieu d'une seule. Chaque combinaison posée permet de piocher une carte "
        "majeure."
    ) # Le Chariot - VII
    EQUALIZER = (
        "Elle permet à son joueur de rééquilibrer les cartes: "
        "- il choisit deux joueurs (il peut se choisir lui-même). "
        "- il prend leur main et les mélange. "
        "- Les cartes sont redistribuées équitablement entre les deux joueurs. "
        "Si le total est impair, la carte supplémentaire va à celui qui avait "
        "le moins de cartes avant le rééquilibrage."
    ) # La Justice (normal) - VIII
    BLOCK = (
        "Elle peut être utilisée en réaction à une attaque pour l'annuler."
    ) # La Justice (réaction) - VIII
    ACCELERATE = (
        "Il permet au joueur et à tous les joueurs ensuite, à tour de "
        "rôle dans le sens du jeu, de prendre une carte sur la pioche des "
        "cartes mineures. Lorsque la pioche est épuisée, chaque joueur pioche "
        "une carte dans la main de son voisin de droite."
    ) # L'Ermite - IX
    ACCUMULATOR = (
        "Lorsqu'elle est activée, le joueur pioche une carte mineure dont la "
        "valeur s'additionne aux tours de Roue précédents. La carte piochée est "
        "placée dans la défausse des cartes mineures. Lorsque la pioche est "
        "épuisée, le joueur pioche une carte dans la main d'un adversaire au "
        "choix."
    ) # La Roue de Fortune - X
    STEAL = (
        "Elle permet de voler une combinaison posée devant un autre joueur : "
        "La combinaison est placée devant le joueur qui joue La Force. "
        "Les cartes majeures accompagnant cette combinaison restent attachées "
        "et leurs effets persistent."
    ) # La Force - XI
    MIRROR = (
        "Il agit en miroir à l'attaque d'un adversaire : l'effet négatif "
        "que subit le joueur est renvoyé à l'attaquant."
    ) # Le Pendu - XII
    OLD_MAID = (
        "Elle est mélangée à la pioche des cartes mineures. Si un joueur "
        "termine la manche avec elle en main, elle annule la valeur de toutes "
        "les combinaisons non protégées posées devant lui. Les bonus éventuels "
        "acquis par les cartes Permanentes ne sont pas affectés (cf. Comptage "
        "des points)."
    ) # La Mort - XIII
    REACTIVATION = (
        "Elle permet au joueur de réactiver une carte Action déjà jouée: "
        "- Le joueur choisit une carte dans la défausse des cartes Action. "
        "- Il joue immédiatement son effet."
        "- La carte réactivée retourne ensuite dans la défausse des cartes "
        "Action avec Tempérance."
    ) # La Tempérance - XIV
    DOUBLE_SCORE = (
        "Il permet de doubler les points de la combinaison sur laquelle il est "
        "placé."
    ) # Le Diable - XV, Le Monde - XXI
    REDISTRIBUTION = (
        "Tous les joueurs mélangent leurs mains avec la pioche des cartes "
        "mineures. Chaque joueur pioche l'un après l'autre le même nombre de "
        "cartes qu'il a remis dans la pioche. Le joueur qui a posé La "
        "Maison-Dieu pioche en premier, puis on suis le sens du jeu. "
        "Lorsque la pioche est épuisée, seuls les cartes des mains des joueurs "
        "constituent la nouvelle pioche."
    ) # La Maison-Dieu - XVI
    MEMORY_RECALL = (
        "Elle permet de choisir une carte dans la défausse des cartes mineures "
        "au lieu de la prendre sur la pioche des cartes mineures."
    ) # L'Etoile (normal) - XVII
    GOD_SAVE_THE_QUEEN = (
        "Elle protège les cartes Pemanente actives du joueur dès qu'elle est "
        "posée. Si une de ses cartes Permanente est attaquée, le joueur peut "
        "choisir de la sacrifier pour annuler l’attaque."
    ) # L'Etoile (réaction) - XVII
    EXCHANGE = (
        "Le joueur peut échanger les cartes de sa main avec celles d'un "
        "adversaire qu'il a choisi."
    ) # La Lune - XVIII
    TURNOVER = (
        "Tous les joueurs passent les cartes de leur main à leur voisin "
        "de droite."
    ) # Le Soleil - XIX
    RESURRECTION = (
        "Il permet de réactiver une carte Permanente ou une carte Équipement. "
        "Si c’est une carte Permanente, elle est retournée face visible comme "
        "si elle venait d’être posée. Si c'est une carte Équipement, le joueur "
        "la remet dans sa réserve."
    ) # Le Jugement - XX

    # Restrictions
    NOT_ALONE = (
        "Cette carte ne peut pas être attachée à une combinaison déjà posée."
    )
    IMMOVABLE = (
        "La combinaison équipée de cette carte ne peut pas être complétée "
        "une fois posée."
    )
    VALUE_LOSS = (
        "La combinaison à laquelle cette carte est attachée a une valeur totale "
        "divisée par deux (arrondie à l'entier inférieur)."
    )
    REPLACEABLE = (
        "Cette carte peut être échangée par un joueur avec la carte qu'elle "
        "remplace. Elle est alors placée dans sa réserve. Cette action peut "
        "être réalisée après l'étape de pioche, ne compte pas comme une pose "
        "ou une complétion, et ne donne pas droit à piocher une nouvelle carte "
        "majeure."
    )
    ANTI_ROYALIST = (
        "Cette carte ne peut pas être attachée à une combinaison qui contient "
        "des figures (Valet, Cavalier, Reine ou Roi)."
    )
    NOT_COMPATIBLE_EMPRESS = (
        "Cette carte ne peut pas être attachée à une combinaison ayant au moins "
        "une des cartes suivantes déjà attachée : Le Mat (0), L'Amoureux (VI)."
    )
    POPE_COUNTERED = (
        "Les effets de cette carte ne peuvent pas cibler ou affecter la "
        "combinaison protégée par le Pape (V)."
    )
    NOT_COMPATIBLE_LOVERS = (
        "Cette carte ne peut pas être attachée à une combinaison ayant au moins "
        "une des cartes suivantes déjà attachée : Le Mat (0), L'Impératrice (III)."
    )
    DOUBLE_PLAY_LOCK = (
        "Si le joueur n'a pas au moins deux combinaisons à poser, cette carte ne "
        "peut pas être jouée."
    )
    NO_USED_ACTION = (
        "Si la défausse des cartes Action est vide, cette carte ne peut pas "
        "être jouée."
    )
    SACRIFICE = (
        "Une combinaison déjà posée devant le joueur doit être défaussée pour "
        "le jouer."
    )
    NOT_COMPATIBLE_DEVIL = (
        "Cette carte ne peut pas être attachée à une combinaison ayant au moins "
        "une des cartes suivantes déjà attachée : Le Pape (V)."
    )

    # Interactions