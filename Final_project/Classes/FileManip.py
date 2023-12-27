

class FileManip :
    def __init__(self):
        self.path = 'C:\\Users\\elhim\\OneDrive\\Desktop\\S3\\Python\\'
   


    def get_data(self,subject):
        with open(f"{self.path}{subject}.txt") as my_file:
            ques_list=my_file.readlines()
        ques_list = [ele.strip('\n') for ele in ques_list] 

        return ques_list
    