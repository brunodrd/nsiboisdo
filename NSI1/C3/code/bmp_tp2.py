"""TP « Lire une image octet par octet », séance 2.

Le fichier logo.bmp doit être dans le même dossier que ce programme.
Exécutez le fichier pour lancer les tests : décommentez chaque ligne
du bloc final quand la fonction correspondante est écrite.
"""


def entier_petit_boutiste(donnees: bytes, debut: int, nb_octets: int) -> int:
    """Renvoie l'entier naturel écrit en petit-boutiste dans les nb_octets
    octets de donnees qui commencent à la position debut.

    Précondition : ces octets se trouvent dans donnees.
    >>> entier_petit_boutiste(bytes([0x3A, 0x6D, 0x1C, 0x00]), 0, 4)
    1862970
    """
    # 1. Vérifier la précondition avec assert
    # 2. L'octet situé à la position debut + i a pour poids 256 ** i
    # À COMPLÉTER
    ...


def informations(nom_fichier: str) -> tuple:
    """Renvoie le triplet (largeur, hauteur, bits par pixel)
    de l'image BMP nom_fichier."""
    donnees = open(nom_fichier, "rb").read()
    assert donnees[0:2] == b"BM", "ce n'est pas un fichier BMP"
    # À COMPLÉTER avec entier_petit_boutiste et le tableau de l'en-tête
    ...


def negatif(nom_source: str, nom_resultat: str) -> None:
    """Écrit dans nom_resultat le négatif de l'image BMP nom_source."""
    donnees = bytearray(open(nom_source, "rb").read())
    # À COMPLÉTER : remplacer chaque octet v des pixels par 255 - v
    open(nom_resultat, "wb").write(donnees)


# ============================================================ Tests
def test_entier_petit_boutiste():
    assert entier_petit_boutiste(bytes([0x3A, 0x6D, 0x1C, 0x00]), 0, 4) == 1862970
    # À COMPLÉTER : ajouter au moins deux tests


def test_informations():
    largeur, hauteur, bits = informations("logo.bmp")
    # À COMPLÉTER : vérifier les valeurs trouvées en section 1,
    # puis la relation taille = début des pixels + largeur × hauteur × 3


if __name__ == "__main__":
    test_entier_petit_boutiste()
    print("entier_petit_boutiste : OK")
    # test_informations(); print("informations : OK")
    # negatif("logo.bmp", "logo_negatif.bmp")
