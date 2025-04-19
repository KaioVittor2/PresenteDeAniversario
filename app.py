import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Carrega relacionamentos e mídia

def get_momentos():
    fotos_dir = os.path.join(app.static_folder, 'fotos')
    arquivos = sorted([
        f for f in os.listdir(fotos_dir)
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4'))
    ])
    momentos = []
    for f in arquivos:
        nome = os.path.splitext(f)[0]
        texto = f"Aqui está nosso momento '{nome.replace('_', ' ')}'. Foi incrível viver isso com você!"
        momentos.append({
            'arquivo': f,
            'nome': nome.replace('_', ' '),
            'texto': texto
        })
    return momentos

# Injeta playlist de áudio em todas as rotas
@app.context_processor
def inject_audio_playlist():
    audio_dir = os.path.join(app.static_folder, 'audio')
    arquivos = sorted([
        f for f in os.listdir(audio_dir)
        if f.lower().endswith(('.mp3', '.wav', '.ogg'))
    ])
    urls = [url_for('static', filename=f'audio/{f}') for f in arquivos]
    return dict(audio_playlist=urls)

@app.route('/')
def home():
    return render_template('home.html', title='Início')

@app.route('/linha-do-tempo')
def linha_do_tempo():
    momentos = get_momentos()
    return render_template('linha_do_tempo.html', title='Linha do Tempo', momentos=momentos)

@app.route('/cartas')
def cartas():
    return render_template('cartas.html', title='Cartas')

@app.route('/playlists')
def playlists():
    return render_template('playlists.html', title='Playlists')

@app.route('/nosso-futuro')
def nosso_futuro():
    return render_template('nosso_futuro.html', title='Nosso Futuro')

if __name__ == '__main__':
    app.run(debug=True)
