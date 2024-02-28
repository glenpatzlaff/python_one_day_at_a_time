def access_control(role_required):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if hasattr(current_user, 'role') and current_user.role == role_required:
                return func(*args, **kwargs)
            else:
                print(f"Access denied. This function requires the {role_required} role.")
        return wrapper
    return decorator

class User:
    def __init__(self, role):
        self.role = role

@access_control('admin')
def delete_database():
    print("Database deleted.")

# Simulating different user roles
admin_user = User('admin')
regular_user = User('user')

# Testing the decorated function with an admin user
current_user = admin_user
delete_database()

# Testing the decorated function with a regular user
current_user = regular_user
delete_database()
