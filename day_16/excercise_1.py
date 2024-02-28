import re

emails = ["user@example.com", "first.last@domain.co.uk", "user_name@domain.co",
          "user@domain", "@example.com", "user@.com"]

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}\b'

for email in emails:
    if re.match(pattern, email):
        print(f"Valid: {email}")
    else:
        print(f"Invalid: {email}")
