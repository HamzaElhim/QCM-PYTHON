from Classes.Levels.FirstLevel import FirstLevel
import random as ra

class SecondLevel(FirstLevel):
    def __init__(self):
        super().__init__()
        self.subject   = "Science"

    def random_index(self, arr):
        my_random = ra.choice(arr)
        arr.remove(my_random)
        return my_random
    
    def getTrueAnswers(self, i, Quiz):
        trueAnswers = []    
        listRandomAns = [1, 2, 3, 4]    
        for j in range(1, 5):
            randomvalueAns = self.random_index(listRandomAns)
            ourdata = Quiz[randomvalueAns + i]
            Quiz[randomvalueAns + i] = str(j) + " - " + ourdata[2:]
            if Quiz[randomvalueAns + i].endswith("*"):
                vtrue = Quiz[randomvalueAns + i ].strip("*")
                trueAnswers.append(vtrue[0])
                print(vtrue)
            else:
                print(Quiz[randomvalueAns + i])          
        return trueAnswers           

    def diplay_quiz(self):
        self.score     = 0
        Ins_file_data  = self.file_data.get_info(self.subject)
        listRandom = [i for i in range(0, len(Ins_file_data), 5)]
        for i in range(0, len(Ins_file_data), 5):
            randomvalue = self.random_index(listRandom)
            ourdatal = Ins_file_data[randomvalue][3:]
            print(f"Q-{i }: {ourdatal}")
            trueAnswers = self.getTrueAnswers(randomvalue, Ins_file_data)                              
            self.check_answer(trueAnswers)

        return {'score':self.score,'subject':self.subject}
