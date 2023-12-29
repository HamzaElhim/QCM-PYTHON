from Classes.Levels.SecondLevel import SecondLevel

class ThirdLevel(SecondLevel):

    def __init__(self):
        super().__init__()
        self.subject   = "Sport"
        print(self.file_data)
        # self.manipulateData()
        # print(self.file_data)

   

    def manipulateData(self, file_data): 
            NewList = []      
            j = 0
            for i in range(len(file_data)):
                if file_data[i].endswith('?'):
                    NewList.append(" ".join(file_data[ j : i + 1 ]))
                    j = i + 1
                elif file_data[i].endswith('.') or file_data[i].endswith('*'):
                    NewList.append(" ".join(file_data[ j : i + 1 ]))
                    j = i + 1

            return NewList


    def diplay_quiz(self):
        self.score     = 0
        Ins_file_data  = self.manipulateData(self.file_data.get_info(self.subject))

        listRandom = [i for i in range(0, len(Ins_file_data), 5)]
        print(listRandom)
        for i in range(1, 6):
            randomvalue = self.random_index(listRandom)
            ourdatal = Ins_file_data[randomvalue][3:]
            print(f"Q-{i }: {ourdatal}")
            trueAnswers = self.getTrueAnswers(randomvalue, Ins_file_data)                              
            self.check_answer(trueAnswers)

        return {'score':self.score,'subject':self.subject}        
      
