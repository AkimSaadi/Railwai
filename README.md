# Exercice

Ceci est un projet de test pour évaluer vos compétences en traitement de données avec Python, et voir comment vous organisez votre code.

### Description du problème

Sur le réseau ferroviaire, une série de mesures a été effectuée le long d'une voie, et les valeurs ont été stockées dans un fichier .csv. Chaque point de mesure est identifié par un identifiant unique (SSCOUNT) et une position GPS (longitude / latitude).

4 mesures sont effectuées, une par composant mesuré, dénotés A, B, C et D. Ils sont mesurés pour détecter un défaut sur l'un ou plusieurs d'entre eux, ce qui peut causer un problème pour le traffic.

A chaque point de mesure, il y a un seuil spécifique que les mesures ne doivent pas dépasser. Si la mesure d'un composant dépasse ce seuil, il est en défaut. 

L'objectif est de récupérer les données de mesure, les comparer au seuil, et produire un nouveau .csv avec 4 colonnes "DEFECT_A", "DEFECT_B", "DEFECT_C", "DEFECT_D" remplies avec 1 s'il y a un défaut sur la mesure associée, 0 sinon.

### Cahier des charges

* L'utilisateur peut déposer un ou plusieurs fichiers .csv à traiter dans /data/, ils sont tous nommés par la date d'enregistrement des mesures. Exemple : "2023-01-23.csv".
* Le programme doit récupérer les données de chaque fichier de /data/ conforme (format de nom correct), les traiter pour remplir les colonnes de défauts et enregistrer le résultat dans un fichier du même nom dans /result/.
* Le programme ne doit pas retraiter un fichier déjà traité s'il est relancé. C'est à dire que si le fichier de /data/ a le même nom qu'un fichier dans /result/, on ne le traite pas.

### Instructions d'exécution du code

Pour créer et activer un environnement virtuel il faut :
* Ouvrir l'invite de commande,
* se rendre dans le répertoire où l'on souhaite créer l'environnement virtuel avec la commande "cd" (change directory),
* taper la commande "python -m venv nom_de_environnement",
* taper la commande "cd nom_de_environnement\Scripts" puis "activate.bat" pour activer l'environnement.

Pour installer les modules nécessaires à l'exécution du fichier main, il faut taper la commande "pip install -r src/requirements.txt".
Pour exécuter le fichier main, il faut taper la commande "python src/main.py".
Pour désactiver l'environnement, il faut taper la commande "deactivate".