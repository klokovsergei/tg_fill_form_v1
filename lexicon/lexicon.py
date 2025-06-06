LEXICON: dict[str, str] = {

    '/start': '<b>Привет ☺️</b>\n\n'
              'Меня зовут Елена Бочкарёва — я дипломированный специалист по правильному питанию, коррекции веса и здоровому образу жизни.\n\n'
              'То, что ты здесь, говорит о твоём желании заботиться о себе. И это замечательно! ✨\n'
              'Я с радостью поддержу тебя на каждом шаге.\n\n'
              'Для начала — небольшой подарок: зарегистрируйся и получи мой авторский гайд по полезным специям.\n'
              'Просто нажми кнопку <b>«Регистрация»</b> и ответь на пару простых вопросов.\n'
              'Так мы сможем оставаться на связи, а я чуть больше узнаю о тебе 🌿\n'
              '<i>Без лишней суеты — просто приятное знакомство 🍀</i>'
    , '/help': 'Здесь будет текст для <b>/help 😊</b>'
    , '/stop': '<b>Работа завершена</b> 🛑\n\n'
               'Бот сохранил всю необходимую информацию о ваших действиях 📦\n'
               'Теперь вы можете закрыть чат или продолжить позже — данные останутся в сохранности 🔐\n\n'
               'С нетерпением жду нового запуска!!! 📈\n'
               'Спасибо, что пользуетесь ботом! 🙌'
    , '/fill': '📝 <b>Анкета для персональной консультации с нутрициологом</b>\n\n'
               'Чтобы составить индивидуальные рекомендации для вас, мне потребуется чуть больше сведений. '
               'Анкета включает шесть важных разделов.\n\n'
               '❗️Будьте откровенны и внимательны при заполнении анкеты — вся предоставленная вами информация '
               'абсолютно конфиденциальна!\n\n'
               'Начинайте с раздела, который удобнее заполнить первым'

    , 'not_admin': 'Ой, эта команда доступна только администратору 🙈\n'
                   'Если ты случайно сюда попал — не переживай, просто вернись назад и нажми нужную кнопку 😊'
    , 'not_join': '⚠️ Похоже, вы ещё не зарегистрировались!\n\n'
                  'Перед началом заполнения анкеты прошу пройти короткий процесс регистрации — это займёт '
                  'буквально пару минут. '
                  'Базовые сведения о вашем возрасте, городе проживания и номере телефона позволят правильно '
                  'организовать дальнейшую работу.\n\n'
                  'Также вы сразу получите небольшой подарок — мой авторский гайд по полезным специям.\n\n'
                  'Зарегистрироваться просто: воспользуйтесь кнопкой <b>«Мой профиль»</b> в главном меню или '
                  'командой /join.'
    , 'new_user': '<code>{bot_name}</code>\n<b>Новый пользователь:</b>  <code>{username}</code>\n'
                  '(ID: {user_id})\nДата регистрации: {time_join}'
    , 'new_join_up': '<code>{bot_name}</code>\n'
                     '<b>Новая регистрация</b> 👤\n\n'
                     '<b>Имя:</b> {firstname}\n'
                     '<b>Фамилия:</b> {lastname}\n'
                     '<b>Username:</b> <code>@{username}</code>\n'
                     '<b>Пол:</b> {gender}\n'
                     '<b>Дата рождения:</b> {birthday}\n'
                     '<b>Возраст:</b> {age}\n'
                     '<b>Город:</b> {city}\n'
                     '<b>Email:</b> <code>{email}</code>\n'
                     '<b>Телефон:</b> <code>+{phone}</code>\n\n'
                     '<b>Дата запуска бота:</b> {time_start}\n'
                     '<b>Дата регистрации:</b> {time_join}'
    , 'cancel_no': '🔍 Не вижу активного действия, которое можно было бы отменить'
    , 'cancel_state': '📋 Вы отменили ввод данных.\nЧтобы вернуться, выберите нужный шаг в меню.'
    , 'already_joined': '👤 Вы уже зарегистрированы.\nЕсли хотите изменить информацию в профиле '
                        '— выберите, что именно нужно обновить, с помощью кнопок ниже.'

    # JOIN

    , 'fill_firstname': '👤 Как вас зовут? Напишите имя:'
    , 'not_name': '❗️Введённый текст не похож на допустимое значение.\n\n'
                  'Можно использовать только буквы — кириллицу или латиницу, без цифр и символов.\n'
                  'Пожалуйста, введите корректное значение.\n'
                  'Если вы хотите прервать заполнение анкеты — отправьте команду /cancel'
    , 'fill_lastname': '👥 Укажите вашу фамилию:'
    , 'fill_gender': 'Укажите ваш пол, выбрав один из вариантов ниже:'
    , 'fill_birthday': '🎂 Укажите вашу дату рождения в формате <b>дд.мм.гггг</b>:'
    , 'not_date': '❗️Похоже, дата указана в неверном формате или такой даты не существует.\n'
                  'Пожалуйста, введите дату рождения в формате <b>дд.мм.гггг</b> (например, 25.12.1990).\n'
                  'Если вы хотите прервать заполнение анкеты — отправьте команду /cancel'
    , 'fill_city': '🏙 Укажите город, в котором вы живёте:'
    , 'not_city': '❗️Похоже, введённый текст не является корректным названием города.\n'
                  'Пожалуйста, введите только название города без цифр и символов.\n'
                  'Если вы хотите прервать заполнение анкеты — отправьте команду /cancel'
    , 'fill_email': '📧 Укажите ваш email-адрес:\nЕсли не хотите указывать — отправьте символ <b>*</b>'
    , 'not_email': '❗️Похоже, вы указали некорректный email.\n\n'
                   'Пожалуйста, введите адрес электронной почты в формате <b>example@domain.com</b>.\n'
                   'Если вы хотите прервать заполнение анкеты — отправьте команду /cancel'
    , 'fill_phone': '📱 Чтобы поделиться номером телефона, нажмите кнопку "Поделиться номером" ниже'
    , 'not_phone': '❗️Похоже, вы отправили не номер телефона.\n'
                   'Пожалуйста, воспользуйтесь кнопкой "Поделиться номером"\n'
                   'Если вы хотите прервать заполнение анкеты — отправьте команду /cancel'
    , 'is_notification': '🔔 Хотите получать уведомления от бота?'
    , 'join_compliant': '🎉 <b>Регистрация завершена! Добро пожаловать!</b>\n\n'
                        'Вы можете редактировать свой профиль через меню.\n\n'
                        'Для получения моей консультации необходимо заполнить анкету. Просто отправьте команду /fill '
                        'и выбирайте нужный блок для заполнения.'
    , 'not_button': '❗️Пожалуйста, выберите один из вариантов, нажав на кнопку под вопросом.\n'
    , 'thanks_number': '📞 Спасибо! Номер телефона получен.'
    , 'not_your_number': '❌ Пожалуйста, отправьте свой СОБСТВЕННЫЙ номер телефона'

    #  GENERAL_INFO

    , 'children': '<b>Отлично, начнём с общей информации 😊</b>\n\n'
                  'Эти вопросы помогут мне лучше понять твою ситуацию.\n'
                  'Отвечай спокойно и честно — здесь всё конфиденциально и только для нашей работы 🌿\n\n'
                  '<b>Первый вопрос:</b>\n'
                  'Есть ли у вас дети?'
    , 'children_info': 'Пожалуйста, напишите, сколько у вас детей и сколько им лет 👶👧🧒\n\n'
                       'Например:\n<i>2 ребёнка: 5 и 15 лет</i>'
    , 'childhood_health': '<b>Спасибо!</b> 😊\n\n'
                          'Теперь немного о вашем детстве.\n'
                          'Это поможет мне лучше понять ваш путь и то, как формировалось ваше здоровье 🧠🧬\n\n'
                          '<b>Как проходило ваше детство в отношении здоровья?</b>\n'
                          '<i>Ответьте в свободной форме — например: "часто болела простудами", "почти не '
                          'болел", "был(а) аллергиком" и т.п.</i>'
    , 'not_so_short': 'Благодарю за ответ! 🙌\n\n'
                      'Если можешь, расскажи чуть подробнее — это поможет мне точнее понять твою ситуацию 🌿\n'
                      '<i>Можно буквально пару предложений — ничего сложного 🙂</i>'
    , 'employment_type': '<b>Благодарю за ответ! 🙌</b>\n\n'
                         'Теперь немного о вашей повседневной активности.\n'
                         '<b>Какой у вас был тип занятости за последние 5 лет?</b>\n'
                         'Выберите наиболее подходящий вариант из списка ниже 👇'
    , 'stress_level': '<b>Уровень стресса</b> 🧠\n\n'
                      'Оцените, пожалуйста, ваш текущий уровень стресса по шкале от 1 до 10:\n'
                      '1 — почти не испытываю стресс\n'
                      '10 — ощущаю сильное напряжение постоянно\n\n'
                      'Нажмите на цифру, которая лучше всего описывает ваше состояние 👇'
    , 'mood_swings': '<b>Как часто у вас бывают перепады настроения?</b>\n\n'
                     'Это может быть связано с разными причинами — и именно поэтому важно учитывать '
                     'такие моменты 🌿\n'
                     'Просто выберите вариант, который ближе всего к вашему опыту.'
    , 'anxiety': '<b>Как часто вы испытываете тревожность?</b>\n\n'
                 'Ответьте так, как чувствуете. Это поможет мне лучше понять вашу эмоциональную нагрузку 🌿'
    , 'apathy': '<b>Как часто вы испытываете апатию?</b>\n\n'
                'Когда ничего не хочется, нет мотивации и даже привычные вещи не радуют…\n'
                'Отвечайте так, как есть — это важно для понимания вашего текущего состояния 💬'
    , 'physical_activity': '<b>Какой у вас уровень физической активности?</b>\n\n'
                           'Выберите наиболее подходящий вариант  🏃‍♂️🏃‍♀️'
    , 'physical_activity_comment': '🏋️ Отлично, что у вас регулярные тренировки!\n\n'
                                   'Пожалуйста, расскажите немного подробнее: как часто вы '
                                   'тренируетесь и какие виды активности предпочитаете?\n\n'
                                   'Например: 3 раза в неделю — силовые и йога.'
    , 'general_info_thanks': '💚 Спасибо за заполнение блока <b>"Общая информация"</b>!\n\n'
                             'Все данные уже сохранены в твоём профиле и будут учтены при подготовке '
                             'к консультации после заполнения всех блоков.\n'
                             'Пока просто двигайся дальше в удобном для тебя темпе 🌿\n\n'
                             'Командой /fill можно выбрать следующий блок для заполнения.'
    , 'filled_general_info': '<b>🗂 Ответы на анкету: Общая информация</b>\n\n'
                             '<b>👶 Дети:</b> {children}\n'
                             '{children_info_block}\n'
                             '<b>🧒 Детство и здоровье:</b>\n{childhood_health}\n'
                             '<b>💼 Тип занятости (последние 5 лет):</b> {employment_type}\n'
                             '<b>😵 Уровень стресса:</b> {stress_level}/10\n'
                             '<b>🎭 Перепады настроения:</b> {mood_swings}\n'
                             '<b>😟 Тревожность:</b> {anxiety}\n'
                             '<b>😶 Апатия:</b> {apathy}\n'
                             '<b>🏃‍♂️ Физическая активность:</b> {physical_activity}\n'
                             '{physical_activity_comment}'
    , 'general_info_yes': '✅ Раздел "Общая информация" уже заполнен'

    # MEDICAL_HISTORY

    , 'diagnosis': '<b>Перейдём к разделу "Медицинский анамнез" 🩺</b>\n\n'
                   'Этот блок поможет мне глубже понять особенности вашего здоровья.\n'
                   'Пожалуйста, отвечайте максимально честно — всё останется между нами и будет использовано '
                   'только для вашей пользы 🌿\n\n'
                   '<b>Какие диагнозы вам выставляли?</b>\n'
                   'Опишите в свободной форме. Если диагнозов не было — тоже укажите это.'
    , 'surgeries': 'Благодарю за ответ! 🙌\n\n'
                   '<b>Были ли у вас операции? 💉</b>\n\n'
                   'Если да — позже вы сможете описать подробнее, какие именно.'
    , 'surgeries_details': 'Пожалуйста, расскажите в свободной форме, какие '
                           'именно операции вы перенесли и когда это было.\n'
                           'Например: аппендэктомия в 2015 году, операция на мениске в 2020 и т.д.\n'
                           'Если помните — добавьте год и краткое описание причины.'
    , 'past_medications': '<b>Какие препараты вы принимали в течение жизни? 💊</b>\n\n'
                          'Укажите всё, что вспомните — название, дозировка (если помните) и причину приёма.\n'
                          'Это поможет лучше понять особенности вашей истории здоровья.'
    , 'current_medications': '<b>Какие препараты вы принимаете в данный момент? 💊</b>\n\n'
                             'Пожалуйста, перечислите их в свободной форме — укажите названия, '
                             'дозировку (если помните) и для чего они назначены.\n'
                             'Если сейчас ничего не принимаете — просто напишите об этом.'
    , 'allergies': '<b>Есть ли у вас аллергии? 🌿</b>\n\n'
                   'Это могут быть лекарства, продукты, пыльца, шерсть животных и т.д.\n'
                   'Пожалуйста, выберите вариант ответа'
    , 'allergies_details': '<b>Хорошо, тогда расскажите немного подробнее ⬇️</b>\n\n'
                           'На что именно у вас аллергия? Пример ответа:\n'
                           '<i>– На пенициллин\n'
                           '– Цветение берёзы\n'
                           '– Орехи, особенно грецкие</i>\n\n'
                           'Если есть реакции, опишите их тоже — это поможет при анализе данных.'
    , 'probiotics_tolerance': '<b>Как вы переносите пробиотики?</b> 🦠\n\n'
                              'Пробиотики — это живые полезные микроорганизмы, которые помогают '
                              'поддерживать здоровье кишечника и иммунной системы.\n'
                              'Иногда при приёме пробиотиков могут возникать разные ощущения — от '
                              'полного комфорта до лёгкого дискомфорта.\n\n'
                              'Пожалуйста, выберите, как вы обычно реагируете на пробиотики:\n'
                              '😊 <b>Хорошо</b> — чувствуете себя лучше, улучшилось пищеварение, '
                              'нет побочных эффектов.\n'
                              '😐 <b>Нейтрально</b> — изменений почти не заметно, организм реагирует спокойно.\n'
                              '😖 <b>Плохо</b> — появлялись неприятные ощущения, дискомфорт, вздутие '
                              'или другие нежелательные симптомы.\n\n'
                              'Выберите подходящий вариант ответа'
    ,
    'probiotics_tolerance_details': '<b>Пожалуйста, уточните, что именно вы ощущали при приёме пробиотиков:</b> 🤔\n\n'
                                    'Например: вздутие, боли в животе, ухудшение самочувствия, кожные реакции и т.д.\n'
                                    'Также можете указать, какие именно пробиотики вы пробовали (если помните).'
    , 'stool_problems': '<b>Есть ли у вас проблемы со стулом?</b> 🚽\n\n'
                        'Выберите наиболее подходящий вариант ответа:\n\n'
                        '— <b>Нет</b>: регулярный стул, без особенностей\n'
                        '— <b>Бывает запор</b>: редкий стул, затруднённое опорожнение\n'
                        '— <b>Бывает понос</b>: частый жидкий стул\n'
                        '— <b>Смешанный тип</b>: чередование запоров и поносов'
    , 'heartburn_frequency': '<b>Бывает ли у вас изжога?</b> 🔥\n\n'
                             'Выберите подходящий вариант ответа'
    , 'heartburn_details': '<b>Расскажите подробнее про изжогу:</b> 🔍\n\n'
                           'Когда она возникает? Что провоцирует? Чем снимаете симптомы (если снимаете)?\n\n'
                           'Ваш ответ поможет точнее оценить состояние ЖКТ'
    , 'current_complaints': '<b>Есть ли у вас сейчас какие-либо жалобы?</b> 🤒\n\n'
                            'Пожалуйста, выберите один из вариантов'
    , 'current_complaints_details': '<b>Пожалуйста, опишите ваши текущие жалобы.</b> 📋\n\n'
                                    'Расскажите в свободной форме:\n'
                                    '— На что именно жалуетесь?\n'
                                    '— Когда появились симптомы?\n'
                                    '— Что уже пробовали делать для улучшения?\n'
                                    '— Был ли какой-то эффект?'
    , 'serious_issues': '<b>Были ли у вас серьёзные травмы, госпитализации или тяжёлые инфекции?</b> 🏥\n\n'
                        'Пожалуйста, выберите подходящий вариант'
    , 'serious_issues_details': '<b>Пожалуйста, расскажите подробнее о серьёзных травмах, '
                                'госпитализациях или инфекциях, которые у вас были.</b>\n\n'
                                'Укажите, когда это произошло, какие последствия были и как '
                                'это повлияло на ваше здоровье.'
    , 'menstrual_issues': '<b>Есть ли у вас проблемы с менструальным циклом?</b> 🌸\n\n'
                          'Выберите вариант ответа'
    , 'menstrual_issues_details': '<b>Пожалуйста, опишите подробнее, с какими нарушениями '
                                  'менструального цикла вы сталкиваетесь.</b>\n\n'
                                  'Уточните, когда начались изменения, насколько они выражены, как '
                                  'часто повторяются и были ли обращения к врачу.'
    , 'family_diseases': '<b>Есть ли у близких родственников хронические заболевания?</b> 🧬\n\n'
                         'Укажите, если у кого-то из родственников (родителей, бабушек/дедушек, братьев/сестёр) были:\n'
                         '— сердечно-сосудистые заболевания\n'
                         '— диабет\n'
                         '— аутоиммунные болезни\n'
                         '— онкология\n'
                         '— нарушения обмена веществ и др.\n\n'
                         'Ответьте в свободной форме: какие именно болезни, у кого, '
                         'в каком возрасте появились (если знаете).'
    , 'family_alive': '<b>Все ли ваши близкие родственники живы?</b> 👨‍👩‍👧‍👦\n\n'
                      'Если кто-то из родителей, бабушек/дедушек или родных братьев/сестёр скончался, '
                      'пожалуйста, укажите, по возможности, причину смерти и возраст, в котором это произошло.\n\n'
                      'Если все живы или у вас нет такой информации — напишите об этом.'
    , 'filled_medical_history': '<code>{bot_name}</code>\n'
                                '<b>Блок "Медицинский анамнез" заполнен 🩺</b>\n\n'
                                '<b>1. Диагнозы:</b> {diagnosis}\n\n'
                                '<b>2. Были ли операции:</b> {surgeries}\n'
                                '<b>Подробности об операциях:</b> {surgeries_details}\n\n'
                                '<b>3. Принимали ли препараты ранее:</b> {past_medications}\n'
                                '<b>4. Принимаете ли сейчас препараты:</b> {current_medications}\n\n'
                                '<b>5. Есть ли аллергии:</b> {allergies}\n'
                                '<b>Подробности об аллергии:</b> {allergies_details}\n\n'
                                '<b>6. Переносимость пробиотиков:</b> {probiotics_tolerance}\n'
                                '<b>Комментарий:</b> {probiotics_tolerance_details}\n\n'
                                '<b>7. Особенности стула:</b> {stool_problems}\n\n'
                                '<b>8. Частота изжоги:</b> {heartburn_frequency}\n'
                                '<b>Комментарий:</b> {heartburn_details}\n\n'
                                '<b>9. Есть ли текущие жалобы:</b> {current_complaints}\n'
                                '<b>Описание жалоб:</b> {current_complaints_details}\n\n'
                                '<b>10. Были ли серьёзные травмы, инфекции, госпитализации:</b> {serious_issues}\n'
                                '<b>Подробности:</b> {serious_issues_details}\n\n'
                                '<b>11. Есть ли особенности менструального цикла:</b> {menstrual_issues}\n'
                                '<b>Комментарий:</b> {menstrual_issues_details}\n\n'
                                '<b>12. Наследственные заболевания:</b> {family_diseases}\n\n'
                                '<b>13. Живы ли близкие родственники:</b> {family_alive}'
    , 'medical_history_thanks': '🩺 Спасибо за заполнение блока <b>"Медицинский анамнез"</b>!\n\n'
                                'Вся информация сохранена в твоём профиле и обязательно будет учтена при '
                                'подготовке к консультации, когда ты завершишь все блоки.\n'
                                'Двигайся в удобном темпе — мы рядом 😊\n\n'
                                'Командой /fill можно выбрать следующий блок для заполнения.'
    , 'medical_history_yes': '✅ Раздел "Общая информация" уже заполнен'

    # SLEEP_SCHEDULE
    , 'sleep_time': '<b>Перейдём к разделу "Сон и режим" 😴</b>\n\n'
                    'Этот блок поможет понять, насколько ваш режим сна способствует восстановлению организма.\n'
                    'Пожалуйста, отвечайте максимально честно — всё останется между нами и будет использовано '
                    'только для вашей пользы 🌿\n\n'
                    '<b>Во сколько вы обычно ложитесь спать и встаете?</b>\n'
                    'Ответ в свободной форме. Например: «Ложусь в 23:00, встаю в 07:30».\n'
                    'Если в выходные режим отличается — можете указать отдельно.'
    , 'fall_asleep_speed': '<b>Как быстро вы обычно засыпаете? 🛌</b>\n\n'
                           'Выберите вариант, который лучше всего описывает ваше состояние перед сном:\n\n'
                           '🔹 <b>Легко</b> — засыпаю в течение 10–15 минут, без усилий.\n'
                           '🔹 <b>Средне</b> — требуется немного времени, иногда отвлекают мысли.\n'
                           '🔹 <b>Сложно</b> — часто долго лежу без сна, тревожусь или ворочаюсь.'
    , 'night_awakenings': '<b>Часто ли вы просыпаетесь ночью? 🌙</b>\n\n'
                          'Ночные пробуждения могут влиять на качество отдыха и общее самочувствие. '
                          'Выберите подходящий вариант'
    , 'morning_feeling': '<b>Чувствуете ли вы себя отдохнувшим утром? 🌅</b>\n\n'
                         'Этот вопрос помогает оценить качество сна и восстановления организма.\n'
                         'Выберите наиболее подходящий вариант'
    , 'daytime_sleepiness': '<b>Бывает ли у вас дневная сонливость?</b> 😴\n\n'
                            'Это состояние, когда в течение дня вы чувствуете сильное желание поспать, '
                            'даже если ночью спали достаточно. Такое может мешать работе, учебе или просто '
                            'нормальному самочувствию.\n\nВыберите наиболее подходящий вариант'
    , 'filled_sleep_schedule': '<code>{bot_name}</code>\n'
                               '<b>🛏 Блок "Сон и режим" заполнен:</b>\n\n'
                               '🕰 <b>Время сна и подъёма:</b> {sleep_time}\n'
                               '😴 <b>Скорость засыпания:</b> {fall_asleep_speed}\n'
                               '🌙 <b>Пробуждения ночью:</b> {night_awakenings}\n'
                               '🌞 <b>Отдохнувшие по утрам:</b> {morning_feeling}\n'
                               '💤 <b>Дневная сонливость:</b> {daytime_sleepiness}'
    , 'sleep_schedule_thanks': '💤 Спасибо за заполнение блока <b>"Сон и режим"</b>!\n\n'
                               'Теперь у меня есть представление о вашем режиме сна, что очень важно '
                               'для оценки общего состояния.\n\n'
                               'Все ответы уже сохранены в вашем профиле. Можете продолжить заполнять анкету '
                               'в удобном для вас темпе командой /fill 🌿'
    , 'sleep_schedule_yes': '✅ Раздел "Сон и режим" уже заполнен'

    # HABITS
    , 'smoking': '<b>Раздел "Привычки"</b>\n\n'
                 'Поговорим немного о привычках, которые могут влиять на общее состояние здоровья.\n\n'
                 '<b>🚬 Курите ли вы?</b>'
    , 'smoking_details': '<b>Пожалуйста, уточните детали по курению:</b> 🚬\n\n'
                         'Что именно вы курите (сигареты, вейп, кальян и т.д.)?\n'
                         'Как давно вы курите и как часто?\n'
                         'Пробовали ли бросить — и если да, то с каким результатом?\n\n'
                         'Отвечайте в свободной форме. Эта информация поможет лучше понять '
                         'влияние привычек на здоровье.'
    , 'alcohol': '<b>🍷 Перейдём к теме "Алкоголь".</b>\n\n'
                 'Употребляете ли вы алкогольные напитки?\n'
                 'Выберите наиболее подходящий вариант ответа'
    , 'alcohol_details': '<b>Расскажите подробнее о вашем употреблении алкоголя 🍷</b>\n\n'
                         'Уточните, какие напитки предпочитаете, как часто и в каких количествах употребляете.\n'
                         'Если есть ситуации, когда вы замечаете негативное влияние (например, на сон, настроение, '
                         'пищеварение) — тоже можно упомянуть.'
    , 'other_habits': '<b>Есть ли другие привычки, которые могут быть важны для оценки вашего состояния?</b> 🧩\n\n'
                      'Например, частое употребление энергетиков, кофе, БАДов, курительных '
                      'смесей, жевательных резинок, '
                      'частые перекусы на ходу, привычка не завтракать и т.д.\n\n'
    , 'filled_habits': '<code>{bot_name}</code>\n'
                       '<b>💭 Блок "Привычки" заполнен:</b>\n\n'
                       '🚬 <b>Курение:</b> {smoking}\n'
                       '📋 <b>Детали курения:</b> {smoking_details}\n'
                       '🍷 <b>Алкоголь:</b> {alcohol}\n'
                       '📋 <b>Детали алкоголя:</b> {alcohol_details}\n'
                       '🧩 <b>Другие привычки:</b> {other_habits}\n\n'
    , 'habits_thanks': '💚 Спасибо за заполнение блока <b>"Привычки"</b>!\n\n'
                       'Информация уже сохранена.\n'
                       'Двигайся дальше в своём темпе 🌿\n\n'
                       'Командой /fill ты можешь выбрать следующий блок для заполнения.'
    , 'habits_yes': '✅ Раздел "Привычки" уже заполнен'

    # LIFESTYLE
    , 'meals_per_day': '<b>Раздел "Питание и образ жизни" 🍽️</b>\n\n'
                       'Давайте обсудим ваш режиме питания и образе жизни — это поможет мне '
                       'лучше понять ваши ежедневные привычки.\n\n'
                       '<b>🍴 В среднем, сколько раз в день вы едите?</b>'
    , 'breakfast_time': '<b>🍽️ Во сколько вы обычно завтракаете?</b>\n\n'
                        'Можете указать примерное время, как вы это обычно говорите: например,'
                        ' <i>«около восьми», «в 9:30», «после 10»</i> и т.п. ⏰\n\n'
                        'Главное — чтобы было понятно, когда у вас начинается первый приём пищи.'
    , 'heaviest_meal': '<b>🍛 Какой приём пищи у вас самый обильный?</b>\n\n'
                       'Это поможет понять, как распределяется нагрузка на пищеварение в течение дня.\n'
                       'Выберите вариант, который лучше всего описывает вашу привычку'
    , 'cooking_attitude': '<b>👩‍🍳 Готовите ли вы дома и как к этому относитесь?</b>\n'
                          'Пожалуйста, выберите подходящий вариант кнопкой ниже 👇'
    , 'snacks_frequency': 'Перекусы — это нормально, особенно если они осознанные и полезные. 🥜🍎\n\n'
                          '<b>Как часто вы перекусываете между приёмами пищи?</b>\n'
                          'Выберите вариант кнопкой ниже 👇'
    , 'frequent_foods': '<b>🥗 Какие продукты вы едите чаще всего?</b>\n'
                        'Напишите в свободной форме, какие продукты регулярно присутствуют в вашем рационе.\n\n'
                        'Примеры для ориентира:\n'
                        '• 🥩 Мясо\n'
                        '• 🐟 Рыба\n'
                        '• 🌾 Крупы\n'
                        '• 🥛 Молочные продукты\n'
                        '• 🍎 Фрукты\n'
                        '• 🥦 Овощи\n'
                        '• 🥐 Выпечка\n'
                        '• 🍫 Сладости\n'
                        '• 🍔 Фастфуд\n\n'
                        'Если есть что-то ещё — обязательно укажите 📝'
    , 'daily_drinks': '<b>🥤 Какие напитки вы пьёте ежедневно?</b>\n'
                      'Напишите в свободной форме, какие напитки вы обычно употребляете каждый день.\n\n'
                      'Примеры для ориентира:\n'
                      '• 💧 Вода\n'
                      '• 🍵 Чай\n'
                      '• ☕ Кофе\n'
                      '• 🧃 Сок\n'
                      '• 🥤 Газировка\n'
                      '• 🍷 Алкоголь\n\n'
                      'Если есть другие напитки — обязательно укажите 📝'
    , 'food_intolerance': '<b>⚠️ Есть ли у вас пищевая непереносимость или аллергии?</b>\n'
                          'Это важно для понимания особенностей вашего рациона.\n\n'
                          'Выберите один из вариантов кнопкой ниже 👇'
    , 'food_intolerance_details': '<b>📝 Уточните, какие именно продукты вызывают у вас '
                                  'аллергии или непереносимость.</b>\n\n'
                                  '<i>Например: лактоза, глютен, орехи, цитрусовые и т.д.</i>'
    , 'eating_features': '<b>🍽️ Есть ли особенности в вашем питании?</b>\n'
                         'Выберите подходящий вариант, чтобы мы лучше понимали ваш образ питания:\n\n'
    , 'eating_features_details': '<b>📝 Уточните, пожалуйста</b>\n'
                                 'Вы выбрали вариант «Другое» или хотите добавить детали.\n\n'
                                 'Напишите в свободной форме, какие ещё особенности есть в вашем питании: '
                                 'например, поздние ужины, отсутствие аппетита, ночные '
                                 'перекусы, жёсткие ограничения и т.д.'
    , 'past_diets': '<b>🥦 Пробовали ли вы в прошлом жёсткие диеты или голодовки?</b>\n'
                    'Это может быть полезно для понимания вашего пищевого поведения '
                    'и отношения к ограничениям.\n\n'
                    'Пожалуйста, выберите подходящий вариант кнопкой ниже 👇'
    , 'past_diets_details': '<b>📋 Уточните, пожалуйста, какие именно диеты или голодовки вы пробовали.</b>\n'
                            'Можно кратко указать название диеты или описать, в чём '
                            'заключались ограничения. Это поможет лучше понять ваш опыт'
    , 'supplements': '<b>💊 Принимаете ли вы БАДы, витамины или ферменты?</b>'
    , 'readiness_to_change': '<b>🔄 Насколько вы готовы изменить свой образ жизни и питание?</b>\n'
                             'Оцените по шкале от 1 до 10, где:\n'
                             '1 — полностью готов(а) к изменениям\n'
                             '10 — совсем не готов(а)'
    , 'filled_lifestyle': '<code>{bot_name}</code>\n'
                          '<b>🍽️ Раздел "Питание и образ жизни" заполнен!</b>\n\n'
                          'Вот что мы узнали:\n'
                          '• Приёмов пищи в день: {meals_per_day}\n'
                          '• Обычно завтракаете около: {breakfast_time}\n'
                          '• Самый обильный приём пищи: {heaviest_meal}\n'
                          '• Отношение к приготовлению еды: {cooking_attitude}\n'
                          '• Частота перекусов: {snacks_frequency}\n'
                          '• Часто употребляемые продукты: {frequent_foods}\n'
                          '• Напитки, которые пьёте ежедневно: {daily_drinks}\n'
                          '• Пищевая непереносимость или аллергии: {food_intolerance}\n'
                          '• Особенности питания: {eating_features}\n'
                          '• Был ли опыт жёстких диет или голодовок: {past_diets}\n'
                          '• Принимаете ли БАДы, витамины, ферменты: {supplements}\n'
                          '• Готовность менять рацион: {readiness_to_change}'
    , 'lifestyle_thanks': '💚 Спасибо за заполнение блока <b>"Питание и образ жизни"</b>!\n\n'
                          'Информация уже сохранена.\n'
                          'Двигайся дальше в своём темпе 🌿\n\n'
                          'Командой /fill ты можешь выбрать следующий блок для заполнения.'
    , 'lifestyle_yes': '✅ Раздел "Питание и образ жизни" уже заполнен'

    # buttons
    , 'cancel_button': '🚫 Не сейчас'
    , 'join': '📝 Регистрация'
    , 'firstname': '👤 Изменить имя'
    , 'lastname': '👥 Изменить фамилию'
    , 'phone': '📞 Обновить номер телефона'
    , 'birthday': '🎂 Изменить дату рождения'
    , 'email': '✉️ Изменить e-mail'
    , 'yes_button': '✅ Да'
    , 'no_button': '❌ Нет'
    , 'dont_know': '❓ Не знаю'
    , 'male': '👨 Мужской'
    , 'female': '👩 Женский'
    , 'not_applicable': '🔹 Не применимо'

    , 'general_info': '🟡 Общая информация'
    , 'yes_general_info': '✅ Общая информация'
    , 'medical_history': '🟡 Медицинский анамнез'
    , 'yes_medical_history': '✅ Медицинский анамнез'
    , 'lifestyle': '🟡 Питание и образ жизни'
    , 'yes_lifestyle': '✅ Питание и образ жизни'
    , 'sleep_schedule': '🟡 Сон и режим'
    , 'yes_sleep_schedule': '✅ Сон и режим'
    , 'habits': '🟡 Привычки'
    , 'yes_habits': '✅ Привычки'
    , 'goals_docs': 'goals_docs'

    , 'employment_sedentary': '🪑 Сидячий'
    , 'employment_active': '🚶 Активный'
    , 'employment_mixed': '🔁 Смешанный'
    , 'employment_none': '🛋️ Не работаю'

    , 'button_1': '1️⃣ 😊'
    , 'button_2': '2️⃣ 🙂'
    , 'button_3': '3️⃣ 😌'
    , 'button_4': '4️⃣ 😐'
    , 'button_5': '5️⃣ 😕'
    , 'button_6': '6️⃣ 😟'
    , 'button_7': '7️⃣ 😣'
    , 'button_8': '8️⃣ 😫'
    , 'button_9': '9️⃣ 😢'
    , 'button_10': '🔟 😱'

    , 'button_meals_1': '1 🍽️'
    , 'button_meals_2': '2 🍽️'
    , 'button_meals_3': '3 🍽️'
    , 'button_meals_4': '4 🍽️'
    , 'button_meals_5': '5+ 🍽️'

    , 'never': '➖ Никогда'
    , 'rarely': '〰️ Редко'
    , 'often': '🔁 Часто'
    , 'sometimes': '🌀 Иногда'
    , 'regularly': '🔥 Регулярно'
    , 'always': '🔸 Всегда'

    , 'button_low_activity': '🛋 Низкая активность'
    , 'button_walk_5k': '🚶‍♀️ Хожу 5 000 шагов в день'
    , 'button_irregular_sport': '🏓 Занимаюсь нерегулярно'
    , 'button_regular_training': '💪 Регулярные тренировки'

    , 'button_good_tolerance': '😊 Хорошо'
    , 'button_neutral_tolerance': '😐 Нейтрально'
    , 'button_bad_tolerance': '😖 Плохо'

    , 'button_stool_none': '✅ Нет'
    , 'button_stool_constipation': '🪑 Бывает запор'
    , 'button_stool_diarrhea': '💧 Бывает понос'
    , 'button_stool_mixed': '🔄 Смешанный тип'

    , 'button_sleep_easy': '😴 Легко'
    , 'button_sleep_medium': '🌙 Средне'
    , 'button_sleep_hard': '🌀 Сложно'

    , 'button_breakfast': '🍳 Завтрак'
    , 'button_lunch': '🍲 Обед'
    , 'button_dinner': '🌙 Ужин'
    , 'button_equal': '⚖️ Примерно 🟰'

    , 'button_cooking_love': '👨‍🍳 Люблю готовить'
    , 'button_cooking_neutral': '🍲 Готовлю, потому что надо'
    , 'button_cooking_rarely': '🚫 Почти не готовлю'

    , 'overeating': '🧃 Переедание'
    , 'on_the_go': '🏃‍♂️ Еда "на бегу"'
    , 'sweets_after_meal': '🍬 Сладкое после еды'
    , 'emotional_eating': '😥 Эмоциональное питание'
    , 'no_features': '✅ Никаких особенностей'
    , 'other': '📝 Другое'
}

LEXICON_COMMANDS: dict[str, str] = {
    '/help': '❓ Как использовать бота'
    , '/join': '👤 Мой профиль'
    , '/cancel': '🚫 Отменить заполнение формы'
    , '/fill': '📝 Анкета для консультации'
}
