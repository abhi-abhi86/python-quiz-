#-------------------------------
def run_quiz():
    """
    Main function to run the quiz.
    """
    guesses = []
    correct_guesses = 0
    question_num = 0

    for question in questions:
        print("\n----------------------------------------------")
        print(f"Q{question_num + 1}: {question}")
        for option in options[question_num]:
            print(option)

        while True:
            guess = input("Choice (A, B, C, D): ").strip().upper()
            if guess in ['A', 'B', 'C', 'D']:
                break
            else:
                print("❌ Invalid input! Please enter A, B, C, or D only.")

        guesses.append(guess)
        correct_guesses += check_answer(questions[question], guess)
        question_num += 1

    display_score(correct_guesses, guesses)
    play_again()

#-------------------------------
def check_answer(answer, guess):
    """
    Compares user's guess with the correct answer.
    """
    if answer == guess:
        print("✅ CORRECT!")
        return 1
    else:
        print("❌ WRONG!")
        return 0

#-------------------------------
def display_score(correct_guesses, guesses):
    """
    Shows final result and score.
    """
    print("\n----------------------------------------------")
    print("📊 Quiz Results")
    print("----------------------------------------------")

    print("Correct Answers: ", end="")
    for ans in questions.values():
        print(ans, end=" ")

    print("\nYour Guesses:     ", end="")
    for g in guesses:
        print(g, end=" ")

    score = (correct_guesses / len(questions)) * 100
    print(f"\n\n🎯 Your Score: {score:.2f}%")

#-------------------------------
def play_again():
    """
    Asks user if they want to play again.
    """
    again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if again in ['yes', 'y']:
        run_quiz()
    else:
        print("👋 Thanks for playing!")

#-------------------------------
# Questions and Options
questions = {
    "Who is the current Prime Minister of India?": "D",
    "Is the Earth round?": "A",
    "Who is the President of India?": "A",
    "Do you have a brain?": "D",
    "Who won the Miss Universe title for India in 2021?": "B",
    "In what year did the Great October Socialist Revolution take place?": "C"
}

options = [
    ["A. Guido van Rossum", "B. Mahatma Gandhi", "C. Rohit Sharma", "D. Narendra Modi"],
    ["A. Yes", "B. No", "C. Maybe", "D. It's square"],
    ["A. Droupadi Murmu", "B. Ram Nath Kovind", "C. Narendra Modi", "D. Ram Nath Kovind"],
    ["A. Yes", "B. No", "C. Maybe", "D. I have a cell"],
    ["A. Lara Dutta Bhupathi", "B. Harnaaz Sandhu", "C. Urvashi Rautela", "D. Rhea Singha"],
    ["A. 1918", "B. 1928", "C. 1917", "D. 1916"]
]

#-------------------------------
# Run the quiz
run_quiz()
