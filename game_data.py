"""
COMP 163 - Project 3: Quest Chronicles
Game Data Module - Starter Code

Name: Marcellus Hutchins

AI Usage: [Document any AI assistance used]

This module handles loading and validating game data from text files.
"""

import os
from idlelib.rpc import request_queue

from custom_exceptions import (
    InvalidDataFormatError,
    MissingDataFileError,
    CorruptedDataError
)

# ============================================================================
# DATA LOADING FUNCTIONS
# ============================================================================

def load_quests(filename="data/quests.txt"):
    filepath = os.path.join(filename)

    if not os.path.exists(filepath):
        raise MissingDataFileError()

    try:
        with open(filepath, 'r') as f:
            lines = f.read().strip().split('\n\n')
    except Exception:
        raise CorruptedDataError

    raw_data = lines

    quest_data_dict = {}

    for q_data in raw_data:
        quest = {}

        data = q_data.strip().split('\n')

        try:
            for line in data:
                if ':' not in line:
                    raise InvalidDataFormatError()

                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()

                if key in ["REWARD_XP", "REWARD_GOLD", "REQUIRED_LEVEL"]:
                    value = int(value)

                quest[key] = value

            if "QUEST_ID" not in quest:
                raise InvalidDataFormatError()

            quest_id = quest["QUEST_ID"]

            if "TITLE" not in quest or "DESCRIPTION" not in quest or \
                    "REWARD_XP" not in quest or "REWARD_GOLD" not in quest or \
                    "REQUIRED_LEVEL" not in quest:
                raise InvalidDataFormatError()

            if "PREREQUISITE" in quest:
                prerequisite = quest["PREREQUISITE"]
            else:
                prerequisite = "NONE"

            quest_data_dict[quest_id] = {
                "title": quest["TITLE"],
                "description": quest["DESCRIPTION"],
                "reward_xp": quest["REWARD_XP"],
                "reward_gold": quest["REWARD_GOLD"],
                "required_level": quest["REQUIRED_LEVEL"],
                "prerequisite": prerequisite
            }

        except ValueError:
            raise InvalidDataFormatError("Save file format is invalid.")

    return quest_data_dict
    """
    Load quest data from file
    
    Expected format per quest (separated by blank lines):
    QUEST_ID: unique_quest_name
    TITLE: Quest Display Title
    DESCRIPTION: Quest description text
    REWARD_XP: 100
    REWARD_GOLD: 50
    REQUIRED_LEVEL: 1
    PREREQUISITE: previous_quest_id (or NONE)
    
    Returns: Dictionary of quests {quest_id: quest_data_dict}
    Raises: MissingDataFileError, InvalidDataFormatError, CorruptedDataError
    """
    # TODO: Implement this function
    # Must handle:
    # - FileNotFoundError → raise MissingDataFileError
    # - Invalid format → raise InvalidDataFormatError
    # - Corrupted/unreadable data → raise CorruptedDataError
    pass

def load_items(filename="data/items.txt"):
    if not os.path.exists(filename):
        raise MissingDataFileError(f"Item file '{filename}' not found.")

    try:
        with open(filename, "r") as f:
            content = f.read().strip()
    except Exception:
        raise CorruptedDataError("Could not read item data file.")

    if not content:
        raise InvalidDataFormatError("Item file is empty.")

    raw_items = content.split("\n\n")

    item_data_dict = {}

    for block in raw_items:
        lines = block.strip().split("\n")
        item_fields = {}

        for line in lines:
            if ":" not in line:
                raise InvalidDataFormatError(f"Invalid line: {line}")

            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if key == "COST":
                try:
                    value = int(value)
                except ValueError:
                    raise InvalidDataFormatError(f"Invalid COST value: {value}")

            item_fields[key] = value

        required = [
            "ITEM_ID", "NAME", "TYPE", "EFFECT", "COST", "DESCRIPTION"
        ]

        for items in required:
            if items not in item_fields:
                raise InvalidDataFormatError(f"Missing required field: {items}")

        item_id = item_fields["ITEM_ID"]

        item_data_dict[item_id] = {
            "name": item_fields["NAME"],
            "type": item_fields["TYPE"],
            "effect": item_fields["EFFECT"],
            "cost": item_fields["COST"],
            "description": item_fields["DESCRIPTION"]
        }

    return item_data_dict
    """
    Load item data from file

    Expected format per item (separated by blank lines):
    ITEM_ID: unique_item_name
    NAME: Item Display Name
    TYPE: weapon|armor|consumable
    EFFECT: stat_name:value (e.g., strength:5 or health:20)
    COST: 100
    DESCRIPTION: Item description

    Returns: Dictionary of items {item_id: item_data_dict}
    Raises: MissingDataFileError, InvalidDataFormatError, CorruptedDataError
    """
    # TODO: Implement this function
    # Must handle same exceptions as load_quests
    pass

