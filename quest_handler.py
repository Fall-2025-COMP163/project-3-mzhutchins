"""
COMP 163 - Project 3: Quest Chronicles
Quest Handler Module - Starter Code

Name: Marcellus Hutchins

AI Usage: [Document any AI assistance used]

This module handles quest management, dependencies, and completion.
"""
import character_manager
from custom_exceptions import (
    QuestNotFoundError,
    QuestRequirementsNotMetError,
    QuestAlreadyCompletedError,
    QuestNotActiveError,
    InsufficientLevelError
)
from main import all_quests


# ============================================================================
# QUEST MANAGEMENT
# ============================================================================

def accept_quest(character, quest_id, quest_data_dict):
    if quest_id not in quest_data_dict:
        raise QuestNotFoundError()

    quest = quest_data_dict[quest_id]

    required_level = quest["required_level"]
    if character["level"] < required_level:
        raise InsufficientLevelError('Insufficient level')

    prerequisite = quest["prerequisite"]

    if prerequisite != "NONE":
        if prerequisite not in character["completed_quests"]:
            raise QuestRequirementsNotMetError('Prerequisite not met')
    if quest_id in character["completed_quests"]:
        raise QuestAlreadyCompletedError('Quest already completed')
    if quest_id in character["active_quests"]:
        raise QuestRequirementsNotMetError('Quest already active')
    character["active_quests"].append(quest_id)

    return True


    """
    Accept a new quest
    
    Args:
        character: Character dictionary
        quest_id: Quest to accept
        quest_data_dict: Dictionary of all quest data
    
    Requirements to accept quest:
    - Character level >= quest required_level
    - Prerequisite quest completed (if any)
    - Quest not already completed
    - Quest not already active
    
    Returns: True if quest accepted
    Raises:
        QuestNotFoundError if quest_id not in quest_data_dict
        InsufficientLevelError if character level too low
        QuestRequirementsNotMetError if prerequisite not completed
        QuestAlreadyCompletedError if quest already done
    """
    # TODO: Implement quest acceptance
    # Check quest exists
    # Check level requirement
    # Check prerequisite (if not "NONE")
    # Check not already completed
    # Check not already active
    # Add to character['active_quests']
    pass

def complete_quest(character, quest_id, quest_data_dict):
    if quest_id not in quest_data_dict:
        raise QuestNotFoundError('Quest not found')

    quest = quest_data_dict[quest_id]
    if quest_id not in character["active_quests"]:
        raise QuestNotActiveError('Quest not active')
    else:
        character["active_quests"].remove(quest_id)
        character["completed_quests"].append(quest_id)
        reward_xp = quest["reward_xp"]
        reward_gold = quest["reward_gold"]
        character_manager.gain_experience(character, reward_xp)
        character_manager.add_gold(character, reward_gold)
        return {
            "xp": reward_xp,
            "gold": reward_gold,
            "quest_id": quest_id
        }
    """
    Complete an active quest and grant rewards
    
    Args:
        character: Character dictionary
        quest_id: Quest to complete
        quest_data_dict: Dictionary of all quest data
    
    Rewards:
    - Experience points (reward_xp)
    - Gold (reward_gold)
    
    Returns: Dictionary with reward information
    Raises:
        QuestNotFoundError if quest_id not in quest_data_dict
        QuestNotActiveError if quest not in active_quests
    """
    # TODO: Implement quest completion
    # Check quest exists
    # Check quest is active
    # Remove from active_quests
    # Add to completed_quests
    # Grant rewards (use character_manager.gain_experience and add_gold)
    # Return reward summary
    pass

def abandon_quest(character, quest_id):
    if quest_id in character["active_quests"]:
        character["active_quests"].remove(quest_id)
        return True
    else:
        raise QuestNotActiveError('Quest not active')
    """
    Remove a quest from active quests without completing it
    
    Returns: True if abandoned
    Raises: QuestNotActiveError if quest not active
    """
    # TODO: Implement quest abandonment
    pass

def get_active_quests(character, quest_data_dict):
    all_quests = []
    for quest_id in character["active_quests"]:
        all_quests[quest_id] = quest_data_dict[quest_id]
    return all_quests

    """
    Get full data for all active quests
    
    Returns: List of quest dictionaries for active quests
    """
    # TODO: Implement active quest retrieval
    # Look up each quest_id in character['active_quests']
    # Return list of full quest data dictionaries
    pass

def get_completed_quests(character, quest_data_dict):
    all_comp_quests = []
    for quest_id in character["completed_quests"]:
        all_comp_quests[quest_id] = quest_data_dict[quest_id]
    return all_comp_quests
    """
    Get full data for all completed quests
    
    Returns: List of quest dictionaries for completed quests
    """
    # TODO: Implement completed quest retrieval
    pass

def get_available_quests(character, quest_data_dict):
    available_quests = []
    for quest_id in quest_data_dict.items():
        if character["level"] >= quest_data_dict[quest_id]["required_level"] and quest_data_dict['prerequisite'] != "NONE":
            if quest_id not in character["completed_quests"] and quest_id not in character["active_quests"]:
                available_quests.append(quest_data_dict[quest_id])
    return available_quests

    """
    Get quests that character can currently accept
    
    Available = meets level req + prerequisite done + not completed + not active
    
    Returns: List of quest dictionaries
    """
    # TODO: Implement available quest search
    # Filter all quests by requirements
    pass

# ============================================================================
# QUEST TRACKING
# ============================================================================

def is_quest_completed(character, quest_id):
    if quest_id not in character["completed_quests"]:
        return True
    else:
        return False
    """
    Check if a specific quest has been completed
    
    Returns: True if completed, False otherwise
    """
    # TODO: Implement completion check
    pass

