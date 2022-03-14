import telebot
from telebot import types
bot = telebot.TeleBot("5283929903:AAFvdMRcQGdDjYKXNrUZQ2BMd8vljSEGNVY", parse_mode=None)

name = ''
helps = ''
call_numbers = ''

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    i_need = types.KeyboardButton('Я беженец, мне нужна помощь')
    i_want = types.KeyboardButton('Я хочу помочь')
    markup.add(i_need)
    markup.add(i_want)
    bot.send_message(message.chat.id, "Здравствуйте!\n\nЯ бот для беженцев с Донбасса и тех, кто хочет им помочь\n\nВыберите интересующий вас раздел:",reply_markup=markup)
    bot.register_next_step_handler(message,otvet)
#1
@bot.message_handler(commands=['send_help']) #Отправить заявку на совершение доброго дела
def hello(message):
    bot.send_message(message.chat.id, 'Пожалуйста представьтесь')
    bot.register_next_step_handler(message,send_application_for_help)



@bot.message_handler(content_types=['text'])


def otvet(message):
    if message.text == 'Я хочу помочь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
        checklist = types.KeyboardButton('Памятка по сбору вещей для нуждающихся')
        places = types.KeyboardButton('Пункты сбора гуманитарной помощи для беженцев')
        other_help = types.KeyboardButton('Я хочу оказать другую помощь')
        markup.add(checklist)
        markup.add(places)
        markup.add(other_help)
        bot.send_message(message.chat.id,'Выберите интересующий вас раздел:',reply_markup=markup)
        bot.register_next_step_handler(message, send_help)
    elif message.text == 'Я беженец, мне нужна помощь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
        places = types.KeyboardButton('Пункты сбора гуманитарной помощи для беженцев')
        other_help = types.KeyboardButton('Укажите, какая помощь вам необходима')
        markup.add(places)
        markup.add(other_help)
        bot.send_message(message.chat.id, 'Выберите интересующий вас раздел:', reply_markup=markup)
        bot.register_next_step_handler(message, need_help)
    else:
        markup = types.ReplyKeyboardRemove()
        bot.reply_to(message, 'Для старта введите команду /start ',reply_markup=markup)


def send_help(message):
    if message.text == 'Памятка по сбору вещей для нуждающихся':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Я хочу оказать другую помощь')
        markup.add(item1)
        bot.send_message(message.chat.id, '''Памятка по сбору вещей для нуждающихся:\nВ пункте сбора принимаются: 
Сухое детское питание (молочные и безмолочные для детей о О до 3 лет) 

Детское питание (смеси, каши, пюре, соки) 

Пластиковая посуда (посуда, пустышки, детские бутылочки) 

Товары по уходу за детьми (подгузники всех размеров от О до 6. впитывающие детские пеленки) 

Товары по уходу за лежачими пожилым людьми (подгузники, пеленки, салфетки, очищающие пенки) 

Постельные и душевые принадлежности (одеяла, подушки, постельное белье, полотенце, резиновые тапочки) 

Средства личной гигиены (шампуни, зубная паста, зубные щетки, гель для душа, мыло кусковое, туалетная бумага, салфетки) 

Бытовая техника (электрочайники, небольшие холодильники, бытовые удлинители) 

Одежда для взрослых и детей (от О до 14) 

Детские канцелярские принадлежности (книги, раскраски, игрушки) 

Предметы женской гигиены  

Средства индивидуальной защиты (маски, антисептики, перчатки).

Обращаем внимание, что все предметы гуманитарной помощи должны быть НОВЫМИ — в цельной упаковке, с этикетками, в равных пропорциях, укомплектованы в отдельные коробки по группе товаров с ОПИСЬЮ ВЛОЖЕНИЯ. 

Продукты питания — ДЛИТЕЛЬНОГО СРОКА ХРАНЕНИЯ, С ДЕЙСТВИТЕЛЬНЫМ СРОКОМ ГОДНОСТИ.

Вы можете оказать и другую помощь,
для этого нажмите:\n'Я хочу оказать другую помощь'\n
Для возврата в начало: \n\n/start''', reply_markup=markup)
        bot.register_next_step_handler(message,maybe_other_help)
    elif message.text == 'Пункты сбора гуманитарной помощи для беженцев':
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, '''Пункты открыты по адресам в Саратове:\n

- СГМУ, учебный корпус № 6 (Кутякова, 109, 1-й этаж). Контактный телефон 7-937-811-10-85 (Дарья, координатор), 7-987-809-35-38 (Диана, волонтер) – ежедневно с 9.00 до 17.00;

- СГТУ, корпус 25, научно-информационный центр (Политехническая, 77а, каб. 625), с 9.00 до 18.00, выходные – суббота и воскресенье;

- СГК им. Л. В. Собинова, нотная библиотека Саратовской консерватории (проспект Кирова, 1). Контактное лицо – завбиблиотекой, председатель первичной профсоюзной организации работников СГК Ирина Слива;

- во всех общественных приемных "Единой России" в Саратовской области. Телефоны волонтерского центра "ЕР" 8 (8452) 27-12-07 и 8 (8452) 27-84-71;

- аппарат Уполномоченного по правам ребенка Саратовской области (Челюскинцев, 116, каб. 3), с 08.00 до 18.00;

- Центр адаптации и реабилитации инвалидов "Парус надежды" (ул. Орджоникидзе, 125), ежедневно с 08.00 до 20.00. Контактный телефон 96-38-18, в выходные дни 96-45-30, 96-39-44.'
\n\n/start''', reply_markup=markup)
    elif message.text == 'Я хочу оказать другую помощь':
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Пожалуйста, представьтесь', reply_markup=markup)
        bot.register_next_step_handler(message, send_application_for_help)
    else:
        bot.send_message(message.chat.id,'Выберите интересующий вас раздел:')
        bot.register_next_step_handler(message,send_help)

