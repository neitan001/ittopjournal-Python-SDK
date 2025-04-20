__version__ = "0.1.0"

from .core import request_auth_token
from .core import (
    get_evaluation_lessons_api as _get_evaluation_lessons_api,
    get_user_info_api as _get_user_info_api,
    get_feedback_info_api as _get_feedback_info_api,
    get_metric_grade_info_api as _get_metric_grade_info_api,
    get_metric_attendance_info_api as _get_metric_attendance_info_api,
    get_rating_group_info_api as _get_rating_group_info_api,
    get_rating_stream_info_api as _get_rating_stream_info_api,
    get_student_visits_info_api as _get_student_visits_info_api,
)

__all__ = [
    "get_token",
    "get_evaluation_lessons",
    "get_user_info",
    "get_feedback_info",
    "get_metric_grade_info",
    "get_metric_attendance_info",
    "get_rating_group_info",
    "get_rating_stream_info",
    "get_student_visits_info",
]

def get_token(login: str, password: str, application_key: str):
    return request_auth_token(login, password, application_key)

def get_evaluation_lessons(token: str): return _get_evaluation_lessons_api(token)
def get_user_info(token: str): return _get_user_info_api(token)
def get_feedback_info(token: str): return _get_feedback_info_api(token)
def get_metric_grade_info(token: str): return _get_metric_grade_info_api(token)
def get_metric_attendance_info(token: str): return _get_metric_attendance_info_api(token)
def get_rating_group_info(token: str): return _get_rating_group_info_api(token)
def get_rating_stream_info(token: str): return _get_rating_stream_info_api(token)
def get_student_visits_info(token: str): return _get_student_visits_info_api(token)