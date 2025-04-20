import logging
from datetime import datetime
from typing import Optional, Dict, Any
import requests
from pydantic import BaseModel, ValidationError
from .config import *


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ApiErrorResponse(BaseModel):
    error: str
    details: Optional[Dict[str, Any]]

def get_default_headers(extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": ORIGIN,
        "Referer": REFERER,
    }
    if extra_headers:
        headers.update(extra_headers)
    return headers

def get_authorized_headers(token: str) -> Dict[str, str]:
    return get_default_headers({"Authorization": f"Bearer {token}"})

def _validate_response(response: requests.Response, model: Optional[BaseModel] = None) -> Optional[Dict[str, Any]]:
    try:
        response.raise_for_status()
        data = response.json()

        if model:
            validated_data = model(**data).dict()
            logger.debug(f"Валидация успешна: {validated_data}")
            return validated_data
        return data

    except requests.exceptions.HTTPError as e:
        error_data = _parse_error_response(e.response)
        logger.error(f"HTTP Error {e.response.status_code}: {error_data}")
    except ValidationError as e:
        logger.error(f"Ошибка валидации ответа: {e.json()}")
    except Exception as e:
        logger.error(f"Неизвестная ошибка: {e}")
    return None

def _parse_error_response(response: requests.Response) -> Dict[str, Any]:
    try:
        return ApiErrorResponse(**response.json()).dict()
    except Exception:
        return {"error": "Невалидный JSON в ошибке", "raw_response": response.text}

def request_auth_token(login: str, password: str, application_key: str) -> Optional[str]:
    headers = get_default_headers()
    data = {
        "username": login,
        "password": password,
        "application_key": application_key,
    }

    try:
        response = requests.post(AUTH_URL, headers=headers, json=data)
        validated = _validate_response(response, AuthResponse)
        return validated.get("access_token") if validated else None

    except Exception as e:
        logger.error(f"Критическая ошибка при авторизации: {e}", exc_info=True)
        return None

def get_data_from_api(token: str, url: str) -> Optional[Dict[str, Any]]:
    try:
        headers = get_authorized_headers(token)
        response = requests.get(url, headers=headers)
        return _validate_response(response)

    except Exception as e:
        logger.error(f"Ошибка при запросе к {url}: {e}", exc_info=True)
        return None

def make_endpoint_func(url_template: str):
    def wrapper(token: str, **kwargs):
        if 'date' in kwargs:
            try:
                datetime.strptime(kwargs['date'], '%Y-%m-%d')
            except ValueError:
                logger.error(f"Invalid date format: {kwargs['date']}. Use YYYY-MM-DD")
                return None
        
        url = url_template.format(**kwargs)
        return get_data_from_api(token, url)
    return wrapper

get_schedule_api = make_endpoint_func(SCHEDULE_URL)
get_evaluation_lessons_api = make_endpoint_func(EVALUATION_LESSONS_LIST)
get_user_info_api = make_endpoint_func(USER_INFO)
get_feedback_info_api = make_endpoint_func(FEEDBACK_INFO)
get_metric_grade_info_api = make_endpoint_func(METRIC_GRADE)
get_metric_attendance_info_api = make_endpoint_func(METRIC_ATTENDANCE)
get_rating_group_info_api = make_endpoint_func(RATING_GROUP)
get_rating_stream_info_api = make_endpoint_func(RATING_STREAM)
get_student_visits_info_api = make_endpoint_func(STUDENT_VISITS)