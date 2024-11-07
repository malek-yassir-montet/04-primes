"""Module math qui utilise sqrt pour calculer la racine carrée d'un nombre."""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """Fonction qui renvoit si un nombre est premier ou non"""

    if p in (0, 1):
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False

    return True

#### Fonction principale

def main():
    """Fonction qui affiche tous les nombres premiers entre 0 et 100"""
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
