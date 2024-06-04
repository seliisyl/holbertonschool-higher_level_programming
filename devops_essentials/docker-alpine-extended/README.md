Exercice 1: 1. Personnalisez votre image Docker basée sur Alpine

Objectif:
Étendez l'image Docker créée dans la tâche précédente pour :

Installez le package curl.
Ajoutez un fichier de configuration nommé config.txt contenant le texte « Bienvenue dans Docker ! ».
Lorsque le conteneur Docker est exécuté, il devrait pouvoir exécuter des commandes curl. De plus, le fichier config.txt doit être accessible et contenir le texte spécifié
Voici les étapes:

1-Création du Fichier de Configuration
Créez un fichier nommé config.txt dans le répertoire du projet et ajoutez-y le texte "Welcome to Docker!":
   echo "Welcome to Docker!" > config.txt

2-Modification du Dockerfile
Créez un nouveau fichier Dockerfile ou modifiez celui existant pour inclure les instructions suivantes :
  # Utiliser l'image de base Alpine
FROM alpine:latest

# Installer le paquet curl
RUN apk add --no-cache curl

# Copier le fichier de configuration dans l'image
COPY config.txt /app/config.txt

# Spécifier la commande par défaut (facultatif)
CMD ["cat", "/app/config.txt"]


3. Construction de l'Image Docker
Construisez l'image Docker en utilisant la commande suivante :
  docker build -t extended-hello-alpine .

4-Test du Conteneur Docker
Vérification de l'Installation de Curl
Exécutez un conteneur à partir de l'image créée et testez la commande curl :
  docker run extended-hello-alpine curl https://www.google.com

Vérification du Fichier de Configuration
Confirmez l'existence et le contenu du fichier config.txt :
  docker run extended-hello-alpine cat /app/config.txt

