from Classes.Users import Users
from Classes.Levels.FirstLevel  import FirstLevel
from Classes.Levels.SecondLevel import SecondLevel
from Classes.Levels.ThirdLevel import ThirdLevel



def getIndent():
    return "            =========================="
def getMenu():
    print(getIndent() + "===================================")
    print(getIndent() + "======== Menu ====================")
    print(getIndent() + " 1 : Start Quiz")
    print(getIndent() + " 2 : Show My information")
    print(getIndent() + " 3 : Show System Roles")
    print(getIndent() + " 4 : Quiet from program")



def getTopic():
    print("============================")
    print("1 : Culture") #represente the level 1
    print("2 : Science") #represente the level 2
    print("3 : Sport ")  #represente the level 3

def getRules():
    print( getIndent() + "=========================================")
    print( getIndent() + "======= System Rules ====================")
    print( getIndent() + "==> Users should use numbers as input.")
    print( getIndent() + "==> Users can Repeat the quiz & the largest score will be taken.")
    print( getIndent() + "==> User data will be saved in separated file.")

     

    

print(getIndent() +" Welcome to Your Quiz ====================")
firstName = input(getIndent() + " Enter your first name : ")
lastName  = input(getIndent() + " Enter your last name  : ")
User = Users(firstName, lastName)

operation = 0
levels = [FirstLevel(), SecondLevel(),ThirdLevel()]
while True :
    if operation not in range(1, 5):
        getMenu()
        operation = int(input("Choose your operation : "))
    elif operation == 1:
        topic = 0
        while topic not in range(1, 4):
            getTopic() 
            topic = int(input("> Choose your topic : "))
        dect_quiz_info=levels[topic - 1].diplay_quiz() 
        print("Your sccore is : ", dect_quiz_info['score']) 
        User.setQuizData(dect_quiz_info)
        getMenu()
        operation = int(input("> Choose your operation : "))  
    elif operation == 2:
        User.getUserInfo()
        getMenu()
        operation = int(input("> Choose your operation : "))
    elif operation == 3:
        getRules()
        getMenu()
        operation = int(input("> Choose your operation : "))
    elif operation == 4:
        User.saveData()
        break



