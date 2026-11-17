adumin_permissions = {"read", "write", "delete", "manage_users"}
editor_permissions = {"read","write"}

user_permissions = editor_permissions
required_permissions = {"delete"}

can_perform = required_permissions.issubset(user_permissions)

print(f"can user perform action requiring admin permissions? {can_perform}")
