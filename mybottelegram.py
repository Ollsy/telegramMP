import telebot
from handler import get_chats_id_info
# Конфигурация
TOKEN = "7737786825:AAER3bVUc3jCLcpaK_6nFzmLN312vZAfFkc"  # Замените на токен бота
SOURCE_TARGET_CHAT_ID_DICT = get_chats_id_info('blacklist.txt', 'clearlist.txt')

# SOURCE_CHAT_ID = "-411516982"  # Отсюда будем пересылать
# TARGET_CHAT_ID = "-1001431040944"  # Сюда будем пересылать

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 Бот работает! Добавьте меня в обе группы.")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message.chat.id, message.chat.title)
@bot.channel_post_handler(func=lambda message: True)
def echo_all(message):
    print(message.chat.id, message.chat.title)
# Обработчик для фото
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if int(message.chat.id) in SOURCE_TARGET_CHAT_ID_DICT:
        print("фото получено")
        try:
            # Отправляем фото в целевую группу
            bot.send_photo(
                chat_id = SOURCE_TARGET_CHAT_ID_DICT[int(message.chat.id)],

                photo=message.photo[-1].file_id,  # Берем фото максимального качества
            
            )
        except Exception as e:
            print(f"Ошибка: {e}")

# Обработчик для видео
@bot.message_handler(content_types=['video'])
def handle_video(message):
    if int(message.chat.id) in SOURCE_TARGET_CHAT_ID_DICT:
        try:
            # Отправляем видео в целевую группу
            bot.send_video(
                chat_id = SOURCE_TARGET_CHAT_ID_DICT[int(message.chat.id)],
                video=message.video.file_id,
             
            )
        except Exception as e:
            print(f"Ошибка: {e}")

@bot.channel_post_handler(content_types=['photo'])
def handle_photo(message):
    print("фото получено")
    if int(message.chat.id) in SOURCE_TARGET_CHAT_ID_DICT:
        print("канал черновик для фото найден")
        try:
            # Отправляем фото в целевую группу
            bot.send_photo(
                chat_id = SOURCE_TARGET_CHAT_ID_DICT[int(message.chat.id)],

                photo=message.photo[-1].file_id,  # Берем фото максимального качества
            
            )
        except Exception as e:
            print(f"Ошибка: {e}")

# Обработчик для видео
@bot.channel_post_handler(content_types=['video'])
def handle_video(message):
    print('видео получено')
    if int(message.chat.id) in SOURCE_TARGET_CHAT_ID_DICT:
        print('канал черновика найден')
        try:
            # Отправляем видео в целевую группу
            bot.send_video(
                chat_id = SOURCE_TARGET_CHAT_ID_DICT[int(message.chat.id)],
                video=message.video.file_id,
             
            )
        except Exception as e:
            print(f"Ошибка: {e}")

# dict_of_chat = {"key1":(12121212, 25452)}
if __name__ == "__main__":
     print("Бот запущен!")
     bot.infinity_polling(timeout=10, long_polling_timeout=5)
# print(dict_of_chat["key1"])
