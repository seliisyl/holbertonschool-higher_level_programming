Exercice 0
-Créer une image Docker simple basée sur Alpine qui imprime "Hello, World!" à la console

1- Savoir si Docker est installé pour vérifier en éxécute 
   Docker --version

2- Ouvrir le fichier Dockerfile avec "vi" (qui est un éditeur de texte) et ajouter ces lignes:
   # Utiliser l'image de base Alpine
   FROM alpine:latest

   # Spécifier la commande pour imprimer "Hello, World!"
   CMD ["echo", "Hello, World!"]

3- Construction de l'Image Docker exécutez la commande suivante pour construire l'image Docker :
   docker build -t hello-alpine .
Cette commande indique à Docker de construire une image à partir du Dockerfile dans le répertoire courant (.) et de la taguer avec le nom hello-alpine.


4. Exécution du Conteneur Docker
   Une fois l'image construite, exécutez un conteneur à partir de cette image en utilisant la commande suivante :

   docker run hello-alpine
Si tout est correctement configuré, vous verrez "Hello, World!" imprimé dans votre console.
Exemple:

salimata@MacBook-Air-de-Salimata docker-alpine-hello % docker --version

Docker version 26.1.1, build 4cf5afa
salimata@MacBook-Air-de-Salimata docker-alpine-hello % ls
Dockerfile
salimata@MacBook-Air-de-Salimata docker-alpine-hello % vi Dockerfile
salimata@MacBook-Air-de-Salimata docker-alpine-hello % docker build -t hello-alpine .

[+] Building 3.8s (5/5) FINISHED                                             docker:desktop-linux
 => [internal] load build definition from Dockerfile                                         0.2s
 => => transferring dockerfile: 215B                                                         0.1s
 => [internal] load metadata for docker.io/library/alpine:latest                             2.3s
 => [internal] load .dockerignore                                                            0.0s
 => => transferring context: 2B                                                              0.0s
 => [1/1] FROM docker.io/library/alpine:latest@sha256:77726ef6b57ddf65bb551896826ec38bc3e53  0.9s
 => => resolve docker.io/library/alpine:latest@sha256:77726ef6b57ddf65bb551896826ec38bc3e53  0.0s
 => => sha256:77726ef6b57ddf65bb551896826ec38bc3e53f75cdde31354fbffb4f25238 1.85kB / 1.85kB  0.0s
 => => sha256:216266c86fc4dcef5619930bd394245824c2af52fd21ba7c6fa0e618657d4c3b 528B / 528B   0.0s
 => => sha256:1d34ffeaf190be23d3de5a8de0a436676b758f48f835c3a2d4768b798c15a 1.47kB / 1.47kB  0.0s
 => => sha256:d25f557d7f31bf7acfac935859b5153da41d13c41f2b468d16f729a5b8836 3.62MB / 3.62MB  0.3s
 => => extracting sha256:d25f557d7f31bf7acfac935859b5153da41d13c41f2b468d16f729a5b883634f    0.4s
 => exporting to image                                                                       0.2s
 => => exporting layers                                                                      0.0s
 => => writing image sha256:3435e039f06b0125d83eb1dc0842eb092fd6330b2ce3e30e88f0ccfc14fbc88  0.0s
 => => naming to docker.io/library/hello-alpine                                              0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/0trsktwnuzyrgoxm3i2itlgf8

What's Next?
  1. Sign in to your Docker account → docker login
  2. View a summary of image vulnerabilities and recommendations → docker scout quickview
salimata@MacBook-Air-de-Salimata docker-alpine-hello % docker run hello-alpine

Hello, World!
Exercice 1

