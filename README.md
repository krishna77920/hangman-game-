Hangman Game, Python Console Version

Overview  
This project is a console-based Hangman game written in Python. The player tries to guess a randomly selected word, one letter at a time, before running out of lives. The game features ASCII-art hangman visuals, checks for valid input, and includes a large word list to keep the gameplay interesting.

Features  

- Random word selection from an extensive word list  
- ASCII hangman graphics displayed as lives decrease  
- Input validation (letters only, no repeats, single character)  
- Life-based gameplay with clear visual indicators  
- Win/Loss detection with final word reveal  
- Simple, clean game loop suitable for beginners and study  

Technologies / Tools Used  

- Python 3.x  
- Standard Library (no external dependencies)  
- Random module for word selection  
- Input() for user interaction  
- ASCII-art for visualization  

Works on:  

- Windows Terminal  
- macOS Terminal  
- Linux Shell  
- VS Code / PyCharm terminal  

Steps to Install & Run the Project  
1. Install Python  
Download from: https://www.python.org/downloads/  
Make sure Python is added to your system PATH.  
2. Download the project  
Option A: Clone the repository  
git clone <your-repository-url>  

Option B: Download ZIP and extract it.  
3. Navigate to the project folder  
cd hangman  

4. Run the game  
python hangman.py  

(or use python3 depending on your system)  

Instructions for Testing  
You can test the program by checking the following behaviors:  
Functional Tests  

- Game starts correctly  
It should ask for your name and greet you.  

- Letter guessing works  
Correct letters reveal their positions.  
Incorrect letters reduce lives.  

- Input validation  
Entering more than one character shows an error.  
Entering digits or symbols is rejected.  
Guessing the same letter twice shows a warning.  

- Win condition  
Guess all letters → game displays “YOU WON.”  

- Lose condition  
Reach 0 lives → full hangman displayed + “YOU LOSE” message.  

- Word display update  
Letters appear as _ until correctly guessed.  

Edge Case Tests  

- Press Enter without typing anything  
- Guess uppercase letters (should still work due to .lower())  
- Word with repeated letters (e.g., “banana”) shows all occurrences  

If all behaviors match expected results, the program is functioning correctly.  

If you want, I can also create:  
- A GitHub-optimized README with badges, screenshots, sections, and formatting  
- An MIT license file  
- A version with installation via pip  
- A more advanced Hangman (colors, difficulty levels, GUI)  

Just let me know! 
