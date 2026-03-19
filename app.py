import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Mon pokedex", page_icon="https://img.icons8.com/color/48/red-team--v1.png")
st.title("Mon Pokedex")

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
            st.write("Type : " + ", ".join(types))
            # st.write(", ".join(types))
        
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