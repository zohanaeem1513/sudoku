# 🧩 Sudoku Solver

> A Python-powered Sudoku Solver that cracks any valid 9×9 puzzle using the classic **Backtracking Algorithm** — fast, elegant, and fully automated.

---

## 📖 About the Project

This project solves any valid 9×9 Sudoku puzzle programmatically. It recursively scans the board for empty cells, tests candidate digits against Sudoku's row, column, and 3×3 box rules, and **backtracks** whenever a guess leads to a dead end — repeating this process until the entire puzzle is solved.

It's a compact, readable demonstration of recursion and constraint-based problem solving in pure Python — no external libraries required.

---

## ✨ Features

- ✅ Solves **any valid 9×9 Sudoku puzzle** automatically
- 🔁 Implements the **Backtracking Algorithm** with recursion
- 🧠 Validates every guess against **row, column, and 3×3 box** constraints
- 🖥️ Clean, formatted **console output** of the board (before & after)
- ⚡ Lightweight — built with **pure Python**, zero dependencies
- 🧩 Easy to extend with your own puzzles

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Core programming language |

---

## 🐍 Python Concepts Used

- **Functions** — modular, single-responsibility design
- **Recursion** — the engine driving the solving process
- **Backtracking** — undoing invalid guesses to explore alternatives
- **2D Lists** — representing the 9×9 Sudoku grid
- **Nested Loops** — traversing rows, columns, and boxes
- **List Comprehensions** — concise board construction and validation
- **Type Hints** — improved readability and maintainability
- **Constants** — grid size and empty-cell markers
- **Tuples** — returning cell coordinates `(row, col)`
- **Conditional Statements** — rule validation and flow control
- **Modules** — clean, importable program structure

---

## 🧠 Algorithm Overview

The solver uses **Backtracking**, a depth-first search technique:

1. **Find** the next empty cell on the board.
2. **Try** digits `1–9` in that cell.
3. **Validate** each digit against Sudoku rules:
   - Not already in the same **row**
   - Not already in the same **column**
   - Not already in the same **3×3 box**
4. **Recurse** — if the digit is valid, move to the next empty cell.
5. **Backtrack** — if no digit works, reset the cell and return to the previous one.
6. **Repeat** until the board is completely filled.

```
Empty cell found? ──▶ Try 1–9 ──▶ Valid? ──▶ Recurse deeper
                                   │
                                   ▼ No
                              Backtrack ◀── Dead end
```

**Time Complexity:** `O(9^m)` in the worst case, where `m` is the number of empty cells.
**Space Complexity:** `O(m)` due to the recursion stack.

---

## 📁 Project Structure

```
SUDOKU SOLVER/
├── sudoku.py        # Main solver — backtracking logic & board display
├── README.md        # Project documentation
└── .gitignore       # Files excluded from version control
```

---

## 📋 Requirements

- **Python 3.8+**
- No external packages — runs on the standard library only 🎉

---

## ▶️ How to Run

```bash
python sudoku.py
```

That's it — the solver prints the original puzzle, solves it, and displays the completed board.

---

## 🖥️ Sample Output

```
Original Puzzle:
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9

Solved Puzzle: ✅
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

---

## 🎓 Learning Outcomes

Through this project, I strengthened my understanding of:

- Designing and implementing **recursive algorithms**
- Applying **backtracking** to constraint-satisfaction problems
- Modeling grid-based problems with **2D data structures**
- Writing **clean, modular, and type-hinted** Python code
- Analyzing **time and space complexity** of search algorithms


## 👩‍💻 Author

**Zoha**
*AI/ML Engineer | Python Developer*

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---

⭐ **If you found this project helpful, consider giving it a star!**
