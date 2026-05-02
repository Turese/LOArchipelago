from typing import NamedTuple

from enum import IntFlag, auto


class LocationCat(IntFlag):
    OVERWORLD_ITEM = auto()
    SKILL_UNLOCK = auto()
    RECRUIT = auto()
    COMBAT_VICTORY = auto() # combat victory for aggressive npcs
    FRIENDLY_FIRE = auto() # combat victory for nonaggressive npcs
    RAT_FRIENDLY_FIRE = auto() # combat victory for rats that are nonaggressive towards the rat king
    MERCHANT = auto()
    DOOR_MERCHANT = auto()  # merchants that appear at the door
    EVENT_ITEM = auto()
    LOOT = auto()

class DL(IntFlag):
    EXPLORER = auto()
    SURVIVOR = auto()
    CURSED = auto()

class LocationData(NamedTuple):
    str_name: str
    category: LocationCat
    id: int
    difficulty_lock: set[DL] = set()
    cursed_name: str | None = None

location_name_groups: dict[str, set[str]] = {
    "SAFE": {},
    "RUSTY_CROWN": {},
}

# map game locations to their corresponding games
video_game_requirements: dict[str, set[str]] = {
    # "VIDEO_GAME_LOCATION_NAME": {"REQUIRED_ITEM_NAME"},
}

VIDEO_GAME_LOCATIONS: dict[str, LocationData] = {
    "GAME_SKILL_WAKE_THE_BLOOD_KNIGHT": LocationData("Complete Video Game - Wake the Blood Knight", LocationCat.SKILL_UNLOCK, 1),
    "GAME_SKILL_WIZARDS_HELL": LocationData("Complete Video Game - Wizards Hell: Arcane Tears", LocationCat.SKILL_UNLOCK, 2),
    "GAME_SKILL_SUPER_JUMPLAD": LocationData("Complete Video Game - Super Jumplad", LocationCat.SKILL_UNLOCK, 3),
    "GAME_SKILL_SUPER_JUMPLAD_3": LocationData("Complete Video Game - Super Jumplad 3", LocationCat.SKILL_UNLOCK, 4),
    "GAME_SKILL_CATAFALQUE": LocationData("Complete Video Game - Catafalque", LocationCat.SKILL_UNLOCK, 5),
    "GAME_SKILL_HONKOS_GRAND_JOURNEY": LocationData("Complete Video Game - Honko's Grand Journey", LocationCat.SKILL_UNLOCK, 6),
    "GAME_SKILL_MADWHEELS_97": LocationData("Complete Video Game - Madwheels 97", LocationCat.SKILL_UNLOCK, 7),
    "GAME_SKILL_WRAITHSCOURGE": LocationData("Complete Video Game - Wraithscourge", LocationCat.SKILL_UNLOCK, 8),
    "GAME_SKILL_MASSACRE_PRINCESS": LocationData("Complete Video Game - Massacre Princess: Catholicon", LocationCat.SKILL_UNLOCK, 9),
    "GAME_SKILL_KILL_TO_SHOOT": LocationData("Complete Video Game - Kill to Shoot", LocationCat.SKILL_UNLOCK, 10),
    "GAME_SKILL_MYRMIDON": LocationData("Complete Video Game - Myrmidon", LocationCat.SKILL_UNLOCK, 11),
    "GAME_SKILL_MYRMIDON_XII": LocationData("Complete Video Game - Myrmidon XII", LocationCat.SKILL_UNLOCK, 12),
    "GAME_SKILL_SCREAMATORIUM": LocationData("Complete Video Game - Screamatorium", LocationCat.SKILL_UNLOCK, 13),
    "GAME_SKILL_FROGIT_ABOUT_IT": LocationData("Complete Video Game - Frogit About It", LocationCat.SKILL_UNLOCK, 14),
    "GAME_SKILL_BLOOD_GHOUL_ORGY_3": LocationData("Complete Video Game - Blood Ghoul Orgy 3", LocationCat.SKILL_UNLOCK, 15),
    "GAME_SKILL_OCTOCOOK": LocationData("Complete Video Game - Octocook", LocationCat.SKILL_UNLOCK, 16),
    "GAME_SKILL_SPACE_TRUCKERZ": LocationData("Complete Video Game - Space Truckerz", LocationCat.SKILL_UNLOCK, 17),
    "GAME_SKILL_REPTILE_FOOTBALL": LocationData("Complete Video Game - Reptile Football", LocationCat.SKILL_UNLOCK, 18),
    "GAME_SKILL_CROSSWORD_CHALLENGE": LocationData("Complete Video Game - Auntie Wilma's Crossword Challenge", LocationCat.SKILL_UNLOCK, 19)
}

F3_HALL_LOCATIONS: dict[str, LocationData] = {
    "F3_LARGE_SHADE_COMBAT_VICTORY": LocationData("Floor 3 - Slay Large Shade '??? ?? ?????'", LocationCat.COMBAT_VICTORY, 101),
    "F3_PLANTER_KEY": LocationData("Floor 3 Hall - Item Hidden in Planter", LocationCat.OVERWORLD_ITEM, 102),
    "F3_PLAYING_CARD": LocationData("Floor 3 Hall: Playing Card in Vending Machine", LocationCat.EVENT_ITEM, 103),
    "F3_ONLOOKER_DOORWAY_COMBAT_VICTORY": LocationData("Floor 3 Hall - Slay Onlooker by Apt. 37 Entrance", LocationCat.COMBAT_VICTORY, 104),
    "F3_ONLOOKER_STAIRWELL_COMBAT_VICTORY": LocationData("Floor 3 Hall - Slay Onlookers by Stairwell Door", LocationCat.COMBAT_VICTORY, 105),
    "F3_CLINT_COMBAT_VICTORY": LocationData("Floor 3 Hall - Slay Clint (Day 2-4)", LocationCat.COMBAT_VICTORY, 106),
    "F3_LOUIS_LOWER_HALF_COMBAT_VICTORY": LocationData("Floor 3 Hall - Slay Louis' Lower Half", LocationCat.COMBAT_VICTORY, 107),
    "F3_MASKED_SHADOW_GIFT": LocationData("Floor 3 Hall - Gift from Masked Shadow", LocationCat.EVENT_ITEM, 108),
    "F3_HAND_WORMS_COMBAT_VICTORY": LocationData("Floor 3 Hall - Slay Hand Worms", LocationCat.COMBAT_VICTORY, 109),
    "F3_VENDING_MACHINE_CHIPS": LocationData("Floor 3 Hall - Vending Machine Item 1", LocationCat.MERCHANT, 110),
    "F3_VENDING_MACHINE_SPICY": LocationData("Floor 3 Hall - Vending Machine Item 2", LocationCat.MERCHANT, 111),
    "F3_VENDING_MACHINE_GUMMI_BEARS": LocationData("Floor 3 Hall - Vending Machine Item 3", LocationCat.MERCHANT, 112),
    "F3_VENDING_MACHINE_CHEESE": LocationData("Floor 3 Hall - Vending Machine Item 4", LocationCat.MERCHANT, 113),
    "F3_VENDING_MACHINE_ONIONOS": LocationData("Floor 3 Hall - Vending Machine Item 5", LocationCat.MERCHANT, 114)
}

APT_30_MAIN_LOCATIONS: dict[str, LocationData] = {
    "APT_30_TAXIDERMY_EAGLE": LocationData("Apt. 30 Entryway - Item Near Front Door", LocationCat.OVERWORLD_ITEM, 1103),
    "APT_30_TAXIDERMY_DOG": LocationData("Apt. 30 Entryway - Item on Table Near Couch", LocationCat.OVERWORLD_ITEM, 1104),
    "APT_30_NE_TAXIDERMY_CREATURE": LocationData("Apt. 30 Office - Item on North Table 1", LocationCat.OVERWORLD_ITEM, 1105),
    "APT_30_NE_SCALPEL": LocationData("Apt. 30 Office - Item on North Table 2", LocationCat.OVERWORLD_ITEM, 1106),
    "APT_30_NE_SQUIRREL": LocationData("Apt. 30 Office - Item Near Door", LocationCat.OVERWORLD_ITEM, 1107),
    "APT_30_NE_WHISKEY": LocationData("Apt. 30 Office - Item Near Far Wall", LocationCat.OVERWORLD_ITEM, 1108),
    "APT_30_NW_SPIRIT_BOARD": LocationData("Apt. 30 Bedroom - Item on Topmost Table Near Door", LocationCat.OVERWORLD_ITEM, 1109),
    "APT_30_NW_SHRUNKEN_HEAD": LocationData("Apt. 30 Bedroom - Item Near Far Wall", LocationCat.OVERWORLD_ITEM, 1110),
    "APT_30_NW_GRANOLA_BAR": LocationData("Apt. 30 Bedroom - Item on Bottom Table", LocationCat.OVERWORLD_ITEM, 1111),
    "APT_30_NW_CASH": LocationData("Apt. 30 Bedroom - Item on Center Table", LocationCat.OVERWORLD_ITEM, 1112),
    "APT_30_NW_WIRECUTTER_COMBAT_VICTORY": LocationData("Apt. 30 Bedroom - Slay Wirecutter", LocationCat.COMBAT_VICTORY, 1113),
    "APT_30_SW_FIRST_AID_KIT": LocationData("Apt. 30 Bathroom - Item Near Shower", LocationCat.OVERWORLD_ITEM, 1114),
    "APT_30_SW_FIRST_AID_BOX": LocationData("Apt. 30 Bathroom - First Aid Box Loot", LocationCat.LOOT, 1115),
    "APT_30_SW_NEEDLES_COMBAT_VICTORY": LocationData("Apt. 30 Bathroom - Slay Needles", LocationCat.COMBAT_VICTORY, 1116),
    "APT_30_SW_MEDICINE_CABINET": LocationData("Apt. 30 Bathroom - Medicine Cabinet Loot", LocationCat.LOOT, 1117),
    "APT_30_SW_TOOTHPASTE": LocationData("Apt. 30 Bathroom - Item on Counter", LocationCat.OVERWORLD_ITEM, 1118),
    "APT_30_SE_THROWING_KNIFE": LocationData("Apt. 30 Kitchen - Item on Dining Table 1", LocationCat.OVERWORLD_ITEM, 1119),
    "APT_30_SE_DINNER_PLATE": LocationData("Apt. 30 Kitchen - Item on Dining Table 2", LocationCat.OVERWORLD_ITEM, 1120),
    "APT_30_SE_SCISSORS": LocationData("Apt. 30 Kitchen - Slay Scissors", LocationCat.COMBAT_VICTORY, 1121),
    "APT_30_SE_CHEFS_KNIFE": LocationData("Apt. 30 Kitchen - Item on Counter", LocationCat.OVERWORLD_ITEM, 1122),
    "APT_30_FRIDGE": LocationData("Apt. 30 Kitchen - Fridge Loot", LocationCat.LOOT, 1123),
}

APT_30_FLESH_LOCATIONS: dict[str, LocationData] = {
    "APT_30_TAXIDERMY_COMBAT_VICTORY": LocationData("Apt. 30 Entryway - Slay Taxidermy", LocationCat.COMBAT_VICTORY, 1101),
    "APT_30_TAXIDERMY_AUDREY_LOOT": LocationData("Apt. 30 Entryway - Taxidermy Audrey Loot", LocationCat.EVENT_ITEM, 1102),
    "APT_30_FLESH_ROGUE_COMBAT_VICTORY": LocationData("Apt. 30 Flesh - Slay Rogue Taxidermy", LocationCat.COMBAT_VICTORY, 1124),
    "APT_30_FLESH_TIGER_COMBAT_VICTORY": LocationData("Apt. 30 Flesh - Slay Tiger", LocationCat.COMBAT_VICTORY, 1125),
    "APT_30_FLESH_ABOM_COMBAT_VICTORY": LocationData("Apt. 30 Flesh - Slay Abomination", LocationCat.COMBAT_VICTORY, 1126),
    "APT_30_FLESH_PATCHWORK_BOOTS": LocationData("Apt. 30 Flesh - Item on Bottom Table", LocationCat.OVERWORLD_ITEM, 1127),
    "APT_30_FLESH_SW_PATCHWORK_CLUB": LocationData("Apt. 30 Flesh Southwest - Item on Table", LocationCat.OVERWORLD_ITEM, 1128),
    "APT_30_FLESH_SW_SATYR_COMBAT_VICTORY": LocationData("Apt. 30 Flesh Southwest - Slay Satyr", LocationCat.COMBAT_VICTORY, 1129),
    "APT_30_FLESH_NE_PATCHWORK_HAT": LocationData("Apt. 30 Flesh Northeast - Item on Table", LocationCat.OVERWORLD_ITEM, 1130),
    "APT_30_FLESH_NE_CROW_COMBAT_VICTORY": LocationData("Apt. 30 Flesh Northeast - Slay Crow", LocationCat.COMBAT_VICTORY, 1131),
    "APT_30_FLESH_SE_NEEDLE_GLOVES": LocationData("Apt. 30 Flesh Southeast - Item on Table", LocationCat.OVERWORLD_ITEM, 1132),
    "APT_30_FLESH_SE_LIMBS_COMBAT_VCTORY": LocationData("Apt. 30 Flesh Southeast - Slay Limbs", LocationCat.COMBAT_VICTORY, 1133),
    "APT_30_FLESH_NW_CROCODILE_COMBAT_VICTORY": LocationData("Apt. 30 Flesh Northwest - Slay Crocodile", LocationCat.COMBAT_VICTORY, 1134),
    "APT_30_FLESH_NW_PATCHWORK_JACKET": LocationData("Apt. 30 Flesh Northwest - Item on Table", LocationCat.OVERWORLD_ITEM, 1135)
}

