#Utilisation de python3.8 comme image parente
FROM python:3.8

#On défini le répertoire de travail, ici ce sera /app
WORKDIR /app 

#On copie le répertoire courant dans le dossier /app du conteneur
COPY ./ /app

#On installe les packages du requirements.txt dans le conteneur 
RUN pip3 install -r requirements.txt 

#On éxecute l'application lors du lancement du conteneur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
