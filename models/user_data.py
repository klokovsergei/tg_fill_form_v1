from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class UserJoin:
    firstname: str = ''
    lastname: str = ''
    gender: str = ''
    username: str = ''
    birthday: Optional[datetime] = None
    email: str = ''
    city: str = ''
    time_start: Optional[datetime] = None  # дата запуска бота
    time_join: Optional[datetime] = None  # дата прохождения регистрации
    phone: str = ''
    is_alive: bool = False
    notification: bool = False


@dataclass
class GeneralInfo:
    children: bool = False
    children_info: str = ''
    childhood_health: str = ''
    employment_type: str = ''
    stress_level: int = 0
    mood_swings: str = ''
    anxiety: str = ''
    apathy: str = ''
    physical_activity: str = ''
    physical_activity_comment: str = ''


@dataclass
class MedicalHistory:
    input_diagnoses: str = ''

@dataclass
class UserData:
    user_join: UserJoin = field(default_factory=UserJoin)
    general_info: GeneralInfo = field(default_factory=GeneralInfo)
    medical_history: MedicalHistory = field(default_factory=MedicalHistory)
    is_join: bool = False
    is_form_filled: bool = False
