from flask import Flask, render_template
import os

# Caminho para o diretório de templates
template_dir = os.path.abspath('pages')
app = Flask(__name__, template_folder=template_dir)

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)