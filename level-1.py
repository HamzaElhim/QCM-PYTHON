with open('C:\\Users\\elhim\\OneDrive\\Desktop\\S3\\Python\\quizQuestions.txt','r') as my_file:
    ques_list=my_file.readlines()

def check_answer(answers,score):
    righ_answer=True
    for y in range(0,len(answers)):
        answer=input("==>")
        if(answer!=answers[y]):
            righ_answer=False
    
    if(righ_answer):
         score+=1
    return score



score=0
for i in range(0,len(ques_list),5):
    print(ques_list[i].strip())
    answers=[]
    for j in range(1,5):
        if(ques_list[i+j].strip()[-1]=="*"):
            answers.append(ques_list[i+j][0])
            print(ques_list[i+j].strip('*\n'))
        else :
            print(ques_list[i+j].strip())
    
    score=check_answer(answers,score)

print(f"your score is => '{score}' points ")
