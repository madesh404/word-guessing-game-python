# Word Guessing Game (Python)

A simple command-line word guessing game inspired by Hangman and Wordle.  
The game randomly selects a **5-letter English word** from a word list, and the player must guess the word one letter at a time with a limited number of attempts.

---

## 🔧 Features

- Uses a list of **valid 5-letter English words**
- Randomly selects a secret word each game
- Player guesses one letter at a time
- Shows which letters have been correctly guessed
- Tracks remaining attempts (default: 6)
- Clean, simple command-line interface

---

## 📂 Project Structure

```
Word Guessing Game/
├── word_guessing_game.py           
├── 5-letter-words.txt     
└── README.md          
```
- **main.py** — the game logic  
- **5-letter-words.txt** — list of 5-letter English words  
- **README.md** — project documentation (this file)

---

## ▶️ How to Run

1. Make sure you have **Python 3** installed.
2. Clone or download the project.
3. Navigate to the project directory in your terminal:

```bash
cd "Word Guessing Game"
python word_guessing_game.py

---

## 📜 How the Game Works

You start with 6 attempts.
Enter one letter per guess.
If the letter is in the word, all positions of that letter are revealed.
If the letter is not in the word, you lose an attempt.
The game ends when:
    ✅ You guess all letters (win), or
    ❌ You run out of attempts (lose)


## 📘 Word List Source

The file 5-letter-words.txt contains a large list of common English 5-letter words.
You can replace or expand this list with any 5-letter dictionary.

## ✨ Future Improvements (Optional Ideas)

- Wordle-style colored feedback (green/yellow/gray)

- Track used letters

- Add scoring or difficulty modes

- GUI version using Tkinter or PyGame

- Web version using Flask / React

## 📜 License

MIT License. Free to use for learning or projects.

---