def is_quest_active(character, quest_id):
    if quest_id in character["active_quests"]:
        return True
    else:
        return False
    """
    Check if a specific quest is currently active
    
    Returns: True if active, False otherwise
    """
    # TODO: Implement active check
    pass

def can_accept_quest(character, quest_id, quest_data_dict):
    if quest_id not in character["completed_quests"] and quest_data_dict['prerequisite'] != "NONE":
        return True

    """
    Check if character meets all requirements to accept quest
    
    Returns: True if can accept, False otherwise
    Does NOT raise exceptions - just returns boolean
    """
    # TODO: Implement requirement checking
    # Check all requirements without raising exceptions
    pass

def get_quest_prerequisite_chain(quest_id, quest_data_dict):
    prerequisite_chain = []
    for quest_id in quest_data_dict.items():
        prerequisite_chain.append(quest_data_dict['prerequisite'][quest_id])
    else:
        raise QuestNotFoundError('Quest not found')
    """
    Get the full chain of prerequisites for a quest
    
    Returns: List of quest IDs in order [earliest_prereq, ..., quest_id]
    Example: If Quest C requires Quest B, which requires Quest A:
             Returns ["quest_a", "quest_b", "quest_c"]
    
    Raises: QuestNotFoundError if quest doesn't exist
    """
    # TODO: Implement prerequisite chain tracing
    # Follow prerequisite links backwards
    # Build list in reverse order
    pass

# ============================================================================
# QUEST STATISTICS
# ============================================================================

def get_quest_completion_percentage(character, quest_data_dict):
    total_quests = len(quest_data_dict)
    completed_quests = len(character['completed_quests'])
    percentage = (completed_quests / total_quests) * 100
    return percentage
    """
    Calculate what percentage of all quests have been completed
    
    Returns: Float between 0 and 100
    """
    # TODO: Implement percentage calculation
    # total_quests = len(quest_data_dict)
    # completed_quests = len(character['completed_quests'])
    # percentage = (completed / total) * 100
    pass

def get_total_quest_rewards_earned(character, quest_data_dict):
    total_gold = 0
    total_xp = 0
    for quest_id in character["completed_quests"]:
        total_gold += quest_data_dict['gold_reward'][quest_id]
        total_xp += quest_data_dict['xp_reward'][quest_id]
    total_reward = {'total_xp': total_xp,
                    'total_gold': total_gold}
    return total_reward
    """
    Calculate total XP and gold earned from completed quests
    
    Returns: Dictionary with 'total_xp' and 'total_gold'
    """
    # TODO: Implement reward calculation
    # Sum up reward_xp and reward_gold for all completed quests
    pass

def get_quests_by_level(quest_data_dict, min_level, max_level):
    quests = []
    for quest_data_dict['required_level'] in range(min_level, max_level + 1):
        quests.append(quest_data_dict)
    return quests
    """
    Get all quests within a level range
    
    Returns: List of quest dictionaries
    """
    # TODO: Implement level filtering
    pass

# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def display_quest_info(quest_data):
    """
    Display formatted quest information
    
    Shows: Title, Description, Rewards, Requirements
    """
    # TODO: Implement quest display
    print(f"\n=== {quest_data['title']} ===")
    print(f"Description: {quest_data['description']}")
    print(f"Rewards: {quest_data['rewards']}")
    print(f"Required level: {quest_data['required_level']}")
    print(f"Requirements: {quest_data['prerequisite']}")
    pass

def display_quest_list(quest_list):
    for quest_data in quest_list.items():
        display_quest_info(quest_data)
    """
    Display a list of quests in summary format
    
    Shows: Title, Required Level, Rewards
    """
    # TODO: Implement quest list display
    pass

def display_character_quest_progress(character, quest_data_dict):
    print(len(character['active_quests']))
    print(len(character['completed_quests']))
    get_quest_completion_percentage(character, quest_data_dict)
    get_total_quest_rewards_earned(character, quest_data_dict)
    """
    Display character's quest statistics and progress
    
    Shows:
    - Active quests count
    - Completed quests count
    - Completion percentage
    - Total rewards earned
    """
    # TODO: Implement progress display
    pass

# ============================================================================
# VALIDATION
# ============================================================================

def validate_quest_prerequisites(quest_data_dict):
    for quest_data in quest_data_dict.items():
        prerequisite = quest_data["prerequisite"]
        if prerequisite == "NONE":
            continue
        if prerequisite not in quest_data_dict:
            raise QuestNotFoundError('Quest prerequisite not found')

    return True
    """
    Validate that all quest prerequisites exist
    
    Checks that every prerequisite (that's not "NONE") refers to a real quest
    
    Returns: True if all valid
    Raises: QuestNotFoundError if invalid prerequisite found
    """
    # TODO: Implement prerequisite validation
    # Check each quest's prerequisite
    # Ensure prerequisite exists in quest_data_dict
    pass


# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== QUEST HANDLER TEST ===")
    
     #Test data
    test_char = {
         'level': 1,
         'active_quests': [],
         'completed_quests': [],
         'experience': 0,
         'gold': 100
     }

    test_quests = {
         'first_quest': {
             'quest_id': 'first_quest',
             'title': 'First Steps',
             'description': 'Complete your first quest',
             'reward_xp': 50,
             'reward_gold': 25,
             'required_level': 1,
             'prerequisite': 'NONE'
         }
     }

    try:
         accept_quest(test_char, 'first_quest', test_quests)
         print("Quest accepted!")
    except QuestRequirementsNotMetError as e:
         print(f"Cannot accept: {e}")

