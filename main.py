"""
COMP 163 - Project 3: Quest Chronicles
Main Game Module - Starter Code

Name: Marcellus Hutchins

AI Usage: [Document any AI assistance used]

This is the main game file that ties all modules together.
Demonstrates module integration and complete game flow.
"""
from random import choice

# Import all our custom modules
import character_manager
import inventory_system
import quest_handler
import combat_system
import game_data
from custom_exceptions import *

# ============================================================================
# GAME STATE
# ============================================================================

# Global variables for game data
current_character = None
all_quests = {}
all_items = {}
game_running = False

# ============================================================================
# MAIN MENU
# ============================================================================

def main_menu():
    print('Main Menu Options:'
          '(1) New Game\n'
          '(2) Load Game\n'
          '(3) Exit\n')
    player_choice = int(input("Select your choice: "))
    if player_choice == 1:
        player_choice = 'New Game'
    elif player_choice == 2:
        player_choice = 'Load Game'
    elif player_choice == 3:
        player_choice = 'Exit'
    return player_choice
    """
    Display main menu and get player choice
    
    Options:
    1. New Game
    2. Load Game
    3. Exit
    
    Returns: Integer choice (1-3)
    """
    # TODO: Implement main menu display
    # Show options
    # Get user input
    # Validate input (1-3)
    # Return choice
    pass

def new_game():
    character_name = input("Please enter your character's name: ")
    character_class = input("Please enter your character's class: ")
    try:
        new_character = character_manager.create_character(character_name, character_class)
        character_manager.save_character(new_character, 1)
        game_loop()
    except InvalidCharacterClassError:
        print("Invalid character class entered. Please try again.")

        
    """
    Start a new game
    
    Prompts for:
    - Character name
    - Character class
    
    Creates character and starts game loop
    """
    global current_character
    
    # TODO: Implement new game creation
    # Get character name from user
    # Get character class from user
    # Try to create character with character_manager.create_character()
    # Handle InvalidCharacterClassError
    # Save character
    # Start game loop
    pass

def load_game():
    save_chr = (character_manager.list_saved_characters())
    for Char, name in enumerate(save_chr, start=1):
        print(f"{Char}. {name}")
    try:
        character_name = int(input("Please enter your character #"))
        character_manager.load_character(character_name)
        game_loop()
    except CharacterNotFoundError:
        print("Invalid character entered. Please try again.")
    except SaveFileCorruptedError:
        print('Save file is corrupt')




    """
    Load an existing saved game
    
    Shows list of saved characters
    Prompts user to select one
    """
    global current_character
    
    # TODO: Implement game loading
    # Get list of saved characters
    # Display them to user
    # Get user choice
    # Try to load character with character_manager.load_character()
    # Handle CharacterNotFoundError and SaveFileCorruptedError
    # Start game loop
    pass

# ============================================================================
# GAME LOOP
# ============================================================================

def game_loop():
    while game_running:
       player_choice = game_menu()
        if player_choice == 1

        save_game()

    """
    Main game loop - shows game menu and processes actions
    """
    global game_running, current_character
    
    game_running = True
    
    # TODO: Implement game loop
    # While game_running:
    #   Display game menu
    #   Get player choice
    #   Execute chosen action
    #   Save game after each action
    pass

def game_menu():
    print("\n=== GAME MENU ===")
    print("1. View Character Stats")
    print("2. View Inventory")
    print("3. Quest Menu")
    print("4. Explore (Find Battles)")
    print("5. Shop")
    print("6. Save and Quit")
    player_choice = int(input("Select your choice: "))
    return player_choice
    """
    Display game menu and get player choice
    
    Options:
    1. View Character Stats
    2. View Inventory
    3. Quest Menu
    4. Explore (Find Battles)
    5. Shop
    6. Save and Quit
    
    Returns: Integer choice (1-6)
    """
    # TODO: Implement game menu
    pass

# ============================================================================
# GAME ACTIONS
# ============================================================================

def view_character_stats():
    character_manager.load_character(current_character,1)
    quest_handler.get_quest_completion_percentage(current_character,all_quests)
    """Display character information"""
    global current_character
    
    # TODO: Implement stats display
    # Show: name, class, level, health, stats, gold, etc.
    # Use character_manager functions
    # Show quest progress using quest_handler
    pass

