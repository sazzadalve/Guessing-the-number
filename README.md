A simple command-line number guessing game built with Python.
The computer randomly selects a number between 1 and 100, and the player must guess it within a limited number of attempts.

🚀 Features
🔢 Random number generation (1–100)
🎚️ Two difficulty levels:
Easy → 10 attempts
Hard → 5 attempts

📉 Hints after each guess (Too High / Too Low)
🏆 Win/Lose result system
🛡️ Input validation (optional improvement)

🛠️ Technologies Used
Python 3
random module

🧠 Game Rules
The computer selects a number between 1 and 100.
You must guess the correct number.
After each guess:
If guess > number → "Too High"
If guess < number → "Too Low"
If attempts reach 0 → You lose.

Project Structure
guess_game.py
README.md
📸 Example Output
I'm thinking of a number between 1 and 100.
Choose difficulty: 'easy' or 'hard': easy

You have 10 attempts remaining.
Make a guess: 50
Too high.

You have 9 attempts remaining.
Make a guess: 25
Too low.
🔮 Future Improvements
🔁 Add replay option
📊 Track high scores

🧠 Add difficulty levels (Medium mode)
🖥️ Convert to GUI (Tkinter)
🌐 Convert to Web App (Flask / Django)

👨‍💻 Author
Sazzad Hossen
Aspiring Python & Backend Developer
Building projects to improve problem-solving skills 🚀

⭐ Support
If you like this project, consider giving it a ⭐ on GitHub!