"""
COMP 163 - Project 3: Quest Chronicles
Combat System Module - Starter Code

Name: Marcellus Hutchins

AI Usage: [Document any AI assistance used]

Handles combat mechanics
"""
import random

from custom_exceptions import (
    InvalidTargetError,
    CombatNotActiveError,
    CharacterDeadError,
    AbilityOnCooldownError
)

# ============================================================================
# ENEMY DEFINITIONS
# ============================================================================

def create_enemy(enemy_type):
    enemy_list = ['goblin', 'orc', 'dragon']
    if enemy_type not in enemy_list:
        raise InvalidTargetError()
    try:
        if enemy_type == 'goblin':
            enemy = {'name':'Goblin',
                    'health':50,
                    'Strength':8,
                    'Magic': 2,
                    'xp_reward': 25,
                    'gold_reward': 10}
        elif enemy_type == 'orc':
            enemy = {'name':'Orc',
                     'health':80,
                     'Strength':12,
                     'Magic':5,
                     'xp_reward': 50,
                     'gold_reward': 25}
        elif enemy_type == 'dragon':
            enemy = {'name':'Dragon',
                     'health':200,
                     'Strength':25,
                     'Magic': 15,
                     'xp_reward': 200,
                     'gold_reward': 100}
        return enemy
    except InvalidTargetError:
        print("Invalid target entered. Please try again.")

    """
    Create an enemy based on type
    
    Example enemy types and stats:
    - goblin: health=50, strength=8, magic=2, xp_reward=25, gold_reward=10
    - orc: health=80, strength=12, magic=5, xp_reward=50, gold_reward=25
    - dragon: health=200, strength=25, magic=15, xp_reward=200, gold_reward=100
    
    Returns: Enemy dictionary
    Raises: InvalidTargetError if enemy_type not recognized
    """
    # TODO: Implement enemy creation
    # Return dictionary with: name, health, max_health, strength, magic, xp_reward, gold_reward
    pass

def get_random_enemy_for_level(character_level):
    if character_level in range(3):
        field_monster = create_enemy('goblin')
    elif character_level in range(3,6):
        field_monster = create_enemy('orc')
    elif character_level >= 6:
        field_monster = create_enemy('dragons')
    return field_monster
    """
    Get an appropriate enemy for character's level
    
    Level 1-2: Goblins
    Level 3-5: Orcs
    Level 6+: Dragons
    
    Returns: Enemy dictionary
    """
    # TODO: Implement level-appropriate enemy selection
    # Use if/elif/else to select enemy type
    # Call create_enemy with appropriate type
    pass

# ============================================================================
# COMBAT SYSTEM
# ============================================================================

