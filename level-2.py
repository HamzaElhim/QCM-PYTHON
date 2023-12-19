import random as ra


with open('C:\\Users\\elhim\\OneDrive\\Desktop\\S3\\Python\\quizQuestions.txt','r') as my_file:
    ques_list=my_file.readlines()

def check_answer(answers,score):
    righ_answer=True
    for y in range(0,len(answers)):
        answer=int(input("==>"))
        if(answer not in answers):
            righ_answer=False
            break
        else :
            answers.remove(answer)
    
    if(righ_answer):
         score+=1
    return score


def random_index(arr):
    my_random=ra.choice(arr)
    arr.remove(my_random)
    return my_random



score=0
arr_quesions=[0,5,10,15,20]



for i in range(1,6) :
    arr_answers=[1,2,3,4]
    random_num_qus=random_index(arr_quesions)
    question=ques_list[random_num_qus][3:].strip()
    print(f"Q-{i}: {question}")
    answers=[]
    for j in range(1,5):
        random_num_ans=random_index(arr_answers)
        answ=ques_list[random_num_qus+random_num_ans][2:]
        if(ques_list[random_num_qus+random_num_ans].strip()[-1]=="*"):
            answers.append(j)
            print(f"{j}-{answ.strip('*\n')}")
        else :
            print(f"{j}-{answ.strip()}")
    

    score=check_answer(answers,score)

print(f"your score is => '{score}' points ")
