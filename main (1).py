import json


def load_player_data():
    with open('basketball_players.json', 'r') as file:
        data = json.load(file)
    return data


def basketball_chatbot():
    print("Welcome to the Basketball Players Chatbot! ")
    print("Ask me about your favorite basketball players only good ones.")

    player_data = load_player_data()

    while True:
        user_input = input("Kanye West: ").lower()

        if user_input == 'exit':
            print("Kanye West: Goodbye loser!")
            break
        elif 'hello' in user_input:
            print("Kanye West: Hello there! Ask me about basketball players.")
        else:
            response = get_player_info(user_input, player_data)
            print("Kanye West:", response)

def get_player_info(player_name, data):
 
    player_name_lower = player_name.lower()

    matching_players = [player for player in data.keys() if player_name_lower in   
    player.lower()]

    if matching_players:
      
        return f"{matching_players[0]}: {data[matching_players[0]]}"
    else:
        return f"Sorry, I don't have information about {player_name}."

if __name__ == "__main__":
    basketball_chatbot()
