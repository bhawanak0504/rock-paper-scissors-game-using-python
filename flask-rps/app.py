from flask import Flask, render_template, request
import random

app = Flask(__name__)

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "win"
    else:
        return "lose"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    player_choice = request.form['choice']
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    return render_template('index.html', user_choice=player_choice, computer_choice=computer_choice, result=result)

if __name__ == '__main__':
    app.run(debug=True)