from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'strong_secret_key_12345'

def init_db():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS topup_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id TEXT NOT NULL,
            game_name TEXT NOT NULL,
            package_name TEXT NOT NULL,
            payment_method TEXT NOT NULL,
            sender_phone TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return conn

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>متجر شحن الألعاب بالفليكسي</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { background-color: #0b0f19; color: #e2e8f0; font-family: sans-serif; }
        .card { background-color: #1e293b; border: 1px solid #334155; border-radius: 12px; }
        .form-control, .form-select { background-color: #0f172a; border: 1px solid #334155; color: #fff; }
        .form-control:focus, .form-select:focus { background-color: #0f172a; color: #fff; border-color: #3b82f6; }
        .btn-topup { background-color: #ef4444; color: white; font-weight: bold; }
        .btn-topup:hover { background-color: #dc2626; color: white; }
    </style>
</head>
<body class="py-4">
    <div class="container" style="max-width: 700px;">
        <div class="text-center mb-4">
            <h1 class="fw-bold text-danger"><i class="fa-solid fa-gamepad me-2"></i>متجر شحن الألعاب</h1>
            <p class="text-secondary">شحن جواهر وشدات عبر Djezzy, Ooredoo, Mobilis, و BaridiMob</p>
        </div>

        <div class="card p-4 shadow-sm mb-4">
            <h4 class="card-title text-info mb-3"><i class="fa-solid fa-bolt me-2"></i>طلب شحن جديد</h4>
            <form action="/submit_order" method="POST">
                <div class="mb-3">
                    <label class="form-label">اختر اللعبة:</label>
                    <select name="game_name" class="form-select" required>
                        <option value="Free Fire">Free Fire (جواهر)</option>
                        <option value="PUBG Mobile">PUBG Mobile (شدات UC)</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label class="form-label">معرّف اللاعب (Player ID):</label>
                    <input type="text" name="player_id" class="form-control" placeholder="أدخل ID حسابك" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">اختر الحزمة:</label>
                    <select name="package_name" class="form-select" required>
                        <option value="100 Diamonds / UC">100 جوهرة / UC</option>
                        <option value="310 Diamonds / UC">310 جوهرة / UC</option>
                        <option value="520 Diamonds / UC">520 جوهرة / UC</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label class="form-label">طريقة الدفع:</label>
                    <select name="payment_method" class="form-select" required>
                        <option value="Djezzy Flexy">Djezzy Flexy (جازي)</option>
                        <option value="Ooredoo Storm">Ooredoo Storm (أوريدو)</option>
                        <option value="Mobilis Arsselli">Mobilis Arsselli (موبيليس)</option>
                        <option value="BaridiMob">BaridiMob / CCP</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label class="form-label">رقم مرسل الفليكسي / الإيصال:</label>
                    <input type="text" name="sender_phone" class="form-control" placeholder="06XXXXXXXX / 07XXXXXXXX" required>
                </div>
                <button type="submit" class="btn btn-topup w-100 py-2"><i class="fa-solid fa-cart-shopping me-1"></i> إرسال طلب الشحن</button>
            </form>
        </div>

        <div class="card p-4 shadow-sm">
            <h4 class="card-title text-warning mb-3"><i class="fa-solid fa-clock-rotate-left me-2"></i>سجل الطلبات</h4>
            <div class="table-responsive">
                <table class="table table-dark table-hover mb-0 text-center">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>اللعبة</th>
                            <th>Player ID</th>
                            <th>الدفع</th>
                            <th>الرقم</th>
                            <th>الحالة</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for order in orders %}
                        <tr>
                            <td>{{ order['id'] }}</td>
                            <td>{{ order['game_name'] }}</td>
                            <td><code>{{ order['player_id'] }}</code></td>
                            <td>{{ order['payment_method'] }}</td>
                            <td>{{ order['sender_phone'] }}</td>
                            <td><span class="badge bg-warning text-dark">قيد المعالجة</span></td>
                        </tr>
                        {% else %}
                        <tr><td colspan="6" class="text-muted">لا توجد طلبات شحن حالياً</td></tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    conn = get_db_connection()
    orders = conn.execute('SELECT * FROM topup_orders ORDER BY id DESC').fetchall()
    conn.close()
    return render_template_string(HTML_TEMPLATE, orders=orders)

@app.route('/submit_order', methods=['POST'])
def submit_order():
    game_name = request.form.get('game_name')
    player_id = request.form.get('player_id')
    package_name = request.form.get('package_name')
    payment_method = request.form.get('payment_method')
    sender_phone = request.form.get('sender_phone')

    if game_name and player_id and package_name and payment_method and sender_phone:
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO topup_orders (game_name, player_id, package_name, payment_method, sender_phone) VALUES (?, ?, ?, ?, ?)',
            (game_name, player_id, package_name, payment_method, sender_phone)
        )
        conn.commit()
        conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5003, debug=True)

