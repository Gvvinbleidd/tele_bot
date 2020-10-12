import telebot
import config
from telebot import types
from telebot.types import InputMediaPhoto


bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
  btn1 = types.KeyboardButton('Скачать обои')
  btn2 = types.KeyboardButton('Для чего это нужно?')
  btn3 = types.KeyboardButton('Как установить обои?')
  btn4 = types.KeyboardButton('Хочу помочь!')
  btn5 = types.KeyboardButton('Поддержка и сотрудничество')
  #btn6 = types.KeyboardButton('Сотрудничество')
  markup.add(btn1, btn2, btn3, btn4, btn5)
  send_mess = f"<b>Здравствуйте, {message.from_user.first_name}</b>!\nВы зашли к боту Капля мёда - обои для православных.\nНажмите внизу на кнопку, которая Вас интересует" #{message.from_user.last_name} - добавляет фамилию человека
  bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()

	#раздел скачать обои
	if get_message_bot == "скачать обои":
		photo = open('wallpapers/logo.png', 'rb')
		bot.send_photo(message.chat.id, photo)

		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Скачать обои", url="https://drive.google.com/drive/folders/1iC2f2jdXvZVDBjd1TfmoBN23SdKvmQLn?usp=sharing"))
		final_message = "Вы сможете скачать обои, которые есть у нас в лучшем качестве. Вот ссылка - <a href='https://drive.google.com/drive/folders/1iC2f2jdXvZVDBjd1TfmoBN23SdKvmQLn?usp=sharing'>Скачать</a>.\n \nЕсли у вас возникли какие-то проблемы со скачиванием или установкой, а быть может у вас есть предложения напишите пожалуйста в поддержку. Кнопка находится внизу."
	
	#elif get_message_bot == "молитвы":
		#photo = open('wallpapers/1.jpg', 'rb')
		#bot.send_photo(message.chat.id, photo)
		#bot.send_message(message.chat.id, "Это обои номер 1", parse_mode='html')

	elif get_message_bot == "в главное меню...":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Скачать обои')
		btn2 = types.KeyboardButton('Для чего это нужно?')
		btn3 = types.KeyboardButton('Как установить обои?')
		btn4 = types.KeyboardButton('Хочу помочь!')
		btn5 = types.KeyboardButton('Поддержка и сотрудничество')
		#btn6 = types.KeyboardButton('Сотрудничество')
		markup.add(btn1, btn2, btn3, btn4, btn5)
		final_message = "Вы в главном меню, выберете пункт меню"

	#раздел для чего это нужно
	elif get_message_bot == "для чего это нужно?":
		#photo = open('wallpapers/question-mark.png', 'rb')
		#bot.send_photo(message.chat.id, photo)

		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Скачать обои')
		btn2 = types.KeyboardButton('Для чего это нужно?')
		btn3 = types.KeyboardButton('Как установить обои?')
		btn4 = types.KeyboardButton('Хочу помочь!')
		btn5 = types.KeyboardButton('Поддержка и сотрудничество')
		#btn6 = types.KeyboardButton('Сотрудничество')
		markup.add(btn1, btn2, btn3, btn4, btn5)
		final_message = "Очи - окна души. Задумайтесь, а можете и посчитать: насколько часто на дню вы смотрите в свой телефон?\nВ современном мире мало сказать, что это происходит ''слишком часто'', тут больше подходит слово ''постоянно''. И тогда встаёт следующий вопрос: почему бы не поставить этот инструмент на ''служение'' Богу? Для начала с маленькой казалось бы незаметной вещи - обоев для телефона, но которая чаще всего мелькает перед глазами и может стать причиной обращения мыслей в сторону Бога.\n \nНо тут важно добавить, что сами обои, и, к примеру, молитвы на них, не для того, чтобы просто ''висеть'' в телефоне, а для того, чтобы человек, увидев краткую Иисусову молитву у себя в телефоне, направил свое сердце и мысли к Богу, про себя или вслух помолился, где бы он ни был: ''Господи Иисусе Христе, Сыне Божий, помилуй мя грешнаго''. Ведь Господь видит наше сердце и наши мысли, и пусть это будет маленький шажок, но всё таки он будет в сторону Бога, а не от него, и это хорошо."

	#раздел как установить
	elif get_message_bot == "как установить обои?":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Для iphone", url="https://support.apple.com/ru-ru/HT200285"), types.InlineKeyboardButton("Для android", url="https://tarifam.ru/kak-ustanovit-oboi-na-telefon/"))
		final_message = "Инструкция по установке обоев на телефон(или вы можете сами найти в поисковике):\n \nДля iphone\nhttps://support.apple.com/ru-ru/HT200285\nДля android\nhttps://tarifam.ru/kak-ustanovit-oboi-na-telefon/\n \n*ресурсы являются сторонними"

	elif get_message_bot == "хочу помочь!":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Поддержать материально", url="https://money.yandex.ru/to/410011303719295"), types.InlineKeyboardButton("Поддержать репостом", url="https://www.instagram.com/kaplya.meda/"))
		final_message = "Как вы уже успели заметить, а если всё таки обошли стороной этот факт, то говорим вам прямо сейчас, наши обои для телефона вы можете скачать БЕСПЛАТНО.\n \nМы не берём денег за скачивание и использование, но при этом, если у вас есть желание отблагодарить наш проект и помочь его развитию, то вы можете сделать пожертвование или поддерживать нас ежемесячно.\n \nЕсли у вас нет возможности помочь материально, то мы с удовольствием примем вашу помощь в виде репоста нашего аккаунта или любого понравившегося вам поста из нашего Instagram. Этим вы можете помочь не только нам, но и вашим знакомым, которые также смогут скачать и установить обои, и с их помощью чаще обращать свой взор к Богу.\n \nС благодарностью, Храни Вас Господь!"

	elif get_message_bot == "поддержка и сотрудничество":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Поддержка", url="https://t.me/sergeyfrolov95"))
		final_message = "Вы можете задать интересующие вас вопросы, получить техническую помощь или внести свои предложение по улучшению нашей работы.\nВот ссылка - <a href='https://t.me/sergeyfrolov95'>Поддержка</a>"

	#elif get_message_bot == "сотрудничество":
		#markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		#btn1 = types.KeyboardButton('Скачать обои')
		#btn2 = types.KeyboardButton('Для чего это нужно?')
		#btn3 = types.KeyboardButton('Как установить обои?')
		#btn4 = types.KeyboardButton('Хочу помочь!')
		#btn5 = types.KeyboardButton('Поддержка')
		#btn6 = types.KeyboardButton('Сотрудничество')
		#markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
		#final_message = "Тут кнопки (кто ты: спонсор, партнер, мне нужна помощь) текст для фондов, спонсоров и партнеров"

	else: 
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Скачать обои')
		btn2 = types.KeyboardButton('Для чего это нужно?')
		btn3 = types.KeyboardButton('Как установить обои?')
		btn4 = types.KeyboardButton('Хочу помочь!')
		btn5 = types.KeyboardButton('Поддержка и сотрудничество')
		#btn6 = types.KeyboardButton('Сотрудничество')
		markup.add(btn1, btn2, btn3, btn4, btn5)
		final_message = "Так, так, так\nПостой, лучше нажми на одну из интерактивных кнопок ниже"
	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

#@bot.callback_query_handler(func=lambda call: True)
#def callback_inline(call):
#    try:
#        if call.message:
#            if call.data == '1':
#                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
#            elif call.data == '2':
#                bot.send_message(call.message.chat.id, 'Бывает 😢')
# 
#            # remove inline buttons
#            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
#                reply_markup=None)
# 
#            # show alert
#            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
#                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!")
# 
#    except Exception as e:
#        print(repr(e))
 
# RUN
bot.polling(none_stop=True)