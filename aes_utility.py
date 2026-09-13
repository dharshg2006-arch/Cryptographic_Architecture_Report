import os
from crypto.cipher import AES

def encrypt_message(plain_text, key):
	nonce = os.urandom(12)
	cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
	
	cipher_text, tag = cipher.encrypt_and_digest(plain_text.encode('utf-8'))
	
def decrypt_message(nonce, cipher_text, tag, key):
	cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
	try:
		decrypt_text = cipher.decrypt_and_verify(cipher_text, tag)
		return decrypted_text.decode('utf-8')
	except ValueError:
		return "Decryption Failed: Ciphertext or Tag tampered with!"
		
if__name__ == "__main":
	secret_key = os.urandom(32)
	secret_data = "Confidential Enterprise Data Assets"
	
	print(f"Original Text: {secret_data}")
	n, c, t = encrypt_message(secret_data, secret_key)
	print(f"Ciphertext (Hex): {c.hex()}")
	
	decrpted = decrypt_message(n, c, t, secret_key)
	print(f"Decrypted Text: {decrypted}")
