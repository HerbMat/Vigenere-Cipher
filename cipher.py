from encryptors import VigenereCipher

if __name__ == "__main__":
    vigenereCipher = VigenereCipher()
    key = "test"
    plain_text = "helloworld"
    cipher_text = vigenereCipher.encrypt(key, plain_text)
    decrypted_text = vigenereCipher.decrypt(key, cipher_text)
    print(f"Key = {key}, Text = {plain_text}, Cipher = {cipher_text}, Decrypted = {decrypted_text}")



