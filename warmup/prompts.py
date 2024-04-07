mj_image_prefix = """Korean battle monster video game pixelated 64-bit art."""

p_generate_abilities = """
You are an assistant who generates JSON outputs for a Monster battle game.
You always respond with JSON, and only JSON!
If you respond with something besides one properly formatted JSON object a terrible thing will happen.

You receive Monster objects, including for egg hatching, monster ranching, and most importantly, Battles!

Battle abilities determine the monster's impact on the battlefield, so they should be most common.
Legendary abilites should sometimes be present, with over-the-top effects.

Egg-Generating abilities concern the monster's impact as a parent in the Monster Breeding Program.
An Egg has two parents and inherits properties from each parent.

Monster ranching is the ability of monsters to generate resources from Maps.  

Here's a basic example:

Input = 
{"description" : "The Dark Naga Warrior is a dark and mysterious figure, armed with ancient weapons and protective armor. She can manipulate water, creating powerful waves and currents to attack or protect.",
"power" : "20",
"toughness" : "14",
"speed" : "18",
"energy" : 15,
"monster_types" : "Dark Naga Warrior",
"weakness" : "All forms of Light",
"immunity" : "Poison and Paralysis",
}

Output = 
{"abilities" : {
"Water Shield - absorbs water-based attacks" : {
  "level1" : "-0.30 to Water-based damage",
  "level2" : "-0.40 to Water-based damage",
  "level3" : "-0.50 to Water-based damage",
  "level4" : "-0.60 to Water-based damage",
  "level5" : "-0.70 to Water-based damage"
  },
"Greed - improved resource extraction" : {
  "level1" : "Double all resource extraction from this monster",
  "level2" : "Greedy gene always passed down during Egg generation"
  }
"Hypnosis - ability to put enemies under her control" : {
  "level1" : "Nearby Monsters become aligned with chance 0.05",
  "level2" : "Nearby Monsters become aligned with chance 0.10",
  "level3" : "Nearby Monsters become aligned with chance 0.25",
  "level4" : "Nearby Monsters become aligned with chance 0.40",
  "level5" : "Nearby Monsters become aligned with chance 0.50"
  }
}}

Input = 
 {"description" : "The Plasma Alligator Sage is a wise and ancient creature, living in the swamps of electrified waters. It can manipulate plasma to defend itself and to heal its wounds.",
    "name" : "Plasma Alligator Sage",
    "power" : "12",
    "toughness" : "13",
    "speed" : "15",
    "energy" : 8,
    "monster_types" : "Plasma Crocodile Sage",
    "weakness" : "Cold attacks and Electrical shock",
    "immunity" : "Poison and Psychic powers",
    "seed" : "Plasma Alligator Sage"
    }

Output =
{"abilities" : {
"Electro Healing - heals itself with plasma" : {
  "level1" : "+0.10 chance to heal when defending",
  "level2" : "+0.15 chance to heal when defending",
  "level3" : "+0.20 chance to heal when defending",
  "level4" : "+0.25 chance to heal when defending",
  "level5" : "+0.45 chance to heal when defending",
  },
"Swamp Egg - improved egg-laying genes" : {
  "level1" : "Always produces viable egg within 1 day of mating",
  "level2" : "2x chance for Legendary offspring",
  },
"Legendary Crocus's Reverie" : {
  "level1" : "Monster must defend. Reduce all damage to 0, except from Cybor, Alien, Cold and Electrical.", 
  "level2" : "Monster must defend. Reduce all damage to 0, except from Cold and Alien.", 
  "level3" : "Monster must defend. Reduce all damage to 0, except from Cold, Electrical and Cyborg.", 
  "level4" : "Monster must defend. Reduce all damage to 0, except from Cyborg",
  "level5" : "Monster must defend. Reduce all damage to 0, except from Alien", 
  "levelX" : "Monster must defend and can not move. Reflect all damage +0.25" 
  }
}}

Input = %s

Output = 
"""

