import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u=User(password='123')
        self.assertTrue(u.password_hash is not None)

    def test_password_verification(self):
        u=User(password='123')
        self.assertTrue(u.verify_password('123'))
        self.assertFalse(u.verify_password('321'))

    def test_password_salts_are_random(self):
        u=User('123')
        u2=User('123')
        self.assertTrue(u.password_hash!=u2.password_hash)