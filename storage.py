import pickle
import os


def recover_file_data() -> list:
    """Récupère les données dans le fichier ("register.txt")"""
    # type and assign
    file = open("register.txt", "rb")
    file_size = os.path.getsize("register.txt")
    list_file: list
    # vérifie s'il y a des données dans le dossier "register.txt" et sinon il renvoie une liste vide
    if file_size != 0:
        list_file = pickle.load(file)
        file.close()
        return list_file
    else:
        file.close()
        return []


def record_file_data(list_user: list) -> None:
    """Enregistre la liste dans le fichier ("register.txt")"""
    # enregistre les données
    file = open("register.txt", "wb")
    pickle.dump(list_user, file)
    file.close()
