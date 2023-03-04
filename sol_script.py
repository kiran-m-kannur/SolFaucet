from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    balance = None
    if request.method == 'POST':
        account_address = request.form['account_address']
        process = subprocess.Popen(['solana', 'balance', account_address], stdout=subprocess.PIPE)
        output = process.communicate()[0]
        balance = output.decode('utf-8').strip()
    return render_template('index.html', balance=balance)

if __name__ == '__main__':
    app.run(debug=True)
