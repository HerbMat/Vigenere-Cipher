from unittest import TestCase
from encryptors import VigenereCipher


class TestVigenereCipher(TestCase):
    def setUp(self) -> None:
        self.vigenere_cipher = VigenereCipher()

    def test_encrypt(self):
        cipher_text = self.vigenere_cipher.encrypt("test", "helloworld")
        assert cipher_text == "biefibhlfh"

    def test_decrypt(self):
        plain_text = self.vigenere_cipher.decrypt("test", "biefibhlfh")
        assert plain_text == "helloworld"
