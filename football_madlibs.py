# Football Mad Libs Game in Python

def football_mad_libs():
    # Prompt the user for inputs related to football
    team_name = input("Enter the name of your favorite football team: ")
    player_name = input("Enter the name of your favorite football player: ")
    position = input("Enter your favorite football position: ")
    dream = input("Describe your football dream: ")

    # Generate the Football Mad Libs story using user inputs
    madlib = f"You are a die-hard fan of {team_name}, and your favorite player is {player_name}. You dream of playing as a {position} for {team_name} someday. Your ultimate football dream is to {dream}."

    # Display the Football Mad Libs story
    print("\nFootball Mad Libs Story:")
    print(madlib)

if __name__ == "__main__":
    print("Welcome to Football Mad Libs!\n")
    football_mad_libs()
