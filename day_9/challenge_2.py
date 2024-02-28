import re

text = "Please contact us at support@example.com or sales@example.com."
pattern = re.compile(r'\b[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-z]+')

emails = pattern.findall(text)
for email in emails:
    print(email)
