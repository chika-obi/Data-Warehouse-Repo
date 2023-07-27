import random

# Define the questions and their options with correct answers
questions = {
    "What is the capital of France?": {
        'options': ['A. London', 'B. Paris', 'C. Rome', 'D. Madrid'],
        'answer': 'B'
    },
    "Which planet is known as the Red Planet?": {
        'options': ['A. Venus', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
        'answer': 'B'
    },
    "Who painted the Mona Lisa?": {
        'options': ['A. Vincent van Gogh', 'B. Pablo Picasso', 'C. Leonardo da Vinci', 'D. Claude Monet'],
        'answer': 'C'
    },
}

# Randomly select a question from the dictionary
question = random.choice(list(questions.keys()))

# Display the selected question and its options
print(question)
for option in questions[question]['options']:
    print(option)

# Prompt the user to enter their answer
answer = input("Enter the letter corresponding to your answer: ")

# Convert the user's answer to uppercase for consistency
answer = answer.upper()

# Check if the user's answer is correct
if answer == questions[question]['answer']:
    print("Correct! Great job.")
else:
    print("Sorry, that's incorrect.")