quiz = {
    "question1" : {
        "question" : "What is the capital of India?",
        "answer" : "Delhi"
    },
    "question2" : {
        "question" : "What is the capital of Japan?",
        "answer" : "Tokyo"
    }
}
score = 0
totalQuestions = 0
for key, value in quiz.items():
    print(value['question'])
    totalQuestions = totalQuestions + 1

    answer = input("Answer :- ")
    
    if(answer.lower() == value['answer'].lower()):
        score = score + 1
        print("Your score is = ", score)
    else:
        print("Your score is = ", score)

print("Your final score in percentage is = ", (int)((score/totalQuestions)*100),"%")


