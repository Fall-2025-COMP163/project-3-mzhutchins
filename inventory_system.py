"""
COMP 163 - Project 3: Quest Chronicles
Inventory System Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

This module handles inventory management, item usage, and equipment.
"""

from custom_exceptions import (
    InventoryFullError,
    ItemNotFoundError,
    InsufficientResourcesError,
    InvalidItemTypeError
)

# Maximum inventory size
MAX_INVENTORY_SIZE = 20

# ============================================================================
# INVENTORY MANAGEMENT
# ============================================================================

def add_item_to_inventory(character, item_id):
    if len(character['inventory']) >= MAX_INVENTORY_SIZE:
        raise InventoryFullError('Inventory full')
    else:
        character['inventory'].append(item_id)
        return True

    """
    Add an item to character's inventory
    
    Args:
        character: Character dictionary
        item_id: Unique item identifier
    
    Returns: True if added successfully
    Raises: InventoryFullError if inventory is at max capacity
    """
    # TODO: Implement adding items
    # Check if inventory is full (>= MAX_INVENTORY_SIZE)
    # Add item_id to character['inventory'] list
    pass

def remove_item_from_inventory(character, item_id):
    if item_id in character['inventory']:
        character['inventory'].remove(item_id)
        return True
    else:
        raise ItemNotFoundError('Item not found')

    """
    Remove an item from character's inventory
    
    Args:
        character: Character dictionary
        item_id: Item to remove
    
    Returns: True if removed successfully
    Raises: ItemNotFoundError if item not in inventory
    """
    # TODO: Implement item removal
    # Check if item exists in inventory
    # Remove item from list
    pass

def has_item(character, item_id):
    if item_id in character.inventory:
        return True
    else:
        return False
    """
    Check if character has a specific item
    
    Returns: True if item in inventory, False otherwise
    """
    # TODO: Implement item check
    pass

def count_item(character, item_id):
    num_items = character.inventory.count(item_id)
    return num_items
    """
    Count how many of a specific item the character has
    
    Returns: Integer count of item
    """
    # TODO: Implement item counting
    # Use list.count() method
    pass

def get_inventory_space_remaining(character):
    inventory_space = MAX_INVENTORY_SIZE - len(character.inventory)
    return inventory_space
    """
    Calculate how many more items can fit in inventory
    
    Returns: Integer representing available slots
    """
    # TODO: Implement space calculation
    pass

def clear_inventory(character):
    cleared_items = character.inventory.copy()
    character.inventory.clear()
    return cleared_items
    """
    Remove all items from inventory
    
    Returns: List of removed items
    """
    # TODO: Implement inventory clearing
    # Save current inventory before clearing
    # Clear character's inventory list
    pass

# ============================================================================
# ITEM USAGE
# ============================================================================

def use_item(character, item_id, item_data):
    if item_id in character['inventory']:
        if item_data['type'] == 'consumable':
            effect = item_data["effect"]
            stat_name, value_str = effect.split(":")
            value = int(value_str)
            if stat_name in character:
                character[stat_name] += value
            character["inventory"].remove(item_id)
        else:
            raise InvalidItemTypeError('Invalid item type')
    else:
        raise ItemNotFoundError('item not found')
    return f"Used {item_id}. {stat_name} increased by {value}."
    """
    Use a consumable item from inventory
    
    Args:
        character: Character dictionary
        item_id: Item to use
        item_data: Item information dictionary from game_data
    
    Item types and effects:
    - consumable: Apply effect and remove from inventory
    - weapon/armor: Cannot be "used", only equipped
    
    Returns: String describing what happened
    Raises: 
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'consumable'
    """
    # TODO: Implement item usage
    # Check if character has the item
    # Check if item type is 'consumable'
    # Parse effect (format: "stat_name:value" e.g., "health:20")
    # Apply effect to character
    # Remove item from inventory
    pass

