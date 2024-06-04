2. Automatisez la création et le push d'images de conteneur à l'aide des actions GitHub
obligatoir

Voici les étapes pour créer un référentiel GitHub, ajouter un Dockerfile et configurer un workflow GitHub Actions pour automatiser la construction et le push d'une image Docker vers le registre de conteneurs GitHub.

Guide étape par étape
1. Créer un référentiel GitHub
Créer un nouveau référentiel :

Allez sur GitHub et créez un nouveau référentiel en cliquant sur l'icône "+" et en sélectionnant "Nouveau référentiel".
Nommez votre référentiel (par exemple, docker-image-repo).
Ajoutez éventuellement une description et choisissez la visibilité (public ou privé).
Initialisez le référentiel avec un README (optionnel).
Cliquez sur "Créer un référentiel".

2_Cloner le référentiel sur votre machine locale :
https://github.com/seliisyl/docker-image-repo.gite

3-Ajouter votre Dockerfile au référentiel :
Créez un fichier Dockerfile à la racine de votre référentiel.
echo 'FROM ubuntu:latest' > Dockerfile
echo 'RUN apt-get update && apt-get install -y nginx' >> Dockerfile
echo 'CMD ["nginx", "-g", "daemon off;"]' >> Dockerfile

4-Poussez le Dockerfile sur GitHub :
git add Dockerfile
git commit -m "Ajouter Dockerfile"
git push origin main

2. Configuration du workflow GitHub Actions
Créer le fichier de workflow GitHub Actions :

Créez les répertoires .github/workflows dans votre référentiel.
Créez un fichier nommé docker-image.yml à l'intérieur de .github/workflows.
Définissez le workflow dans docker-image.yml :

name: CI pour l'image Docker

on:
  push:
    branches:
      - main

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
    - name: Récupérer le référentiel
      uses: actions/checkout@v2

    - name: Configurer Docker Buildx
      uses: docker/setup-buildx-action@v1

    - name: Se connecter au registre de conteneurs GitHub
      uses: docker/login-action@v2
      with:
        registry: ghcr.io
        username: ${{ github.actor }}
        password: ${{ secrets.CR_PAT }}

    - name: Construire et pousser l'image Docker
      uses: docker/build-push-action@v3
      with:
        context: .
        push: true
        tags: ghcr.io/${{ github.repository_owner }}/docker-image-repo:latest


Configuration des secrets GitHub pour l'authentification :

Accédez à votre référentiel GitHub, cliquez sur Paramètres > Secrets > Actions.
Cliquez sur Nouveau secret de référentiel et créez un secret nommé CR_PAT.
Générez un jeton d'accès personnel avec les scopes write:packages, read:packages, et delete:packages (si nécessaire) et collez-le dans le champ Value.
Enregistrez le secret.
3. Tester le workflow
Poussez une modification pour déclencher le workflow :

Apportez une petite modification au référentiel, par exemple, modifiez le README ou le Dockerfile.

echo "Test CI workflow" >> README.md
git add README.md
git commit -m "Test CI workflow"
git push origin main

Vérifiez le workflow :

Accédez à l'onglet Actions de votre référentiel pour voir le workflow s'exécuter.
Assurez-vous que l'image Docker est construite et poussée vers le registre de conteneurs GitHub.

Dockerfile:
# Utiliser l'image de base Ubuntu
FROM ubuntu:latest

# Mettre à jour les packages et installer Nginx
RUN apt-get update && apt-get install -y nginx

# Exposer le port 80
EXPOSE 80

# Commande pour lancer Nginx
CMD ["nginx", "-g", "daemon off;"]

Explication des instructions
FROM ubuntu:latest : Utilise l'image officielle d'Ubuntu comme image de base.
RUN apt-get update && apt-get install -y nginx : Met à jour les packages disponibles et installe Nginx.
EXPOSE 80 : Indique que le conteneur écoute sur le port 80.
CMD ["nginx", "-g", "daemon off;"] : Spécifie la commande à exécuter lorsque le conteneur démarre, ici, Nginx est démarré en mode de premier plan.