def validate_quest_data(quest_dict):
    required_keys = {
        'quest_id':"",
        'title':"",
        'description':'',
        'reward_xp':int(),
        'reward_gold':int(),
        'required_level':int(),
        'prerequisite':""
    }
    for key in required_keys:
        if key not in quest_dict:
            raise MissingDataFileError(f"Missing required data: {key}")

    return True
    """
    Validate that quest dictionary has all required fields
    
    Required fields: quest_id, title, description, reward_xp, 
                    reward_gold, required_level, prerequisite
    
    Returns: True if valid
    Raises: InvalidDataFormatError if missing required fields
    """
    # TODO: Implement validation
    # Check that all required keys exist
    # Check that numeric values are actually numbers
    pass

def validate_item_data(item_dict):
    required_keys = {
        'item_id':"",
        'name':"",
        'type':"",
        'effect':"",
        'cost':"",
        'description':'',

    }
    accept_type = ['weapon', 'armor', 'consumable']

    for key in required_keys:
        if key not in item_dict:
            raise InvalidDataFormatError(f"Missing required data: {key}")
    for value in required_keys['type']:
        if value not in accept_type:
            raise InvalidDataFormatError(f"Missing required data: {value}")

    return True
    """
    Validate that item dictionary has all required fields
    
    Required fields: item_id, name, type, effect, cost, description
    Valid types: weapon, armor, consumable
    
    Returns: True if valid
    Raises: InvalidDataFormatError if missing required fields or invalid type
    """
    # TODO: Implement validation
    pass

def create_default_data_files():
    data_dir = "data"

    try:
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
    except PermissionError:
        print("Error: No permission to create data directory.")
        return False

    quests_path = os.path.join(data_dir, "quests.txt")
    items_path = os.path.join(data_dir, "items.txt")
    health = {}
    default_quests = "QUEST_ID: starter_quest"
    TITLE: 'Slay a Goblin'
    DESCRIPTION: 'Go to a nearby village and slay a goblin'
    REWARD_XP: 50
    REWARD_GOLD: 20
    REQUIRED_LEVEL: 1
    PREREQUISITE: "NONE"

    default_items = "TEM_ID: potion_small"
    NAME: "Small Health Potion"
    TYPE: "consumable"
    EFFECT: {health: 20}
    COST: int(15)
    DESCRIPTION: 'Restores a small amount of health.'


    if not os.path.exists(quests_path):
        try:
            with open(quests_path, "w") as f:
                f.write(default_quests)
        except PermissionError:
            print("Error: No permission to write quests.txt.")
            return False

    if not os.path.exists(items_path):
        try:
            with open(items_path, "w") as f:
                f.write(default_items)
        except PermissionError:
            print("Error: No permission to write items.txt.")
            return False

    return True
    """
    Create default data files if they don't exist
    This helps with initial setup and testing
    """
    # TODO: Implement this function
    # Create data/ directory if it doesn't exist
    # Create default quests.txt and items.txt files
    # Handle any file permission errors appropriately
    pass

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def parse_quest_block(lines):
    quest = {}

    for line in lines:
        if ":" not in line:
            raise InvalidDataFormatError(f"Invalid line format: {line}")

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if key in ["REWARD_XP", "REWARD_GOLD", "REQUIRED_LEVEL"]:
            try:
                value = int(value)
            except ValueError:
                raise InvalidDataFormatError(f"Invalid number for {key}: {value}")

        quest[key] = value

    return quest
    """
    Parse a block of lines into a quest dictionary
    
    Args:
        lines: List of strings representing one quest
    
    Returns: Dictionary with quest data
    Raises: InvalidDataFormatError if parsing fails
    """
    # TODO: Implement parsing logic
    # Split each line on ": " to get key-value pairs
    # Convert numeric strings to integers
    # Handle parsing errors gracefully
    pass

def parse_item_block(lines):
    item = {}

    for line in lines:
        if ":" not in line:
            raise InvalidDataFormatError(f"Invalid line format: {line}")

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if key == "COST":
            try:
                value = int(value)
            except ValueError:
                raise InvalidDataFormatError(f"Invalid COST value: {value}")

        item[key] = value

    return item
    """
    Parse a block of lines into an item dictionary
    
    Args:
        lines: List of strings representing one item
    
    Returns: Dictionary with item data
    Raises: InvalidDataFormatError if parsing fails
    """
    # TODO: Implement parsing logic
    pass

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== GAME DATA MODULE TEST ===")
    
    #Test creating default files
    create_default_data_files()
    
    #Test loading quests
    try:
        quests = load_quests()
        print(f"Loaded {len(quests)} quests")
    except MissingDataFileError:
        print("Quest file not found")
    except InvalidDataFormatError as e:
        print(f"Invalid quest format: {e}")
    
    #Test loading items
    try:
        items = load_items()
        print(f"Loaded {len(items)} items")
    except MissingDataFileError:
        print("Item file not found")
    except InvalidDataFormatError as e:
        print(f"Invalid item format: {e}")

