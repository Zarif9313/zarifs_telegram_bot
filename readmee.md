#  Churn Prediction AI Bot

Bu loyiha sun’iy intellekt asosida mijozlarning kompaniyani tark etish ehtimolini aniqlovchi tizimdir. Model foydalanuvchidan olingan ma’lumotlar asosida churn (tark etish) ehtimolini hisoblaydi va natijani Telegram bot orqali qaytaradi.

---

##  Loyiha Tuzilmasi

churn-predictor-bot/
├── data/
│ └── dataset.csv # Mijozlar ma’lumotlari
│
├── model/
│ ├── model.pkl # Treningdan o‘tgan ML modeli
│ └── scaler.pkl # StandardScaler obyekti
│
├── bot/
│ └── bot.py # Telegram bot kodi
│
├── notebook.ipynb # Modelni tayyorlash uchun kodlar
├── report.md # Texnik hisobot (markdown)
└── README.md # Ushbu fayl


---

## Foydalanilgan texnologiyalar

- Python 3.x
- Jupyter Notebook
- Scikit-learn
- Pandas, NumPy
- Pickle
- Telegram Bot API

---

## Qanday ishga tushiriladi

### 1. Repozitoriyani klonlash

```bash
git clone https://github.com/username/churn-predictor-bot.git
cd churn-predictor-bot
2. Virtual muhit yaratish (ixtiyoriy)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Kerakli kutubxonalarni o‘rnatish
pip install -r requirements.txt
4. Modelni yaratish
Jupyter Notebook (notebook.ipynb) faylini ishga tushiring va kodlarni bajarib model.pkl va scaler.pkl fayllarini yarating.

5. Telegram botni ishga tushurish
bot/bot.py faylida TOKEN = 'your_telegram_bot_token' qatorini to‘ldiring va quyidagicha ishga tushiring:

python bot/bot.py
🧪 Natijalar
RandomForestClassifier modeli bilan ~85% aniqlik

Model churn ehtimolini foizda qaytaradi (masalan: Churn probability: 78%)

Oddiy matnli interfeys orqali oson foydalanish

📌 Foydalanish namunasi
Telegram botga yuboriladigan ma’lumot formati:

gender: Female
SeniorCitizen: 0
Partner: Yes
Dependents: No
tenure: 12
PhoneService: Yes
MultipleLines: No
InternetService: Fiber optic
OnlineSecurity: No
OnlineBackup: Yes
DeviceProtection: No
TechSupport: No
StreamingTV: Yes
StreamingMovies: No
Contract: Month-to-month
PaperlessBilling: Yes
PaymentMethod: Credit card (automatic)
MonthlyCharges: 85.5
TotalCharges: 1020.5
Bot javobi:

 Churn ehtimoli: 78%
 Tavsiya: Bu mijozni sodiqlik dasturi orqali ushlab qolish mumkin.
 Muallif
Ism: Dexqonov Muhammadrózi

Email: dehqonovmuhammadrozi@gmail.com

Telegram: @f_o_bb