APT_30_TAXIDERMY_LOCATIONS: dict[str, LocationData] = {
    **APT_30_MAIN_LOCATIONS, 
    **APT_30_FLESH_LOCATIONS
}

APT_31_STARGAZER_LOCATIONS: dict[str, LocationData] = {
    "APT_31_STARGAZER_COMBAT_VICTORY": LocationData("Apt. 31 - Slay Stargazer", LocationCat.COMBAT_VICTORY, 201),
    "APT_31_JUICE": LocationData("Apt. 31 - Item on Kitchen Counter", LocationCat.OVERWORLD_ITEM, 202),
    "APT_31_FRIDGE": LocationData("Apt. 31 - Fridge Loot", LocationCat.LOOT, 203),
    "APT_31_CASH": LocationData("Apt. 31 - Item on Dining Table", LocationCat.OVERWORLD_ITEM, 204),
    "APT_31_TRASH": LocationData("Apt. 31 Kitchen - Trash Can", LocationCat.LOOT, 205),
    "APT_31_DARK_TRASH": LocationData("Apt. 31 Kitchen - Trash Can (Lights off)", LocationCat.LOOT, 206),
    "APT_31_BATHROOM_VINEGAR": LocationData("Apt. 31 Bathroom - Item on Counter Near Door", LocationCat.OVERWORLD_ITEM, 207),
    "APT_31_BATHROOM_EYE_DROPS": LocationData("Apt. 31 Bathroom - Second Item on Counter Near Door", LocationCat.OVERWORLD_ITEM, 208),
    "APT_31_BATHROOM_DCLOGGER": LocationData("Apt. 31 Bathroom - First Item on Floor", LocationCat.OVERWORLD_ITEM, 209),
    "APT_31_BATHROOM_DCLOGGER_2": LocationData("Apt. 31 Bathroom - Second Item on Floor", LocationCat.OVERWORLD_ITEM, 210, difficulty_lock={DL.EXPLORER}),
    "APT_31_BATHROOM_MEDICINE_CABINET": LocationData("Apt. 31 Bathroom - Medicine Cabinet Loot", LocationCat.LOOT, 211),
    "APT_31_BATHROOM_SOAP": LocationData("Apt. 31 Bathroom - Item on Center Counter", LocationCat.OVERWORLD_ITEM, 212),
    "APT_31_BEDROOM_METAL_BAT": LocationData("Apt. 31 Bedroom - Item on Table", LocationCat.OVERWORLD_ITEM, 213),
    "APT_31_BEDROOM_TONIC": LocationData("Apt. 31 Bedroom - Item on Table Near Safe", LocationCat.OVERWORLD_ITEM, 214, difficulty_lock={DL.EXPLORER}),
    "APT_31_BEDROOM_SAFE_ITEM": LocationData("Apt. 31 Bedroom - Item in Safe", LocationCat.LOOT, 215),
    "APT_31_OBSERVATORY_PLUTO_DISC": LocationData("Apt. 31 Observatory - Item Near Door", LocationCat.OVERWORLD_ITEM, 216),
    "APT_31_OBSERVATORY_VOID_DISC": LocationData("Apt. 31 Observatory - Item On Center Table", LocationCat.OVERWORLD_ITEM, 217),
    "APT_31_OBSERVATORY_TRASH": LocationData("Apt. 31 Observatory - Trash Can", LocationCat.LOOT, 218),
    "APT_31_TELESCOPE_DISC_EXPOSURE": LocationData("Apt. 31 Observatory - Expose Void Disc to Telescope", LocationCat.EVENT_ITEM, 219)
}

APT_32_TEETH_LOCATIONS_MAIN: dict[str, LocationData] = {
    "APT_32_ENTRY_BANDAGES": LocationData("Apt. 32 - Item on Table Near Child's Bedroom (Day 2-5)", LocationCat.OVERWORLD_ITEM, 301, difficulty_lock={DL.EXPLORER}),
    "APT_32_ENTRY_HOODIE": LocationData("Apt. 32 - Item on Table Near Master Bedroom (Day 2-5)", LocationCat.OVERWORLD_ITEM, 302, difficulty_lock={DL.EXPLORER}),
    "APT_32_TOOTHLING_A_COMBAT_VICTORY": LocationData("Apt. 32 - Slay Toothling Near Bathroom (Day 2-5)", LocationCat.COMBAT_VICTORY, 303),
    "APT_32_TOOTHLING_B_COMBAT_VICTORY": LocationData("Apt. 32 - Slay Toothling Near Child's Bedroom (Day 2-5)", LocationCat.COMBAT_VICTORY, 304),
    "APT_32_CLINT_DAY_5_COMBAT_VICTORY": LocationData("Apt. 32 - Slay Clint (Day 4-5)", LocationCat.COMBAT_VICTORY, 305),
    "APT_32_CLINT_DAY_9_COMBAT_VICTORY": LocationData("Apt. 32 - Slay Clint (Day 9+)", LocationCat.COMBAT_VICTORY, 306),
    "APT_32_BATHROOM_MEDICELL": LocationData("Apt. 32 Bathroom - Item on Counter (Day 2-5)", LocationCat.OVERWORLD_ITEM, 307),
    "APT_32_BATHROOM_TONIC": LocationData("Apt. 32 Bathroom - Second Item on Counter (Day 2-5)", LocationCat.OVERWORLD_ITEM, 308, difficulty_lock={DL.EXPLORER}),
    "APT_32_BATHROOM_MOP": LocationData("Apt. 32 Bathroom - Item on Floor by Shower (Day 2-5)", LocationCat.OVERWORLD_ITEM, 309),
    "APT_32_BATHROOM_DOOR_KNOB": LocationData("Apt. 32 Bathroom - Item From Joel (Day 2-5)", LocationCat.EVENT_ITEM, 310),
    "APT_32_BATHROOM_RECRUIT_JOEL": LocationData("Apt. 32 Bathroom - Recruit Joel (Day 2-4)", LocationCat.RECRUIT, 311),
    "APT_32_BATHROOM_JOEL_COMBAT_VICTORY": LocationData("Apt. 32 Bathroom - Slay Joel (Day 2-4)", LocationCat.FRIENDLY_FIRE, 312),
    "APT_32_BATHROOM_JOEL_DAY_5_COMBAT_VICTORY": LocationData("Apt. 32 Bathroom - Slay Joel (Day 5)", LocationCat.COMBAT_VICTORY, 313),
    "APT_32_BATHROOM_JOEL_DAY_9_COMBAT_VICTORY": LocationData("Apt. 32 Bathroom - Slay Joel (Day 9)", LocationCat.COMBAT_VICTORY, 314),
    "APT_32_CHILD_BEDROOM_TOOTHLING_COMBAT_VICTORY": LocationData("Apt. 32 Child's Bedroom - Slay Toothlings (Day 2-5)", LocationCat.COMBAT_VICTORY, 315),
    "APT_32_CHILD_BEDROOM_BEN_COMBAT_VICTORY": LocationData("Apt. 32 Child's Bedroom - Slay Benjamin (Day 2-4)", LocationCat.FRIENDLY_FIRE, 316),
    "APT_32_CHILD_BEDROOM_BEN_DAY_9_COMBAT_VICTORY": LocationData("Apt. 32 Child's Bedroom - Slay Mound of Teeth and Gums (Day 9+)", LocationCat.FRIENDLY_FIRE, 317),
    "APT_32_CHILD_BEDROOM_BEN_PLAY": LocationData("Apt. 32 Child's Bedroom - Play Soldiers with Ben", LocationCat.EVENT_ITEM, 318),
    "APT_32_CHILD_BEDROOM_BASEBALL_CAP": LocationData("Apt. 32 Child's Bedroom - Item On Table by Door (Day 2-5)", LocationCat.OVERWORLD_ITEM, 319),
    "APT_32_CHILD_BEDROOM_TEDDY_BEAR": LocationData("Apt. 32 Child's Bedroom - Item Between Beds (Day 2-5)", LocationCat.OVERWORLD_ITEM, 320),
    "APT_32_TUNNELS_JAW_REVOLVER": LocationData("Teeth Hell - Item in Southwest Tunnel", LocationCat.COMBAT_VICTORY, 339),
    "APT_32_TUNNELS_MASTICATOR_COMBAT_VICTORY": LocationData("Teeth Hell - Slay Masticator (Bottom Left Tunnel)", LocationCat.COMBAT_VICTORY, 340),
    "APT_32_TUNNELS_TOOTH_MASTICATOR_COMBAT_VICTORY": LocationData("Teeth Hell - Slay Tooth Fairy and Masticator", LocationCat.COMBAT_VICTORY, 341),
    "APT_32_TUNNELS_FIRST_AID_KIT": LocationData("Teeth Hell - Item in Northwest Tunnel", LocationCat.OVERWORLD_ITEM, 342),
    "APT_32_TUNNELS_TOOTH_GROUP_A_COMBAT_VICTORY": LocationData("Teeth Hell - Slay Tooth Group (Top Left Tunnel)", LocationCat.COMBAT_VICTORY, 343),
    "APT_32_TUNNELS_TOOTH_LEECH": LocationData("Teeth Hell - Slay Tooth Leech", LocationCat.COMBAT_VICTORY, 344),
    "APT_32_TUNNELS_BABY_TEETH_SUPERBOSS_COMBAT_VICTORY": LocationData("Teeth Hell - Slay Baby Teeth (Day 9+)", LocationCat.COMBAT_VICTORY, 345),
    "APT_32_TUNNELS_TOOTH_RIFLE": LocationData("Teeth Hell - Baby Teeth Tunnel Item 1", LocationCat.OVERWORLD_ITEM, 346),
    "APT_32_TUNNELS_TOOTH_SCIMITAR": LocationData("Teeth Hell - Baby Teeth Tunnel Item 2", LocationCat.OVERWORLD_ITEM, 347),
    "APT_32_TUNNELS_HEALING_SPRAY": LocationData("Teeth Hell - Item in Southeast Tunnel", LocationCat.OVERWORLD_ITEM, 348),
    "APT_32_TUNNELS_TOOTH_GROUP_B_COMBAT_VICTORY": LocationData("Teeth Hell - Slay Tooth Group (Bottom Right Tunnel)", LocationCat.OVERWORLD_ITEM, 349)
}

APT_32_TEETH_BEHIND_DOOR_KNOB: dict[str, LocationData] = {
    "APT_32_MASTER_BEDROOM_TANK_TOP": LocationData("Apt. 32 Master Bedroom - Item on Table Near Door (Day 2-5)", LocationCat.OVERWORLD_ITEM, 321),
    "APT_32_MASTER_BEDROOM_SAFE_ITEM": LocationData("Apt. 32 Master Bedroom - Item in Safe (Day 2-5)", LocationCat.LOOT, 322),
    "APT_32_MASTER_BEDROOM_TERATOMA_COMBAT_VICTORY": LocationData("Apt. 32 Master Bedroom - Slay Teratoma (Day 2-5)", LocationCat.COMBAT_VICTORY, 323),
    "APT_32_MASTER_BEDROOM_BALM": LocationData("Apt. 32 Master Bedroom - Item on Table by Bed (Day 2-5)", LocationCat.OVERWORLD_ITEM, 324),
    "APT_32_MASTER_BEDROOM_MADISON_COMBAT_VICTORY": LocationData("Apt. 32 Master Bedroom - Slay Madison (Day 2-4)", LocationCat.COMBAT_VICTORY, 325),
    "APT_32_MASTER_BEDROOM_MADISON_DAY_5_COMBAT_VICTORY": LocationData("Apt. 32 Master Bedroom - Slay Madison (Day 5)", LocationCat.COMBAT_VICTORY, 326),
    "APT_32_MASTER_BEDROOM_MADISON_DAY_9_COMBAT_VICTORY": LocationData("Apt. 32 Master Bedroom - Slay Madison (Day 9+)", LocationCat.COMBAT_VICTORY, 327),
    "APT_32_MASTER_BEDROOM_ARMY_FIGURE": LocationData("Apt. 32 Master Bedroom - Item on Table in Bottom Right (Day 2-5)", LocationCat.OVERWORLD_ITEM, 328),
    "APT_32_MASTER_BEDROOM_PURSE": LocationData("Apt. 32 Master Bedroom - Item Near Crib (Day 2-5)", LocationCat.OVERWORLD_ITEM, 329),
    "APT_32_MASTER_BEDROOM_BABY_TEETH_COMBAT_VICTORY": LocationData("Apt. 32 Master Bedroom - Defeat Baby Teeth (Day 2-5)", LocationCat.COMBAT_VICTORY, 330),
    "APT_32_KITCHEN_TOOTH_FAIRY_COMBAT_VICTORY": LocationData("Apt. 32 Kitchen - Slay Tooth Fairy (Day 2-5)", LocationCat.COMBAT_VICTORY, 331, difficulty_lock={DL.CURSED}),
    "APT_32_FRIDGE": LocationData("Apt. 32 Kitchen - Fridge Loot (Day 2-5)", LocationCat.LOOT, 332),
    "APT_32_KITCHEN_DRAWINGS": LocationData("Apt. 32 Kitchen - Item on Wall By Fridge (Day 2-5)", LocationCat.OVERWORLD_ITEM, 333),
    "APT_32_KITCHEN_FRYING_PAN": LocationData("Apt. 32 Kitchen - Item on West Kitchen Island (Day 2-5)", LocationCat.OVERWORLD_ITEM, 334),
    "APT_32_KITCHEN_CHEEZ_STIX": LocationData("Apt. 32 Kitchen - Item on East Kitchen Island (Day 2-5)", LocationCat.OVERWORLD_ITEM, 335),
    "APT_32_TRASH": LocationData("Apt. 32 Kitchen - Trash Can (Day 2-5)", LocationCat.OVERWORLD_ITEM, 336),
    "APT_32_KITCHEN_VINEGAR_1": LocationData("Apt. 32 Kitchen - Item on Floor by Trash 1 (Day 2-5)", LocationCat.OVERWORLD_ITEM, 337),
    "APT_32_KITCHEN_VINEGAR_2": LocationData("Apt. 32 Kitchen - Item on Floor by Trash 2 (Day 2-5)", LocationCat.OVERWORLD_ITEM, 338, difficulty_lock={DL.EXPLORER}),
    }