def maybe_other_help(message):
    if message.text == 'Я хочу оказать другую помощь':
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Пожалуйста, представьтесь', reply_markup=markup)
        bot.register_next_step_handler(message, send_application_for_help)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
        i_need = types.KeyboardButton('Я беженец, мне нужна помощь')
        i_want = types.KeyboardButton('Я хочу помочь')
        markup.add(i_need)
        markup.add(i_want)
        bot.send_message(message.chat.id,
                         "Здравствуйте!\n\nЯ бот для беженцев с Донбасса и тех, кто хочет им помочь\n\nВыберите интересующий вас раздел:",
                         reply_markup=markup)
        bot.register_next_step_handler(message, otvet)

def need_help(message):
    if message.text == 'Пункты сбора гуманитарной помощи для беженцев':
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, '''Пункты открыты по адресам в Саратове:\n

- СГМУ, учебный корпус № 6 (Кутякова, 109, 1-й этаж). Контактный телефон 7-937-811-10-85 (Дарья, координатор), 7-987-809-35-38 (Диана, волонтер) – ежедневно с 9.00 до 17.00;

- СГТУ, корпус 25, научно-информационный центр (Политехническая, 77а, каб. 625), с 9.00 до 18.00, выходные – суббота и воскресенье;

- СГК им. Л. В. Собинова, нотная библиотека Саратовской консерватории (проспект Кирова, 1). Контактное лицо – завбиблиотекой, председатель первичной профсоюзной организации работников СГК Ирина Слива;

- во всех общественных приемных "Единой России" в Саратовской области. Телефоны волонтерского центра "ЕР" 8 (8452) 27-12-07 и 8 (8452) 27-84-71;

- аппарат Уполномоченного по правам ребенка Саратовской области (Челюскинцев, 116, каб. 3), с 08.00 до 18.00;

- Центр адаптации и реабилитации инвалидов "Парус надежды" (ул. Орджоникидзе, 125), ежедневно с 08.00 до 20.00. Контактный телефон 96-38-18, в выходные дни 96-45-30, 96-39-44.'
        \n\n/start''', reply_markup=markup)
    elif message.text == 'Укажите, какая помощь вам необходима':
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Пожалуйста, представьтесь', reply_markup=markup)
        bot.register_next_step_handler(message, need_application_for_help)
    else:
        bot.send_message(message.chat.id,'Выберите интересующий вас раздел:')
        bot.register_next_step_handler(message,need_help)

def need_application_for_help(message):
    global name
    name = message.text
    bot.reply_to(message, f'Здравствуйте, {name}')
    bot.send_message(message.chat.id,'Какая помощь вам необходима?')
    bot.register_next_step_handler(message,nhelp)

def nhelp(message):
    global helps
    helps = message.text
    bot.send_message(message.chat.id, "Чтобы мы приняли ваше обращение в обработку, пожалуйста, оставьте свой номер телефона в формате '+79001234567' или '89001234567'")
    bot.register_next_step_handler(message, ncall_number)

def ncall_number(message):
    global call_numbers
    call_numbers = message.text
    bot.send_message(793220243, f'Новая заявка от беженца!\nИмя: {name}\nПомощь: {helps}\nКонтакты: {call_numbers}')
    bot.send_message(message.chat.id, f'{name}, мы получили ваше обращение.\n\nВ случае одобрения заявки мы отправим вам инструкцию на ваш номер телефона.\n\nЧтобы заполнить форму снова, введите: /start ')


def send_application_for_help(message):
    global name
    name = message.text
    bot.reply_to(message, f'Здравствуйте, {name}')
    bot.send_message(message.chat.id,'Какую помощь вы можете оказать беженцам?')
    bot.register_next_step_handler(message,shelp)


def shelp(message):
    global helps
    helps = message.text
    bot.send_message(message.chat.id, "Чтобы мы приняли ваше обращение в обработку, пожалуйста, оставьте свой номер телефона в формате '+79001234567' или '89001234567'")
    bot.register_next_step_handler(message, scall_number)

def scall_number(message):
    global call_numbers
    call_numbers = message.text
    bot.send_message(793220243, f'Новая заявка от добровольца!\nИмя: {name}\nПомощь: {helps}\nКонтакты: {call_numbers}')
    bot.send_message(message.chat.id, f'{name}, спасибо за помощь!\n\nВ случае одобрения заявки мы отправим вам инструкцию на ваш номер телефона.\n\nЧтобы заполнить форму снова, введите: /start ')




bot.infinity_polling()
