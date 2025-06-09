import telebot
import joblib
import pandas as pd
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Model va scalerlarni yuklash
model = joblib.load('model/model.pkl')
scaler = joblib.load('model/scaler.pkl')
model_cols = joblib.load('model/model_cols.pkl')

# Telegram token
TOKEN = '7694427496:AAEyeZXtKdiUagGTkoDA05vFydVE1Otzm-c'
bot = telebot.TeleBot(TOKEN)

# Model xususiyatlari
features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
            'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
            'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
            'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
            'PaymentMethod', 'MonthlyCharges', 'TotalCharges']

# O‘zbekcha tushuntmalar
instructions = {
    'gender': "👤 Jinsingizni tanlang:",
    'SeniorCitizen': "👴 Yoshi katta (senior) fuqaromisiz?\n0 - Yo‘q, 1 - Ha",
    'Partner': "💍 Sizning turmush o‘rtog‘ingiz bormi?",
    'Dependents': "👶 Sizga qaram (bola, qarindosh) mavjudmi?",
    'tenure': "📅 Necha oydan beri bizning xizmatimizdasiz? (0 - 72 oralig‘ida son kiriting)",
    'PhoneService': "📞 Telefon xizmati bormi?",
    'MultipleLines': "📱 Bir nechta telefon liniyalari mavjudmi?",
    'InternetService': "🌐 Internet xizmati turi:",
    'OnlineSecurity': "🔐 Onlayn xavfsizlik xizmati:",
    'OnlineBackup': "💾 Onlayn nusxa ko‘chirish xizmati:",
    'DeviceProtection': "🛡 Qurilma himoyasi xizmati:",
    'TechSupport': "🧰 Texnik yordam xizmati:",
    'StreamingTV': "📺 Onlayn TV xizmati:",
    'StreamingMovies': "🎬 Onlayn kino xizmati:",
    'Contract': "📄 Shartnoma turi:",
    'PaperlessBilling': "📧 Qog‘ozsiz to'lovgdan foydalanasizmi?",
    'PaymentMethod': "💳 To‘lov usulingiz:",
    'MonthlyCharges': "💵 Oylik to‘lovni kiriting (masalan: 70.5):",
    'TotalCharges': "💰 Umumiy to‘langan summani kiriting (masalan: 3500):"
}

# Variantlar
options = {
    'gender': ['Erkak', 'Ayol'],
    'Partner': ['Ha', 'Yo‘q'],
    'Dependents': ['Ha', 'Yo‘q'],
    'PhoneService': ['Bor', 'Yo‘q'],
    'MultipleLines': ['Bor', 'Yo‘q', 'Telefon yo‘q'],
    'InternetService': ['DSL', 'Optik tolali', 'Yo‘q'],
    'OnlineSecurity': ['Bor', 'Yo‘q', 'Internet yo‘q'],
    'OnlineBackup': ['Bor', 'Yo‘q', 'Internet yo‘q'],
    'DeviceProtection': ['Bor', 'Yo‘q', 'Internet yo‘q'],
    'TechSupport': ['Bor', 'Yo‘q', 'Internet yo‘q'],
    'StreamingTV': ['Bor', 'Yo‘q', 'Internet yo‘q'],
    'StreamingMovies': ['Bor', 'Yo‘q', 'Internet yo‘q'],
    'Contract': ['Oylik', '1 yil', '2 yil'],
    'PaperlessBilling': ['Ha', 'Yo‘q'],
    'PaymentMethod': ['Elektron chek', 'Pochta orqali chek', 'Bank avtomatik', 'Kredit karta']
}

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "📊 Salom! Men Telecom mijozning ketishini bashorat qiluvchi botman.\n"
                                      "➡️ Bashoratni boshlash uchun /predict ni yuboring.")

@bot.message_handler(commands=['predict'])
def handle_predict(message):
    chat_id = message.chat.id
    user_data[chat_id] = []
    ask_next_feature(message, 0)

def ask_next_feature(message, idx):
    chat_id = message.chat.id
    if idx != 0:
        user_data[chat_id].append(message.text)

    if idx < len(features):
        current_feature = features[idx]
        instruction = instructions.get(current_feature, f"{current_feature} ni kiriting:")
        markup = ReplyKeyboardRemove()

        if current_feature in options:
            markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            for opt in options[current_feature]:
                markup.add(KeyboardButton(opt))
        bot.send_message(chat_id, instruction, reply_markup=markup)

        bot.register_next_step_handler(message, lambda msg: ask_next_feature(msg, idx + 1))
    else:
        bot.send_message(chat_id, "✅ Barcha ma'lumotlar olindi. Natijani hisoblamoqdamiz...")
        predict_result(chat_id)

def predict_result(chat_id):
    row = user_data[chat_id]
    df_input = pd.DataFrame([row], columns=features)

    # To'g'ri turga o'tkazish
    for col in ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']:
        df_input[col] = pd.to_numeric(df_input[col], errors='coerce')

    # One-hot kodlash
    df_input_encoded = pd.get_dummies(df_input)

    # Yo‘q ustunlar to‘ldirish
    for col in model_cols:
        if col not in df_input_encoded:
            df_input_encoded[col] = 0
    df_input_encoded = df_input_encoded[model_cols]

    # Scaling
    input_scaled = scaler.transform(df_input_encoded)

    # Bashorat
    proba = model.predict_proba(input_scaled)[0][1]
    foiz = round(proba * 100, 2)
    bot.send_message(chat_id, f"Mijozning ketish ehtimolligi: {foiz}% ga teng")

# Botni ishga tushurish
bot.infinity_polling()