APT_32_TEETH_LOCATIONS = {
    **APT_32_TEETH_LOCATIONS_MAIN,
    **APT_32_TEETH_BEHIND_DOOR_KNOB
}

APT_33_LOCATIONS: dict[str, LocationData] = {
    "APT_33_LIVING_ROOM_CASH": LocationData("Apt. 33 Living Room - Item on Coffee Table", LocationCat.OVERWORLD_ITEM, 401),
    "APT_33_LIVING_ROOM_SCREAMATORIUM": LocationData("Apt. 33 Living Room - Item on Shelf", LocationCat.EVENT_ITEM, 402),
    "APT_33_BEDROOM_REFUSE_SHADOW": LocationData("Apt. 33 Bedroom - Set Boundaries With Masked Shadow", LocationCat.EVENT_ITEM, 403),
    "APT_33_BATHROOM_FIRST_AID_KIT": LocationData("Apt. 33 Bathroom - Item on Counter", LocationCat.OVERWORLD_ITEM, 404),
    "APT_33_BATHROOM_RECRUIT_ROACHES": LocationData("Apt. 33 Bathroom - Recruit Roaches", LocationCat.RECRUIT, 405),
    "APT_33_RECRUIT_PHILLIPPE": LocationData("Apt. 33 Living Room - Recruit Phillippe", LocationCat.RECRUIT, 406),
    "APT_33_RECRUIT_RAT_BABY": LocationData("Apt. 33 Living Room  - Recruit Rat Child", LocationCat.RECRUIT, 407),
    "APT_33_ROACH_QUEST": LocationData("Apt. 33 Living Room - Solve the Roaches' Dilemma", LocationCat.EVENT_ITEM, 408)
}

# MODIFIERS - 500s
FRONT_DOOR_LOCATIONS: dict[str, LocationData] = {}

APT_33_MEAT_LOCATIONS: dict[str, LocationData] = {
    "APT_33_MEAT_SPINE_COMBAT_VICTORY": LocationData("Apt. 33 Meat World Living Room - Slay Spine", LocationCat.FRIENDLY_FIRE, 601),
    "APT_33_MEAT_SPINE_SPARE": LocationData("Apt. 33 Meat World Living Room - Spare Spine", LocationCat.EVENT_ITEM, 602),
    "APT_33_MEAT_CONFUSION_COMBAT_VICTORY": LocationData("Apt. 33 Meat World Bedroom - Slay Confusion", LocationCat.COMBAT_VICTORY, 603),
    "APT_33_MEAT_STRETCH_FACE_COMBAT_VICTORY": LocationData("Apt. 33 Meat World Living Room - Slay Stretch Face", LocationCat.COMBAT_VICTORY, 604)
}

APT_34_FROZEN_ENTRYWAY_LOCATIONS: dict[str, LocationData] = {
    "APT_34_SALT": LocationData("Apt. 34 - Item on Table Near Entrance", LocationCat.OVERWORLD_ITEM, 701),
}

APT_34_BEDROOM_WEST_LOCATIONS: dict[str, LocationData] = {
    "APT_34_BEDROOM_SALT": LocationData("Apt. 34 Bedroom - Item on Upper Table", LocationCat.OVERWORLD_ITEM, 702),
    "APT_34_BEDROOM_TUQUE_COMBAT_VICTORY": LocationData("Apt. 34 Bedroom - Slay Tuque", LocationCat.COMBAT_VICTORY, 706),
}

APT_34_BEDROOM_EAST_LOCATIONS: dict[str, LocationData] = {
    "APT_34_BEDROOM_JEWELRY_BOX": LocationData("Apt. 34 Bedroom - Item on Bedside Table", LocationCat.OVERWORLD_ITEM, 703),
    "APT_34_BEDROOM_SPADE": LocationData("Apt. 34 Bedroom - Item on South Table 1", LocationCat.OVERWORLD_ITEM, 704),
    "APT_34_BEDROOM_VODKA": LocationData("Apt. 34 Bedroom - Item on South Table 2", LocationCat.OVERWORLD_ITEM, 705),
    "APT_34_BEDROOM_EARMUFFS_COMBAT_VICTORY": LocationData("Apt. 34 Bedroom - Slay Earmuffs", LocationCat.COMBAT_VICTORY, 707),
}

# the br is bathroom
APT_34_KITCHEN_BATHROOM_EAST_LOCATIONS: dict[str, LocationData] = {
    "APT_34_KITCHEN_ORANGE_COLA": LocationData("Apt. 34 Kitchen - Item on Table", LocationCat.OVERWORLD_ITEM, 708),
    "APT_34_KITCHEN_TRASH": LocationData("Apt. 34 Kitchen - Trash Can", LocationCat.OVERWORLD_ITEM, 709),
    "APT_34_FRIDGE": LocationData("Apt. 34 Kitchen - Fridge Loot", LocationCat.LOOT, 710),
    "APT_34_KITCHEN_TRAPPER_HAT_COMBAT_VICTORY": LocationData("Apt. 34 Kitchen - Slay Trapper Hat", LocationCat.COMBAT_VICTORY, 711),
    "APT_34_BATHROOM_TOOTHPASTE": LocationData("Apt. 34 Bathroom - Item on Table by Door", LocationCat.OVERWORLD_ITEM, 722),
}

APT_34_BATHROOM_WEST_LOCATIONS: dict[str, LocationData] = {
    "APT_34_BATHROOM_SCARF_COMBAT_VICTORY": LocationData("Apt. 34 Bathroom - Slay Scarf", LocationCat.COMBAT_VICTORY, 723),
    "APT_34_BATHROOM_BALM": LocationData("Apt. 34 Bathroom - Item on Counter 1", LocationCat.OVERWORLD_ITEM, 724),
    "APT_34_BATHROOM_MEDICATION": LocationData("Apt. 34 Bathroom - Item on Counter 2", LocationCat.OVERWORLD_ITEM, 725),
    "APT_34_BATHROOM_TONIC": LocationData("Apt. 34 Bathroom - Item on Counter 3", LocationCat.OVERWORLD_ITEM, 726),
}

APT_34_OFFICE_NORTH_LOCATIONS: dict[str, LocationData] = {
    "APT_34_OFFICE_KLYSOX": LocationData("Apt. 34 Office - Item Near North Entrance 1", LocationCat.OVERWORLD_ITEM, 727),
    "APT_34_OFFICE_SALT": LocationData("Apt. 34 Office - Item Near North Entrance 2", LocationCat.OVERWORLD_ITEM, 728),
}

APT_34_OFFICE_SOUTH_LOCATIONS: dict[str, LocationData] = {
    "APT_34_OFFICE_TRISCARF_COMBAT_VICTORY": LocationData("Apt. 34 Office - Slay Triscarf", LocationCat.COMBAT_VICTORY, 729),
    "APT_34_OFFICE_TONIC": LocationData("Apt. 34 Office - Item Above Television 1", LocationCat.OVERWORLD_ITEM, 730),
    "APT_34_OFFICE_HAMMER": LocationData("Apt. 34 Office - Item Above Television 2", LocationCat.OVERWORLD_ITEM, 731),
    "APT_34_OFFICE_OLD_CONSOLE": LocationData("Apt. 34 Office - Item Below Television", LocationCat.OVERWORLD_ITEM, 732),
}

APT_34_CLOSET_LOCATIONS: dict[str, LocationData] = {
    "APT_34_OFFICE_HOCKEY_CARDS": LocationData("Apt. 34 Office - Item on Table by South Entrance", LocationCat.OVERWORLD_ITEM, 733),
    "APT_34_CLOSET_HOCKEY_STICK": LocationData("Apt. 34 Closet - Item on Floor", LocationCat.OVERWORLD_ITEM, 734),
    "APT_34_CLOSET_HOCKEY_TROPHY": LocationData("Apt. 34 Closet - Lefthand Item", LocationCat.OVERWORLD_ITEM, 735),
    "APT_34_CLOSET_CASH": LocationData("Apt. 34 Closet - Righthand Item", LocationCat.OVERWORLD_ITEM, 736)
}

APT_34_KITCHEN_LOWER_LOCATIONS: dict[str, LocationData] = {
    "APT_34_KITCHEN_LOWER_BALACLAVA_COMBAT_VICTORY": LocationData("Apt. 34 Kitchen Lower - Slay Balaclava", LocationCat.COMBAT_VICTORY, 712),
    "APT_34_KITCHEN_LOWER_WRAPPED_GIFT": LocationData("Apt. 34 Kitchen Lower - Item on Table", LocationCat.OVERWORLD_ITEM, 713),
}

APT_34_LONG_BEDROOM_WEST_LOCATIONS: dict[str, LocationData] = {
    "APT_34_LONG_BEDROOM_FIRST_AID_KIT": LocationData("Apt. 34 South Bedroom - Item on Table by Entrance", LocationCat.OVERWORLD_ITEM, 714),
    "APT_34_LONG_BEDROOM_MANTEAU_COMBAT_VICTORY": LocationData("Apt. 34 South Bedroom - Slay Manteau", LocationCat.COMBAT_VICTORY, 715),  
}

APT_34_LONG_BEDROOM_SW_LOCATIONS: dict[str, LocationData] = {
    "APT_34_LONG_BEDROOM_GAMEKID_COLOR": LocationData("Apt. 34 South Bedroom - Item on Lower Table", LocationCat.OVERWORLD_ITEM, 716),
}

APT_34_LONG_BEDROOM_CENTER_LOCATIONS: dict[str, LocationData] = {
    "APT_34_LONG_BEDROOM_POMPOM_COMBAT_VICTORY": LocationData("Apt. 34 South Bedroom - Slay Pompom", LocationCat.COMBAT_VICTORY, 717),
}

APT_34_LONG_BEDROOM_NORTH_LOCATIONS: dict[str, LocationData] = {
    "APT_34_LONG_BEDROOM_WAKE_THE_BLOOD_KNIGHT": LocationData("Apt. 34 South Bedroom - Item on Center Table 1", LocationCat.OVERWORLD_ITEM, 720),
    "APT_34_LONG_BEDROOM_STIMULANT": LocationData("Apt. 34 South Bedroom - Item on Center Table 2", LocationCat.OVERWORLD_ITEM, 721),
}

APT_34_LONG_BEDROOM_EAST_LOCATIONS: dict[str, LocationData] = {
    "APT_34_LONG_BEDROOM_CASH": LocationData("Apt. 34 South Bedroom - Item on Righthand Table", LocationCat.OVERWORLD_ITEM, 718),
    "APT_34_LONG_BEDROOM_MERCURY_DISC": LocationData("Apt. 34 South Bedroom - Item on Floor Top Right", LocationCat.OVERWORLD_ITEM, 719),
}

APT_34_FROZEN_LOCATIONS = {
    **APT_34_FROZEN_ENTRYWAY_LOCATIONS,
    **APT_34_BEDROOM_WEST_LOCATIONS,
    **APT_34_BEDROOM_EAST_LOCATIONS,
    **APT_34_KITCHEN_BATHROOM_EAST_LOCATIONS,
    **APT_34_BATHROOM_WEST_LOCATIONS,
    **APT_34_OFFICE_NORTH_LOCATIONS,
    **APT_34_OFFICE_SOUTH_LOCATIONS,
    **APT_34_CLOSET_LOCATIONS,
    **APT_34_KITCHEN_LOWER_LOCATIONS,
    **APT_34_LONG_BEDROOM_WEST_LOCATIONS,
    **APT_34_LONG_BEDROOM_SW_LOCATIONS,
    **APT_34_LONG_BEDROOM_CENTER_LOCATIONS,
    **APT_34_LONG_BEDROOM_NORTH_LOCATIONS,
    **APT_34_LONG_BEDROOM_EAST_LOCATIONS
}


APT_35_SIBYL_LOCATIONS: dict[str, LocationData] = {
    "APT_35_FRIDGE": LocationData("Apt. 35 Kitchen - Fridge Loot", LocationCat.LOOT, 801)
}

