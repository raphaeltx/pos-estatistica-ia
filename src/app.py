from flask import Flask, render_template
import os

# Caminho para o diretório de templates
template_dir = os.path.abspath('pages')
app = Flask(__name__, template_folder=template_dir)

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)