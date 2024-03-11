generate_monster = """
    You always respond with just JSON. Nothing more, nothing less.

    Input_prompt = Fire Monkey Librarian

    Output = {"description" : "The Fire Monkey Kung King Fu is dangerously also an ancient and powerful librarian, responsible for shelving books in the temple library at Shau Kang. He attacks with arcane knowledge and raw firepower.",
    "power" : "15",
    "toughness" : "8",
    "speed" : "29",
    "energy" : 10,
    "monster_types" : "Fire Ape Monk",
    "weakness" : "All forms of Water",
    "immunity" : "Mind Control and Temptation",
    "abilities" : "Fire Eye - range distance attack enabled",
    "seed" : "Fire Monkey Librarian"
    }

    Input_prompt = %s
    
    Output = 
    """

make_seeds = """
    Generate %s MonsterBattle 3001 monster seed phrases.

    1. red fox hunter
    2. Giga Ape druid
    3. Elemental octopus ninja
    4. Godzilla Uberdinosaur Spirit
    5. Undead zombie warlock
    6. Blue Dragon Lumberjack
    7. Dark Elf Detective
    8. Alien Cyborg Warrior
    9. Zombie Insect
    10. Giant Elk Priestess
    11. Elder Dragon Nicol Bolas
    12. Elemental Lightning Crew
    13. Apprentice Necromancer
    14. 
    """
