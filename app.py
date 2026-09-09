from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_LAYOUT = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>متجر ayoub_shop_FF</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #f8fafc; text-align: center; padding: 20px; margin: 0; }
        h1 { color: #ff4655; font-size: 24px; margin-top: 20px; }
        p { color: #94a3b8; }
        .container { max-width: 450px; margin: 0 auto; }
        .card { background: #1e293b; border-radius: 12px; padding: 20px; margin: 15px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.5); border: 1px solid #334155; }
        .card h3 { color: #38bdf8; margin-top: 0; }
        input, select { width: 90%; padding: 12px; margin: 8px 0; border-radius: 8px; border: 1px solid #475569; background-color: #0f172a; color: #fff; font-size: 14px; box-sizing: border-box; }
        button { background: #ff4655; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: bold; width: 90%; transition: 0.3s; }
        button:hover { background: #e03e4d; }
        .success-box { background: #14532d; border: 1px solid #22c55e; padding: 15px; border-radius: 8px; margin-bottom: 20px; color: #4ade80; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎮 متجر ayoub_shop_FF شحن الجواهر</h1>
        <p>شحن جواهر Free Fire عن طريق الـ ID بسرعة وأمان</p>

        {% if success %}
        <div class="success-box">
            ✅ تم استلام طلبك بنجاح! سيتم الشحن الحساب برقم ID: <b>{{ player_id }}</b> قريباً.
        </div>
        {% endif %}

        <div class="card">
            <form action="/buy" method="POST">
                <h3>تعبئة معلومات الشحن</h3>
                
                <input type="text" name="player_id" placeholder="أدخل ID الحساب (Player ID)" required>
                
                <select name="pack" required>
                    <option value="" disabled selected>اختر العرض المطلوب</option>
                    <option value="100 الجواهر - $1.00">💎 100 جوهرة ($1.00)</option>
                    <option value="310 الجواهر - $3.00">💎 310 جوهرة ($3.00)</option>
                    <option value="520 الجواهر - $5.00">💎 520 جوهرة ($5.00)</option>
                    <option value="1060 الجواهر - $10.00">💎 1060 جوهرة ($10.00)</option>
                </select>

                <select name="payment" required>
                    <option value="" disabled selected>اختر طريقة الدفع</option>
                    <option value="CCP / BaridiMob">CCP / BaridiMob</option>
                    <option value="Flexy">Flexy</option>
                    <option value="Binance / USDT">Binance / USDT</option>
                </select>

                <br><br>
                <button type="submit">تأكيد طلب الشراء</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_LAYOUT, success=False)

@app.route('/buy', methods=['POST'])
def buy():
    player_id = request.form.get('player_id')
    pack = request.form.get('pack')
    payment = request.form.get('payment')
    
    # طباعة الطلب في اللوج لترصد الطلبات
    print(f"[NEW ORDER] ID: {player_id} | Pack: {pack} | Payment: {payment}")
    
    return render_template_string(HTML_LAYOUT, success=True, player_id=player_id)

if __name__ == '__main__':
    app.run()
