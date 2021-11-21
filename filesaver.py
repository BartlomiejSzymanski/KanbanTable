import json
import os

class FileSaver:
    '''
    Class responsible for file operations.
    '''
    def __init__(self,filename):
        self.__file = filename
        with open(self.__file, "w+") as ff:
            ff.close()

    def save_to_file(self,Table):
        '''
        Takes Table object and saves dict_of_asmts from each Column object within list_of_col

        '''
        with open(self.__file, "w+") as ff:
            for column in Table.list_of_col:
                line = str(column.dict_of_asmts) + "LF"
                ff.write(str(line))
            ff.close()    
                
    def get_from_file(self,table):
        '''
        Reads str() from file and separates it by "LF" keyword into each dict_of_asmts of Column type  inside Table
        '''
        with open(self.__file, "r") as ff:
                package = ff.read()
                lines = package.split("LF")
                lines.pop()
                colnum = 0
                
                for line in lines:
                    line = line.replace("'", '"')
                    
                    if line != '':
                        line = json.loads(line)
                    else:
                        line = dict()    
                    
                    table.list_of_col[colnum].dict_of_asmts_setter = line
                    colnum += 1
                

    
    def get_dict_from_file(self):
        '''
        Formats file contents with json.loads()
        '''
        with open(self.file, "r") as ff:
            data = ff.read()
            data = data.replace("'", '"')
            if data != '':
                file_dict = json.loads(data)
            else:
                file_dict = dict()
                 
            ff.close
        return file_dict 
