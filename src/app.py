from flask import Flask, render_template
import os

# Obter o diretório atual do arquivo app.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho para o diretório de pages
template_dir = os.path.join(current_dir, 'pages')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)