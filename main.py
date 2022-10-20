import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt


# header = st.container()
# data_set = st.container()
# features = st.container()
# modelTraining = st.container()

# st.set_page_config(page_title="App détection billet")

# st.title("Application de détection des faux billets")

st.title('Détection de faux billets')

# 1. Read me	
st.header("Read me")
st.markdown("""<style>.streamlit-expanderHeader{font-size: 17px;}</style>
<div style="text-align: justify;">intro.</div>""", unsafe_allow_html=True)
st.write("""explication structure dataset""")
st.write("""Le notebook du modèle, les scripts FastAPI, Streamlit et Dockerfiles sont disponibles sur [GitHub](https://).""")

# 2. Dépot de fichier
st.header("Drop a file section")
file = st.file_uploader("Dans un premier temps, vous devez déposer votre fichier au format .csv")

option = st.radio("Quel type de billet souhaitez-vous visualiser ?", ("Tous les billets", "Uniquement les faux"), 1)

# 3. Analyse du fichier

# url_estimator = "https://github.com/thibautcr/p10/blob/06e4a1a72aa488f7c1b9aa407c5b8393946025e2/estimator.pkl?raw=true"
# url_scaler =  "https://github.com/thibautcr/p10/blob/06e4a1a72aa488f7c1b9aa407c5b8393946025e2/scaler.pkl?raw=true"
# estimator = pd.read_pickle(url_estimator) 
# scaler = pd.read_pickle(url_scaler) 

# estimator = st.pd.read_pickle('estimator.pkl')
# scaler = st.pd.read_pickle('scaler.pkl')

# estimator = pickle.load(open('estimator.pkl', 'rb'))
# scaler = pickle.load(open('scaler.pkl', 'rb'))

# FONCTIONNE
# estimator = open("estimator.pkl",'rb')
# scaler = open("scaler.pkl",'rb')

# estimator = pd.read_pickle(open("estimator.pkl",'rb'))
# scaler = pd.read_pickle(open("scaler.pkl",'rb'))

# estimator = pd.read_pickle(estimator) 
# scaler = pd.read_pickle(scaler) 

st.header("Analyse des billets")
st.write("""En cliquant sur le bouton "Execute" ci-dessous, notre algorithme de prédiction viendra analyser les billets contenu dans le fichier :
1. d'une part, en respectant les parametres optimaux que nous lui calculé
2. d'autre part, en réutilisant les valeurs observées dans son entrainement préalable sur les 1200 billets du jeu d'entrainement""")

# st.write(type(estimator))
# st.write(estimator)

# st.write(type(scaler)) 
# st.write(scaler)
# if st.button("Execute"):
# 	data_test = pd.read_csv(file, sep=",", decimal=".").reset_index()
# 	data_index = file.id
# 	data_test = scaler.transform(file.loc[:,file.columns != "id"])
# 	y_pred = estimator.predict(data_test)
# 	y_prob = pd.DataFrame(estimator.predict_proba(data_test).round(4))
# 	results = pd.DataFrame(index = data_index)
# 	results["Prédiction RegLog"] = y_pred
# 	results["Probabilité d'un vrai billet"] = y_prob[1].values
# 	st.dataframe(data=results)
	
	

# if st.button("Execute"):
#     try:
#         file = pd.read_csv(file, sep=",", decimal=".")
#         if file.shape[1] != 7:
#             raise Exception("Le fichier n'a pas le nombre de colonnes attendues, vérifiez l'encodage (utf8; sep = ',' ; dec = '.') ou les colonnes fournies.")
#         elif not (file.columns == ['diagonal', 'height_left', 'height_right', 'margin_low', 'margin_up','length', 'id']).all():
#             raise Exception('Les colonnes entrées ne correspondent pas au schéma ci-dessus, vérifiez le nom des colonnes')
#         elif file[["id"]].duplicated().any():
#             raise Exception('Attention il y a des doublons dans la colonne "id".')
#         file.rename(columns={"id":"ide"}, inplace=True)
#     except UnicodeDecodeError:
#         st.write('Vérifiez que votre fichier est un fichier *csv* encodé en utf-8 avec comme séparateur décimal un "." et comme séparateur de valeurs une ",".')
#     except ValueError:
#         st.write("Veuillez sélectionner un fichier existant.")
	
#     else :
	
	
	
# 4. Entrainement du modèle
st.header("""Entrainement du modèle""")
st.write("""méthodologie utlisée : pistes explorées, entrainement, optimisation, ..., résultats ,""")


st.markdown("""Thibaut Cressent""")
