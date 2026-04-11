🧠 Quiz Game — Day 17
A terminal-based true/false quiz game built in Python as part of Angela Yu's 100 Days of Code bootcamp.
Features

Sequential true/false questions loaded from a data file
Real-time score feedback after each answer
Case-insensitive answer checking
Final score summary on completion

Project structure
day-17/
├── main.py            # Entry point: builds the question bank and runs the quiz
├── data.py            # Raw question data (list of dicts)
├── question_model.py  # Question class (text + answer)
└── quiz_brain.py      # QuizBrain class (game logic, scoring, progression)
How to run
bashpython main.py
No external dependencies — standard library only.
Example session
Q. 1: A slug's blood is green. True or False? True
You got it right
The correct answer was: True
Your current score is 1/1.

Q. 2: The loudest animal is the African Elephant. True or False? True
You got it wrong :(
The correct answer was: False
Your current score is 1/2.

...

You've completed the quiz
Your final score was: 9/12
Course context
Built on Day 17 of 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu. Introduces object-oriented programming fundamentals: class definitions, __init__, instance attributes, and methods.