APT_36_WOUNDED_LOCATIONS: dict[str, LocationData] = {
    "APT_36_LIVING_ROOM_BASEBALL_BAT": LocationData("Apt. 36 Living Room - Item on Lefthand Table", LocationCat.OVERWORLD_ITEM, 901),
    "APT_36_LIVING_ROOM_CASH": LocationData("Apt. 36 Living Room - Item on Righthand Table", LocationCat.OVERWORLD_ITEM, 902),
    "APT_36_LIVING_ROOM_ONLOOKER_COMBAT_VICTORY": LocationData("Apt. 36 Living Room - Slay Onlooker", LocationCat.COMBAT_VICTORY, 903),
    "APT_36_LIVING_ROOM_LOUIS_LEG_COMBAT_VICTORY": LocationData("Apt. 36 Living Room - Slay Louis' Leg", LocationCat.COMBAT_VICTORY, 904),
    "APT_36_BATHROOM_TONIC": LocationData("Apt. 36 Bathroom - Item on Sink", LocationCat.OVERWORLD_ITEM, 905),
    "APT_36_BATHROOM_BANDAGES": LocationData("Apt. 36 Bathroom - Item on Table", LocationCat.OVERWORLD_ITEM, 906),
    "APT_36_BATHROOM_PADLOCK_KEY": LocationData("Apt. 36 Bathroom - Item Dropped by Wounded Neighbor", LocationCat.OVERWORLD_ITEM, 907),
    "APT_36_BATHROOM_WOUNDED_NEIGHBOR_KNIFE": LocationData("Apt. 36 Bathroom - Item on Body", LocationCat.OVERWORLD_ITEM, 908),
    "APT_36_BATHROOM_WOUNDED_NEIGHBOR_COMBAT_VICTORY": LocationData("Apt. 36 Bathroom - Slay Wounded Neighbor", LocationCat.COMBAT_VICTORY, 909),
    "APT_36_BEDROOM_SAFE_ITEM": LocationData("Apt. 36 Bedroom - Item in Safe", LocationCat.LOOT, 910),
    "APT_36_BEDROOM_SIMPLE_KEY": LocationData("Apt. 36 Bedroom - Item on Table", LocationCat.OVERWORLD_ITEM, 911),
    "APT_36_BEDROOM_OBSERVER_COMBAT_VICTORY": LocationData("Apt. 36 Bedroom - Slay Observer", LocationCat.COMBAT_VICTORY, 912)
}

APT_37_VINCENT_LOCATIONS_MAIN: dict[str, LocationData] = {
    "APT_37_LOUIS_TAIL": LocationData("Apt. 37 Living Room - Slay Louis' Tail", LocationCat.OVERWORLD_ITEM, 1001),
    "APT_37_TABLE_PLATE_1": LocationData("Apt. 37 Kitchen - Item on Table 1", LocationCat.OVERWORLD_ITEM, 1002),
    "APT_37_TABLE_THROWING_KNIVES": LocationData("Apt. 37 Kitchen - Second Item on Table", LocationCat.OVERWORLD_ITEM, 1003),
    "APT_37_TABLE_FORKS": LocationData("Apt. 37 Kitchen - Third Item on Table", LocationCat.OVERWORLD_ITEM, 1004),
    "APT_37_TABLE_PLATE_2": LocationData("Apt. 37 Kitchen - Fourth Item on Table", LocationCat.OVERWORLD_ITEM, 1005, difficulty_lock={DL.EXPLORER}),
    "APT_37_CARVING_FORK": LocationData("Apt. 37 Kitchen - Item on Counter", LocationCat.OVERWORLD_ITEM, 1006),
    "APT_37_FRIDGE": LocationData("Apt. 37 Kitchen - Fridge Loot", LocationCat.LOOT, 1007),
    "APT_37_TRASH": LocationData("Apt. 37 Kitchen - Trash Can", LocationCat.LOOT, 1008),
    "APT_37_WHISKEY": LocationData("Apt. 37 Living Room - Item on Left Table 2", LocationCat.OVERWORLD_ITEM, 1009),
    "APT_37_CRAFTING_KIT": LocationData("Apt. 37 Living Room - Second Item on Left Table", LocationCat.OVERWORLD_ITEM, 1010),
    "APT_37_CHOCKY_BAR": LocationData("Apt. 37 Living Room - Item by Window", LocationCat.OVERWORLD_ITEM, 1011),
    "APT_37_ONLOOKER_COMBAT_VICTORY": LocationData("Apt. 37 Living Room - Slay Onlooker by Entrance", LocationCat.COMBAT_VICTORY, 1012),
    "APT_37_VINCENT_COMBAT_VICTORY": LocationData("Apt. 37 Living Room - Slay Vincent", LocationCat.COMBAT_VICTORY, 1013),
    "APT_37_BATHROOM_CLEANEREX": LocationData("Apt. 37 Bathroom - Item on Floor", LocationCat.OVERWORLD_ITEM, 1014),
    "APT_37_BATHROOM_MEDICELL": LocationData("Apt. 37 Bathroom - Item on Counter 1", LocationCat.OVERWORLD_ITEM, 1015),
    "APT_37_BATHROOM_BANDAGES": LocationData("Apt. 37 Bathroom - Item on Counter 2", LocationCat.OVERWORLD_ITEM, 1016),
    "APT_37_BATHROOM_GAWKER_COMBAT_VICTORY": LocationData("Apt. 37 Bathroom - Slay Gawker", LocationCat.COMBAT_VICTORY, 1017),
    "APT_37_PROJECTOR_ROOM_ONLOOKER_COMBAT_VICTORY": LocationData("Apt. 37 Projector Room - Slay Onlooker", LocationCat.COMBAT_VICTORY, 1018),
    "APT_37_PROJECTOR_ROOM_WIZARDS_HELL": LocationData("Apt. 37 Projector Room - Item on Lower Left Table", LocationCat.OVERWORLD_ITEM, 1019),
    "APT_37_PROJECTOR_ROOM_GOLF_CLUB": LocationData("Apt. 37 Projector Room - Item on Projector Table 1", LocationCat.OVERWORLD_ITEM, 1020),
    "APT_37_PROJECTOR_ROOM_CLOTH": LocationData("Apt. 37 Projector Room - Item on Projector Table 2", LocationCat.OVERWORLD_ITEM, 1021),
    "APT_37_PROJECTOR_ROOM_PHOTO": LocationData("Apt. 37 Projector Room - Imprint Image on Photo Paper", LocationCat.EVENT_ITEM, 1022),
    "APT_37_BEDROOM_GUINEA_PIG": LocationData("Apt. 37 Bedroom - Item by Door", LocationCat.OVERWORLD_ITEM, 1023),
    "APT_37_BEDROOM_GLASSES": LocationData("Apt. 37 Bedroom - Item On Table 1", LocationCat.OVERWORLD_ITEM, 1024),
    "APT_37_BEDROOM_CASH": LocationData("Apt. 37 Bedroom - Item On Table 2", LocationCat.OVERWORLD_ITEM, 1025),
    "APT_37_BEDROOM_ONLOOKER_A_COMBAT_VICTORY": LocationData("Apt. 37 Bedroom - Slay Onlookers", LocationCat.COMBAT_VICTORY, 1026),
    "APT_37_BEDROOM_TRASH": LocationData("Apt. 37 Bedroom - Trash Can", LocationCat.LOOT, 1027)
}
    
APT_37_LOCKED_ROOM_LOCATIONS: dict[str, LocationData] = {
    "APT_37_LOCKED_ROOM_TRASH": LocationData("Apt. 37 Locked Room - Trash Can", LocationCat.LOOT, 1028),
    "APT_37_LOCKED_ROOM_WHISKEY": LocationData("Apt. 37 Locked Room - Item on Table by Door 1", LocationCat.OVERWORLD_ITEM, 1029),
    "APT_37_LOCKED_ROOM_BEER": LocationData("Apt. 37 Locked Room - Item on Table by Door 2", LocationCat.OVERWORLD_ITEM, 1030),
    "APT_37_LOCKED_ROOM_TONIC": LocationData("Apt. 37 Locked Room - Item on West Table 1", LocationCat.OVERWORLD_ITEM, 1031, difficulty_lock={DL.EXPLORER}),
    "APT_37_LOCKED_ROOM_BANDAGES": LocationData("Apt. 37 Locked Room - Item on West Table 2", LocationCat.OVERWORLD_ITEM, 1032),
    "APT_37_LOCKED_ROOM_MACHETE": LocationData("Apt. 37 Locked Room - Item on West Table 3", LocationCat.OVERWORLD_ITEM, 1033),
    "APT_37_LOCKED_ROOM_FIRST_AID_KIT": LocationData("Apt. 37 Locked Room - Item on West Table 4", LocationCat.OVERWORLD_ITEM, 1034),
    "APT_37_LOCKED_ROOM_CLOGS": LocationData("Apt. 37 Locked Room - Item on Floor by Bed", LocationCat.OVERWORLD_ITEM, 1035),
    "APT_37_LOCKED_ROOM_CLOTH": LocationData("Apt. 37 Locked Room - Item on Table by Bed", LocationCat.OVERWORLD_ITEM, 1036),
    "APT_37_LOCKED_ROOM_EYE_MONSTERS_COMBAT_VICTORY": LocationData("Apt. 37 Locked Room - Slay Eye Monsters", LocationCat.COMBAT_VICTORY, 1037)
}

APT_37_VINCENT_LOCATIONS = {
    **APT_37_VINCENT_LOCATIONS_MAIN,
    **APT_37_LOCKED_ROOM_LOCATIONS
}

APT_38_ROOMMATES_LOCATIONS_MAIN: dict[str, LocationData] = {
    "APT_38_FIBER_DRAGON_COMBAT_VICTORY": LocationData("Apt. 38 - Slay Fiber Dragon", LocationCat.COMBAT_VICTORY, 1201),
    "APT_38_LOUIS_UPPER_HALF_COMBAT_VICTORY": LocationData("Apt. 38 - Slay Louis' Upper Half", LocationCat.COMBAT_VICTORY, 1202),
    "APT_38_LOUIS_HEAD_COMBAT_VICTORY": LocationData("Apt. 38 - Slay Louis' Head", LocationCat.COMBAT_VICTORY, 1203),
    "APT_38_LOUIS_TORSO_COMBAT_VICTORY": LocationData("Apt. 38 - Slay Louis' Torso", LocationCat.COMBAT_VICTORY, 1204),
    "APT_38_FRIDGE": LocationData("Apt. 38 Kitchen - Fridge Loot", LocationCat.LOOT, 1205),
    "APT_38_CASH": LocationData("Apt. 38 Kitchen - Item on Kitchen Island", LocationCat.OVERWORLD_ITEM, 1206),
    "APT_38_TRASH": LocationData("Apt. 38 Kitchen - Trash Can", LocationCat.LOOT, 1207),
    "APT_38_FORK": LocationData("Apt. 38 Kitchen - Item on Dining Table 1", LocationCat.OVERWORLD_ITEM, 1208),
    "APT_38_FORK_2": LocationData("Apt. 38 Kitchen - Item on Dining Table 2", LocationCat.OVERWORLD_ITEM, 1209),
    "APT_38_PLATE_1": LocationData("Apt. 38 Kitchen - Item on Dining Table 3", LocationCat.OVERWORLD_ITEM, 1210, difficulty_lock={DL.EXPLORER}),
    "APT_38_PLATE_2": LocationData("Apt. 38 Kitchen - Item on Dining Table 4", LocationCat.OVERWORLD_ITEM, 1211, difficulty_lock={DL.EXPLORER}),
    "APT_38_HIVE_MAN_COMBAT_VICTORY": LocationData("Apt. 38 - Slay Charlie the Hive Man", LocationCat.COMBAT_VICTORY, 1232),
    "APT_38_PIERRE_GIFT": LocationData("Apt. 38 Pierre's Room - Item on First Table", LocationCat.OVERWORLD_ITEM, 1233),
    "APT_38_PIERRE_CHOCKY_BAR": LocationData("Apt. 38 Pierre's Room - Item on Second Table", LocationCat.OVERWORLD_ITEM, 1234),
    "APT_38_PIERRE_CLOWN_DRAWING": LocationData("Apt. 38 Pierre's Room - Gift From Pierre", LocationCat.EVENT_ITEM, 1235),
    "APT_38_PIERRE_CLOWN_WIG": LocationData("Apt. 38 Pierre's Room - Pierre Combat Reward", LocationCat.EVENT_ITEM, 1236),
    "APT_38_BATHROOM_FIRST_AID_KIT": LocationData("Apt. 38 Bathroom - Item on Counter 1", LocationCat.OVERWORLD_ITEM, 1237),
    "APT_38_BATHROOM_CLOTH": LocationData("Apt. 38 Bathroom - Item on Counter 2", LocationCat.OVERWORLD_ITEM, 1238),
    "APT_38_BATHROOM_CLEANEREX": LocationData("Apt. 38 Bathroom - Item Near Sink", LocationCat.OVERWORLD_ITEM, 1239)
}

APT_38_KAELEY_INTRO_LOCATIONS = {
    "APT_38_KAELEY_COMBAT_VICTORY": LocationData("Apt. 38 - Slay Kaeley", LocationCat.FRIENDLY_FIRE, 1212),
    "APT_38_KAELEY_PURCHASE": LocationData("Apt. 38 - Purchase Item from Kaeley", LocationCat.MERCHANT, 1213),
}

KAELEY_NW_LOCATIONS = {
    "APT_38_KAELEY_SHURIKEN": LocationData("Apt. 38 Kaeley Maze Northwest Chamber - Item 1", LocationCat.OVERWORLD_ITEM, 1214),
    "APT_38_KAELEY_SHOTGUN_SHELLS": LocationData("Apt. 38 Kaeley Maze Northwest Chamber - Item 2", LocationCat.OVERWORLD_ITEM, 1215),
}

KAELEY_W_LOCATIONS = {
    "APT_38_KAELEY_PITCHFORK": LocationData("Apt. 38 Kaeley Maze West Chamber - Item 1", LocationCat.OVERWORLD_ITEM, 1216),
    "APT_38_KAELEY_STIMULANT": LocationData("Apt. 38 Kaeley Maze West Chamber - Item 2", LocationCat.OVERWORLD_ITEM, 1217),
}

KAELEY_SW_LOCATIONS = {
    "APT_38_KAELEY_GIFT": LocationData("Apt. 38 Kaeley Maze Southwest Chamber - Item 1", LocationCat.OVERWORLD_ITEM, 1218),
    "APT_38_KAELEY_RIFLE_AMMO": LocationData("Apt. 38 Kaeley Maze Southwest Chamber - Item 2", LocationCat.OVERWORLD_ITEM, 1219),
}

