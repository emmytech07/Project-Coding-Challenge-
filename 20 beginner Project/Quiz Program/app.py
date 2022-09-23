# Dictionary that stores questions and answer_challenge
# have a variable that tracks the score of the year
# loop thorugh the dictionary using the key values
# display each question to the user and allow them to anwer
# Tell them if they are right or wrong 
# show the final result when quiz is completed

quiz = {
    "Questions 1": {
        "Question" :"What is my age",
        "Answer": "22"
    },
    "Questions 2": {
        "Question" :"What is my Name",
        "Answer": "Hope"
    },
    "Questions 3": {
        "Question" :"What is my School",
        "Answer": "Joy International"
    },
    "Questions 4": {
        "Question" :"What is my friend name",
        "Answer": "Jesus"
    }
}

score = 0

for key, value in quiz.items():
    print(value["Question"])
    answer = input("Answer? ")

    if answer.lower() == value['Answer'].lower():
        print("Correct")
        score = score +1 
        print(f"Your score is: {score}")
        print()
    else:
        print("wrong!")
        print("The Answer is : " + value['Answer'])
        print("Your score is: "+ str(score))
        print()

print(f"you got {score} out of 4 questions correctly")
print("your Percentage score is: " + str(int(score/7 * 100) + "%"))