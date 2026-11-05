import random
import operator


def generate_math_problem(min_val=1, max_val=10):

    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul
    }

    num1 = random.randint(min_val, max_val)
    num2 = random.randint(min_val, max_val)
    symbol = random.choice(list(operations.keys()))

    if symbol == "-" and num1 < num2:
        num1, num2 = num2, num1

    operation_function = operations[symbol]
    correct_answer = operation_function(num1, num2)

    problem_text = f"{num1} {symbol} {num2}"

    return problem_text, correct_answer

if __name__ == "__main__":
    print("Welcome to the Random Math Quiz! (Type 'exit' to quit)\n")

    while True:
        problem, answer = generate_math_problem()

        user_input = input(f"What is {problem}? ")
        if user_input.strip().lower() == 'exit':
            print("Thanks for playing!")
            break

        try:
            if int(user_input) == answer:
                print("✅ Correct!")
            else:
                print(f"❌ Incorrect. The correct answer was {answer}.")
        except ValueError:
            print("Please enter a valid integer.")
