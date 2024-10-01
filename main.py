"""ca sert a quoi ?"""
from primes import isprime

#### Fonction principale
def main():

    """
    Retourne
    Args:
    Returns:
    """

    isprime(1)
    isprime(2)
    isprime(4)

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()

if __name__ == "__main__":
    main()