KAELEY_CENTER_LEFT_LOCATIONS = {
    "APT_38_KAELEY_GIFT_2": LocationData("Apt. 38 Kaeley Maze Center-left Chamber - Item", LocationCat.OVERWORLD_ITEM, 1220),
}

KAELEY_CENTER_RIGHT_LOCATIONS = {
    "APT_38_KAELEY_TONIC": LocationData("Apt. 38 Kaeley Maze Center-right Chamber - Item 1", LocationCat.OVERWORLD_ITEM, 1221),
    "APT_38_KAELEY_PISTOL_BULLETS": LocationData("Apt. 38 Kaeley Maze Center-right Chamber - Item 2", LocationCat.OVERWORLD_ITEM, 1222),
}

KAELEY_CENTER_LOCATIONS = {
    "APT_38_KAELEY_ELIXIR": LocationData("Apt. 38 Kaeley Maze Center Chamber - Item", LocationCat.OVERWORLD_ITEM, 1223),
}

KAELEY_S_LOCATIONS = {
    "APT_38_KAELEY_GIFT_3": LocationData("Apt. 38 Kaeley Maze South Chamber - Item 1", LocationCat.OVERWORLD_ITEM, 1224),
    "APT_38_KAELEY_MAGNUM_BULLET": LocationData("Apt. 38 Kaeley Maze South Chamber - Item 2", LocationCat.OVERWORLD_ITEM, 1225),
    "APT_38_KAELEY_SNAKE_WHIP": LocationData("Apt. 38 Kaeley Maze South Chamber - Item 3", LocationCat.OVERWORLD_ITEM, 1226),
}

KAELEY_SE_LOCATIONS = {
    "APT_38_KAELEY_FIRST_AID_KIT": LocationData("Apt. 38 Kaeley Maze Southeast Chamber - Item 1", LocationCat.OVERWORLD_ITEM, 1227),
    "APT_38_KAELEY_GRENADE": LocationData("Apt. 38 Kaeley Maze Southeast Chamber - Item 2", LocationCat.OVERWORLD_ITEM, 1228),
}

KAELEY_E_LOCATIONS ={
    "APT_38_KAELEY_HEALING_SPRAY": LocationData("Apt. 38 Kaeley Maze East Chamber - Item", LocationCat.OVERWORLD_ITEM, 1229),
}

KAELEY_NE_LOCATIONS = {
    "APT_38_KAELEY_GIFT_4": LocationData("Apt. 38 Kaeley Maze Northeast Chamber - Item 1", LocationCat.OVERWORLD_ITEM, 1230),
    "APT_38_KAELEY_SMG_AMMO": LocationData("Apt. 38 Kaeley Maze Northeast Chamber - Item 2", LocationCat.OVERWORLD_ITEM, 1231),
}

F3_JANITOR_CLOSET_LOCATIONS: dict[str, LocationData] = {
    "F3_CLOSET_WALLET": LocationData("Floor 3 Janitor Closet - Item on South Table 1", LocationCat.OVERWORLD_ITEM, 1301),
    "F3_CLOSET_KEY": LocationData("Floor 3 Janitor Closet - Item on West Table", LocationCat.OVERWORLD_ITEM, 1302),
    "F3_CLOSET_ROACH": LocationData("Floor 3 Janitor Closet - Roach", LocationCat.OVERWORLD_ITEM, 1303),
    "F3_CLOSET_JACKET_FIGURINE": LocationData("Floor 3 Janitor Closet - Item on South Table 2", LocationCat.OVERWORLD_ITEM, 1304)
}

APT_38_ROOMMATES_LOCATIONS = {
    **APT_38_ROOMMATES_LOCATIONS_MAIN,
    **APT_38_KAELEY_INTRO_LOCATIONS,
    **KAELEY_NW_LOCATIONS,
    **KAELEY_W_LOCATIONS,
    **KAELEY_SW_LOCATIONS,
    **KAELEY_CENTER_LEFT_LOCATIONS,
    **KAELEY_CENTER_RIGHT_LOCATIONS,
    **KAELEY_CENTER_LOCATIONS,
    **KAELEY_S_LOCATIONS,
    **KAELEY_SE_LOCATIONS,
    **KAELEY_E_LOCATIONS,
    **KAELEY_NE_LOCATIONS
}

GLITCH_WORLD_MAIN_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_BGRAAT_COMBAT_VICTORY": LocationData("Glitch World - Slay bgR aa|t", LocationCat.COMBAT_VICTORY, 1401),
    "GLITCH_GA2RD_COMBAT_VICTORY": LocationData("Glitch World - Slay gaA2 rd", LocationCat.COMBAT_VICTORY, 1402),
}

GLITCH_WORLD_END_CHAMBER_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_LAST_WILL": LocationData("Glitch World End Chamber - Item on Pedestal", LocationCat.OVERWORLD_ITEM, 1403),
    "GLITCH_EYEW0RM_COMBAT_VICTORY": LocationData("Glitch World End Chamber - Slay eyEW0rm", LocationCat.COMBAT_VICTORY, 1404),
    "GLITCH_BLACK_KEY": LocationData("Glitch World End Chamber - Item on Floor", LocationCat.OVERWORLD_ITEM, 1405),
}

GLITCH_WORLD_WEST_AND_SOUTHWEST_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_W_GLITCH_ELIXIR": LocationData("Glitch World West - Item From NPC", LocationCat.EVENT_ITEM, 1423),
    "GLITCH_W_CRIM50N_IM92_COMBAT_VICTORY": LocationData("Glitch World West - Slay crIm\50n Im9*2", LocationCat.COMBAT_VICTORY, 1424),
    "GLITCH_W_FTBLHELMT": LocationData("Glitch World West - Item Behind crIm\50n Im9*2", LocationCat.OVERWORLD_ITEM, 1425),
    "GLITCH_SW_TR2NK_COMBAT_VICTORY": LocationData("Glitch World Southwest - Slay tR2 nk", LocationCat.COMBAT_VICTORY, 1426),
    "GLITCH_SW_YELLOW_KEY": LocationData("Glitch World Southwest - Item in North Room", LocationCat.OVERWORLD_ITEM, 1427),
    "GLITCH_SW_AMBROSE": LocationData("Glitch World Southwest - Take Ambrose", LocationCat.EVENT_ITEM, 1428),
    "GLITCH_SW_SKNFCE_COMBAT_VICTORY": LocationData("Glitch World Southwest - Sk?nFce", LocationCat.COMBAT_VICTORY, 1430),
    "GLITCH_SW_WHITE_KEY": LocationData("Glitch World Southwest - Item Behind Sk?nFce", LocationCat.OVERWORLD_ITEM, 1431),
}

GLITCH_WORLD_SLIME_ROOM_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_SW_SLIME_COMBAT_VICTORY": LocationData("Glitch World Southwest - Slay ****** (Slime)", LocationCat.COMBAT_VICTORY, 1429),
}

GLITCH_WORLD_MAZE_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_MAZE_SKEL3TON_NE_COMBAT_VICTORY": LocationData("Glitch World Maze - Slay First skE l3t{On", LocationCat.COMBAT_VICTORY, 1432),
    "GLITCH_MAZE_SKEL3TON_CENTER_COMBAT_VICTORY": LocationData("Glitch World Maze - Slay Second skE l3t{On", LocationCat.COMBAT_VICTORY, 1433),
    "GLITCH_MAZE_SKEL3TON_W_COMBAT_VICTORY": LocationData("Glitch World Maze - Slay Third skE l3t{On", LocationCat.COMBAT_VICTORY, 1434),
    "GLITCH_MAZE_HEAD_COMBAT_VICTORY": LocationData("Glitch World Maze - Slay hE@A d", LocationCat.COMBAT_VICTORY, 1435),
    "GLITCH_MAZE_HLING_SPRAY": LocationData("Glitch World Maze - First Item", LocationCat.OVERWORLD_ITEM, 1436),
    "GLITCH_MAZE_YELLOW_KEY": LocationData("Glitch World Maze - Second Item", LocationCat.OVERWORLD_ITEM, 1437),
    "GLITCH_MAZE_VNAGE_UCKY_TIEAKERS": LocationData("Glitch World Maze - Third Item", LocationCat.OVERWORLD_ITEM, 1438)
}

GLITCH_WORLD_EAST_W_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_E_RED_KEY": LocationData("Glitch World East - Item in Center Chamber", LocationCat.OVERWORLD_ITEM, 1413),
    "GLITCH_E_TR2NK_COMBAT_VICTORY": LocationData("Glitch World East - Slay tR2 nk", LocationCat.COMBAT_VICTORY, 1411),
}

GLITCH_WORLD_EAST_E_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_E_LLEECH_COMBAT_VICTORY": LocationData("Glitch World East - Slay lLEeCh", LocationCat.COMBAT_VICTORY, 1412),
    "GLITCH_E_YELLOW_KEY": LocationData("Glitch World East - Item Behind lLEeCh", LocationCat.OVERWORLD_ITEM, 1414),
}

GLITCH_WORLD_NE_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_NE_PULLOUT_COMBAT_VICTORY": LocationData("Glitch World Northeast - Slay PUl#Lout", LocationCat.COMBAT_VICTORY, 1415),
    "GLITCH_NE_GREEN_KEY": LocationData("Glitch World Northeast - Item Behind PUl#Lout", LocationCat.OVERWORLD_ITEM, 1416),
    "GLITCH_NE_R0ACH3_A": LocationData("Glitch World Northeast - Slay r0 Ach3 North", LocationCat.COMBAT_VICTORY, 1417),
    "GLITCH_NE_R0ACH3_B": LocationData("Glitch World Northeast - Slay r0 Ach3 South", LocationCat.COMBAT_VICTORY, 1418),
}

GLITCH_WORLD_NE_HYDRA_LAIR_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_SLIME_HYDRA_COMBAT_VICTORY": LocationData("Glitch World - Slay Slime Hydra", LocationCat.COMBAT_VICTORY, 1439),
}

GLITCH_WORLD_SE_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_SE_CRIM50N_IM92_COMBAT_VICTORY": LocationData("Glitch World Southeast - Slay crIm\50n Im9*2", LocationCat.COMBAT_VICTORY, 1419),
    "GLITCH_E_SE_P1TCH5_COMBAT_VICTORY": LocationData("Glitch World East by Southeast - Slay p1tc h5", LocationCat.COMBAT_VICTORY, 1421),
    "GLITCH_E_SE_RMYJCKET": LocationData("Glitch World East by Southeast - Item", LocationCat.OVERWORLD_ITEM, 1422),
}

GLITCH_WORLD_HONKO_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_HONKO_COMBAT_VICTORY": LocationData("Glitch World - Slay Honko", LocationCat.COMBAT_VICTORY, 1420),
}

GATE_ROOM_NE_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_SHORTCUT_BLUE_KEY": LocationData("Glitch World Gate Room - Item in Dead End", LocationCat.OVERWORLD_ITEM, 1406),
}

GATE_ROOM_WEST_GHOST_METALBAT_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_GHOS7T_COMBAT_VICTORY": LocationData("Glitch World Gate Room West - Slay gHos7 T", LocationCat.COMBAT_VICTORY, 1409),
    "GLITCH_METTAL_BA2T": LocationData("Glitch World Gate Room West - Item at Dead End", LocationCat.OVERWORLD_ITEM, 1410),
}

GATE_ROOM_SE_HAIRHEAD_GUN_LOCATIONS: dict[str, LocationData] = {
    "GLITCH_HAIRHE3AD_COMBAT_VICTORY": LocationData("Glitch World Gate Room East - Slay hAiRhE3ad", LocationCat.COMBAT_VICTORY, 1407),
    "GLITCH_GUN_COMBAT_VICTORY": LocationData("Glitch World Gate Room East - Slay gun", LocationCat.COMBAT_VICTORY, 1408),
}

GLITCH_WORLD_LOCATIONS: dict[str, LocationData] = {
    **GLITCH_WORLD_MAIN_LOCATIONS,
    **GLITCH_WORLD_END_CHAMBER_LOCATIONS,
    **GLITCH_WORLD_WEST_AND_SOUTHWEST_LOCATIONS,
    **GLITCH_WORLD_SLIME_ROOM_LOCATIONS,
    **GLITCH_WORLD_MAZE_LOCATIONS,
    **GLITCH_WORLD_EAST_W_LOCATIONS,
    **GLITCH_WORLD_EAST_E_LOCATIONS,
    **GLITCH_WORLD_NE_LOCATIONS,
    **GLITCH_WORLD_NE_HYDRA_LAIR_LOCATIONS,
    **GLITCH_WORLD_SE_LOCATIONS,
    **GLITCH_WORLD_HONKO_LOCATIONS,
    **GATE_ROOM_NE_LOCATIONS,
    **GATE_ROOM_WEST_GHOST_METALBAT_LOCATIONS,
    **GATE_ROOM_SE_HAIRHEAD_GUN_LOCATIONS
}



"""
--- F2 LOCATIONS --- 
"""

