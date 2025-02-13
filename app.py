from flask import Flask, render_template, request, redirect, url_for
import qrcode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['link']
        color = request.form['color']
        generate_qr(data, color)
        return redirect(url_for('qr_code'))
    return render_template('index.html')

@app.route('/qr_code')
def qr_code():
    return render_template('qr_code.html')

def generate_qr(data, color):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color='white')
    
    # Ensure the static directory exists
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    
    img.save(os.path.join(static_dir, 'MyQRCode.png'))

if __name__ == '__main__':
    app.run(debug=True)