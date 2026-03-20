import streamlit as st
import requests
import pandas as pd

# Dico images types pokemon
type_badges = {
    "fire": "https://img.icons8.com/color/48/fire-element.png",
    "water": "https://img.icons8.com/color/48/water-element.png",
    "grass": "https://img.icons8.com/color/48/grass.png",
    "electric": "https://img.icons8.com/color/48/lightning-bolt.png",
    "psychic": "https://img.icons8.com/color/48/brain.png",
    "ice": "https://img.icons8.com/color/48/snowflake.png",
    "dragon": "https://img.icons8.com/color/48/dragon.png",
    "dark": "https://img.icons8.com/color/48/moon-symbol.png",
    "fairy": "https://img.icons8.com/color/48/fairy.png",
    "normal": "https://img.icons8.com/color/48/circle.png",
    "fighting": "https://img.icons8.com/color/48/boxing.png",
    "flying": "https://img.icons8.com/color/48/bird.png",
    "poison": "https://img.icons8.com/color/48/poison.png",
    "ground": "https://img.icons8.com/color/48/mountain.png",
    "rock": "https://img.icons8.com/color/48/rock.png",
    "bug": "https://img.icons8.com/color/48/bug.png",
    "ghost": "https://img.icons8.com/color/48/ghost.png",
    "steel": "https://img.icons8.com/color/48/metal.png"
}

st.set_page_config(page_title="Mon pokedex", page_icon="https://img.icons8.com/color/48/red-team--v1.png")
st.title("Mon Pokedex :)")

# Choisir un pokemon
pokemon_name = st.text_input("Entrez le nom d'un pokemon")

if pokemon_name :

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200 :

        data = response.json()

        col_1, col_2 = st.columns([2, 1])

        with col_1 :

            st.subheader("Name : " + data["name"].capitalize())
            types = [type["type"]["name"].capitalize() for type in data["types"]]
            #st.write("Type : " + ", ".join(types))

            st.write("Type :")
            cols = st.columns(len(data["types"]))

            for i, type_info in enumerate(data["types"]):
                type_name = type_info["type"]["name"]

                with cols[i] :
                    st.image(type_badges[type_name], width=50)
                    st.caption(type_name.capitalize())
        
        with col_2 : 

            # Image
            st.image(data["sprites"]["front_default"], use_container_width=True)

        st.write("---")

        st.write("### Talents")
        for talent in data["abilities"] :

            #print(talent)
            st.write(f"Talent : {talent["ability"]["name"]}")

        st.write("---")

        # Stats
        st.write("### Stats")

        for stat in data["stats"]:

            st.write(f"{stat["stat"]["name"].capitalize()} : {stat["base_stat"]}")

        st.write("---")
        
        # Attaques
        moves_data = []

        for move in data["moves"]:

            moves_data.append({
                "Attaque" : move["move"]["name"],
                "Méthode": move["version_group_details"][0]["move_learn_method"]["name"],
                "Niveau": move["version_group_details"][0]["level_learned_at"]
            })
        df_moves = pd.DataFrame(moves_data)

        st.subheader("Attaques")
        st.dataframe(df_moves)
        
    
    else :

        st.error("pokemon non trouvé")