F2_HALL_EAST_LOCATIONS: dict[str, LocationData] = {
    "F2_LARGE_SHADE_COMBAT_VICTORY": LocationData("Floor 2 Hall - Slay Large Shade '????? ??? ??'", LocationCat.COMBAT_VICTORY, 1501),
    "F2_NESTOR_HAND_WORMS_COMBAT_VICTORY": LocationData("Floor 2 Hall - Slay Hand Worms", LocationCat.COMBAT_VICTORY, 1502),
    "F2_APT_21_KEY": LocationData("Floor 2 Hall - Item in Junk Pile", LocationCat.OVERWORLD_ITEM, 1503),
    "F2_PISTOL": LocationData("Floor 2 Hall - First Item After Beast Chase", LocationCat.OVERWORLD_ITEM, 1504, difficulty_lock={DL.SURVIVOR, DL.EXPLORER}),
    "F2_PISTOL_BULLETS_1": LocationData("Floor 2 Hall - Second Item After Beast Chase", LocationCat.OVERWORLD_ITEM, 1505, difficulty_lock={DL.SURVIVOR, DL.EXPLORER}),
    "F2_PISTOL_BULLETS_2": LocationData("Floor 2 Hall - Third Item After Beast Chase", LocationCat.OVERWORLD_ITEM, 1506, difficulty_lock={DL.EXPLORER}),
    "F2_GRASSHOPPER_COMBAT_VICTORY": LocationData("Floor 2 Hall - Slay Grasshopper", LocationCat.COMBAT_VICTORY, 1507),
    "F2_GRINNING_BEAST_CHASE_POOL_CUE": LocationData("Floor 2 Hall - Item During Beast Chase", LocationCat.OVERWORLD_ITEM, 1508, difficulty_lock={DL.CURSED}),
    "F2_GRINNING_BEAST_COMBAT_VICTORY": LocationData("Floor 2 Hall - Defeat the Grinning Beast", LocationCat.COMBAT_VICTORY, 1509),
    "F2_RECRUIT_ASTER": LocationData("Floor 2 Hall - Recruit Aster", LocationCat.RECRUIT, 1510)
}

APT_20_JEANNE_PHASE1_LOCATIONS: dict[str, LocationData] = {
    "APT_20_JEANNE_COMBAT_VICTORY": LocationData("Apt. 20 Phase 1 - Slay Jeanne", LocationCat.FRIENDLY_FIRE, 1601),
    "APT_20_CLEANEREX": LocationData("Apt. 20 Phase 1 - Item on North Table", LocationCat.OVERWORLD_ITEM, 1602),
    "APT_20_MOP": LocationData("Apt. 20 Phase 1 - Item in Northwest Corner", LocationCat.OVERWORLD_ITEM, 1603),
    "APT_20_FORK": LocationData("Apt. 20 Phase 1 - Item on Dining Table", LocationCat.OVERWORLD_ITEM, 1604),
    "APT_20_MUFFIN": LocationData("Apt. 20 Phase 1 - Item on Kitchen Counter", LocationCat.OVERWORLD_ITEM, 1605),
    "APT_20_CLEAVER": LocationData("Apt. 20 Phase 1 - Item on Lower Counter", LocationCat.OVERWORLD_ITEM, 1606),
    "APT_20_FRIDGE": LocationData("Apt. 20 Phase 1 - Fridge Loot", LocationCat.LOOT, 1607),
    "APT_20_BATHROOM_MEDICINE_CABINET": LocationData("Apt. 20 Bathroom Phase 1 - Medicine Cabinet Loot", LocationCat.OVERWORLD_ITEM, 1608),
    "APT_20_BATHROOM_ROACH": LocationData("Apt. 20 Bathroom Phase 1 - Cockroach", LocationCat.OVERWORLD_ITEM, 1609),
    "APT_20_BATHROOM_SOAP": LocationData("Apt. 20 Bathroom Phase 1 - Item on Counter", LocationCat.OVERWORLD_ITEM, 1610),
}

APT_20_JEANNE_PHASE2_LOCATIONS: dict[str, LocationData] = {
    "APT_20_HYDRA_A_COMBAT_VICTORY": LocationData("Apt. 20 Phase 2 - Slay Hydra Head West of Door", LocationCat.COMBAT_VICTORY, 1611),
    "APT_20_HYDRA_B_COMBAT_VICTORY": LocationData("Apt. 20 Phase 2 - Slay Hydra Head East of Door", LocationCat.COMBAT_VICTORY, 1612),
    "APT_20_JEANNE_HYDRA_COMBAT_VICTORY": LocationData("Apt. 20 Phase 2 - Slay Jeanne (Hydra)", LocationCat.FRIENDLY_FIRE, 1613),
    "APT_20_HYDRA_C_COMBAT_VICTORY": LocationData("Apt. 20 Phase 2 - Slay Hydra Head Near South Entrance", LocationCat.COMBAT_VICTORY, 1614),
    "APT_20_W_HYDRA_COMBAT_VICTORY": LocationData("Apt. 20 Phase 2 West - Slay the Four Hydra Heads", LocationCat.COMBAT_VICTORY, 1615),
    "APT_20_W_MOTORCYCLE_HELMET": LocationData("Apt. 20 Phase 2 West - Item on Northwest Table", LocationCat.OVERWORLD_ITEM, 1616),
    "APT_20_W_VODKA": LocationData("Apt. 20 Phase 2 West - Item on Northeast Table", LocationCat.OVERWORLD_ITEM, 1617),
    "APT_20_W_CASH": LocationData("Apt. 20 Phase 2 West - Item on South Table", LocationCat.OVERWORLD_ITEM, 1618),
    "APT_20_E_HYDRA_COMBAT_VICTORY": LocationData("Apt. 20 Phase 2 East - Slay the Three Hydra Heads", LocationCat.COMBAT_VICTORY, 1619),
    "APT_20_E_TONIC": LocationData("Apt. 20 Phase 2 East - Item on West Table", LocationCat.OVERWORLD_ITEM, 1620),
    "APT_20_E_VINTAGE_SNEAKERS": LocationData("Apt. 20 Phase 2 East - Item on Northeast Table", LocationCat.OVERWORLD_ITEM, 1621),
    "APT_20_E_STUDDED_JACKET": LocationData("Apt. 20 Phase 2 East - Item on Southeast Table", LocationCat.OVERWORLD_ITEM, 1622),
    "APT_20_E_CASH": LocationData("Apt. 20 Phase 2 East - Item on East Table", LocationCat.OVERWORLD_ITEM, 1623),
    "APT_20_HYDRA_HEADS": LocationData("Apt. 20 Phase 2 - Reward From Jeanne (All Heads Slain)", LocationCat.EVENT_ITEM, 1624),
    "APT_20_HYDRA_LAUNDRY": LocationData("Apt. 20 Phase 2 - Bring Jeanne Her Laundry", LocationCat.EVENT_ITEM, 1625)
}

APT_20_JEANNE_LOCATIONS = {
    **APT_20_JEANNE_PHASE1_LOCATIONS,
    **APT_20_JEANNE_PHASE2_LOCATIONS
}

APT_21_LYLE_MAIN_LOCATIONS = {
    "APT_21_TRASH": LocationData("Apt. 21 - Trash Can", LocationCat.LOOT, 1701),
    "APT_21_FRIDGE": LocationData("Apt. 21 - Fridge", LocationCat.LOOT, 1702),
    "APT_21_CROSSWORD_BOOK": LocationData("Apt. 21 - Item on Coffee Table", LocationCat.OVERWORLD_ITEM, 1703),
    "APT_21_LYLE_COMBAT_VICTORY": LocationData("Apt. 21 - Slay Shutterbug", LocationCat.FRIENDLY_FIRE, 1704),
    "APT_21_FIRST_KISS_GIFT": LocationData("Apt. 21 - First Trade With Lyle", LocationCat.EVENT_ITEM, 1705),
    "APT_21_SECOND_KISS_GIFT": LocationData("Apt. 21 - Second Trade With Lyle", LocationCat.EVENT_ITEM, 1706),
    "APT_21_CLOSET_JUNK": LocationData("Apt. 21 Closet - First Item on Table", LocationCat.OVERWORLD_ITEM, 1707),
    "APT_21_CLOSET_DCLOGGER": LocationData("Apt. 21 Closet - Second Item on Table", LocationCat.OVERWORLD_ITEM, 1708),
    "APT_21_CLOSET_BROOM": LocationData("Apt. 21 Closet - Item Between Boxes", LocationCat.OVERWORLD_ITEM, 1709),
    "APT_21_CLOSET_ANTIDOTE": LocationData("Apt. 21 Closet - Item on Shelf", LocationCat.OVERWORLD_ITEM, 1710),
    "APT_21_CLOSET_LOKJAW_COMBAT_VICTORY": LocationData("Apt. 21 Closet - Slay Lokjaw", LocationCat.COMBAT_VICTORY, 1711),
    "APT_21_CLOSET_SAFE": LocationData("Apt. 21 Closet - Item in Safe", LocationCat.LOOT, 1712),
    "APT_21_BATHROOM_SOAP": LocationData("Apt. 21 Bathroom - Item on Floor Near Tub", LocationCat.OVERWORLD_ITEM, 1713),
    "APT_21_BATHROOM_ANXIETY_MEDS": LocationData("Apt. 21 Bathroom - First Item on Counter", LocationCat.OVERWORLD_ITEM, 1714),
    "APT_21_BATHROOM_MEDICELL": LocationData("Apt. 21 Bathroom - Second Item on Counter", LocationCat.OVERWORLD_ITEM, 1715),
    "APT_21_BATHROOM_EYECLUSTER_COMBAT_VICTORY": LocationData("Apt. 21 Bathroom - Eyecluster Combat Victory", LocationCat.COMBAT_VICTORY, 1716),
    "APT_21_BATHROOM_MEDICINE_CABINET": LocationData("Apt. 21 Bathroom - Medicine Cabinet", LocationCat.LOOT, 1717),
}

APT_21_LYLE_DARK_ROOM_LOCATIONS = {
    "APT_21_DARK_ROOM_KEY": LocationData("Apt. 21 Dark Room - Item Between Shelves", LocationCat.OVERWORLD_ITEM, 1718),
    "APT_21_DARK_ROOM_PHOTO": LocationData("Apt. 21 Dark Room - Develop Photograph", LocationCat.EVENT_ITEM, 1719),
    "APT_21_DARK_ROOM_PHOTO_PAPER": LocationData("Apt. 21 Dark Room - Item from Photo Paper Stack", LocationCat.OVERWORLD_ITEM, 1732),
}

APT_21_LYLE_BEDROOM_LOCATIONS = {
    "APT_21_BEDROOM_BEEF_1": LocationData("Apt. 21 Bedroom - First Item on Meat Floor", LocationCat.OVERWORLD_ITEM, 1720),
    "APT_21_BEDROOM_BEEF_2": LocationData("Apt. 21 Bedroom - Second Item on Meat Floor", LocationCat.OVERWORLD_ITEM, 1721),
    "APT_21_BEDROOM_BEEF_3": LocationData("Apt. 21 Bedroom - Third Item on Meat Floor", LocationCat.OVERWORLD_ITEM, 1722, difficulty_lock={DL.EXPLORER}),
    "APT_21_BEDROOM_BEEF_4": LocationData("Apt. 21 Bedroom - First Item on South Table", LocationCat.OVERWORLD_ITEM, 1723),
    "APT_21_BEDROOM_SPACE_TRUCKERZ": LocationData("Apt. 21 Bedroom - Second Item on South Table", LocationCat.OVERWORLD_ITEM, 1724),
    "APT_21_BEDROOM_MNW": LocationData("Apt. 21 Bedroom - Item on Southeast Table", LocationCat.OVERWORLD_ITEM, 1725),
    "APT_21_BEDROOM_FORK": LocationData("Apt. 21 Bedroom - First Item on Northwest Table", LocationCat.OVERWORLD_ITEM, 1726),
    "APT_21_BEDROOM_BEEF_5": LocationData("Apt. 21 Bedroom - Second Item on Northwest Table", LocationCat.OVERWORLD_ITEM, 1727),
    "APT_21_BEDROOM_PLATE": LocationData("Apt. 21 Bedroom - Third Item on Northwest Table", LocationCat.OVERWORLD_ITEM, 1728),
    "APT_21_BEDROOM_KNIFE": LocationData("Apt. 21 Bedroom - Fourth Item on Northwest Table", LocationCat.OVERWORLD_ITEM, 1729),
    "APT_21_BEDROOM_BEEF_6": LocationData("Apt. 21 Bedroom - Fifth Item on Northwest Table", LocationCat.OVERWORLD_ITEM, 1730, difficulty_lock={DL.EXPLORER}),
    "APT_21_BEDROOM_BATTERIES": LocationData("Apt. 21 Bedroom - Item on Shelf", LocationCat.OVERWORLD_ITEM, 1731)
}

APT_21_LYLE_LOCATIONS = {
    **APT_21_LYLE_MAIN_LOCATIONS,
    **APT_21_LYLE_DARK_ROOM_LOCATIONS,
    **APT_21_LYLE_BEDROOM_LOCATIONS
}

