from aiogram.fsm.state import StatesGroup, State


class FSMMedicalHistory(StatesGroup):
    diagnosis = State()  # Какие диагнозы вам выставляли?
    surgeries = State()  # Были ли у вас операции?
    surgeries_details = State()  # уточнения если "Да"
    past_medications = State()  # Какие лекарства принимали в течение жизни?
    current_medications = State()  # Какие препараты принимаете сейчас?
    allergies = State()  # Есть ли у вас аллергии?
    allergies_details = State()  # уточнения если "Да"
    probiotics_tolerance = State()  # Как переносите приём пробиотиков?
    probiotics_tolerance_details = State()  # уточнения если "Плохо"
    stool_problems = State()  # Есть ли у вас проблемы со стулом?
    heartburn_frequency = State()  # Беспокоит ли изжога?
    heartburn_details = State()  # Когда появляется (если есть)
    current_complaints = State()  # Жалобы на настоящее время
    current_complaints_details = State()  # уточнения если "Да"
    serious_issues = State()  # Травмы, госпитализации, инфекции
    serious_issues_details = State()  # уточнения если "Да"
    menstrual_issues = State()  # Нарушения менструального цикла (только для женщин)
    menstrual_issues_details = State()  # уточнения если "Да"
    family_diseases = State()  # Заболевания родственников
    family_alive = State()  # 22. Все ли родственники живы?
    family_death_details = State()  # уточнения если "Нет"

