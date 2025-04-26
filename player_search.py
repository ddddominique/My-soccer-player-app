import requests

def real_func():
    def get_player_info(name):
        url = "https://free-api-live-football-data.p.rapidapi.com/football-players-search"

        querystring = {"search":name}

        headers = {
            "x-rapidapi-key": "APIKEY",
            "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        

        if response.status_code == 200:
            player_data = response.json()
            return player_data
        else:
            print(f"did not get it, we get {response.status_code}")

    def get_player_details(id):
        url = "https://free-api-live-football-data.p.rapidapi.com/football-get-player-detail"
        
        querystring = {"playerid":id}

        headers = {
        "x-rapidapi-key": "APIKEY",
        "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
        }

        response_details = requests.get(url, headers=headers, params=querystring)

        if response_details.status_code == 200:
            player_details = response_details.json()
            return player_details
        


    name = input("Enter a player's name: ")
    player_info = get_player_info(name)



    if player_info:
        first_player = player_info["response"]["suggestions"][0]
        player_id = first_player["id"]
        more_info = get_player_details(player_id)
        actual_details = more_info["response"]["detail"]
        print(f"Name: {first_player["name"]}")
        print(f"Club: {first_player["teamName"]}")
        print(f"Height: {actual_details[0]["value"]["fallback"]}")
        print(f"Age: {actual_details[2]["value"]["numberValue"]}")
        print(f"Preferred foot: {actual_details[3]["value"]["fallback"]}")
        print(f"Country: {actual_details[4]["value"]["fallback"]}")
        print(f"Market Value: {actual_details[5]["value"]["fallback"]}")