def view_inventory():
    """Display and manage inventory"""

    global current_character, all_items
    try:
        inventory_system.display_inventory(current_character,all_items)
        print('Do you wish to..\n 1. Use item\n 2. Equip weapon\n Equip armor\n 3.Drop item')
        player_choice = int(input("Select your choice: "))
        item_choice = int(input('select item: '))
        if player_choice == 1:
            inventory_system.use_item(current_character, item_choice, all_items)
        elif player_choice == 2:
            inventory_system.equip_weapon(current_character, item_choice, all_items)
        elif player_choice == 3:
            inventory_system.equip_armor(current_character, item_choice, all_items)
        else:
            inventory_system.remove_item_from_inventory(current_character, item_choice)
    except Exception as e:
        print(e)
    # TODO: Implement inventory menu
    # Show current inventory
    # Options: Use item, Equip weapon/armor, Drop item
    # Handle exceptions from inventory_system
    pass

def quest_menu():
    try:
        print("\n=== QUEST MENU ===")
        """Quest management menu"""
        quest_choice = int(input('What quest are you on?'))
        print(quest_handler.get_active_quests(current_character,all_quests))
        print(quest_handler.get_available_quests(current_character,all_quests))
        print(quest_handler.get_completed_quests(current_character,all_quests))
        print(quest_handler.accept_quest(current_character,quest_choice,all_quests))
        print(quest_handler.abandon_quest(current_character,quest_choice))
        print('Back')
    except Exception as e:
        print(e)
    global current_character, all_quests
    
    # TODO: Implement quest menu
    # Show:
    #   1. View Active Quests
    #   2. View Available Quests
    #   3. View Completed Quests
    #   4. Accept Quest
    #   5. Abandon Quest
    #   6. Complete Quest (for testing)
    #   7. Back
    # Handle exceptions from quest_handler
    pass

def explore():
    try:
        enemy = combat_system.get_random_enemy_for_level(current_character)
        combat_system.SimpleBattle(current_character, enemy)
        dead = character_manager.is_character_dead(current_character)
        if dead is False:
            return combat_system.get_victory_rewards(enemy)
        else:
            return handle_character_death()
    except Exception as e:
        print(e)
    """Find and fight random enemies"""
    global current_character
    
    # TODO: Implement exploration
    # Generate random enemy based on character level
    # Start combat with combat_system.SimpleBattle
    # Handle combat results (XP, gold, death)
    # Handle exceptions
    pass

def shop():
    """Shop menu for buying/selling items"""
    global current_character, all_items
    
    # TODO: Implement shop
    # Show available items for purchase
    # Show current gold
    # Options: Buy item, Sell item, Back
    # Handle exceptions from inventory_system
    pass

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def save_game():
    """Save current game state"""
    global current_character
    
    # TODO: Implement save
    # Use character_manager.save_character()
    # Handle any file I/O exceptions
    pass

def load_game_data():
    try:
        game_data.load_quests()
        game_data.load_items()
    except MissingDataFileError as e:
        print(e)
        print('creating defualt data file')
        game_data.create_default_data_files()
    except InvalidDataFormatError as e:
        print(e)
    """Load all quest and item data from files"""
    global all_quests, all_items
    
    # TODO: Implement data loading
    # Try to load quests with game_data.load_quests()
    # Try to load items with game_data.load_items()
    # Handle MissingDataFileError, InvalidDataFormatError
    # If files missing, create defaults with game_data.create_default_data_files()
    pass

def handle_character_death():
    print('You have Died\n would you like to quit now or revive?')
    death_choie = int(input('(1) Quit\n(2) Revive\n'))
    if death_choie == 1:
        game_running = False
    else:
        character_manager.revive_character(current_character)
    """Handle character death"""
    global current_character, game_running
    
    # TODO: Implement death handling
    # Display death message
    # Offer: Revive (costs gold) or Quit
    # If revive: use character_manager.revive_character()
    # If quit: set game_running = False
    pass

def display_welcome():
    """Display welcome message"""
    print("=" * 50)
    print("     QUEST CHRONICLES - A MODULAR RPG ADVENTURE")
    print("=" * 50)
    print("\nWelcome to Quest Chronicles!")
    print("Build your character, complete quests, and become a legend!")
    print()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main game execution function"""
    
    # Display welcome message
    display_welcome()
    
    # Load game data
    try:
        load_game_data()
        print("Game data loaded successfully!")
    except MissingDataFileError:
        print("Creating default game data...")
        game_data.create_default_data_files()
        load_game_data()
    except InvalidDataFormatError as e:
        print(f"Error loading game data: {e}")
        print("Please check data files for errors.")
        return
    
    # Main menu loop
    while True:
        choice = main_menu()
        
        if choice == 1:
            new_game()
        elif choice == 2:
            load_game()
        elif choice == 3:
            print("\nThanks for playing Quest Chronicles!")
            break
        else:
            print("Invalid choice. Please select 1-3.")

if __name__ == "__main__":
    main()

