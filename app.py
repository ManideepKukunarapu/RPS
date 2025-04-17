from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

options = ['Rock', 'Paper', 'Scissors']

def get_winner(user, computer):
    if user == computer:
        return "tied"
    elif (user == 'Rock' and computer == 'Scissors') or \
         (user == 'Paper' and computer == 'Rock') or \
         (user == 'Scissors' and computer == 'Paper'):
        return "win"
    else:
        return "lose"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json['choice']
    computer_choice = random.choice(options)
    result = get_winner(user_choice, computer_choice)
    return jsonify({
        'computer': computer_choice,
        'result': result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
