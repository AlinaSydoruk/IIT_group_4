from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/participant/<int:participant_id>')
def participant(participant_id):

    participant_data = {
        1: {'name': 'Костенко Павло Сергійович', 'age': 20, 'email': 'pashasonic10@gmail.com',
            'sex':'Чоловіча', 'country':'Австрія', 'city':'Відень'},
        2: {'name': 'Сидорук Аліна Костянтинівна', 'age': 19, 'email': 'sydorukalina2020@gmail.com',
            'sex':'Жіноча', 'country':'Швейцарія', 'city':'Люцерн'},
        3: {'name': 'Хижняк Валерія Валеріївна', 'age': 19, 'email': 'valeriia_khyzhniak@gmail.com',
            'sex': 'Жіноча', 'country':'Австрія', 'city':'Відень'}
    }
    participant_info = participant_data.get(participant_id)
    if not participant_info:
        return 'Учасник не знайдений'
    return render_template('participant.html', participant=participant_info)

if __name__ == '__main__':
    app.run(debug=True)