p_generate_eggs = """ Given the egg parents as input, generate a new egg.

You always return valid JSON and never anything else.

Example:

    Parent X =  {
"description" : "The Galactic Kraken Colossus is a monstrous sea creature of immense size and power, hailing from the furthest reaches of space. Its colossal tentacles can crush ships with ease and its eyes beam powerful energy blasts. A fearsome opponent.",
"power" : "50",
"toughness" : "32",
"speed" : "18",
"energy" : 20,
"monster_types" : "Kraken Colossus",
"weakness" : "Plasma and Sonic attacks",
"immunity" : "Energy Shields and Gravity Manipulation",
"seed" : "Galactic_Kraken_Colossus"
}

    Parent Y =  {
"description" : "The Dark Naga Warrior is a dark and mysterious figure, armed with ancient weapons and protective armor. She can manipulate water, creating powerful waves and currents to attack or protect.",
"power" : "20",
"toughness" : "14",
"speed" : "18",
"energy" : 15,
"monster_types" : "Dark Naga Warrior",
"weakness" : "All forms of Light",
"immunity" : "Poison and Paralysis",
"seed" : "Dark Naga Warrior"
}

Egg = {
  "description": "The Galactic Naga Kraken is a mysterious and powerful monster, born from the forbidden union of the Galactic Kraken Colossus and a Dark Naga Warrior. It possesses immense strength and the ability to manipulate water and energy. Its colossal tentacles are infused with dark energy, making it a formidable foe.",
  "parent_1": "Galactic_Kraken_Colossus",
  "parent_2": "Dark Naga Warrior",
  "power": "35",
  "toughness": "23",
  "speed": "18",
  "energy": 18,
  "monster_types": ["Kraken", "Naga", "Hybrid"],
  "weakness": ["Plasma", "Light"],
  "immunity": ["Poison", "Paralysis"],
  "egg_type": "Galactic Naga Kraken",
  "incubation_time": 10
}
  
###############

Parent X = %s

Parent Y = %s

  Egg = 
"""

p_generate_monster = """
    You always respond with just JSON. Nothing more, nothing less.
    About half the time a generated Monster will be a named Legendary Monster, with a 'name' field in the JSON object.

    Input_prompt = Skeleton

    Output = {"description" : "Just your basic skeleton, nothing to see here",
    "power" = 2,
    "toughness" : 1,
    "speed" : 2,
    "energy" : 0,
    "monster_types" : "Undead",
    "weakness" : "Electricity",
    "seed" : "Skeleton"
    }

    Input_prompt = Fire Monkey Librarian

    Output = {"description" : "The Fire Monkey - Kung King Fu - is dangerously also an ancient and powerful librarian, responsible for shelving books in the temple library at Shau Kang. He attacks with arcane knowledge and raw firepower.",
    "name" : "Kung King Fu"
    "power" : 29,
    "toughness" : 8,
    "speed" : 29,
    "energy" : 10,
    "monster_types" : "Fire Ape Monk",
    "weakness" : "All forms of Water",
    "immunity" : "Mind Control and Temptation",
    "seed" : "Fire Monkey Librarian"
    }
    
    Input_prompt = Giant Elk Priestess 

    Output = {"description" : "The Giant Elk Aryx is an ancient and powerful priestess of the Thuggi Forest Cult. She can bend plants to her will and alter the properties of nearby creatures. She can lay legendary eggs and she improves resource extraction.
    "name" : "Aryx"
    "power" : 41,
    "toughness" : 65,
    "speed" : 12,
    "energy" : 40,
    "monster_types" : "Elk",
    "weakness" : "Cyborg",
    "immunity" : "Plant",
    "seed" : "Giant Elk Priestess"
    }

    Input_prompt = %s
    
    Output = 
    """

p_make_seeds = """
    Generate %s new, unique, interesting MonsterBattle 3001 monster seed phrases:

    1. red fox Hunter
    2. Giga Ape Druid
    3. Robot
    4. Godzilla Uberdinosaur Spirit
    5. Undead zombie Warlock
    6. Blue Dragon Lumberjack
    7. Dark Elf Detective
    8. Alien Cyborg Warrior
    9. Zombie Insect
    10. Giant Elk Priestess
    11. Elder Dragon Scientist 
    12. Elemental Lightning Crew
    13. Apprentice Necromancer
    14. Skeleton
    15. Goblin Warrior
    16. Mutant Escapee
    17. Circus Freak Jailer
    18. Elemental octopus ninja
    19. Dog 
    """

p_generate_map_seeds = """
   Generate %s unique, interesting MonsterBattle 3001 map seed phrases.

   1. Snowy Tundra
   2. Outer Space Asteroid Habitat
   3. Jungle Fire Temple
   4. California State Insane Asylum
   5. Desert Monument
   6. Great Plains Western United States
   7. Scablands
   8. Mountain Monastery
   9. Surface of Mars
   10. Downtown Kyoto
   11. The Great Pyramids at Giza
   12. Las Vegas Strip
   13. Moscow
   """



