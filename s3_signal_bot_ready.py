
import telegram
from PIL import Image, ImageDraw
from io import BytesIO

# ✅ توكن البوت الرسمي
BOT_TOKEN = '7734889574:AAEVsTgNHXD_Cse0avYr8nhRjqCHGGAsQbk'
# ✅ معرف القناة التي سيُرسل لها التوصيات
CHAT_ID = '@Islam_king_trading'

bot = telegram.Bot(token=BOT_TOKEN)

def build_signal_message(pair, direction, entry, sl, tp1, tp2, trade_type, confidence):
    rr1 = round(abs(tp1 - entry) / abs(entry - sl), 2)
    rr2 = round(abs(tp2 - entry) / abs(entry - sl), 2)
    return (
        f"📡 S³ Signal – {pair} {direction}\n\n"
        f"Entry: {entry}\nSL: {sl}\nTP1: {tp1}\nTP2: {tp2}\n\n"
        f"📈 R:R → TP1: {rr1} · TP2: {rr2}\n\n"
        f"🧱 Trade Type: {trade_type}\n"
        f"🔹 Confidence: {confidence}\n\n"
        "📍 Reason:\n"
        "✔ Sweep above liquidity\n"
        "✔ Rejection Wick (M15)\n"
        "✔ Retest of OB + Entry on M5\n\n"
        "🖼️ Chart attached below 👇"
    )

def send_signal(pair, direction, entry, sl, tp1, tp2, trade_type, confidence):
    msg = build_signal_message(pair, direction, entry, sl, tp1, tp2, trade_type, confidence)

    # توليد صورة توصية بسيطة
    img = Image.new('RGB', (800, 400), color='white')
    draw = ImageDraw.Draw(img)
    draw.text((20, 20), f"{pair} {direction} Setup\nEntry: {entry}\nSL: {sl}\nTP1: {tp1}\nTP2: {tp2}", fill='black')
    buf = BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    bot.send_photo(chat_id=CHAT_ID, photo=buf, caption=msg)

# 🚀 إرسال توصية تلقائية عند التشغيل
send_signal(
    pair='XAU/USD',
    direction='BUY',
    entry=2364.00,
    sl=2359.50,
    tp1=2370.00,
    tp2=2378.00,
    trade_type='Scalp (M5 Confirmation)',
    confidence='High (90%)'
)
