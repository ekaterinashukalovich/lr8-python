import unittest
from models.author import Author
from models.user import User
from models.user_currency import UserCurrency
from models.currency import Currency


class TestModels(unittest.TestCase):

    def test_author_getters_setters(self):
        a = Author("Ekaterina", "P3121")
        self.assertEqual(a.name, "Ekaterina")
        self.assertEqual(a.group, "P3121")

        a.name = "Anna"
        a.group = "T1101"
        self.assertEqual(a.name, "Anna")
        self.assertEqual(a.group, "T1101")

    def test_author_invalid_name(self):
        with self.assertRaises(ValueError):
            Author("", "P3121")

    def test_user_getters_setters(self):
        u = User(1, "Алиса")
        self.assertEqual(u.id, 1)
        self.assertEqual(u.name, "Алиса")

        u.name = "Елизавета"
        self.assertEqual(u.name, "Елизавета")

    def test_user_invalid_id(self):
        with self.assertRaises(ValueError):
            User(-1, "Test")

    def test_user_currency_basic(self):
        uc = UserCurrency(1, "R01235")
        self.assertEqual(uc.user_id, 1)
        self.assertEqual(uc.currency_id, "R01235")

    def test_user_currency_invalid(self):
        with self.assertRaises(ValueError):
            UserCurrency("abc", 123)

    def test_currency_model(self):
        c = Currency("R01235", "840", "USD", "Доллар США", 92.45, 1)
        self.assertEqual(c.currency_id, "R01235")
        self.assertEqual(c.num_code, "840")
        self.assertEqual(c.char_code, "USD")
        self.assertEqual(c.name, "Доллар США")
        self.assertEqual(c.value, 92.45)
        self.assertEqual(c.nominal, 1)
