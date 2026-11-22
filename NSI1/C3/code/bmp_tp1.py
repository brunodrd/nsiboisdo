"""TP « Lire une image octet par octet », séance 1.

Le fichier logo.bmp doit être dans le même dossier que ce programme.
Il suffit d'exécuter ce fichier : rien n'est à compléter.
"""


def compter_couleurs(nom_fichier: str) -> int:
    """Renvoie le nombre de couleurs différentes d'une image BMP
    à 24 bits par pixel, sans remplissage en fin de ligne."""
    donnees = open(nom_fichier, "rb").read()
    debut = donnees[10]          # position du premier octet des pixels
    couleurs = []
    for i in range(debut, len(donnees), 3):
        pixel = donnees[i:i + 3]
        if pixel not in couleurs:
            couleurs.append(pixel)
    return len(couleurs)


if __name__ == "__main__":
    print("nombre de couleurs :", compter_couleurs("logo.bmp"))
