from Classes.Users import Users
from Classes.Levels.FirstLevel  import FirstLevel
from Classes.Levels.SecondLevel import SecondLevel
from Classes.Levels.ThirdLevel import ThirdLevel




def getMenu():
    
    print("============================")
    print("======== Menu ===========")
    print("1 : Start Quiz")
    print("2 : Show My information")
    print("3 : Show System Roles")
    print("4 : Quiet from program")



def getTopic():
    print("============================")
    print("1 : Culture") #represente the level 1
    print("2 : Science") #represente the level 2
    print("3 : Sport ")  #represente the level 3

def getRules():
    print("============================")
    print("======= System Rules ======")
    print("==> Users should use numbers as input.")
    print("==> Users can Repeat the quiz & the largest score will be taken.")
    print("==> User data will be saved in separated file.")

     




    

print("================== Welcome to Your Quiz ==============")
firstName = input("Enter your first name : ")
lastName  = input(" Enter your last name  : ")
User = Users(firstName, lastName)

operation = 0
levels = [FirstLevel(), SecondLevel(),ThirdLevel()]
while True:
    if operation not in range(1, 5):
        getMenu()
        operation = int(input("Choose your operation : "))
    elif operation == 1:
        topic = 0
        while topic not in range(1, 4):
            getTopic() #topic
            topic = int(input("Choose your topic : "))
        dect_quiz_info=levels[topic - 1].diplay_quiz() 
        print("Your sccore is : ", dect_quiz_info['score']) 
        User.setQuizData(dect_quiz_info)
        getMenu()
        operation = int(input("Choose your operation : "))  
    elif operation == 2:
        User.getUserInfo()
        getMenu()
        operation = int(input("Choose your operation : "))
    elif operation == 3:
        getRules()
        getMenu()
        operation = int(input("Choose your operation : "))
    elif operation == 4:
        User.saveData()
        break



