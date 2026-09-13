import os
from Crypto.Publickey import RSA 
from Crypto.Signature import pss 
from Crypto.Hash import SHA256

def generate_key_pair():
    """Generates a secure RSA 2048-bit key pair"""
	key = RSA.generate(2048)
	private_key = key.export_key()
	public_key = key.public_key().export_key()
	return private_key, public_key
	
def sign_message(message: bytes, private_key_bytes: bytes)-> bytes:
    """Signs a message using the RSA private key."""
	key = RSA.import_key(private_key_bytes)
	h = SHA256.new(message)
	signature = pss.new(key).sign(h)
	return signature

def verify_signature(message: bytes, signature: bytes, public_key_bytes: bytes) -> bool:
    """Verifies the digital signature using the RSA public key."""
	key = RSA.import_key(public_key_bytes)
	h = SHA256.new(message)\
	verifier = pss.new(key)
	try:
	    verifier.verify(h, signature)
		return True
	except (ValueError, TypeError):
	    return False
	    
if__name__ "__main":
   print("---RSA Signature Demonstration---")
   priv_key, pub_key = generate_key_pair()
   
   
   document = b"Authorized transactions data log token"
   sig = sign_message(document, priv_key)
   print(f"Signature generated successfully.")
   
   is_valid = verify_signature(document, sig, pub_key)
   print(f"Signature Verification Result: {is_valid}")
