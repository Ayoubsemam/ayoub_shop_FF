from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_code = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>متجر Free Fire</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #1a1a2e; color: #fff; text-align: center; padding: 20px; }
            h1 { color: #e94560; }
            .card { background: #16213e; border-radius: 10px; padding: 15px; margin: 15px auto; max-width: 300px; box-shadow: 0 4px 8px rgba(0,0,0,0.3); }
            button { background: #e94560; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 16px; }
            button:hover { background: #0f3460; }
        </style>
    </head>
    <body>
        <h1>مرحباً بك في متجر ayoub_shop_FF</h1>
        <p>اختر العرض المناسب للشراء:</p>
        <div class="card">
            <h3>💎 100 جوهرة</h3>
            <p>السعر: 1.00 $</p>
            <button onclick="alert('تم استلام الطلب!')">شراء الآن</button>
        </div>
        <div class="card">
            <h3>💎 520 جوهرة</h3>
            <p>السعر: 5.00 $</p>
            <button onclick="alert('تم استلام الطلب!')">شراء الآن</button>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run()
