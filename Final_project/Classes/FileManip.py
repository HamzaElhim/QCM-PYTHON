class FileManip :
    def __init__(self):
        self.path = 'C:\\Users\\pc\\Documents\\SecondYear\\Programs\\New folder\\QCM-PYTHON\\Final_project\\Data\\'
        
    def get_info(self, subject):
        """
        PARAMETERS :
            => subject : the selected subject that the user once to take a quiz in
        ROLE :
            => get the quiz from of the selected subject from the file

        RETURN :
            list of questions
        """
        with open(f"{self.path}{subject}.txt") as my_file:
            ques_list=my_file.readlines()
        ques_list = [ele.strip('\n') for ele in ques_list] 
        return ques_list 
    
    def write_user_data(self, userData):
        """
        PARAMETERS :
            => userData : the user information : firstName - lastName - quiz subjects and score that the user take
        ROLE :
            => write infomation of the user in a file

        """
        with open(f"{self.path}UsersData.txt",'a') as my_file:
            my_file.write(f'\n{userData}')
    