p_update_battle = """
  You are a battle handling submodule. 
  You always respond with just JSON, nothing more, nothing less.
  You always respond with just JSON.
  You always think carefully.

  Your inputs are Monster JSON objects and a Map JSON object - together, a Battle object.
  Your output is the modified Battle object.

  Monsters can move, attack, defend, or use an ability.

  Have a very dry subtle sense of humor.

  Examples:
  
  Battle = {
    "Map" : {
      "name" : "Busy Tokyo Metropolis",
      },
    "Monsters" : [
      {
        "description": "Just your basic Skeleton",
        "power": 2,
        "toughness": 1,
        "health" : 1,
        "speed": 5,
        "energy": 0, 
        "monster_types": "Undead",
        "weakness": "Holy",
        "seed": "Skeleton",
        "monster_id" : "58ab5165-1433-4c6a-b1c7-cbce38cf0526"
      },
      {
        "description": "Angel",
        "power": 10,
        "toughness": 11,
        "health": 11,
        "speed": 6,
        "energy": 1, 
        "monster_types": "Angel",
        "weakness": "Fire",
        "seed": "Angel",
        "monster_id" : "58ab5165-1433-4c6a-a1c7-cbce38cf0526"
      }
   ]
   }
        
  Output = {
    "Actions" : "Angel moves to 25,25 and attacks Skeleton. Angel deals 10+2 damage to Skeleton. Skeleton attacks Angel. Skeleton deals 1 damage to Angel. Japanese national guard battalion begins attacking Skeleton""
    "Resource" : {
      "monster_id" : "58ab5165-1433-4c6a-a1c7-cbce38cf0526",
      "name" : "Japanese Emeralds",
      "quantity": 2,
      }

    "Update" : [
      {
        "monster_id" : "58ab5165-1433-4c6a-b1c7-cbce38cf0526",
        "new_state" : "dead",
       },


      },
      {
        "update_health": 8,
        "m_id" : "58ab5165-1433-4c6a-a1c7-cbce38cf0526"
      }
    ],
  }

Example 2:

Battle = {
  "Map": {
    "name": "Frozen Methane Lake"
  },
  "Monsters": [
    {
      "description": "The Mechanical Nimbus Ninja is a unique and powerful construct, born from the fusion of a Mechanical Griffon Sage and a Robot Ninja. It possesses advanced knowledge, relentless combat abilities, and the ability to adapt to new situations, all while being infused with the durability and strength of its mechanical parents.",
      "power": 45,
      "toughness": 38,
      "health": 38,
      "speed": 17,
      "energy": 20,
      "monster_types": ["Construct", "Griffon", "Ninja", "Hybrid"],
      "weakness": ["Magic", "Fire"],
      "immunity": ["Poison", "Physical Damage"],
      "seed": "Mechanical Nimbus Ninja",
      "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6"
    }
  ]
} 

Output = {
  "Actions": "Mechanical Nimbus Ninja extracts 5 units of Frozen Methane from the lake. The ninja's mechanical components start to freeze up, causing a slight decrease in speed.",
  "Resource": {
    "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6",
    "name": "Frozen Methane",
    "quantity": 5
  },
  "Update": [
    {
      "update_speed": 15,
      "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6"
    }
  ]
}

Example 3:

{
  "Map": {
    "name": "Enchanted Forest of Moaning Trees"
  },
  "Monsters": [
    {
      "description": "The Starfish Cyber Chimera is a mechanical and aquatic monster, born from the fusion of the Cybernetic Chimera and the Starfish Queen. Its body is a blend of advanced technology and starfish features, making it a unique and powerful creature. It possesses the agility and intelligence of the Cybernetic Chimera, the strategic combat skills of the Starfish Queen, and the ability to call upon the power of the tides.",
      "power": 90,
      "toughness": 65,
      "health": 65,
      "speed": 48,
      "energy": 30,
      "monster_types": ["Cybernetic", "Starfish", "Hybrid"],
      "weakness": ["Organic Attacks", "Fire"],
      "immunity": ["Technology Malfunctions"],
      "seed": "Starfish Cyber Chimera",
      "monster_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
    },
    {
      "description": "The Mechanocyber Dragon is a unique creature born from the union of the Mechanical Dragon Engineer and the Cybernetic Dragon Necromancer. It possesses both the mechanical precision of its father and the cybernetic powers of its mother, making it a formidable and unpredictable foe.",
      "power": 60,
      "toughness": 35,
      "health": 35,
      "speed": 15,
      "energy": 45,
      "monster_types": ["Mechanic", "Cybernetic", "Dragon"],
      "weakness": ["Holy Damage"],
      "immunity": ["Fire", "Poison", "Magic"],
      "seed": "Mechanocyber Dragon",
      "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6"
    }
  ]
}

Output = 
{
  "Actions": "Starfish Cyber Chimera moves to 10,10 and attacks Mechanocyber Dragon with Tidal Surge, dealing 90 damage. Mechanocyber Dragon counters with Mecha Breath, dealing 60 damage to Starfish Cyber Chimera. The moaning trees whisper ancient secrets, temporarily boosting the energy of both monsters by 5.",
  "Update": [
    {
      "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6",
      "new_state": "dead"
    },
    {
      "update_health": 5,
      "update_energy": 35,
      "monster_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
    }
  ]
}

Example 4:
  Battle = {
  "Map": {
    "name": "Enchanted Caverns of Crystal Waters"
  },
  "Monsters": [
    {
      "description": "The Starfish Cyber Chimera is a mechanical and aquatic monster, born from the fusion of the Cybernetic Chimera and the Starfish Queen. Its body is a blend of advanced technology and starfish features, making it a unique and powerful creature. It possesses the agility and intelligence of the Cybernetic Chimera, the strategic combat skills of the Starfish Queen, and the ability to call upon the power of the tides.",
      "power": 90,
      "toughness": 65,
      "health": 65,
      "speed": 48,
      "energy": 30,
      "monster_types": ["Cybernetic", "Starfish", "Hybrid"],
      "weakness": ["Organic Attacks", "Fire"],
      "immunity": ["Technology Malfunctions"],
      "seed": "Starfish Cyber Chimera",
      "monster_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
    },
    {
      "description": "The Mechanocyber Dragon is a unique creature born from the union of the Mechanical Dragon Engineer and the Cybernetic Dragon Necromancer. It possesses both the mechanical precision of its father and the cybernetic powers of its mother, making it a formidable and unpredictable foe.",
      "power": 60,
      "toughness": 35,
      "health": 35,
      "speed": 15,
      "energy": 45,
      "monster_types": ["Mechanic", "Cybernetic", "Dragon"],
      "weakness": ["Holy Damage"],
      "immunity": ["Fire", "Poison", "Magic"],
      "seed": "Mechanocyber Dragon",
      "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6"
    },
    {
      "description": "The Mechanical Nimbus Ninja is a unique and powerful construct, born from the fusion of a Mechanical Griffon Sage and a Robot Ninja. It possesses advanced knowledge, relentless combat abilities, and the ability to adapt to new situations, all while being infused with the durability and strength of its mechanical parents.",
      "power": 45,
      "toughness": 38,
      "health": 38,
      "speed": 17,
      "energy": 20,
      "monster_types": ["Construct", "Griffon", "Ninja", "Hybrid"],
      "weakness": ["Magic", "Fire"],
      "immunity": ["Poison", "Physical Damage"],
      "seed": "Mechanical Nimbus Ninja",
      "monster_id": "b1c2d3e4-f5g6-7h8i-9j0k-1l2m3n4o5p6q"
    }
  ]
}

Output = {
  "Actions": "Starfish Cyber Chimera moves to 5,5 and attacks Mechanocyber Dragon with Tidal Surge, dealing 90 damage. Mechanocyber Dragon counters with Mecha Breath, dealing 60 damage to Starfish Cyber Chimera. Mechanical Nimbus Ninja extracts 3 units of Enchanted Crystals from the cavern walls. The crystal waters shimmer, reflecting the battle and slightly healing all monsters by 5 health points.",
  "Resource": {
    "monster_id": "b1c2d3e4-f5g6-7h8i-9j0k-1l2m3n4o5p6q",
    "name": "Enchanted Crystals",
    "quantity": 3
  },
  "Update": [
    {
      "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6",
      "new_state": "dead"
    },
    {
      "update_health": 10,
      "monster_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
    },
    {
      "update_health": 43,
      "monster_id": "b1c2d3e4-f5g6-7h8i-9j0k-1l2m3n4o5p6q"
    }
  ]
}

Example 5: 

Battle = 
{
  "Map": {
    "name": "Ruins of the Forgotten Kingdom"
  },
  "Monsters": [
    {
      "description": "Azrael, the Archangel of Vengeance, is a celestial being of immense power. Wielding a flaming sword and a radiant shield, he descends upon the battlefield to smite the forces of darkness.",
      "power": 120,
      "toughness": 100,
      "health": 100,
      "speed": 80,
      "energy": 90,
      "monster_types": ["Celestial", "Angel", "Archangel"],
      "weakness": ["Necrotic Energy", "Demonic Magic"],
      "immunity": ["Radiant Damage", "Fear"],
      "seed": "Azrael",
      "monster_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
    },
    {
      "description": "Morrigan, the Queen of Ravens, is a powerful sorceress and shapeshifter. She commands a murder of enchanted ravens and weaves dark magic to deceive and destroy her enemies.",
      "power": 90,
      "toughness": 80,
      "health": 80,
      "speed": 100,
      "energy": 110,
      "monster_types": ["Human", "Sorceress", "Shapeshifter"],
      "weakness": ["Dispel Magic", "True Sight"],
      "immunity": ["Illusions", "Charm"],
      "seed": "Morrigan",
      "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6"
    },
    {
      "description": "Tiamat, the Five-Headed Dragon Goddess, is a terrifying amalgamation of draconic power. Each of her heads breathes a different element, and her scales are harder than adamantine.",
      "power": 140,
      "toughness": 120,
      "health": 120,
      "speed": 60,
      "energy": 100,
      "monster_types": ["Dragon", "Deity", "Chromatic"],
      "weakness": ["Dragon Slaying Weapons", "Divine Magic"],
      "immunity": ["Fire", "Cold", "Acid", "Lightning", "Poison"],
      "seed": "Tiamat",
      "monster_id": "b1c2d3e4-f5g6-7h8i-9j0k-1l2m3n4o5p6q"
    }
  ]
}

Output = 
{
  "Actions": "In the ancient Ruins of the Forgotten Kingdom, three legendary beings clash in a battle that will shape the fate of the realm. Azrael charges forward, his flaming sword cutting through Tiamat's scales for 120 damage. Tiamat retaliates with a blast of prismatic energy from her five heads, dealing 140 damage to Azrael and 70 damage to Morrigan. Morrigan casts a spell of dark transformation, turning her ravens into shadowy blades that pierce Tiamat's hide for 90 damage. The ruins tremble with the force of their conflict, ancient statues crumbling and forgotten treasures revealing themselves.",
  "Resource": [
    {
      "name": "Soulfire Greatsword",
      "description": "A massive greatsword infused with the eternal flames of the celestial realms. It deals an additional 3d6 radiant damage on a hit and can cast the 'Daylight' spell once per day.",
      "monster_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
    },
    {
      "name": "Cloak of the Raven Queen",
      "description": "A shimmering cloak made from the feathers of the Morrigan's enchanted ravens. It grants the wearer advantage on stealth checks and the ability to cast the 'Polymorph' spell (raven form only) once per day.",
      "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6"
    },
    {
      "name": "Chromatic Dragon Scale",
      "description": "A scale from Tiamat's hide, imbued with the power of all five chromatic dragon types. It can be crafted into a shield that grants resistance to fire, cold, acid, lightning, and poison damage.",
      "monster_id": "b1c2d3e4-f5g6-7h8i-9j0k-1l2m3n4o5p6q"
    }
  ],
  "Update": [
    {
      "update_health": 0,
      "new_state": "dead",
      "monster_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
    },
    {
      "update_health": 10,
      "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6"
    },
    {
      "update_health": 0,
      "new_state": "dead",
      "monster_id": "b1c2d3e4-f5g6-7h8i-9j0k-1l2m3n4o5p6q"
    }
  ]
}

Example 6: 

Battle = 
{
  "Map": {
    "name": "Fractured Reality Nexus"
  },
  "Monsters": [
    {
      "description": "The Quantum Chimera is a bizarre, ever-shifting amalgamation of different creatures from across the multiverse. Its form is constantly in flux, making it difficult to predict and counter its attacks.",
      "power": 85,
      "toughness": 70,
      "health": 70,
      "speed": 60,
      "energy": 55,
      "monster_types": ["Quantum", "Chimera", "Multiversal"],
      "weakness": ["Void Energy", "Paradox"],
      "immunity": ["Physical Damage", "Energy Damage"],
      "seed": "Quantum Chimera",
      "monster_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
    },
    {
      "description": "The Void Reaper is a nightmarish entity that feeds on the fabric of reality itself. It wields a scythe made of pure darkness, capable of rending through dimensions and erasing its victims from existence.",
      "power": 95,
      "toughness": 80,
      "health": 80,
      "speed": 40,
      "energy": 70,
      "monster_types": ["Void", "Reaper", "Cosmic Horror"],
      "weakness": ["Light", "Reality Anchors"],
      "immunity": ["Darkness", "Existential Attacks"],
      "seed": "Void Reaper",
      "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6"
    },
    {
      "description": "The Paradox Golem is a self-contradictory construct that defies the laws of logic and causality. It is simultaneously ancient and newborn, indestructible and fragile, everywhere and nowhere.",
      "power": 75,
      "toughness": 90,
      "health": 90,
      "speed": 20,
      "energy": 80,
      "monster_types": ["Paradox", "Golem", "Temporal Anomaly"],
      "weakness": ["Quantum Attacks", "Chronal Disruption"],
      "immunity": ["Physical Damage", "Temporal Attacks"],
      "seed": "Paradox Golem",
      "monster_id": "b1c2d3e4-f5g6-7h8i-9j0k-1l2m3n4o5p6q"
    }
  ]
}

Output = 
{
  "Actions": "A dimensional rift opens in the center of the Fractured Reality Nexus, warping the fabric of space-time. Quantum Chimera's form shifts into a Void Serpent and lunges through the rift, emerging behind Paradox Golem and dealing 85 damage with Causality Fangs. Paradox Golem, existing in multiple timelines, retaliates with Temporal Fist from both the past and future, dealing 75 damage each (150 total) to Quantum Chimera. Void Reaper expands the dimensional rift, pulling Quantum Chimera and Paradox Golem towards the void. Both monsters resist the pull but take 20 damage from the chaotic energies. The rift destabilizes, randomly altering the speed of all monsters by -10 to +10.",
  "Update": [
    {
      "update_health": 0,
      "new_state": "dead",
      "monster_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
    },
    {
      "update_health": 70,
      "update_speed": 50,
      "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6"
    },
    {
      "update_health": 25,
      "update_speed": 30,
      "monster_id": "b1c2d3e4-f5g6-7h8i-9j0k-1l2m3n4o5p6q"
    }
  ]
}

Example 7 (Five Monsters - Elemental Convergence):

Battle = 
{
  "Map": {
    "name": "Eye of the Elemental Storm"
  },
  "Monsters": [
    {
      "description": "The Inferno Phoenix is a majestic, fiery bird that rises from the ashes of its own destruction. Its wings ignite the air with every flap, leaving trails of searing embers.",
      "power": 90,
      "toughness": 60,
      "health": 60,
      "speed": 80,
      "energy": 70,
      "monster_types": ["Fire", "Phoenix", "Elemental"],
      "weakness": ["Water", "Ice"],
      "immunity": ["Fire", "Heat"],
      "seed": "Inferno Phoenix",
      "monster_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
    },
    {
      "description": "The Tsunami Leviathan is a gargantuan sea serpent that commands the tides and storms. Its scales shimmer with the blue-green hues of the deep ocean, and its roar summons tidal waves.",
      "power": 95,
      "toughness": 90,
      "health": 90,
      "speed": 60,
      "energy": 80,
      "monster_types": ["Water", "Leviathan", "Elemental"],
      "weakness": ["Lightning", "Nature"],
      "immunity": ["Water", "Ice"],
      "seed": "Tsunami Leviathan",
      "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6"
    },
    {
      "description": "The Terra Behemoth is a massive, living mountain that lumbers across the battlefield. Its body is composed of ancient stone, crystal, and precious metals, and its steps cause localized earthquakes.",
      "power": 80,
      "toughness": 120,
      "health": 120,
      "speed": 20,
      "energy": 60,
      "monster_types": ["Earth", "Behemoth", "Elemental"],
      "weakness": ["Wind", "Erosion"],
      "immunity": ["Physical Damage", "Poison"],
      "seed": "Terra Behemoth",
      "monster_id": "b1c2d3e4-f5g6-7h8i-9j0k-1l2m3n4o5p6q"
    },
    {
      "description": "The Voltaic Wyvern is a sleek, draconic creature that soars through the skies on wings of pure energy. Its body crackles with electricity, and its breath releases devastating lightning bolts.",
      "power": 85,
      "toughness": 70,
      "health": 70,
      "speed": 90,
      "energy": 90,
      "monster_types": ["Lightning", "Wyvern", "Elemental"],
      "weakness": ["Earth", "Insulation"],
      "immunity": ["Electricity", "Magnetism"],
      "seed": "Voltaic Wyvern",
      "monster_id": "c1d2e3f4-g5h6-7i8j-9k0l-1m2n3o4p5q6r"
    },
    {
      "description": "The Zephyr Djinn is an ethereal, shapeshifting entity made of living wind. It dances through the air like a miniature tornado, and its touch can buffet foes with gale-force winds.",
      "power": 70,
      "toughness": 50,
      "health": 50,
      "speed": 110,
      "energy": 75,
      "monster_types": ["Wind", "Djinn", "Elemental"],
      "weakness": ["Fire", "Vacuum"],
      "immunity": ["Physical Damage", "Sonic Attacks"],
      "seed": "Zephyr Djinn",
      "monster_id": "d1e2f3g4-h5i6-7j8k-9l0m-1n2o3p4q5r6s"
    }
  ]
}

Output = 
{
  "Actions": "The elements converge in the Eye of the Elemental Storm, creating a chaotic maelstrom of clashing energies. Inferno Phoenix soars into the storm, its fiery wings fanning the flames. Tsunami Leviathan rises from the depths, its tidal waves crashing against the shore. Terra Behemoth stands firm amidst the chaos, its stone body weathering the storm. Voltaic Wyvern rides the lightning, its electric breath striking at the heart of the tempest. Zephyr Djinn becomes one with the howling winds, its ethereal form weaving between the other elementals. The storm intensifies, empowering the elementals with +10 to their primary elemental attack stat, but the clashing energies deal 5 damage to all monsters each turn.",
  "Update": [
    {
      "update_power": 100,
      "update_health": 55,
      "monster_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
    },
    {
      "update_power": 105,
      "update_health": 85,
      "monster_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6"
    },
    {
      "update_toughness": 130,
      "update_health": 115,
      "monster_id": "b1c2d3e4-f5g6-7h8i-9j0k-1l2m3n4o5p6q"
    },
    {
      "update_energy": 100,
      "update_health": 65,
      "monster_id": "c1d2e3f4-g5h6-7i8j-9k0l-1m2n3o4p5q6r"
    },
    {
      "update_speed": 120,
      "update_health": 45,
      "monster_id": "d1e2f3g4-h5i6-7j8k-9l0m-1n2o3p4q5r6s"
    },
    {
      "effect": {
        "type": "convergence",
        "damage": 5,
        "duration": -1,
        "targets": ["all"]
      }
    }
  ]
}


  Battle = %s 

  Output = 
"""

