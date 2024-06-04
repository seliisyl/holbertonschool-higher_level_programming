# Utiliser l'image de base Alpine
FROM alpine:latest

# Installer le paquet curl
RUN apk add --no-cache curl

# Copier le fichier de configuration dans l'image
COPY config.txt /app/config.txt

# Spécifier la commande par défaut
CMD ["cat", "/app/config.txt"]
