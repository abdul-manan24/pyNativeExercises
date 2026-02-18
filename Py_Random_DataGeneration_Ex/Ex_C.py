# __Challenge__

# Generate 6 digit Random Secure OTP.

import secrets
import string

allowed_characters = string.digits

otp = ''.join(secrets.choice(allowed_characters) for _ in range(6))
    
print(f"Your OTP is: {otp}")

# __Method Two__

import secrets

#Getting systemRandom class instance out of secrets module
secretsGenerator = secrets.SystemRandom()

print("Generating 6 digit random OTP")
otp = secretsGenerator.randrange(100000, 999999)

print("Secure random OTP is ", otp)