def equip_weapon(character, item_id, item_data):
    if item_id not in character["inventory"]:
        raise ItemNotFoundError(f"{item_id} not found in inventory.")

    item_data = item_data[item_id]
    if item_data["type"] != "weapon":
        raise InvalidItemTypeError(f"{item_id} is not a weapon.")

    if "equipped_weapon" in character and character["equipped_weapon"] is not None:
        old_weapon = character["equipped_weapon"]
        old_data = item_data[old_weapon]

        stat_name, value = old_data["effect"].split(":")
        value = int(value)

        character[stat_name] -= value

        character["inventory"].append(old_weapon)

    stat_name, value = item_data["effect"].split(":")
    value = int(value)

    character['item_data'] = item_data
    character[stat_name] += value
    character["equipped_weapon"] = item_id
    character["inventory"].remove(item_id)

    return f"Equipped {item_id}. {stat_name} +{value}."
    """
    Equip a weapon
    
    Args:
        character: Character dictionary
        item_id: Weapon to equip
        item_data: Item information dictionary
    
    Weapon effect format: "strength:5" (adds 5 to strength)
    
    If character already has weapon equipped:
    - Unequip current weapon (remove bonus)
    - Add old weapon back to inventory
    
    Returns: String describing equipment change
    Raises:
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'weapon'
    """
    # TODO: Implement weapon equipping
    # Check item exists and is type 'weapon'
    # Handle unequipping current weapon if exists
    # Parse effect and apply to character stats
    # Store equipped_weapon in character dictionary
    # Remove item from inventory
    pass

def equip_armor(character, item_id, item_data):
    if item_id not in character["inventory"]:
        raise ItemNotFoundError(f"{item_id} not found in inventory.")

    item_data = item_data[item_id]
    if item_data["type"] != "armor":
        raise InvalidItemTypeError(f"{item_id} is not armor.")

    if "equipped_armor" in character and character["equipped_armor"] is not None:
        old_armor = character["equipped_armor"]
        old_data = item_data[old_armor]

        stat_name, value = old_data["effect"].split(":")
        value = int(value)

        character[stat_name] -= value

        character["inventory"].append(old_armor)

    stat_name, value = item_data["effect"].split(":")
    value = int(value)

    character[stat_name] += value

    character["equipped_armor"] = item_id

    character["inventory"].remove(item_id)

    return f"Equipped {item_id}. {stat_name} +{value}."
    """
    Equip armor
    
    Args:
        character: Character dictionary
        item_id: Armor to equip
        item_data: Item information dictionary
    
    Armor effect format: "max_health:10" (adds 10 to max_health)
    
    If character already has armor equipped:
    - Unequip current armor (remove bonus)
    - Add old armor back to inventory
    
    Returns: String describing equipment change
    Raises:
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'armor'
    """
    # TODO: Implement armor equipping
    # Similar to equip_weapon but for armor
    pass

def unequip_weapon(character):
    if character['equipped_weapon'] is not None:
        weapon_id = character["equipped_weapon"]
        if weapon_id in character["item_data"]:
            weapon_data = character["item_data"]
            stat_name, value = weapon_data["effect"].split(":")
            value = int(value)
            character[stat_name] -= value
        if len(character['inventory']) < MAX_INVENTORY_SIZE:
            character["inventory"].append(weapon_id)
            character["equipped_weapon"] = None
        else:
            raise InventoryFullError('Inventory full')
        return weapon_id
    """
    Remove equipped weapon and return it to inventory
    
    Returns: Item ID that was unequipped, or None if no weapon equipped
    Raises: InventoryFullError if inventory is full
    """
    # TODO: Implement weapon unequipping
    # Check if weapon is equipped
    # Remove stat bonuses
    # Add weapon back to inventory
    # Clear equipped_weapon from character
    pass

def unequip_armor(character):
    if character['equipped_armor'] is not None:
        armor_id = character["equipped_armor"]
        if armor_id in character["item_data"]:
            armor_data = character["item_data"]
            stat_name, value = armor_data["effect"].split(":")
            value = int(value)
            character[stat_name] -= value
        if len(character['inventory']) < MAX_INVENTORY_SIZE:
            character["inventory"].append(armor_id)
            character["equipped_armor"] = None
        else:
            raise InventoryFullError('Inventory full')
        return armor_id
    """
    Remove equipped armor and return it to inventory
    
    Returns: Item ID that was unequipped, or None if no armor equipped
    Raises: InventoryFullError if inventory is full
    """
    # TODO: Implement armor unequipping
    pass

