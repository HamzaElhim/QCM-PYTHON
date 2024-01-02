from Classes.FileManip import FileManip

class Users :

    def __init__(self, firstName, lastName):
        self.file_data = FileManip()
        self.quiz_data = []
        self.firstName = firstName
        self.lastName  = lastName
    
    

    def setQuizData(self, QuizData):
        """
        PARAMETERS :
            => QuizData : represent the infomation of the quiz that the user passed
        ROLE :
            => get information about the passed quiz and store them in list
            => in case that the user passed the same quiz twice write the haghest score

        """
        if self.quiz_data != []:
            counter  = 0
            for i in range(len(self.quiz_data)):                
                if(self.quiz_data[i]['subject'] == QuizData['subject']):
                    counter += 1
                    if(QuizData['score'] >= self.quiz_data[i]['score']):
                        self.quiz_data[i]['score'] = QuizData['score']
            if(counter == 0):
                self.quiz_data.append(QuizData)
        else:
                self.quiz_data.append(QuizData)
                    

    def saveData(self):
        """
        ROLE :
            => store all user information in list 
            => store this information in a file
            
        """
        user_data=[self.firstName, self.lastName]
        for element in self.quiz_data :
            user_data.append(f" {element['subject']} : {element['score']} ")
        
        self.file_data.write_user_data(" ; ".join(user_data))



            
    def getUserInfo(self):
        print(f"FirstName : {self.firstName}")
        print(f"LastName : {self.lastName}")
        for element in self.quiz_data:
            print(f"Topic : {element['subject']} = > Score : {element['score']}")
