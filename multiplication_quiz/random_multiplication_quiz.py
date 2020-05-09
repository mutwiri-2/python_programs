#! python3

# random_multiplication_quiz.py - a program to randomly ask multiplication questions and count the number of correct answers given by user

import random, pyinputplus as pyip, time

number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = f"Question {question_number+1}: {num1} * {num2} = __\n"

    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$'%(num1*num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print("You ran out of time!")
    except pyip.RetryLimitException:
        print("You ran out of attempts!")
    else:
        print("Good that's the Correct answer!")
        correct_answers += 1
    time.sleep(1)
print(f"You got {correct_answers} correct out of a possible {number_of_questions}")