# ============================================================================
# SHOP SYSTEM
# ============================================================================

def purchase_item(character, item_id, item_data):
    if len(character['inventory']) < MAX_INVENTORY_SIZE:
        if item_data['cost'] < character['gold']:
            character['gold'] -= item_data['cost']
            character['inventory'].append(item_id)
            return True
        else:
            raise InsufficientResourcesError('Not enough gold.')
    else:
        raise InventoryFullError('Inventory full')
    """
    Purchase an item from a shop
    
    Args:
        character: Character dictionary
        item_id: Item to purchase
        item_data: Item information with 'cost' field
    
    Returns: True if purchased successfully
    Raises:
        InsufficientResourcesError if not enough gold
        InventoryFullError if inventory is full
    """
    # TODO: Implement purchasing
    # Check if character has enough gold
    # Check if inventory has space
    # Subtract gold from character
    # Add item to inventory
    pass

def sell_item(character, item_id, item_data):
    if item_id in character.inventory:
        sell_price = item_data['cost'] //2
        character.inventory.remove(item_id)
        character.gold += sell_price
        return sell_price
    else:
        return ItemNotFoundError('Item not found')
    """
    Sell an item for half its purchase cost
    
    Args:
        character: Character dictionary
        item_id: Item to sell
        item_data: Item information with 'cost' field
    
    Returns: Amount of gold received
    Raises: ItemNotFoundError if item not in inventory
    """
    # TODO: Implement selling
    # Check if character has item
    # Calculate sell price (cost // 2)
    # Remove item from inventory
    # Add gold to character
    pass

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def parse_item_effect(effect_string):
    effect_list = effect_string.split(':')
    effects = (effect_list[0], int(effect_list[1]))
    return effects
    """
    Parse item effect string into stat name and value
    
    Args:
        effect_string: String in format "stat_name:value"
    
    Returns: Tuple of (stat_name, value)
    Example: "health:20" → ("health", 20)
    """
    # TODO: Implement effect parsing
    # Split on ":"
    # Convert value to integer
    pass

def apply_stat_effect(character, stat_name, value):
    if stat_name == 'health':
        if (value + character.health) < character.max_health:
            character.health += value
        else:
            character.health = character.max_health
    elif stat_name == 'strength':
        character.strength += value
    elif stat_name == 'magic':
        character.magic += value
    return character[stat_name]
    """
    Apply a stat modification to character
    
    Valid stats: health, max_health, strength, magic
    
    Note: health cannot exceed max_health
    """
    # TODO: Implement stat application
    # Add value to character[stat_name]
    # If stat is health, ensure it doesn't exceed max_health
    pass

def display_inventory(character, item_data_dict):
    inventory = character.get("inventory", [])

    item_counts = {}
    for item_id in inventory:
        item_counts[item_id] = item_counts.get(item_id, 0) + 1

    print(f"{'ID':<10} {'Name':<20} {'Type':<12} {'Qty':<4}")

    for item_id, count in item_counts.items():
        item_info = item_data_dict.get(item_id, {})
        name = item_info.get("name", "Unknown")
        item_type = item_info.get("type", "Unknown")
        print(f"{item_id:<10} {name:<20} {item_type:<12} {count:<4}")

    """
    Display character's inventory in formatted way
    
    Args:
        character: Character dictionary
        item_data_dict: Dictionary of all item data
    
    Shows item names, types, and quantities
    """
    # TODO: Implement inventory display
    # Count items (some may appear multiple times)
    # Display with item names from item_data_dict
    pass

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== INVENTORY SYSTEM TEST ===")
    
    #Test adding items
    test_char = {'inventory': [], 'gold': 100, 'health': 80, 'max_health': 80}

    try:
        add_item_to_inventory(test_char, "health_potion")
        print(f"Inventory: {test_char['inventory']}")
    except InventoryFullError:
        print("Inventory is full!")
    
    #Test using items
    test_item = {
        'item_id': 'health_potion',
        'type': 'consumable',
        'effect': 'health:20'
    }

    try:
        result = use_item(test_char, "health_potion", test_item)
        print(result)
    except ItemNotFoundError:
        print("Item not found")

