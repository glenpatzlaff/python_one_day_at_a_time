import re

text = "Important dates: 12-05-2021, 23/10/2020, and 01.01.2023."

pattern = r'\b\d{2}[-./]\d{2}[-./]\d{4}\b'

dates = re.findall(pattern, text)
print("Dates found:", dates)
