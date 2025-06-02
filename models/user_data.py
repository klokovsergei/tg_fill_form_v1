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
    is_fill: bool = False
    children: str = ''
    children_info: str = ''
    childhood_health: str = ''
    employment_type: str = ''
    stress_level: str = ''
    mood_swings: str = ''
    anxiety: str = ''
    apathy: str = ''
    physical_activity: str = ''
    physical_activity_comment: str = ''


@dataclass
class MedicalHistory:
    is_fill: bool = False
    diagnosis: str = ''
    surgeries: str = ''
    surgeries_details: str = ''
    past_medications: str = ''
    current_medications: str = ''
    allergies: str = ''
    allergies_details: str = ''
    probiotics_tolerance: str = ''
    probiotics_tolerance_details: str = ''
    stool_problems: str = ''
    heartburn_frequency: str = ''
    heartburn_details: str = ''
    current_complaints: str = ''
    current_complaints_details: str = ''
    serious_issues: str = ''
    serious_issues_details: str = ''
    menstrual_issues: str = ''
    menstrual_issues_details: str = ''
    family_diseases: str = ''
    family_alive: str = ''

@dataclass
class SleepSchedule:
    is_fill: bool = False
    sleep_time: str = ''
    fall_asleep_speed: str = ''
    night_awakenings: str = ''
    morning_feeling: str = ''
    daytime_sleepiness: str = ''

@dataclass
class Habits:
    is_fill: bool = False
    smoking: str = ''
    smoking_details: str = ''
    alcohol: str = ''
    alcohol_details: str = ''
    other_habits: str = ''

@dataclass
class UserData:
    user_join: UserJoin = field(default_factory=UserJoin)
    general_info: GeneralInfo = field(default_factory=GeneralInfo)
    medical_history: MedicalHistory = field(default_factory=MedicalHistory)
    sleep_schedule: SleepSchedule = field(default_factory=SleepSchedule)
    habits: Habits = field(default_factory=Habits)
    is_join: bool = False
    is_form_filled: bool = False
