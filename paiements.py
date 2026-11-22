from abc import ABC, abstractmethod


def carte_valide(numero):
    """Vérification simple : chiffres uniquement et somme modulo 10."""
    numero = str(numero)
    if not numero.isdigit() or len(numero) < 4:
        return False
    chiffres = [int(c) for c in numero]
    return sum(chiffres) % 10 == 0


class Paiement(ABC):
    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        self._montant = float(montant)

    @abstractmethod
    def payer(self):
        pass


class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        if not carte_valide(numero):
            raise ValueError("Numéro de carte invalide.")
        if not str(cvv).isdigit() or len(str(cvv)) not in (3, 4):
            raise ValueError("CVV invalide.")
        self._numero = str(numero)
        self._cvv = str(cvv)

    def payer(self):
        return f"CarteBancaire (****{self._numero[-4:]}) : {self._montant:.2f} payés."


class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)
        if "@" not in email:
            raise ValueError("Email invalide.")
        if not token:
            raise ValueError("Token requis.")
        self._email = email
        self._token = token

    def payer(self):
        return f"PayPal ({self._email}) : {self._montant:.2f} payés."


class Crypto(Paiement):
    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        if not wallet_id or not reseau:
            raise ValueError("Wallet ou réseau manquant.")
        self._wallet_id = wallet_id
        self._reseau = reseau.upper()

    def payer(self):
        return f"Crypto ({self._reseau}) : {self._montant:.2f} payés."


def traiter_paiements(liste):
    for p in liste:
        print(p.payer())


if __name__ == "__main__":
    paiements = [
        CarteBancaire(100, "123455", "123"),
        CarteBancaire(50, "5555", "456"),
        PayPal(30, "amina@mail.com", "tok1"),
        PayPal(75, "khalid@mail.com", "tok2"),
        Crypto(200, "wallet_A", "btc"),
        Crypto(40, "wallet_B", "eth"),
    ]

    traiter_paiements(paiements)