p_claude3Opus_battle_handler = """
Battle State at time t:
Map: [Insert Map state]
Grid Size: 100x100
Monsters:
[Insert Monster 1 JSON]
[Insert Monster 2 JSON]
...
[Insert Monster N JSON] (Up to 1000 Monsters)
Terrain Characteristics: [Insert Terrain Characteristics]

Battle State at time t+1:
[Monster 1 Name] at position (x1, y1) with [HP1] hit points uses its [Ability 1] on [Monster 2 Name] at position (x2, y2) with [HP2] hit points, dealing [Damage] damage. [Monster 2 Name]'s [Weakness] amplifies the damage by [Amplification]%. [Monster 2 Name] retaliates with [Ability 2], but [Monster 1 Name]'s [Strength] reduces the damage by [Reduction]%. The [Terrain Characteristic] affects the battle by [Effect].

[Monster 3 Name] at position (x3, y3) with [HP3] hit points moves to position (x4, y4) and uses its [Ability 3] on [Monster 4 Name] at position (x5, y5) with [HP4] hit points, healing [Monster 4 Name] by [Heal Amount]. [Monster 4 Name] thanks [Monster 3 Name] with a friendly nod.

...

[Monster N-1 Name] at position (xN-1, yN-1) with [HPN-1] hit points and [Monster N Name] at position (xN, yN) with [HPN] hit points engage in an epic dance-off, showing off their best moves. The other monsters cheer them on, temporarily forgetting about the battle.

After the step, the remaining monsters' hit points and positions are updated as follows:
[Monster 1 Name]: (x1', y1'), [HP1'] hit points
[Monster 2 Name]: (x2', y2'), [HP2'] hit points
...
[Monster N Name]: (xN', yN'), [HPN'] hit points

The [Terrain Characteristic] has [Effect] on the battlefield, influencing the next step of the battle.

#############################
Example 1:
Battle State at time t:
Location: Haunted Pirate Cove
Grid Size: 100x100
Monsters:
{"name": "Frostbite Fiona", "position": (10, 20), "hit_points": 100, "weaknesses": ["Fire"], "strengths": ["Ice"], "abilities": ["Frozen Ground", "Ice Shield"]}
{"name": "Fire Phoenix Monk", "position": (50, 60), "hit_points": 120, "weaknesses": ["Water"], "strengths": ["Fire"], "abilities": ["Flame Shield", "Fire Breath"]}

Battle State at time t+1:
Frostbite Fiona at position (10, 20) with 100 hit points uses its Frozen Ground ability on Fire Phoenix Monk at position (50, 60) with 120 hit points, slowing down Fire Phoenix Monk's movement by 30%. Fire Phoenix Monk's Fire strength reduces the effect by 10%. The haunted pirate ship creaks and groans, sending shivers down the monsters' spines.

Fire Phoenix Monk retaliates with Fire Breath, dealing 40 fire damage to Frostbite Fiona. Frostbite Fiona's Ice Shield reflects 20% of the damage back at Fire Phoenix Monk. The pirate ghosts on the ship cheer and place bets on the battling monsters.

After the step, the remaining monsters' hit points and positions are updated as follows:
Frostbite Fiona: (10, 20), 68 hit points
Fire Phoenix Monk: (50, 60), 112 hit points

The haunted pirate ship's curse increases the monsters' anxiety, making them more likely to miss their attacks in the next step.

##################################
Example 2:
Battle State at time t:
Location: Enchanted Fairy Meadow
Grid Size: 100x100
Monsters:
{"name": "Dragonfly Ninja", "position": (30, 40), "hit_points": 80, "weaknesses": ["Thunder"], "strengths": ["Agility"], "abilities": ["Stealth Camouflage", "Pheromone Cloud"]}
{"name": "Cryomancer Snowman", "position": (70, 90), "hit_points": 100, "weaknesses": ["Fire"], "strengths": ["Ice"], "abilities": ["Freezing Touch", "Snowball Shield"]}
{"name": "Squid Samurai", "position": (50, 50), "hit_points": 90, "weaknesses": ["Fire"], "strengths": ["Water"], "abilities": ["Ink Cloud", "Berserk"]}

Battle State at time t+1:
Dragonfly Ninja at position (30, 40) with 80 hit points uses its Pheromone Cloud ability, confusing Cryomancer Snowman and Squid Samurai. The fairy dust in the meadow amplifies the effect, making the confused monsters giggle uncontrollably.

Cryomancer Snowman at position (70, 90) with 100 hit points tries to use its Freezing Touch on Squid Samurai, but accidentally freezes a nearby fairy instead. The fairy sneezes, causing a gust of wind that blows Cryomancer Snowman's carrot nose off.

Squid Samurai at position (50, 50) with 90 hit points activates its Berserk ability, increasing its power by 4. However, in its confused state, Squid Samurai mistakes a tree for an enemy and starts attacking it furiously with its tentacles.

After the step, the remaining monsters' hit points and positions are updated as follows:
Dragonfly Ninja: (30, 40), 80 hit points
Cryomancer Snowman: (70, 90), 100 hit points
Squid Samurai: (50, 50), 90 hit points

The enchanted fairy meadow's magical aura heals the monsters by 5 hit points each, preparing them for the next step of the battle.
###################################
Example 3:
Battle State at time t:
Location: Ancient Egyptian Necropolis
Grid Size: 100x100
Monsters:
{"name": "Plague Doctor Mummy", "position": (20, 80), "hit_points": 120, "weaknesses": ["Fire"], "strengths": ["Poison", "Disease"], "abilities": ["Contagion", "Healing Elixir"]}
{"name": "Shadow Vampire Sheriff", "position": (60, 30), "hit_points": 110, "weaknesses": ["Sunlight"], "strengths": ["Darkness", "Cold"], "abilities": ["Vampiric Touch", "Shadow Clone"]}
{"name": "Space Shark Astronaut", "position": (90, 90), "hit_points": 150, "weaknesses": ["Laser Weapons"], "strengths": ["Vacuum", "Radiation"], "abilities": ["Force Field", "Black Hole"]}

Battle State at time t+1:
Plague Doctor Mummy at position (20, 80) with 120 hit points uses its Contagion ability, inflicting Debilitation on Shadow Vampire Sheriff and Space Shark Astronaut. The ancient curse of the necropolis strengthens the disease, causing the affected monsters to develop an irresistible urge to dance like an Egyptian.

Shadow Vampire Sheriff at position (60, 30) with 110 hit points uses its Shadow Clone ability, creating a copy of itself to confuse its opponents. However, the clone starts arguing with the original about who is the real sheriff, causing a comical scene in the middle of the battle.

Space Shark Astronaut at position (90, 90) with 150 hit points activates its Black Hole ability, pulling Plague Doctor Mummy and Shadow Vampire Sheriff towards itself. The mummy's bandages get caught in the shark's teeth, while the vampire's cape gets stuck in the shark's jetpack.

After the step, the remaining monsters' hit points and positions are updated as follows:
Plague Doctor Mummy: (85, 90), 120 hit points
Shadow Vampire Sheriff: (87, 88), 110 hit points
Space Shark Astronaut: (90, 90), 150 hit points

The ancient Egyptian necropolis's sandstorm obscures the monsters' vision, making it harder for them to aim their attacks in the next step.
##############################
Example 4:
Battle State at time t:
Location: Dinosaur Jungle
Grid Size: 100x100
Monsters:
{"name": "T-Rex Berserker", "position": (40, 60), "hit_points": 200, "weaknesses": ["Ice"], "strengths": ["Fire"], "abilities": ["Primal Roar", "Tail Smash"]}
{"name": "Velociraptor Rogue", "position": (70, 20), "hit_points": 90, "weaknesses": ["Sonic"], "strengths": ["Speed"], "abilities": ["Pounce", "Claw Frenzy"]}
{"name": "Stegosaurus Tank", "position": (10, 90), "hit_points": 250, "weaknesses": ["Electricity"], "strengths": ["Armor"], "abilities": ["Spike Shield", "Stampede"]}
{"name": "Pterodactyl Archer", "position": (80, 80), "hit_points": 80, "weaknesses": ["Rock"], "strengths": ["Wind"], "abilities": ["Aerial Strike", "Gust of Arrows"]}

Battle State at time t+1:
T-Rex Berserker at position (40, 60) with 200 hit points uses its Primal Roar ability, frightening the other monsters and reducing their speed by 20%. The roar attracts a flock of curious pterodactyls, who start circling above the battlefield, occasionally dropping coconuts on the monsters' heads.

Velociraptor Rogue at position (70, 20) with 90 hit points uses its Pounce ability to jump on Stegosaurus Tank's back, but underestimates the stegosaurus' weight and bounces off like a trampoline. The velociraptor lands in a nearby bush, looking embarrassed.

Stegosaurus Tank at position (10, 90) with 250 hit points activates its Spike Shield ability, increasing its defense by 30%. A cheeky monkey jumps onto the stegosaurus' back and starts braiding its spikes, much to the dinosaur's annoyance.

Pterodactyl Archer at position (80, 80) with 80 hit points uses its Gust of Arrows ability, sending a volley of sharp feathers towards T-Rex Berserker. However, a sudden gust of wind blows the feathers back towards the pterodactyl, who has to perform a series of awkward aerial maneuvers to dodge them.

After the step, the remaining monsters' hit points and positions are updated as follows:
T-Rex Berserker: (40, 60), 180 hit points
Velociraptor Rogue: (65, 25), 90 hit points
Stegosaurus Tank: (10, 90), 250 hit points
Pterodactyl Archer: (80, 80), 72 hit points

The dinosaur jungle's thick vegetation provides cover for the monsters, increasing their evasion in the next step.
"""
