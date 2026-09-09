from flask import Flask, request, redirect, render_template_string
import urllib.parse

app = Flask(__name__)

# رقم واتساب الخاص بك شامل رمز الدولة
WHATSAPP_NUMBER = "213559188468"

# رابط صورة الخلفية
BG_IMAGE_URL = "https://share.google/4cLU5w4hjNM2FhGiq"

HTML_LAYOUT = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>متجر ayoub_shop_FF</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.85)), url('{{ bg_url }}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #f8fafc;
            text-align: center;
            padding: 20px;
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container { max-width: 450px; width: 100%; margin: 0 auto; }
        .card { 
            background: rgba(30, 41, 59, 0.9); 
            backdrop-filter: blur(8px);
            border-radius: 16px; 
            padding: 25px; 
            box-shadow: 0 8px 32px rgba(0,0,0,0.6); 
            border: 1px solid rgba(255, 255, 255, 0.1); 
        }
        h1 { color: #ff4655; font-size: 24px; margin-bottom: 5px; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
        p { color: #cbd5e1; font-size: 14px; margin-bottom: 20px; }
        input, select { 
            width: 100%; 
            padding: 14px; 
            margin: 10px 0; 
            border-radius: 10px; 
            border: 1px solid #475569; 
            background-color: rgba(15, 23, 42, 0.8); 
            color: #fff; 
            font-size: 15px; 
            box-sizing: border-box; 
        }
        input:focus, select:focus {
            border-color: #ff4655;
            outline: none;
        }
        button { 
            background: #25d366; 
            color: white; 
            border: none; 
            padding: 14px; 
            border-radius: 10px; 
            cursor: pointer; 
            font-size: 16px; 
            font-weight: bold; 
            width: 100%; 
            margin-top: 10px;
            transition: 0.3s; 
            box-shadow: 0 4px 12px rgba(37, 211, 102, 0.3);
        }
        button:hover { background: #128c7e; }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <h1>🎮 متجر ayoub_shop_FF</h1>
            <p>اختر العرض المناسب وأدخل الـ ID للشحن عبر واتساب</p>
            
            <form action="/buy" method="POST">
                <input type="text" name="player_id" placeholder="أدخل ID الحساب (Player ID)" required>
                
                <select name="pack" required>
                    <option value="" disabled selected>اختر العرض المطلوب</option>
                    <option value="100 جوهرة (220 د.ج)">💎 100 جوهرة - 220 د.ج</option>
                    <option value="520 جوهرة (1100 د.ج)">💎 520 جوهرة - 1,100 د.ج</option>
                    <option value="1060 جوهرة (2200 د.ج)">💎 1060 جوهرة - 2,200 د.ج</option>
                    <option value="2180 جوهرة (4400 د.ج)">💎 2180 جوهرة - 4,400 د.ج</option>
                    <option value="5600 جوهرة (11000 د.ج)">💎 5600 جوهرة - 11,000 د.ج</option>
                    <option value="20000 جوهرة (39000 د.ج)">👑 20000 جوهرة - 39,000 د.ج</option>
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
    return render_template_string(HTML_LAYOUT, bg_url=BG_IMAGE_URL)

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
