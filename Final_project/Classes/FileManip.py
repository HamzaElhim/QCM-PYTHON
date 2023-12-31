class FileManip :
    def __init__(self):
        self.path = 'C:\\Users\\pc\\Documents\\SecondYear\\Programs\\New folder\\QCM-PYTHON\\Final_project\\Data\\'
        
    def get_info(self, subject):
        with open(f"{self.path}{subject}.txt") as my_file:
            ques_list=my_file.readlines()
        ques_list = [ele.strip('\n') for ele in ques_list] 
        return ques_list 
    
    def write_user_data(self,userData):
        with open(f"{self.path}UsersData.txt",'a') as my_file:
            my_file.write(f'\n{userData}')
    