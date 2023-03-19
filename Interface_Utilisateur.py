####Interface Utilisateur pour la prévision des prix des maisons.
###Lancement du modèle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Chargement des données d'apprentissage train.csv
train_data = pd.read_csv('train.csv')

#Recupération des donnnées regroupées dans notre traitement avant de lancer le modèle 
#Total des salles de bains
train_data['allbath'] = train_data['BsmtFullBath'] + (train_data['BsmtHalfBath']/2) + train_data['FullBath'] + (train_data['HalfBath']/2)
#Ancienneté de la maison : date de vente-date de rénovation
train_data['Anciennete'] = train_data['YrSold'] - train_data['YearRemodAdd']
#Conversion de la superficie en m²
train_data['SurfaceHabitable'] = train_data['GrLivArea']/(10.764)

# Sélection des variables pertinentes pour la prédiction du prix des maisons (en fonction des stats desc effectuées)
features = ['OverallQual', 'SurfaceHabitable','Anciennete' ,'BedroomAbvGr', 'allbath', 'GarageCars','Fireplaces']
train_data = train_data[features + ['SalePrice']]

# Prétraitement des données en encodant les variables catégorielles et en remplaçant les valeurs manquantes

train_data = train_data.fillna(train_data.mean())

# Séparer les données en variables X et variable cible y (SalePrice)
X = train_data.drop('SalePrice', axis=1)
y = train_data['SalePrice']

# Creation du modèle RandomForest
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Split des données du modèle sur les données d'entraînement
model.fit(X, y)

#  le modèle est enregisté sous format pickle et sera utilisé pour notre interface ci-dessous
joblib.dump(model, 'house_price_model.pkl')


###Création de l'interface
import tkinter as tk
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from PIL import Image, ImageTk

# Chargement du modèle entraîné (enregistré précédemment)
model = RandomForestRegressor()
model = joblib.load("house_price_model.pkl")

# Définition l'interface graphique utilisateur
root = tk.Tk()
root.geometry('800x600')
root.title("House Price Predictor")


# Créer le titre
title_label = tk.Label(root, text='Estimation du prix de vente des maisons', font=('Arial', 24, 'bold'))
title_label.pack(side='top', pady=20)

# Description de l'interface
presentation_text = """Cette application basée sur le modèle Random Forest vous permet de prédire le prix d'une maison en fonction de plusieurs caractéristiques telles que la note de la maison, la superficie de la maison et le nombre de pièces.
Pour faire une prédiction, remplissez simplement le formulaire ci-dessous et cliquez sur le bouton "Prédire le prix". #Groupe 7
"""
presentation_label = tk.Label(root, text=presentation_text, font=('Arial', 10))
presentation_label.pack(side='top', padx=20, pady=10)

# création des étiquettes et des champs d'entrée pour chaque variable retenue
label_1 = tk.Label(root, text="Note globale de la Maison (0 à 10) :")
entry_1 = tk.Entry(root)

label_2 = tk.Label(root, text="Superficie de la maison (en m²) :")
entry_2 = tk.Entry(root)

label_3 = tk.Label(root, text="Ancienneté depuis la dernière date de rénovation (en années) :")
entry_3 = tk.Entry(root)


label_4 = tk.Label(root, text="Nombre de chambres :")
entry_4 = tk.Entry(root)

label_5 = tk.Label(root, text="Nombre de salles de bains complètes :")
entry_5 = tk.Entry(root)


label_6 = tk.Label(root, text="Nombre de voitures pouvant rentrer dans le garage :")
entry_6 = tk.Entry(root)

label_7 = tk.Label(root, text="Nombre de cheminées dans la maison :")
entry_7 = tk.Entry(root)


label_1.pack()
entry_1.pack()

label_2.pack()
entry_2.pack()

label_3.pack()
entry_3.pack()

label_4.pack()
entry_4.pack()

label_5.pack()
entry_5.pack()


label_6.pack()
entry_6.pack()

label_7.pack()
entry_7.pack()

# Chargement des images
#SIAD
image1 = Image.open('siad.jpg')
image1 = image1.resize((100, 100)) 
photo1 = ImageTk.PhotoImage(image1)




label = tk.Label(root, image=photo1)
label.pack(side='top', anchor='ne') # position : nord est 

#HOUSE
image2 = Image.open('house.jpg')
image2 = image2.resize((200, 200)) # dimensionn de l'image
photo2 = ImageTk.PhotoImage(image2)


label = tk.Label(root, image=photo2)
label.pack(side='top', anchor='nw') # position nord ouest


# fonction de prédiction
def predict_price():
    # recupération des données et les lier directement avec les variables
    data = {'OverallQual': [int(entry_1.get())],
            'SurfaceHabitable': [int(entry_2.get())],
            'Anciennete': [int(entry_3.get())],
            'BedroomAbvGr': [int(entry_4.get())],
            'allbath': [int(entry_5.get())],
            'GarageCars': [int(entry_6.get())],
            'Fireplaces': [int(entry_7.get())]}

    
    # les données seront dsous format d'un dataframe
    df = pd.DataFrame(data)
    
 
    # lancement du modèle pour prédire le prix de la maison
    prix = model.predict(df)
    
    # Affichage de la prédiction dans une boîte de dialogue
    tk.messagebox.showinfo("House Price Prediction", "Le prix de la maison estimé est : " + str(round(prix[0], 2)) + "$")
    
#  bouton pour soumettre les données et exécuter la fonction de prédiction
submit_button = tk.Button(root, text="Prédire le prix", command=predict_price)
#submit_button.pack(side='bottom', pady=20)
submit_button.place(x=630, y=550, width=100, height=40)

# Main
#root.configure(bg='gray')
root.mainloop()
