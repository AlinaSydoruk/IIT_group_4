from flask import Flask, render_template, request
import redis

app = Flask(__name__)
try:
    cache = redis.Redis(host='redis', port=6379)
except Exception as e:
    print(f"Error connecting to Redis: {e}")
    cache = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_word', methods=['POST'])
def add_word():
    try:
        word = request.form['word2']
        translation = request.form['translation']
        if cache:
            cache.set(word, translation)
            print(f"Added word: {word}, Translation: {translation}")
            return render_template('add_word_result.html')
        else:
            return "Error: Cache is not available"
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/translate', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        try:
            word = request.form['word1']
            if cache:
                translation = cache.get(word)
                if translation:
                    translation = translation.decode('utf-8')  # Декодуємо байтовий рядок в рядок Unicode
                    return render_template('result.html', word=word, translation=translation)
                else:
                    return render_template('result.html', word=word, translation="Translation not found")
            else:
                return "Error: Cache is not available"
        except Exception as e:
            return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
