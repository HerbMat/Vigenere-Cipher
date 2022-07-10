from typing import Callable


class VigenereCipher:
    def __init__(self):
        self._first_letter_pos = ord("a")
        self._last_letter_pos = ord("z")

    def encrypt(self, key: str, plain_text: str) -> str:
        return self._calculate_substitution_letter(key, plain_text, self._next_cipher_letter)

    def decrypt(self, key: str, cipher_text: str) -> str:
        return self._calculate_substitution_letter(key, cipher_text, self._next_plain_text_letter)

    def _next_cipher_letter(self, plain_text_letter, key_letter):
        shift = self._calculate_shift(key_letter)
        cipher_letter_pos = ord(plain_text_letter) + shift
        if cipher_letter_pos > self._last_letter_pos:
            cipher_letter_pos = self._first_letter_pos + cipher_letter_pos - self._last_letter_pos
        return chr(cipher_letter_pos)

    def _next_plain_text_letter(self, plain_text_letter, key_letter):
        shift = self._calculate_shift(key_letter)
        cipher_letter_pos = ord(plain_text_letter) - shift
        if cipher_letter_pos < self._first_letter_pos:
            cipher_letter_pos = self._last_letter_pos + cipher_letter_pos - self._first_letter_pos
        return chr(cipher_letter_pos)

    def _calculate_shift(self, key_letter: str) -> int:
        return ord(key_letter) - self._first_letter_pos

    def _calculate_substitution_letter(self, key: str, text: str, substitute: Callable[[str, str], str]) -> str:
        key_length = len(key)
        text_arr = []
        for i, text_letter in enumerate(text):
            key_letter = key[i % key_length]
            text_arr.append(substitute(text_letter, key_letter))
        return "".join(text_arr)
