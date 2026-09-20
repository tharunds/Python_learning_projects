import random
quiz_data = {
    "What is the keyword used to define a function in Python?": "def",
    "Which data type is immutable: a list or a tuple?": "tuple",
    "What method removes all items from a dictionary?": "clear",
    "What operator checks if a key exists in a dictionary?": "in",
    "What exception is raised when accessing a missing key via brackets?": "KeyError",
    "What is the default return value of a function that doesn't have a return statement?": "None",
    "Which built-in function returns the number of items in a dictionary?": "len",
    "What character is used to start a single-line comment in Python?": "#",
    "What is the name of the method used to add an item to the end of a list?": "append",
    "Which file extension is standard for Python source files?": ".py"
}
def python_trivia_game():
    
    question_list=list(quiz_data.keys())
    total_question=5
    score=0
    selected_question=random.sample(question_list,total_question)

    for i,question in enumerate(selected_question):
        print(f"{i+1} {question}")
        answer=input("enter your answer").lower().strip()
        if answer==quiz_data[question].lower():
            score=score+1
        else:
            print(f"wrong answer the correct answer is {quiz_data[question].lower()}")
    if(score>3):
        print("------congratulation------ ")
        print("your score=",score)
    else:
        print("--better luck next time---")
        print("your score=",score)
python_trivia_game()

