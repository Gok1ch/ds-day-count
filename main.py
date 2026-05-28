from datetime import date
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1509574251512856669/5KEw70ZN-WPO34Zaybeg__U4ElNW4afsxurYmyVUQMukR3RRHzfjKpJK0Gu8B6mbPnEt"

start = date(2026, 1, 15)
today = date.today()

days = (today - start).days

# Правильное склонение
if days % 10 == 1 and days % 100 != 11:
    word = "день"
elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
    word = "дня"
else:
    word = "дней"

# Текст сообщения
if word == "день":
    message = f"📅 Прошёл {days} {word} без чурки"
else:
    message = f"📅 Прошло {days} {word} без чурки"

requests.post(WEBHOOK_URL, json={"content": message})
