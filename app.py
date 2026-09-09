from flask import Flask, request, redirect, render_template_string
import urllib.parse

app = Flask(__name__)

# رقم واتساب الخاص بك شامل رمز الدولة
WHATSAPP_NUMBER = "213559188468"

HTML_LAYOUT = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>متجر ayoub_shop_FF</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #0f172a; color: #f8fafc; text-align: center; padding: 20px; }
        .container { max-width: 450px; margin: 0 auto; }
        .card { background: #1e293b; border-radius: 12px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); border: 1px solid #334155; }
        h1 { color: #ff4655; font-size: 22px; }
        input, select { width: 90%; padding: 12px; margin: 10px 0; border-radius: 8px; border: 1px solid #475569; background-color: #0f172a; color: #fff; font-size: 14px; box-sizing: border-box; }
        button { background: #25d366; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: bold; width: 90%; transition: 0.3s; }
        button:hover { background: #128c7e; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎮 متجر ayoub_shop_FF لشحن الجواهر</h1>
        <p style="color: #94a3b8;">اختر العرض وأدخل ID لإتمام الدفع عبر واتساب</p>
        <div class="card">
            <form action="/buy" method="POST">
                <input type="text" name="player_id" placeholder="أدخل ID الحساب (Player ID)" required>
                <select name="pack" required>
                    <option value="" disabled selected>اختر العرض المطلوب</option>
                    <option value="100 جوهرة ($1.00)">💎 100 جوهرة ($1.00)</option>
                    <option value="520 جوهرة ($5.00)">💎 520 جوهرة ($5.00)</option>
                    <option value="1060 جوهرة ($10.00)">💎 1060 جوهرة ($10.00)</option>
                    <option value="2180 جوهرة ($20.00)">💎 2180 جوهرة ($20.00)</option>
                    <option value="5600 جوهرة ($50.00)">💎 5600 جوهرة ($50.00)</option>
                    <option value="20000 جوهرة ($180.00)">👑 20000 جوهرة ($180.00)</option>
                </select>
                <select name="payment" required>
                    <option value="" disabled selected>اختر طريقة الدفع</option>
                    <option value="BaridiMob / CCP">BaridiMob / CCP</option>
                    <option value="Flexy">Flexy</option>
                    <option value="Binance / USDT">Binance / USDT</option>
                </select>
                <button type="submit">متابعة الشراء عبر WhatsApp 💬</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_LAYOUT)

@app.route('/buy', methods=['POST'])
def buy():
    player_id = request.form.get('player_id')
    pack = request.form.get('pack')
    payment = request.form.get('payment')
    
    message = f"مرحباً، أريد إكمال طلب الشراء من المتجر:\n\n🆔 الـ ID: {player_id}\n💎 العرض: {pack}\n💳 طريقة الدفع المختارة: {payment}\n\nيرجى إرسال معلومات الدفع وإكمال الطلب."
    encoded_message = urllib.parse.quote(message)
    
    whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded_message}"
    return redirect(whatsapp_url)

if __name__ == '__main__':
    app.run()
