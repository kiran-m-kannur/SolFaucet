from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        account_address = request.form['account_address']
        process = subprocess.Popen(['solana', 'airdrop', '1', account_address, '--url', 'https://api.devnet.solana.com'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
        return render_template('index.html', message='Airdrop successful!!')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
