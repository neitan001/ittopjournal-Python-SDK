import ittopjournal

token = ittopjournal.get_token("Логин", "Пароль", "application_key")
user_info = ittopjournal.get_user_info(token)
info = ittopjournal.get_schedule(token, date="2025-04-21")

print(info)