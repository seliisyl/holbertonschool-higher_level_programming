# Utiliser l'image de base Ubuntu
FROM ubuntu:latest

# Mettre à jour les packages et installer Nginx
RUN apt-get update && apt-get install -y nginx

# Exposer le port 80
EXPOSE 80

# Définir le volume pour persister les données
VOLUME /data

# Commande pour lancer Nginx
CMD ["nginx", "-g", "daemon off;"]
