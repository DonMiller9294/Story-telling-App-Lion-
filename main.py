import random

# Define the story scenes and choices
story = {
    "start": {
        "text": "You find yourself in a desert. Do you go left or right?",
        "choices": ["left", "right"]
    },
    "left": {
        "text": "You stumble upon a river Do you drink from it or continue?",
        "choices": ["drink", "continue"]
    },
    "drink": {
        "text": "The water tastes sweet and refreshing. You feel revitalized. You win!",
        "choices": []
    },
    "continue": {
        "text": "You keep walking and eventually get lost in the forest. Game over.",
        "choices": []
    },
    "right": {
        "text": "You encounter a fierce Lion. Do you fight or run?",
        "choices": ["fight", "run"]
    },
    "fight": {
        "text": "You bravely engage the Lion in combat. You defeat it and claim its treasure. You win!",
        "choices": []
    },
    "run": {
        "text": "You turn and run as fast as you can, but the dragon catches up and devours you. Game over.",
        "choices": []
    }
}

# Function to play the game
def play_game():
    current_scene = "start"
    while True:
        scene = story[current_scene]
        print(scene["text"])
        if not scene["choices"]:
            break
        choice = input("Enter your choice: ").lower()
        if choice in scene["choices"]:
            current_scene = choice
        else:
            print("Invalid choice. Try again.")

# Start the game
print("Welcome to the Interactive Storytelling Game!")
play_game()
