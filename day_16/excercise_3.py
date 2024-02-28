import re

passwords = ["Password123@", "passw0rd", "StrongPass#", "VeryStrongPassword1234$"]

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%]).{8,}$'

for password in passwords:
    if re.match(pattern, password):
        print(f"Strong: {password}")
    else:
        print(f"Weak: {password}")
