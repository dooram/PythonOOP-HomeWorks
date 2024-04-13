    import requests

    def get_pokemon_info(pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        response = requests.get(url)

        if response.status_code == 200:
            pokemon = response.json()
            print(f"Name: {pokemon['name'].capitalize()}")
            print(f"ID: {pokemon['id']}")
            print("Abilities:")
            for ability in pokemon['abilities']:
                print(f"  - {ability['ability']['name'].capitalize()}")
            print("Types:")
            for type in pokemon['types']:
                print(f"  - {type['type']['name'].capitalize()}")
        else:
            print(f"Pokemon {pokemon_name.capitalize()} not found")

    get_pokemon_info(str(input("Print pokemon name: ")))