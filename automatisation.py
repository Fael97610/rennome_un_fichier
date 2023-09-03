import os

dossier = '/chemin/vers/votre/dossier'

fichier = os.listdir(dossier)

prefixe = 'test_'

for axe in fichier:
    source = os.path.join(dossier, axe)

    new_name = prefixe + axe

    destination = os.path.join(dossier, new_name)

    os.rename(source, destination)

print("Terminé")    