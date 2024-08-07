<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number Guessing Game - README</title>
</head>
<body>
    <h1>Number Guessing Game</h1>
    <p>Welcome to the Number Guessing Game! This is a simple Python game where the player tries to guess a randomly selected number between 1 and 100.</p>
    
    <h2>File Structure</h2>
    <pre>
    NumberGuessingGame/
    ├── main.py
    ├── game_logic.py
    ├── user_input.py
    └── number_generator.py
    </pre>
    
    <h2>Files Description</h2>
    <ul>
        <li><strong>main.py</strong>: The entry point of the program. It calls the <code>play_game</code> function to start the game.</li>
        <li><strong>game_logic.py</strong>: Contains the main game logic. It uses the <code>generate_number</code> function to generate a random number and the <code>get_user_input</code> function to get input from the user.</li>
        <li><strong>user_input.py</strong>: Handles user input. It ensures the input is a valid number and prompts the user to enter a valid number if the input is invalid.</li>
        <li><strong>number_generator.py</strong>: Generates a random number between 1 and 100 using the <code>random.randint</code> function.</li>
    </ul>
    
    <h2>How to Run</h2>
    <p>Follow these steps to run the Number Guessing Game:</p>
    <ol>
        <li>Ensure you have Python installed on your system. You can download it from <a href="https://www.python.org/downloads/">here</a>.</li>
        <li>Clone or download the NumberGuessingGame project to your local machine.</li>
        <li>Navigate to the project directory in your terminal or command prompt.</li>
        <li>Run the following command to start the game:</li>
    </ol>
    <pre>
    python main.py
    </pre>
    
    <h2>Game Instructions</h2>
    <p>When you run the game, you will be prompted to guess a number between 1 and 100. After each guess, the game will tell you whether your guess was too low, too high, or correct. Keep guessing until you find the correct number. The game will also keep track of the number of attempts you made.</p>
    
    <h2>Example</h2>
    <pre>
    Welcome to the Number Guessing Game!
    Try to guess the number between 1 and 100.
    Your guess: 50
    Too low! Try a higher number.
    Your guess: 75
    Too high! Try a lower number.
    Your guess: 62
    Congratulations! The correct number was 62.
    You guessed it in 3 attempts.
    </pre>
    
    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>
