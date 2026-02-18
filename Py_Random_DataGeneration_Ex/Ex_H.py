# __Challenge__

# Write a code to generate random secure token of 64 bytes and random URL.

import secrets

print(f"Random token: {secrets.token_hex(64)}")
print(f"Random URL: {secrets.token_urlsafe(64)}")