"""
COMP 163 - Project 3: Quest Chronicles
Character Manager Module - Starter Code

Name: Marcellus Hutchins

AI Usage: [Document any AI assistance used]

This module handles character creation, loading, and saving.
"""

import os
from custom_exceptions import (
    InvalidCharacterClassError,
    CharacterNotFoundError,
    SaveFileCorruptedError,
    InvalidSaveDataError,
    CharacterDeadError
)

# ============================================================================
# CHARACTER MANAGEMENT FUNCTIONS
# ============================================================================

def create_character(name, character_class):
    character = {'name': name,
            'class': character_class,
            'level': 1,
            'health': 0,
            'max_health': 100,
            'strength': 10,
            'magic': 5,
            'experience': 0,
            'gold': 20,
            'inventory': [],
            'active_quests': [],
            'completed_quests': [],}
    class_list = ['Warrior', 'Mage', 'Rogue', 'Cleric']
    if character_class not in class_list:
        raise InvalidCharacterClassError(character_class)
    if character_class == 'Warrior':
        character['class'] = 'Warrior'
        character['health'] = 120
        character['strength'] = 15
        character['magic'] = 5
    elif character_class == 'Mage':
        character['class'] = 'Mage'
        character['health'] = 80
        character['strength'] = 8
        character['magic'] = 20
    elif character_class == 'Rogue':
        character['class'] = 'Rogue'
        character['health'] = 90
        character['strength'] = 12
        character['magic'] = 10
    elif character_class == 'Cleric':
        character['class'] = 'Cleric'
        character['health'] = 100
        character['strength'] = 10
        character['magic'] = 15
    return character

    """
    Create a new character with stats based on class
    
    Valid classes: Warrior, Mage, Rogue, Cleric
    
    Returns: Dictionary with character data including:
            - name, class, level, health, max_health, strength, magic
            - experience, gold, inventory, active_quests, completed_quests
    
    Raises: InvalidCharacterClassError if class is not valid
    """
    # TODO: Implement character creation
    # Validate character_class first
    # Example base stats:
    # Warrior: health=120, strength=15, magic=5
    # Mage: health=80, strength=8, magic=20
    # Rogue: health=90, strength=12, magic=10
    # Cleric: health=100, strength=10, magic=15
    
    # All characters start with:
    # - level=1, experience=0, gold=100
    # - inventory=[], active_quests=[], completed_quests=[]
    
    # Raise InvalidCharacterClassError if class not in valid list
    pass

def save_character(character, save_directory="data/save_games"):
    try:
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        filepath = os.path.join(save_directory, f"{character['name']}_save.txt")


        with open(filepath,'w+') as f:

            f.write(f"NAME: {str(character['name'])}\n")
            f.write(f"CLASS: {str(character['class'])}\n")
            f.write(f"LEVEL: {str(character['level'])}\n")
            f.write(f"HEALTH: {str(character['health'])}\n")
            f.write(f"MAX_HEALTH: {str(character['max_health'])}\n")
            f.write(f"STRENGTH: {str(character['strength'])}\n")
            f.write(f"MAGIC: {str(character['magic'])}\n")
            f.write(f"EXPERIENCE: {str(character['experience'])}\n")
            f.write(f"GOLD: {str(character['gold'])}\n")
            f.write(f"INVENTORY: {','.join(character['inventory'])}\n")
            f.write(f"ACTIVE_QUESTS: {','.join(character['active_quests'])}\n")
            f.write(f"COMPLETED_QUESTS: {','.join(character['completed_quests'])}\n")
        return True
    except (PermissionError,IOError) as e:
        print(e)
    """
    Save character to file
    
    Filename format: {character_name}_save.txt
    
    File format:
    NAME: character_name
    CLASS: class_name
    LEVEL: 1
    HEALTH: 120
    MAX_HEALTH: 120
    STRENGTH: 15
    MAGIC: 5
    EXPERIENCE: 0
    GOLD: 100
    INVENTORY: item1,item2,item3
    ACTIVE_QUESTS: quest1,quest2
    COMPLETED_QUESTS: quest1,quest2
    
    Returns: True if successful
    Raises: PermissionError, IOError (let them propagate or handle)
    """
    # TODO: Implement save functionality
    # Create save_directory if it doesn't exist
    # Handle any file I/O errors appropriately
    # Lists should be saved as comma-separated values
    pass

def load_character(character_name, save_directory="data/save_games"):
    filepath = os.path.join(save_directory, f"{character_name}_save.txt")

    if not os.path.exists(filepath):
        raise CharacterNotFoundError('Character not found')

    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except Exception:
        raise SaveFileCorruptedError('save file corrupted')

    character = {}

    try:
        for line in lines:
            key, value = line.strip().split(": ", 1)

            if key in ["INVENTORY", "ACTIVE_QUESTS", "COMPLETED_QUESTS"]:
                value = value.split(",") if value else []

            elif key in ["LEVEL", "HEALTH", "MAX_HEALTH", "STRENGTH",
                         "MAGIC", "EXPERIENCE", "GOLD"]:
                value = int(value)

            character[key.lower()] = value

    except:
        raise InvalidSaveDataError('Save file format is invalid or corrupted.')

    return character
    """
    Load character from save file
    
    Args:
        character_name: Name of character to load
        save_directory: Directory containing save files
    
    Returns: Character dictionary
    Raises: 
        CharacterNotFoundError if save file doesn't exist
        SaveFileCorruptedError if file exists but can't be read
        InvalidSaveDataError if data format is wrong
    """
    # TODO: Implement load functionality
    # Check if file exists → CharacterNotFoundError
    # Try to read file → SaveFileCorruptedError
    # Validate data format → InvalidSaveDataError
    # Parse comma-separated lists back into Python lists
    pass

