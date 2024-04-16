from flask import Flask, render_template, request
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_word', methods=['POST'])
def add_word():
    word = request.form['word2']
    translation = request.form['translation']
    cache.set(word, translation)
    print(f"Added word: {word}, Translation: {translation}")
    return render_template('add_word_result.html')

@app.route('/translate', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        word = request.form['word1']
        translation = cache.get(word)
        if translation:
            translation = translation.decode('utf-8')  # Декодуємо байтовий рядок в рядок Unicode
            return render_template('result.html', word1=word, translation=translation)
        else:
            return render_template('result.html', word1=word, translation="Translation not found")

if __name__ == '__main__':
    app.run(debug=True)
