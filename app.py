from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Route for the home page (game interface)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle game logic after player chooses
@app.route('/play', methods=['POST'])
def play():
    # Get the player's choice from the form
    user_choice = request.form['choice']
    
    # List of possible choices
    choices = ['rock', 'paper', 'scissors']
    
    # Randomly choose the server's choice
    server_choice = random.choice(choices)

    # Determine the winner
    result = determine_winner(user_choice, server_choice)

    return render_template('index.html', user_choice=user_choice, server_choice=server_choice, result=result)

# Function to determine the winner
def determine_winner(user_choice, server_choice):
    if user_choice == server_choice:
        return 'It\'s a tie!'
    elif (user_choice == 'rock' and server_choice == 'scissors') or \
         (user_choice == 'scissors' and server_choice == 'paper') or \
         (user_choice == 'paper' and server_choice == 'rock'):
        return 'You win!'
    else:
        return 'You lose!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

