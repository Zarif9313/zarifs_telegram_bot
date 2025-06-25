#  Loyihaviy Hisobot: Churn Prediction AI Bot

##  Muammo Tavsifi

Mijozlarni yo‘qotish (churn) – har qanday xizmat ko‘rsatuvchi kompaniyalar uchun asosiy muammolardan biridir. Raqobat kuchaygan davrda mijozlar ehtimoliy tarzda kompaniyani tark etadi. Bizning maqsad – mavjud mijozlar ma’lumotlari asosida ular kompaniyani tark etish ehtimolini aniqlashdir.

---

##  Maqsad

- Mijoz ma’lumotlarini tahlil qilish
- Churn (tark etish) ehtimolini aniqlovchi model yaratish
- Modelni Telegram bot orqali foydalanuvchiga qulay shaklda taqdim etish

---

##  Ma’lumotlar Tavsifi

### Dataset manbai:
Kompaniya mijozlariga oid sun’iy yoki ommaviy (public) dataset (CSV shaklida)

### Ustunlar:
- `customerID`: Mijoz ID raqami
- `gender`, `SeniorCitizen`, `Partner`, `Dependents`
- `tenure`: Xizmat muddati (oylarda)
- `PhoneService`, `InternetService`, `OnlineSecurity`, va boshqalar
- `MonthlyCharges`, `TotalCharges`
- `Churn`: Target ustun (Yes/No)

---

##  Ma’lumotlarni Tozalash va Tayyorlash

- `TotalCharges` ustunida `??` yoki bo‘sh qiymatlar aniqlanib, tozalandi
- `TotalCharges` float formatga o‘tkazildi
- Kategorik ustunlar one-hot encoding orqali kodlandi
- Target `Churn` ustuni 0/1 ko‘rinishiga o‘tkazildi

---

##  Model Tanlovi

3 xil model sinovdan o‘tkazildi:

1. **Logistic Regression**
2. **Support Vector Classifier (SVC)**
3. **Random Forest Classifier**

### Natijalar:
| Model                | Accuracy | ROC-AUC |
|---------------------|----------|---------|
| Logistic Regression | 79%      | 0.83    |
| SVC                 | 81%      | 0.85    |
|  Random Forest     | **85%**  | **0.88** |

RandomForest eng yaxshi natija ko‘rsatgani uchun u tanlandi.

---

## 🔬 Modelni Saqlash

- Model `.pkl` formatda saqlandi: `model/model.pkl`
- Feature scaler ham saqlandi: `model/scaler.pkl`

---

## 🤖 Telegram Bot Integratsiyasi

### Texnologiyalar:
- `python-telegram-bot` kutubxonasi
- Telegram webhook emas, polling rejimida ishlaydi
- Foydalanuvchi botga 16+ ta maydonni yuboradi → model natija qaytaradi

### Foydalanuvchi oqimi:

👤 User → 📩 Botga ma'lumot yuboradi
📊 Bot → ML modelga uzatadi
🧠 Model → Churn ehtimolini hisoblaydi
📢 Bot → Javobni qaytaradi (foiz va tavsiya bilan)


---

## 📈 Foydalanuvchiga Qaytariladigan Natija

```text
📊 Churn ehtimoli: 68%
🧠 Tavsiya: Bu mijozni ushlab qolish uchun qo‘shimcha chegirmalar berish tavsiya qilinadi.
🔐 Cheklovlar va Takliflar
Cheklovlar:
Matnli kiritishda format xatoliklari bo‘lishi mumkin

Model faqat statik dataset asosida o‘qitilgan

Yaxshilash yo‘llari:
Web-forma orqali kiritish

Mijozlar tarixi asosida dinamik model

Segmentatsiya asosida maxsus churn sabablari

👨‍💻 Loyiha Muallifi
Ism: Abdihomidov Zarif

Telegram: @zarif0803

Email: zarifabdihomidov@gmail.com