class SimpleBattle:
    """
    Simple turn-based combat system
    
    Manages combat between character and enemy
    """
    
    def __init__(self, character, enemy):
        self.character = character
        self.enemy = enemy
        self.combat_active = True
        self.turn_count = 0

        """Initialize battle with character and enemy"""
        # TODO: Implement initialization
        # Store character and enemy
        # Set combat_active flag
        # Initialize turn counter
        pass
    
    def start_battle(self):
        while self.character['health'] >= 0 and self.enemy['health'] >= 0:
            if self.character['health'] > 0:
                raise CharacterDeadError('Character is Dead')
            elif self.character['health'] == 0:
                battle_results = {'winner' : 'enemy',
                                  'xp_gained' : 0,
                                  'gold_gained' : 0}
                break
            if self.enemy['health'] <= 0:
                battle_results = {'winner' : 'player',
                                  'xp_gained' : self.enemy['xp_reward'],
                                  'gold_gained' : self.enemy['gold_reward']}
                break
        return battle_results








        """
        Start the combat loop
        
        Returns: Dictionary with battle results:
                {'winner': 'player'|'enemy', 'xp_gained': int, 'gold_gained': int}
        
        Raises: CharacterDeadError if character is already dead
        """
        # TODO: Implement battle loop
        # Check character isn't dead
        # Loop until someone dies
        # Award XP and gold if player wins
        pass
    
    def player_turn(self):
        if self.combat_active:
            print('Displays options:\n 1. Basic Attack\n,  2. Special Ability (if available)\n, 3. Try to Run')
            player_choice = int(input('Enter your choice: '))
            if player_choice == 1:
                damage = self.calculate_damage(self.character,self.enemy)
                self.apply_damage(self.enemy, damage)
            elif player_choice == 2:
                use_special_ability(self.character,self.enemy)
            elif player_choice == 3:
                self.attempt_escape()
        else:
            raise CombatNotActiveError('You are not in Combat')

        """
        Handle player's turn
        
        Displays options:
        1. Basic Attack
        2. Special Ability (if available)
        3. Try to Run
        
        Raises: CombatNotActiveError if called outside of battle
        """
        # TODO: Implement player turn
        # Check combat is active
        # Display options
        # Get player choice
        # Execute chosen action
        pass
    
    def enemy_turn(self):
        if self.combat_active:
            damage = (self.enemy['Magic'] + self.enemy['Strength']) * 0.25
            self.character['health'] -= damage
            return self.character['health']
        else:
            raise CombatNotActiveError('You are not in Combat')
        """
        Handle enemy's turn - simple AI
        
        Enemy always attacks
        
        Raises: CombatNotActiveError if called outside of battle
        """
        # TODO: Implement enemy turn
        # Check combat is active
        # Calculate damage
        # Apply to character
        pass
    
    def calculate_damage(self, attacker, defender):
        physical_damage = int(attacker['strength'] - (defender['strength'] // 4))
        magic_damage = int(attacker['magic'] - (defender['magic'] // 4))
        if physical_damage <= 0:
            physical_damage = 1
        if magic_damage <= 0:
            magic_damage = 1
        if attacker['strength'] > attacker['magic']:
            return physical_damage
        else:
            return magic_damage
        """
        Calculate damage from attack
        
        Damage formula: attacker['strength'] - (defender['strength'] // 4)
        Minimum damage: 1
        
        Returns: Integer damage amount
        """
        # TODO: Implement damage calculation
        pass
    
    def apply_damage(self, target, damage):
        if (target.health - damage) >= 0:
            target.health -= damage
        else:
            target.health = 0
        return target.health

        """
        Apply damage to a character or enemy
        
        Reduces health, prevents negative health
        """
        # TODO: Implement damage application
        pass
    
    def check_battle_end(self):
        if self.combat_active:
            if self.character['health'] == 0:
                self.combat_active = False
                return self.enemy
            elif self.enemy['health'] == 0:
                self.combat_active = False
                return self.character


        """
        Check if battle is over
        
        Returns: 'player' if enemy dead, 'enemy' if character dead, None if ongoing
        """
        # TODO: Implement battle end check
        pass
    
    def attempt_escape(self):
        success = random.randint(1,4)
        if success >=2:
            return True
        else:
            return False
        """
        Try to escape from battle
        
        50% success chance
        
        Returns: True if escaped, False if failed
        """
        # TODO: Implement escape attempt
        # Use random number or simple calculation
        # If successful, set combat_active to False
        pass

# ============================================================================
# SPECIAL ABILITIES
# ============================================================================

def use_special_ability(character, enemy):
    special_ability = character['special_ability']
    cooldown = False
    while not cooldown:
        if character['class'] == 'warrior':
            special_ability = 'Power Strike'
            warrior_power_strike(character, enemy)
            cooldown = True
        elif character['class'] == 'mage':
            special_ability = 'Fireball'
            mage_fireball(character, enemy)
            cooldown = True
        elif character['class'] == 'rogue':
            success = random.randint(1, 4)
            if success >= 2:
                special_ability = 'Critical Strike'
                rogue_critical_strike(character,enemy)
                cooldown = True
        elif character['class'] == 'cleric':
            special_ability = 'Heal'
            cleric_heal(character)
        return print(f"{character['class']} uses {special_ability} cooldown is {cooldown}")

    else:
        raise AbilityOnCooldownError('Ablity on Cooldown')


    """
    Use character's class-specific special ability
    
    Example abilities by class:
    - Warrior: Power Strike (2x strength damage)
    - Mage: Fireball (2x magic damage)
    - Rogue: Critical Strike (3x strength damage, 50% chance)
    - Cleric: Heal (restore 30 health)
    
    Returns: String describing what happened
    Raises: AbilityOnCooldownError if ability was used recently
    """
    # TODO: Implement special abilities
    # Check character class
    # Execute appropriate ability
    # Track cooldowns (optional advanced feature)
    pass

def warrior_power_strike(character, enemy):
    physical_damage = character['strength'] - (enemy['strength'] // 2)
    return physical_damage
    """Warrior special ability"""
    # TODO: Implement power strike
    # Double strength damage
    pass

def mage_fireball(character, enemy):
    magic_damage = int(character['magic'] - (enemy['magic'] // 2))
    return magic_damage
    """Mage special ability"""
    # TODO: Implement fireball
    # Double magic damage
    pass

def rogue_critical_strike(character, enemy):
    crit = random.randint(1, 4)
    if crit >= 2:
        physical_damage = (character['strength'] * 3 - enemy['strength']) //4

    else:
        physical_damage = (character['strength'] - enemy['strength']) //4
    return physical_damage

    """Rogue special ability"""
    # TODO: Implement critical strike
    # 50% chance for triple damage
    pass

def cleric_heal(character):
    if (character['health'] + 30) > character['max_health']:
        character['health'] += 30
    else:
        character['health'] = character['max_health']
    """Cleric special ability"""
    # TODO: Implement healing
    # Restore 30 HP (not exceeding max_health)
    pass

# ============================================================================
# COMBAT UTILITIES
# ============================================================================

def can_character_fight(character):
    if character.combat.active == False and character['health'] > 0:
        return True
    else:
        return False
    """
    Check if character is in condition to fight
    
    Returns: True if health > 0 and not in battle
    """
    # TODO: Implement fight check
    pass

def get_victory_rewards(enemy):
    if enemy['health'] == 0:
        character_reward = {'xp': enemy['xp_reward'],
                            'gold': enemy['gold_reward']}
        return character_reward
    """
    Calculate rewards for defeating enemy
    
    Returns: Dictionary with 'xp' and 'gold'
    """
    # TODO: Implement reward calculation
    pass

def display_combat_stats(character, enemy):
    """
    Display current combat status
    
    Shows both character and enemy health/stats
    """
    # TODO: Implement status display
    print(f"\n{character['name']}: HP={character['health']}/{character['max_health']}")
    print(f"{enemy['name']}: HP={enemy['health']}/{enemy['max_health']}")
    pass

def display_battle_log(message):
    """
    Display a formatted battle message
    """
    # TODO: Implement battle log display
    print(f">>> {message}")
    pass

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== COMBAT SYSTEM TEST ===")
    
    # Test enemy creation
    try:
         goblin = create_enemy("goblin")
         print(f"Created {goblin['name']}")
    except InvalidTargetError as e:
         print(f"Invalid enemy: {e}")
    
     #Test battle
    test_char = {
         'name': 'Hero',
         'class': 'Warrior',
         'health': 120,
         'max_health': 120,
         'strength': 15,
         'magic': 5
    }

    battle = SimpleBattle(test_char, goblin)
    try:
         result = battle.start_battle()
         print(f"Battle result: {result}")
    except CharacterDeadError:
         print("Character is dead!")

