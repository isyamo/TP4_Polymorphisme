import unittest
from paiements import CarteBancaire, PayPal, Crypto


class TestPaiements(unittest.TestCase):
    def test_carte_bancaire(self):
        p = CarteBancaire(100, "123455", "123")
        msg = p.payer()
        self.assertIn("CarteBancaire", msg)
        self.assertIn("100.00", msg)

    def test_paypal(self):
        p = PayPal(30, "amina@mail.com", "tok1")
        msg = p.payer()
        self.assertIn("PayPal", msg)
        self.assertIn("30.00", msg)

    def test_crypto(self):
        p = Crypto(200, "wallet_A", "btc")
        msg = p.payer()
        self.assertIn("Crypto", msg)
        self.assertIn("200.00", msg)

    def test_montant_negatif(self):
        with self.assertRaises(ValueError):
            PayPal(-5, "amina@mail.com", "tok1")


if __name__ == "__main__":
    unittest.main()