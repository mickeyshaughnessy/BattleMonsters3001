generate_monster = """
    You always respond with just JSON. Nothing more, nothing less.

    Input_prompt = Fire Monkey Librarian

    Output = {"description" : "The Fire Monkey Kung King Fu is dangerously also an ancient and powerful librarian, responsible for shelving books in the temple library at Shau Kang. He attacks with arcane knowledge and raw firepower.",
    "power" : "15",
    "toughness" : "8",
    "speed" : "29",
    "energy" : 10,
    "monster_types" : "Fire Ape Monk",
    "abilities" : "Fire Eye - range distance attack enabled",
    "seed" = "%s"
    }

    Input_prompt = %s
    
    Output = 
    """
