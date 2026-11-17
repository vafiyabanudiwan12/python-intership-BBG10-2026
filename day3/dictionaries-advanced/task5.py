default_settings = { "theme": "light", "font": 12, "language": "english"}

user_settings = { "theme": "dark", "font": 16 }
final_settings = {**default_settings, **user_settings}
print(final_settings)