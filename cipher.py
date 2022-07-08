

def next_letter(letter_pos: int, cipher_letter_pos: int, last_letter_pos: int, first_letter_pos: int) -> str:
    next_letter_number = letter_pos + cipher_letter_pos - first_letter_pos
    if next_letter_number > last_letter_pos:
        next_letter_number = first_letter_pos + next_letter_number - last_letter_pos
    return chr(next_letter_number)


def next_letter_letter(letter: str, cipher_letter: str, last_letter_pos: int, first_letter_pos: int) -> str:
    next_letter_number = ord(letter) + ord(cipher_letter) - first_letter_pos
    if next_letter_number > last_letter_pos:
        next_letter_number = first_letter_pos + next_letter_number - last_letter_pos
    return chr(next_letter_number)


def prev_letter_letter(letter: str, cipher_letter: str, last_letter_pos: int, first_letter_pos: int) -> str:
    prev_letter_number = ord(letter) + first_letter_pos - ord(cipher_letter)
    if prev_letter_number < first_letter_pos:
        prev_letter_number = last_letter_pos + prev_letter_number - first_letter_pos
    return chr(prev_letter_number)


def encrypt(key: str, plain_text: str) -> str:
    first_letter_pos = ord("a")
    last_letter_pos = ord("z")
    cipher_text_arr = []
    for i, letter in enumerate(plain_text):
        shift = i % key_length
        # cipher_text_arr.append(chr(ord(letter) + ord(key[shift])))
        cipher_text_arr.append(next_letter_letter(letter, key[shift], last_letter_pos, first_letter_pos))
    return "".join(cipher_text_arr)


def decrypt(key: str, cipher_text: str) -> str:
    first_letter_pos = ord("a")
    last_letter_pos = ord("z")
    plain_text_arr = []
    for i, letter in enumerate(cipher_text):
        shift = i % key_length
        # cipher_text_arr.append(chr(ord(letter) + ord(key[shift])))
        plain_text_arr.append(prev_letter_letter(letter, key[shift], last_letter_pos, first_letter_pos))
    return "".join(plain_text_arr)


if __name__ == "__main__":
    key = "test"
    key_length = len(key)
    plain_text = "HelloWorld".lower()
    cipher_text = encrypt(key, plain_text)
    print(f'Plain: {plain_text} Cipher Text: {cipher_text}')
    print(f'Cipher: {cipher_text} Plain Text: {decrypt(key, cipher_text)}')



