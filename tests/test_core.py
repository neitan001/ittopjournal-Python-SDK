import ittopjournal

token = ittopjournal.get_token("Логин", "Пароль", "application_key")
user_info = ittopjournal.get_user_info(token)
info = ittopjournal.get_student_visits_info(token)

print(info)