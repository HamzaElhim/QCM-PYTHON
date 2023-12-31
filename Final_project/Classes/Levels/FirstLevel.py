from Classes.FileManip import FileManip



class FirstLevel:
    def __init__(self):
        self.file_data = FileManip()
        self.subject   = "Culture"

    def  getTrueAnswers(self,i, Quiz):
        """
        PARAMETERS :
            => first one is 'i' : represent the index where the quesion is located 
            => second is 'quiz' : represent the retrived list from the file
        ROLE :
            => print all answers of the question
            => store numbers of right answer in a list 

        RETURN :
            list of correct answer numbers 
        """
        trueAnswers = []        
        for j in range(i + 1, i + 5):
            if Quiz[j].endswith("*"):
                vtrue = Quiz[j].strip("*")
                trueAnswers.append(vtrue[0])
                print(vtrue)
            else:
                print(Quiz[j])
        return trueAnswers   
    

    def check_answer(self,answers):
        """
        PARAMETERS :
            => answers : represent the list of correct answers number
        ROLE :
            =>  accept input from the user
            =>  increment the score in case of correct answer

        """
        righ_answer = True
        for y in range(0,len(answers)):
            answer = input("==>")
            if(answer != answers[y]):
                righ_answer = False
        
        if(righ_answer):
            self.score+=1

    def diplay_quiz(self):
        """
        ROLE :
            => display quiz structure : questions +  final score 

        RETURN :
            dectionary of two element : user final score + quiz subject 
        """
        self.score     = 0
        Ins_file_data  = self.file_data.get_info(self.subject)
        print(f"=========== let's start the {self.subject} quiz ========")
        for i in range(0, len(Ins_file_data), 5):
            print(Ins_file_data[i])
            trueAnswers = self.getTrueAnswers(i,Ins_file_data)  
            self.check_answer(trueAnswers)

        return {'score':self.score,'subject':self.subject}


