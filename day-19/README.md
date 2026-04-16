# 🐢 Day 19 – Turtle Race

A betting game built with Python's `turtle` module. Five coloured turtles race across the screen — place your bet before the race starts and see if your turtle wins.

Part of my progress through Angela Yu's [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/).

---

## How it works

1. A dialog box asks you to bet on a turtle colour (`red`, `blue`, `green`, `yellow`, `purple`)
2. Press **W** to start the race
3. Each turtle advances by a random amount each step
4. The first turtle to cross the finish line (x > 200) wins
5. The result is printed in the terminal

---

## What I practised

- `turtle` module — multiple independent `Turtle` instances, `penup()`, `goto()`, `forward()`
- Event-driven programming — `screen.onkey()` with a function reference (not a call)
- Dictionaries — storing and querying turtle positions by colour name
- `max()` with `key=` — finding the winner elegantly
- `any()` with `.values()` — checking finish condition across all turtles
- Separating game logic into functions (`race`, `check_positions`)

---

## Design note

Angela Yu's version uses a `for` loop with a single `Turtle` instance reused across a list. I chose to instantiate each turtle independently for clarity — the tradeoff is slightly more verbose setup code, but each turtle's identity is explicit and there's no shared state to reason about.

---

## Usage

```bash
python main.py
```

Requires Python 3 with the standard `turtle` module (no external dependencies).

---

## Project structure

```
day-19/
└── main.py
```
