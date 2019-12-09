from flask import Flask, render_template, request
import requests

KEY = 'trnsl.1.1.20180210T063150Z.887a84b1ad9e07eb.a4320e54acdfe84f353c1532a2d97186c7a6e50c'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate(text, lang, res_lang) -> str:
    '''Translate text from lang to res_lang with Yandex Translate API'''
    params = {'key': KEY,
              'text': text,
              'lang': '{}-{}'.format(lang, res_lang)
              }
    response = requests.get(url, params=params)
    translated_text = response.json()['text']
    return ' '.join(translated_text)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.form['text']
    lang = request.form['text_language_select']
    res_lang = request.form['language_for_translation']
    translated_text = translate(text, lang, res_lang)
    return render_template('index.html',
                           text=text,
                           translated_text=translated_text)

if __name__ == '__main__':
    app.run()