APT_22_HARRIET_LOCATIONS = {
    "APT_22_RUBBER_BOOTS": LocationData("Apt. 22 - Item Near Front Door", LocationCat.OVERWORLD_ITEM, 1801),
    "APT_22_JUICE_BOX": LocationData("Apt. 22 Kitchen - Item on Table", LocationCat.OVERWORLD_ITEM, 1802),
    "APT_22_VINEGAR": LocationData("Apt. 22 Kitchen - Item Near Fridge", LocationCat.OVERWORLD_ITEM, 1803),
    "APT_22_FRIDGE": LocationData("Apt. 22 Kitchen - Fridge Loot", LocationCat.LOOT, 1804),
    "APT_22_CHOCKY_BAR": LocationData("Apt. 22 Kitchen - Item on Counter", LocationCat.OVERWORLD_ITEM, 1805),
    "APT_22_TRASH": LocationData("Apt. 22 - Trash Can", LocationCat.LOOT, 1806),
    "APT_22_CASH": LocationData("Apt. 22 - Item on South Table", LocationCat.OVERWORLD_ITEM, 1807),
    "APT_22_BATHROOM_TOOTHPASTE": LocationData("Apt. 22 Bathroom - Item on Counter", LocationCat.OVERWORLD_ITEM, 1808),
    "APT_22_BATHROOM_MEDICINE_CABINET": LocationData("Apt. 22 Bathroom - Medicine Cabinet Loot", LocationCat.LOOT, 1809),
    "APT_22_HARRIET_BEDROOM_CLOTH": LocationData("Apt. 22 Harriet's Bedroom - Item on Floor", LocationCat.OVERWORLD_ITEM, 1810),
    "APT_22_HARRIET_BEDROOM_TRASH": LocationData("Apt. 22 Harriet's Bedroom - Trash Can", LocationCat.LOOT, 1811),
    "APT_22_SOPHIE_BEDROOM_TRASH": LocationData("Apt. 22 Sophie's Bedroom - Trash Can", LocationCat.LOOT, 1812),
    "APT_22_SOPHIE_BEDROOM_MARBLES": LocationData("Apt. 22 Sophie's Bedroom - Item on Desk", LocationCat.OVERWORLD_ITEM, 1813)
}

LEIGH_APT_LOCATION = {
    "BEAST_DEN_RECRUIT_LEIGH": LocationData("Floor 2 - Recruit Leigh", LocationCat.RECRUIT, 1901),
}

LEIGH_QUEST_LOCATION = {
    "LEIGH_APARTMENT_READ_NOTE": LocationData("Leigh's Apartment - Read Martin's Note", LocationCat.EVENT_ITEM, 1902)
}

APT_23_LEIGH_LOCATIONS = {
    **LEIGH_APT_LOCATION,
    **LEIGH_QUEST_LOCATION
}

# modifier 2000
APT_24_EUGENE_SHOP_LOCATIONS = {
    "APT_24_REPTILE_FOOTBALL": LocationData("Eugene's Shop - Buy Shop Level 5 Item", LocationCat.MERCHANT, 2001),
    "APT_24_EUGENE_COMBAT_VICTORY": LocationData("Eugene's Shop - Slay Eugene", LocationCat.FRIENDLY_FIRE, 2002),
}

APT_24_EUGENE_APT_LOCATIONS = {
    "APT_24_MOP": LocationData("Eugene's Apt. Entryway - Item Between Crates", LocationCat.OVERWORLD_ITEM, 2003),
    "APT_24_ENTRY_FACE_WORMS_COMBAT_VICTORY": LocationData("Eugene's Apt. Entryway - Slay Face Worms", LocationCat.COMBAT_VICTORY, 2004),
    "APT_24_COMBAT_KNIFE": LocationData("Eugene's Apt. Entryway - First Item on Table", LocationCat.OVERWORLD_ITEM, 2005),
    "APT_24_KLYSOX": LocationData("Eugene's Apt. Entryway - Second Item on Table", LocationCat.OVERWORLD_ITEM, 2006),
    "APT_24_PISTOL_BULLETS": LocationData("Eugene's Apt. Entryway - Item on South Table", LocationCat.OVERWORLD_ITEM, 2007),
    "APT_24_BATHROOM_MEDICINE_CABINET": LocationData("Eugene's Apt. Bathroom - Medicine Cabinet", LocationCat.LOOT, 2008),
    "APT_24_BATHROOM_SOAP": LocationData("Eugene's Apt. Bathroom - Item on Counter", LocationCat.OVERWORLD_ITEM, 2009),
    "APT_24_LIVINGROOM_FACE_WORMS_COMBAT_VICTORY": LocationData("Eugene's Apt. Living Room - Slay Face Worms", LocationCat.COMBAT_VICTORY, 2010),
    "APT_24_LIVINGROOM_ELEPHANT_STATUETTE": LocationData("Eugene's Apt. Living Room - Item on North Table", LocationCat.OVERWORLD_ITEM, 2011),
    "APT_24_LIVINGROOM_DINNER_PLATE_1": LocationData("Eugene's Apt. Kitchen - First Item on Dining Table", LocationCat.OVERWORLD_ITEM, 2012),
    "APT_24_LIVINGROOM_KNIFE": LocationData("Eugene's Apt. Kitchen - Second Item on Dining Table", LocationCat.OVERWORLD_ITEM, 2013),
    "APT_24_LIVINGROOM_DINNER_PLATE_2": LocationData("Eugene's Apt. Kitchen - Third Item on Dining Table", LocationCat.OVERWORLD_ITEM, 2014),
    "APT_24_LIVINGROOM_FORK": LocationData("Eugene's Apt. Kitchen - Fourth Item on Dining Table", LocationCat.OVERWORLD_ITEM, 2015),
    "APT_24_KITCHEN_FRIDGE": LocationData("Eugene's Apt. Kitchen - Fridge Loot", LocationCat.LOOT, 2016),
    "APT_24_KITCHEN_VINEGAR": LocationData("Eugene's Apt. Kitchen - Item on Counter", LocationCat.OVERWORLD_ITEM, 2017),
    "APT_24_BEDROOM_FACE_WORMS_COMBAT_VICTORY": LocationData("Eugene's Apt. Bedroom - Slay Face Worms", LocationCat.COMBAT_VICTORY, 2018),
    "APT_24_BEDROOM_CHOCKY_BAR_1": LocationData("Eugene's Apt. Bedroom - Item on South Table", LocationCat.OVERWORLD_ITEM, 2019),
    "APT_24_BEDROOM_CHOCKY_BAR_2": LocationData("Eugene's Apt. Bedroom - Item on West Table", LocationCat.OVERWORLD_ITEM, 2020),
}

APT_24_EUGENE_SEWING_CLOSET_LOCATIONS = {
    "APT_24_SEWING_FACE_WORMS_COMBAT_VICTORY": LocationData("Eugene's Apt. Sewing Room - Slay Face Worms", LocationCat.COMBAT_VICTORY, 2021),
    "APT_24_SEWING_DENIM_VEST": LocationData("Eugene's Apt. Sewing Room - Item Near Sewing Bench 1", LocationCat.OVERWORLD_ITEM, 2022),
    "APT_24_SEWING_BUTTON_UP_SHIRT": LocationData("Eugene's Apt. Sewing Room - Item Near Sewing Bench 2", LocationCat.OVERWORLD_ITEM, 2023),
    "APT_24_SAFE_ITEM": LocationData("Eugene's Apt. Sewing Room - Item In Safe", LocationCat.LOOT, 2024),
    "APT_24_SUIT": LocationData("Eugene's Apt. Sewing Room - Item on South Table", LocationCat.OVERWORLD_ITEM, 2025)
}

APT_24_EUGENE_LOCATIONS = {
    **APT_24_EUGENE_SHOP_LOCATIONS,
    **APT_24_EUGENE_APT_LOCATIONS,
    **APT_24_EUGENE_SEWING_CLOSET_LOCATIONS,
}

APT_25_DAN_LOCATIONS = {
    "APT_25_KLYSOX": LocationData("Apt. 25 - Item on Counter", LocationCat.OVERWORLD_ITEM, 2101),
    "APT_25_FRIDGE": LocationData("Apt. 25 - Fridge Loot", LocationCat.LOOT, 2102),
    "APT_25_PLATE": LocationData("Apt. 25 - First Item on Table", LocationCat.OVERWORLD_ITEM, 2103),
    "APT_25_FORK": LocationData("Apt. 25 - Second Item on Table", LocationCat.OVERWORLD_ITEM, 2104),
    "APT_25_DANS_MOM_COMBAT_VICTORY": LocationData("Apt. 25 - Slay Dan's Mom", LocationCat.COMBAT_VICTORY, 2105),
    "APT_25_DANS_ROOM_NEODUO": LocationData("Apt. 25 Dan's Room - Item on Table", LocationCat.OVERWORLD_ITEM, 2106),
    "APT_25_DANS_ROOM_ORANGE_DRINK": LocationData("Apt. 25 Dan's Room - Item on Floor", LocationCat.OVERWORLD_ITEM, 2107)
}

APT_27_TYPEWRITHER_LOCATIONS = {
    "APT_27_TYPEWRITHER_COMBAT_VICTORY": LocationData("Apt. 27 - Slay Typewrither", LocationCat.COMBAT_VICTORY, 2201),
    "APT_27_CRUMPLED_MANUSCRIPT": LocationData("Apt 27 Kitchen - Item on East Table", LocationCat.OVERWORLD_ITEM, 2202),
    "APT_27_TEA_SET": LocationData("Apt. 27 - Item on Coffee Table", LocationCat.OVERWORLD_ITEM, 2203),
    "APT_27_WALLET": LocationData("Apt. 27 Kitchen - Item on Dining Table", LocationCat.OVERWORLD_ITEM, 2204),
    "APT_27_FRIDGE": LocationData("Apt. 27 Kitchen - Fridge Loot", LocationCat.LOOT, 2205),
    "APT_27_TRASH": LocationData("Apt. 27 Kitchen - Trash Can", LocationCat.LOOT, 2206),
    "APT_27_BATHROOM_LEG_WORMS": LocationData("Apt. 27 Bathroom - Slay Leg Worms", LocationCat.COMBAT_VICTORY, 2207),
    "APT_27_BATHROOM_ROACH": LocationData("Apt. 27 Bathroom - Cockroach", LocationCat.OVERWORLD_ITEM, 2208),
    "APT_27_BEDROOM_KITSCH_LAMP": LocationData("Apt. 27 Bedroom - Item Near Bed", LocationCat.OVERWORLD_ITEM, 2209),
    "APT_27_BEDROOM_CLEAN_MANUSCRIPT": LocationData("Apt. 27 Bedroom - Item on Table", LocationCat.OVERWORLD_ITEM, 2210),
    "APT_27_COMPLETE_MANUSCRIPT": LocationData("Apt. 27 Office - Complete Manuscript", LocationCat.EVENT_ITEM, 2211),
    "APT_27_OFFICE_BACKGAMMON": LocationData("Apt. 27 Office - Item on Table", LocationCat.OVERWORLD_ITEM, 2212),
    "APT_27_OFFICE_WHISKEY": LocationData("Apt. 27 Office - Item on Writing Desk", LocationCat.OVERWORLD_ITEM, 2213)
}

APT_28_FLOODED_MAIN_LOCATIONS = {
    "APT_28_DROWNING_COMBAT_VICTORY": LocationData("Apt. 28 - Slay Drowning", LocationCat.COMBAT_VICTORY, 2301),
    "APT_28_LAUNDRY_REAGENT": LocationData("Apt. 28 Laundry Room - Item on Table", LocationCat.OVERWORLD_ITEM, 2302),
    "APT_28_TWILIGHT_VALVE": LocationData("Apt. 28 West Closet - Item", LocationCat.OVERWORLD_ITEM, 2311),
    "APT_28_PIRANHAS_COMBAT_VICTORY": LocationData("Apt. 28 Main Corridor - Slay Piranhas", LocationCat.OVERWORLD_ITEM, 2312),
    "APT_28_CRAB_COMBAT_VICTORY": LocationData("Apt. 28 Main Corridor - Slay Crab", LocationCat.COMBAT_VICTORY, 2313),
    "APT_28_GARBAGE_PIRANHAS_COMBAT_VICTORY": LocationData("Apt. 28 Garbage Room - Slay Piranhas", LocationCat.COMBAT_VICTORY, 2314),
    "APT_28_GARBAGE_OCTOPUS_COMBAT_VICTORY": LocationData("Apt. 28 Garbage North - Slay Octopus", LocationCat.COMBAT_VICTORY, 2315),
    "APT_28_GARBAGE_FIRST_AID_KIT": LocationData("Apt. 28 Garbage North - Item on Table", LocationCat.OVERWORLD_ITEM, 2316),
    "APT_28_GARBAGE_ENZYME": LocationData("Apt. 28 Garbage Room Closet - Item on Table", LocationCat.OVERWORLD_ITEM, 2319),
    "APT_28_GARBAGE_DRAGONFISH_COMBAT_VICTORY": LocationData("Apt. 28 Garbage Room Closet - Slay Dragonfish", LocationCat.COMBAT_VICTORY, 2320),
}

APT_28_TWILIGHT_LOCATIONS = {
    "APT_28_TWILIGHT_PIRANHAS_COMBAT_VICTORY": LocationData("Apt. 28 Twilight - Slay Piranhas", LocationCat.COMBAT_VICTORY, 2303),
    "APT_28_TWILIGHT_PIRANHA_GUY_COMBAT_VICTORY": LocationData("Apt. 28 Twilight - Slay Piranha Guy", LocationCat.FRIENDLY_FIRE, 2304),
    "APT_28_TWILIGHT_FIRST_AID_KIT": LocationData("Apt. 28 Twilight - First Aid Kit", LocationCat.OVERWORLD_ITEM, 2305),
    "APT_28_TWILIGHT_SHURIKEN": LocationData("Apt. 28 Twilight West - Item on Table", LocationCat.OVERWORLD_ITEM, 2306),
    "APT_28_DRAGONFISH_COMBAT_VICTORY": LocationData("Apt. 28 Twilight West - Slay Crab and Dragonfish", LocationCat.COMBAT_VICTORY, 2307),
    "APT_28_TWILIGHT_CRAB_COMBAT_VICTORY": LocationData("Apt. 28 Twilight South - Slay Crabs", LocationCat.COMBAT_VICTORY, 2308),
    "APT_28_JELLYFISH_COMBAT_VICTORY": LocationData("Apt. 28 Twilight South Closet - Slay Jellyfish", LocationCat.COMBAT_VICTORY, 2309),
    "APT_28_MIDNIGHT_VALVE": LocationData("Apt. 28 Twilight South Closet - Item Behind Jellyfish", LocationCat.OVERWORLD_ITEM, 2310),
}

