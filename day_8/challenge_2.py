roles = {
    "Alice": "Engineer",
    "Bob": "Manager",
    "Charlie": "Engineer",
    "Diana": "Designer"
}

# Invert the dictionary
inverted_roles = {}
for name, role in roles.items():
    inverted_roles.setdefault(role, []).append(name)

print(inverted_roles)
