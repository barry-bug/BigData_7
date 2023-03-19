# house_prices_prediction_7
Projet de Big Data M2 SIAD

Ce projet consiste de répondre à un concours Kaggle qui met au défi de prédire le prix final de chaque maison avec une base de données de 79 variables explicatuves décrivant tous les aspects des maisons.

Notre équipe est composé de : 
Paulette ZEMBOU
Imane MAHAMAD
Sekou SANGARE
Majid BARRY


Afin de répondre à cette problématique de prévision des prix des ventes de maison, la démarche générale à suivre consiste à respecter les différentes étapes ci-dessous  : 

Compréhension des données :  nous allons essayer de bien cerner la problématique ainsi que nos données. Pour ce faire, nous allons examiner chaque variable afin de comprendre leur signification et leur pertinence par rapport à ce problème. Cette étape nous permettra d’avoir une idée de notre ensemble de données. Mais, aussi des variables plausible d’influencer le prix des logements. 

Vérification de la qualité des données :  cette phase est importante dans toutes études statistiques.  Elle nous permettra de détecter les différentes données manquantes et aberrantes. Après cela, nous allons vérifier l’indépendance de nos variables. Et, penser à la possibilité d’avoir plus d’informations et une forte corrélation en créant une nouvelle variable à partir des variables existantes.  Aussi, nous procéderons à un regroupement des modalités et un encodage des variables numériques car elles ne peuvent pas être interprétées par les modèles de Machine Learning.

Mise au défi de plusieurs modèles : Ceci nous permettra d'entraîner le modèle et d’ajuster ses hyperparamètres afin d’obtenir les meilleures performances possibles. Les modèles testés sont :  la régression linéaire, le Random Forest, le Gradient Boosting et le Support Vector Machine (SVM). Nous allons rappeler le rôle et la particularité de chacun de ces modèles dans la partie modélisation. Ainsi,  il est important de comprendre les avantages et les inconvénients de chaque modèle et de les comparer pour choisir le plus performant en utilisant des métriques appropriées, telles que la RMSE (Root Mean Squared Error) ou le coefficient de détermination R².

Optimisation du modèle et prédiction : si les performances du modèle ne sont pas satisfaisantes, il est possible d'optimiser le modèle en ajoutant de nouvelles variables, en utilisant des techniques de régularisation,etc. Et, une fois le modèle entraîné et optimisé, il est possible de faire des prédictions sur de nouvelles données et de soumettre les prédictions sur Kaggle pour évaluer les performances du modèle sur un ensemble de test inconnu.

Création d’une interface :  Nous allons proposer une interface python permettant à un utilisateur (potentiellement un futur acheteur de maison) de fournir certaines informations sur une maison (qualité générale, surface habitable, nombre de chambres, année de construction et garage) et de prédire le prix de vente de cette maison en utilisant le modèle qui sera retenu. L'interface est nommé "Interface_Utilisateur", et il faut s'assurer d'avoir bien importer le fichier train.csv pour que ça fonctionne.

Création d’un outil de restitution de données (BI) : il est important d’avoir un accès facile aux données ce qui permettra aux utilisateurs d'accéder facilement aux données importantes en un seul endroit et aux décideurs de prendre des décisions rapide et efficace. Nous utiliserons l’outil Qlik Sense.