APT_28_MIDNIGHT_LOCATIONS = {
    "APT_28_MIDNIGHT_DRAGONFISH_COMBAT_VICTORY": LocationData("Apt. 28 Midnight Room - Slay Dragonfish and Piranhas", LocationCat.COMBAT_VICTORY, 2317),
    "APT_28_ABYSSAL_VALVE": LocationData("Apt. 28 Midnight Room Closet - Item", LocationCat.OVERWORLD_ITEM, 2318),
}

APT_28_ABYSSAL_LOCATIONS = {
    "APT_28_ABYSSAL_CHOCKY_BAR": LocationData("Apt. 28 Abyssal Corridor - Item Left by Summer", LocationCat.OVERWORLD_ITEM, 2321),
    "APT_28_ABYSSAL_STARFISH_COMBAT_VICTORY": LocationData("Apt. 28 Abyssal Corridor - Slay Starfish", LocationCat.COMBAT_VICTORY, 2322),
    "APT_28_ABYSSAL_SHARK_COMBAT_VICTORY": LocationData("Apt 28 Abyssal West - Slay Shark", LocationCat.COMBAT_VICTORY, 2323),
    "APT_28_ABYSSAL_STIMULANT": LocationData("Apt 28 Abyssal Garbage Maze - Southeast Item", LocationCat.OVERWORLD_ITEM, 2324),
    "APT_28_ABYSSAL_HEALING_SPRAY": LocationData("Apt 28 Abyssal Garbage Maze - Southwest Item", LocationCat.OVERWORLD_ITEM, 2325),
    "APT_28_ABYSSAL_ELIXIR": LocationData("Apt 28 Abyssal Garbage Maze - Northwest Item", LocationCat.OVERWORLD_ITEM, 2326),
    "APT_28_ABYSSAL_WEST_JELLYFISH": LocationData("Apt 28 Abyssal West Closet - Slay Jellyfish and Dragonfish", LocationCat.COMBAT_VICTORY, 2327),
    "APT_28_HADAL_VALVE": LocationData("Apt 28 Abyssal West Closet - Item", LocationCat.OVERWORLD_ITEM, 2328),
    "APT_28_ABYSSAL_EAST_JELLYFISH": LocationData("Apt 28 Abyssal East - Slay Jellyfish and Dragonfish", LocationCat.COMBAT_VICTORY, 2329),
    "APT_28_SHRIMP_KNIGHT_COMBAT_VICTORY": LocationData("Apt 28 Final Corridor - Slay Shrimp Knight", LocationCat.COMBAT_VICTORY, 2330),
    "APT_28_SHRIMP_KNIGHT_AUDREY_LOOT": LocationData("Apt 28 Final Corridor - Shrimp Knight Audrey Loot", LocationCat.EVENT_ITEM, 2331),
}

APT_28_HADAL_LOCATIONS = {
    "APT_28_HADAL_LETHARGY_COMBAT_VICTORY": LocationData("Apt 28 Hadal Room - Defeat Lethargy", LocationCat.COMBAT_VICTORY, 2332)
}

APT_28_FLOODED_LOCATIONS = {
    **APT_28_FLOODED_MAIN_LOCATIONS,
    **APT_28_TWILIGHT_LOCATIONS,
    **APT_28_MIDNIGHT_LOCATIONS,
    **APT_28_ABYSSAL_LOCATIONS,
    **APT_28_HADAL_LOCATIONS
}

location_table: dict[str, LocationData] = {
    **VIDEO_GAME_LOCATIONS,
    **F3_HALL_LOCATIONS,
    **APT_30_TAXIDERMY_LOCATIONS,
    **APT_31_STARGAZER_LOCATIONS,
    **GLITCH_WORLD_LOCATIONS,
    **APT_32_TEETH_LOCATIONS,
    **APT_33_LOCATIONS,
    **FRONT_DOOR_LOCATIONS,
    **APT_33_MEAT_LOCATIONS,
    **APT_34_FROZEN_LOCATIONS,
    **APT_35_SIBYL_LOCATIONS,
    **APT_36_WOUNDED_LOCATIONS,
    **APT_37_VINCENT_LOCATIONS,
    **APT_38_ROOMMATES_LOCATIONS,
    **F3_JANITOR_CLOSET_LOCATIONS,
    **F2_HALL_EAST_LOCATIONS,
    **APT_20_JEANNE_LOCATIONS,
    **APT_21_LYLE_LOCATIONS,
    **APT_22_HARRIET_LOCATIONS,
    **APT_23_LEIGH_LOCATIONS,
    **APT_24_EUGENE_LOCATIONS, # todo: fill in
    **APT_25_DAN_LOCATIONS,
    **APT_27_TYPEWRITHER_LOCATIONS,
    **APT_28_FLOODED_LOCATIONS,
}

region_locs: dict[str, set[str]] = {
    # FLOOR 3
    "APT_33_HOME": APT_33_LOCATIONS.keys() | VIDEO_GAME_LOCATIONS.keys(),
    "DOOR_ENCOUNTERS": FRONT_DOOR_LOCATIONS.keys(),
    "FLOOR_3_HALL": F3_HALL_LOCATIONS.keys(),
    "APT_30_TAXIDERMY": APT_30_MAIN_LOCATIONS.keys(),
    "APT_30_TAXIDERMY_FLESH": APT_30_FLESH_LOCATIONS.keys(),
    "APT_31_STARGAZER": APT_31_STARGAZER_LOCATIONS.keys() | APT_33_MEAT_LOCATIONS.keys() ,
    "GLITCH_WORLD_MAIN": GLITCH_WORLD_MAIN_LOCATIONS.keys(),
    "GLITCH_WORLD_WEST_AND_SOUTHWEST": GLITCH_WORLD_WEST_AND_SOUTHWEST_LOCATIONS.keys(),
    "GLITCH_WORLD_SLIME_ROOM": GLITCH_WORLD_SLIME_ROOM_LOCATIONS.keys(),
    "GLITCH_WORLD_END_CHAMBER": GLITCH_WORLD_END_CHAMBER_LOCATIONS.keys(),
    "GATE_ROOM_SOUTH": {},
    "GATE_ROOM_WEST_GHOST_METALBAT": GATE_ROOM_WEST_GHOST_METALBAT_LOCATIONS.keys(),
    "GATE_ROOM_NE": GATE_ROOM_NE_LOCATIONS.keys(),
    "GATE_ROOM_SE_HAIRHEAD_GUN": GATE_ROOM_SE_HAIRHEAD_GUN_LOCATIONS.keys(),
    "GLITCH_WORLD_EAST_W": GLITCH_WORLD_EAST_W_LOCATIONS.keys(),
    "GLITCH_WORLD_EAST_E": GLITCH_WORLD_EAST_E_LOCATIONS.keys(),
    "GLITCH_WORLD_SE": GLITCH_WORLD_SE_LOCATIONS.keys(),
    "GLITCH_WORLD_HONKO": GLITCH_WORLD_HONKO_LOCATIONS.keys(),
    "GLITCH_WORLD_NE": GLITCH_WORLD_NE_LOCATIONS.keys(),
    "GLITCH_WORLD_NE_HYDRA_LAIR": GLITCH_WORLD_NE_HYDRA_LAIR_LOCATIONS.keys(),
    "GLITCH_WORLD_MAZE": GLITCH_WORLD_MAZE_LOCATIONS.keys(),
    "APT_32_TEETH": APT_32_TEETH_LOCATIONS_MAIN.keys(),
    "APT_32_MASTER_BEDROOM_KITCHEN": APT_32_TEETH_BEHIND_DOOR_KNOB.keys(),
    "APT_34_FROZEN_ENTRANCE": APT_34_FROZEN_ENTRYWAY_LOCATIONS.keys(),
    "APT_34_FROZEN_BEDROOM_WEST": APT_34_BEDROOM_WEST_LOCATIONS.keys(),
    "APT_34_FROZEN_BEDROOM_EAST": APT_34_BEDROOM_EAST_LOCATIONS.keys(),
    "APT_34_FROZEN_KITCHEN_BATHROOM_EAST": APT_34_KITCHEN_BATHROOM_EAST_LOCATIONS.keys(),
    "APT_34_FROZEN_BATHROOM_WEST": APT_34_BATHROOM_WEST_LOCATIONS.keys(),
    "APT_34_FROZEN_OFFICE_NORTH": APT_34_OFFICE_NORTH_LOCATIONS.keys(),
    "APT_34_FROZEN_OFFICE_SOUTH": APT_34_OFFICE_SOUTH_LOCATIONS.keys(),
    "APT_34_FROZEN_CLOSET": APT_34_CLOSET_LOCATIONS.keys(),
    "APT_34_FROZEN_KITCHEN_LOWER": APT_34_KITCHEN_LOWER_LOCATIONS.keys(),
    "APT_34_FROZEN_LONG_BEDROOM_WEST": APT_34_LONG_BEDROOM_WEST_LOCATIONS.keys(),
    "APT_34_FROZEN_LONG_BEDROOM_SW": APT_34_LONG_BEDROOM_SW_LOCATIONS.keys(),
    "APT_34_FROZEN_LONG_BEDROOM_CENTER": APT_34_LONG_BEDROOM_CENTER_LOCATIONS.keys(),
    "APT_34_FROZEN_LONG_BEDROOM_NORTH": APT_34_LONG_BEDROOM_NORTH_LOCATIONS.keys(),
    "APT_34_FROZEN_LONG_BEDROOM_EAST": APT_34_LONG_BEDROOM_EAST_LOCATIONS.keys(),
    "APT_35_SIBYL": APT_35_SIBYL_LOCATIONS.keys(),
    "APT_36_WOUNDED": APT_36_WOUNDED_LOCATIONS.keys(),
    "APT_37_VINCENT": APT_37_VINCENT_LOCATIONS_MAIN.keys(),
    "APT_37_LOCKED_ROOM": APT_37_LOCKED_ROOM_LOCATIONS.keys(),
    "APT_38_ROOMMATES": APT_38_ROOMMATES_LOCATIONS_MAIN.keys(),
    "APT_38_KAELEY": APT_38_KAELEY_INTRO_LOCATIONS.keys(),
    "KAELEY_NE": KAELEY_NE_LOCATIONS.keys(),
    "KAELEY_NW": KAELEY_NW_LOCATIONS.keys(),
    "KAELEY_W": KAELEY_W_LOCATIONS.keys(),
    "KAELEY_SW": KAELEY_SW_LOCATIONS.keys(),
    "KAELEY_E": KAELEY_E_LOCATIONS.keys(),
    "KAELEY_CENTER_LEFT": KAELEY_CENTER_LEFT_LOCATIONS.keys(),
    "KAELEY_CENTER_RIGHT": KAELEY_CENTER_RIGHT_LOCATIONS.keys(),
    "KAELEY_CENTER": KAELEY_CENTER_LOCATIONS.keys(),
    "KAELEY_S": KAELEY_S_LOCATIONS.keys(),
    "KAELEY_SE": KAELEY_SE_LOCATIONS.keys(),
    "F3_JANITOR_CLOSET" : F3_JANITOR_CLOSET_LOCATIONS.keys(),
    # FLOOR 2
    "FLOOR_2_EAST": F2_HALL_EAST_LOCATIONS.keys(),
    "APT_20_JEANNE": APT_20_JEANNE_PHASE1_LOCATIONS.keys(),
    "APT_20_JEANNE_HYDRA": APT_20_JEANNE_PHASE2_LOCATIONS.keys(),
    "APT_21_LYLE": APT_21_LYLE_MAIN_LOCATIONS.keys(),
    "LYLE_DARK_ROOM": APT_21_LYLE_DARK_ROOM_LOCATIONS.keys(),
    "LYLE_BEDROOM": APT_21_LYLE_BEDROOM_LOCATIONS.keys(),
    "APT_22_HARRIET": APT_22_HARRIET_LOCATIONS.keys(),
    "LEIGHS_APARTMENT": LEIGH_APT_LOCATION.keys(),
    "LEIGHS_APARTMENT_QUEST": LEIGH_QUEST_LOCATION.keys(),
    "APT_24_EUGENE_SHOP": APT_24_EUGENE_SHOP_LOCATIONS.keys(),
    "APT_24_EUGENE_APT": APT_24_EUGENE_APT_LOCATIONS.keys(),
    "APT_24_EUGENE_SEWING_CLOSET": APT_24_EUGENE_SEWING_CLOSET_LOCATIONS.keys(),
    "APT_25_DAN": APT_25_DAN_LOCATIONS.keys(),
    "APT_27_TYPEWRITHER": APT_27_TYPEWRITHER_LOCATIONS.keys(),
    "APT_28_FLOODED_ENTRYWAY": APT_28_FLOODED_MAIN_LOCATIONS.keys(),
    "APT_28_FLOODED_TWILIGHT": APT_28_TWILIGHT_LOCATIONS.keys(),
    "APT_28_FLOODED_MIDNIGHT": APT_28_MIDNIGHT_LOCATIONS.keys(),
    "APT_28_FLOODED_ABYSSAL": APT_28_ABYSSAL_LOCATIONS.keys(),
    "APT_28_FLOODED_HADAL": APT_28_HADAL_LOCATIONS.keys(),
}

def get_region_to_location():
    mapping = {}
    
    for region, locs in region_locs.items():
        for loc in locs:
            location_entry = location_table[loc]
            mapping[location_entry.str_name] = region
            if location_entry.cursed_name:
                mapping[location_entry.cursed_name] = region
    return mapping

location_to_region: dict[str, str] = get_region_to_location()