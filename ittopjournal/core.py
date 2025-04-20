import requests
from .config import *

def get_default_headers(extra_headers: dict = None) -> dict:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": ORIGIN,
        "Referer": REFERER
    }
    if extra_headers:
        headers.update(extra_headers)
    return headers

def get_authorized_headers(token: str) -> dict:
    return get_default_headers({"Authorization": f"Bearer {token}"})

def request_auth_token(login: str, password: str, application_key: str) -> str:
    headers = get_default_headers()
    data = {
        "username": login,
        "password": password,
        "application_key": application_key
    }

    try:
        response = requests.post(AUTH_URL, headers=headers, json=data)
        if response.status_code != 200:
            print(f"[ittopjournal] Ошибка авторизации: {response.status_code} - {response.text}")
            return None

        token = response.json().get("access_token")
        if not token:
            print("[ittopjournal] Ошибка: Токен доступа отсутствует в ответе.")
            return None

        return token

    except Exception as e:
        print(f"[ittopjournal] Ошибка при выполнении запроса авторизации: {e}")
        return None
    
def get_data_from_api(token: str, url: str):
    try:
        headers = get_authorized_headers(token)
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"[ittopjournal] Ошибка {response.status_code}: {response.text}")
            return None

    except Exception as e:
        print(f"[ittopjournal] Ошибка при получении данных с API: {e}")
        return None

def make_endpoint_func(url):
    return lambda token: get_data_from_api(token, url)

get_evaluation_lessons_api = make_endpoint_func(EVALUATION_LESSONS_LIST)
get_user_info_api = make_endpoint_func(USER_INFO)
get_feedback_info_api = make_endpoint_func(FEEDBACK_INFO)
get_metric_grade_info_api = make_endpoint_func(METRIC_GRADE)
get_metric_attendance_info_api = make_endpoint_func(METRIC_ATTENDANCE)
get_rating_group_info_api = make_endpoint_func(RATING_GROUP)
get_rating_stream_info_api = make_endpoint_func(RATING_STREAM)
get_student_visits_info_api = make_endpoint_func(STUDENT_VISITS)