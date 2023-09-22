import random

# Define a list of story templates with placeholders for words
story_templates = [
    "Once upon a time in a {place}, there lived a {adjective} {noun}.",
    "On a {adjective} {day_of_week} morning, {name} decided to {verb} to the {place}.",
    "In a {adjective} land, there was a brave {noun} who wanted to {verb} the {noun2}."
]

# Function to prompt the player for words and generate the Mad Libs story
def madlibs_game():
    # Choose a random story template
    story_template = random.choice(story_templates)

    # Create a dictionary to store the user's input
    user_input = {}

    # Loop through the template and prompt the user for words
    for word_type in ["place", "adjective", "noun", "day_of_week", "name", "verb", "noun2"]:
        user_input[word_type] = input(f"Enter a {word_type}: ")

    # Generate the Mad Libs story by replacing placeholders with user input
    madlibs_story = story_template.format(**user_input)

    # Display the completed story
    print("\nYour Mad Libs Story:\n")
    print(madlibs_story)

# Start the game
if __name__ == "__main__":
    print("Welcome to the Mad Libs game!\n")
    madlibs_game()