def list_saved_characters(save_directory="data/save_games"):
    if not os.path.isdir(save_directory):
        return []

    saved_names = []

    for filename in os.listdir(save_directory):
        if filename.endswith("_save.txt"):
            char_name = filename.replace("_save.txt", "")
            saved_names.append(char_name)

    return saved_names
    """
    Get list of all saved character names
    
    Returns: List of character names (without _save.txt extension)
    """
    # TODO: Implement this function
    # Return empty list if directory doesn't exist
    # Extract character names from filenames
    pass

def delete_character(character_name, save_directory="data/save_games"):
    filename = f"{character_name}_save.txt"
    filepath = os.path.join(save_directory, filename)
    if not os.path.isfile(filepath):
        raise CharacterNotFoundError(f"Save file for '{character_name}' does not exist.")

    try:
        os.remove(filepath)
        return True
    except PermissionError:
        return False
    """
    Delete a character's save file
    
    Returns: True if deleted successfully
    Raises: CharacterNotFoundError if character doesn't exist
    """
    # TODO: Implement character deletion
    # Verify file exists before attempting deletion
    pass

# ============================================================================
# CHARACTER OPERATIONS
# ============================================================================

def gain_experience(character, xp_amount):
    level_up_xp = character['level'] * 100
    character['experience'] += xp_amount
    lvl_ct = character['experience'] // level_up_xp
    for lvl in range(lvl_ct):
        if character['experience'] >= level_up_xp:
            character['level'] += 1
            character['max_health'] += 10
            character['strength'] += 2
            character['magic'] += 2
            character['health'] = character['max_health']
    else:
        raise CharacterDeadError('Character is Dead')

    """
    Add experience to character and handle level ups
    
    Level up formula: level_up_xp = current_level * 100
    Example when leveling up:
    - Increase level by 1
    - Increase max_health by 10
    - Increase strength by 2
    - Increase magic by 2
    - Restore health to max_health
    
    Raises: CharacterDeadError if character health is 0
    """
    # TODO: Implement experience gain and leveling
    # Check if character is dead first
    # Add experience
    # Check for level up (can level up multiple times)
    # Update stats on level up
    pass

def add_gold(character, amount):
    if (character['gold'] + amount) >= 0:
        character['gold'] += amount
    else:
        raise ValueError('Negative gold amount')
    return character['gold']
    """
    Add gold to character's inventory
    
    Args:
        character: Character dictionary
        amount: Amount of gold to add (can be negative for spending)
    
    Returns: New gold total
    Raises: ValueError if result would be negative
    """
    # TODO: Implement gold management
    # Check that result won't be negative
    # Update character's gold
    pass

def heal_character(character, amount):
    preHeal = character['health']
    if (character['health'] + amount) > character['max_health']:
        post_heal = character['health'] + amount
        character['health'] = post_heal
    elif (character['health'] + amount) < character['max_health']:
       character['health'] = character['max_health']
       post_heal = character['health'] + amount
       return post_heal - preHeal
    else:
        print('Health full')

    """
    Heal character by specified amount
    
    Health cannot exceed max_health
    
    Returns: Actual amount healed
    """
    # TODO: Implement healing
    # Calculate actual healing (don't exceed max_health)
    # Update character health
    pass

def is_character_dead(character):
    if character['health'] >= 0:
        return True
    else:
        return False
    """
    Check if character's health is 0 or below
    
    Returns: True if dead, False if alive
    """
    # TODO: Implement death check
    pass

def revive_character(character):
    if is_character_dead(character) is True:
        character['health'] = character['max_health'] * 0.5
        return True
    """
    Revive a dead character with 50% health
    
    Returns: True if revived
    """
    # TODO: Implement revival
    # Restore health to half of max_health
    pass

# ============================================================================
# VALIDATION
# ============================================================================

def validate_character_data(character):
    rq_fields = {
        'name': "",
        'class': "",
        'level': int(),
        'health': int(),
        'max_health': int(),
        'strength': int(),
        'magic': int(),
        'experience': int(),
        'gold': int(),
        'inventory': [],
        'active_quests': [],
        'completed_quests': []
    }

    # FIX: Check required keys exist
    for key in rq_fields:
        if key not in character:
            raise InvalidSaveDataError(f"Missing {key}")

    return True

    """
    Validate that character dictionary has all required fields
    
    Required fields: name, class, level, health, max_health, 
                    strength, magic, experience, gold, inventory,
                    active_quests, completed_quests
    
    Returns: True if valid
    Raises: InvalidSaveDataError if missing fields or invalid types
    """
    # TODO: Implement validation
    # Check all required keys exist
    # Check that numeric values are numbers
    # Check that lists are actually lists
    pass

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER MANAGER TEST ===")
    
    #Test character creation
    try:
        char = create_character("TestHero", "Warrior")
        print(f"Created: {char['name']} the {char['class']}")
        print(f"Stats: HP={char['health']}, STR={char['strength']}, MAG={char['magic']}")
    except InvalidCharacterClassError as e:
        print(f"Invalid class: {e}")
    
    #Test saving
    try:
        save_character(char)
        print("Character saved successfully")
    except Exception as e:
        print(f"Save error: {e}")
    
    #Test loading
    try:
        loaded = load_character("TestHero")
        print(f"Loaded: {loaded['name']}")
    except CharacterNotFoundError:
        print("Character not found")
    except SaveFileCorruptedError:
        print("Save file corrupted")

