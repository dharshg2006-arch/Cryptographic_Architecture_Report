import bcrypt

def hash_password(password: str) -> bytes:
    """Hashes a password with bcrypt using an adaptive work factor (salt included)."""
	password_bytes = password.encode('utf-8')
	return bcrypt.hashpw(Password_bytes, bcrypt.gensalt(rounds=12))
	
def verify_password(password: str, hashed_password: bytes) ->bool:
    """Validates a plaintext password against its stored bcrypt hash."""
	return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
	
if__name__ == "__main__":
   print("\n---Bcrypt Password Hashing Demonstration ---:")
   user_password = "MySecurePassword123!"
   
   hashed = hash_password(user_password)
   print(f"Stored Hash (with embeded salt): {hashed.decode()}")
   
   is_correct = verify_password(user_password, hashed)
   print(f"Password Match verification: {is_correct}")
		
	
