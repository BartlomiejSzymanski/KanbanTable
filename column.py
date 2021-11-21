
import kanban_exception




class Column:
    '''
    Container class, holding a dictionary of assignment names (key),
    along with their priorities (value).
    '''
    def __init__(self, column_name):

        self.column_name_setter = column_name
        self.dict_of_asmts_setter = dict()



    @property
    def column_name(self):
        return self.__name
    # niepotrzebne, ale zostawiam
    @column_name.setter
    def column_name_setter(self,name):
        self.__name = name
    
    @property
    def dict_of_asmts(self):
        return self.__dict

    @dict_of_asmts.setter
    def dict_of_asmts_setter(self, argument):
        self.__dict = argument


    

    def add_assignment(self, name, priority):
        '''
        Takes name (str), and priority (str), and 
        adds a new key-value pair to dictionary
        '''
        #ew obsluga bledu        
        if  name in self.dict_of_asmts:
            #raise kanban_exception.Name_repetition
            print(f"{name} already in column")
        else:

            #new_assignment = assignment.Assignment(name, priority)
            self.dict_of_asmts.update({name : priority})

    
    def remove_assignment(self,name):
        '''
        Removes assignment with given name (str)
        from dict_of_asmts
        '''

        if  name in self.dict_of_asmts:
            self.dict_of_asmts.pop(name)
        else:
            pass


    

    def sort_by_name_asc(self):
        '''

        sorts assignments' names of dict_of_asmts 
        using sorted() function in ascending order

        '''
        list_of_keys = []
        for key in self.dict_of_asmts:
            list_of_keys.append(key)
        list_of_keys =sorted(list_of_keys)
        new_dict = {}
        for i in list_of_keys:
            new_dict.update({i : self.dict_of_asmts[i]})
        self.dict_of_asmts_setter = new_dict

    

    def sort_by_name_desc(self):
        '''
        sorts assignments' names of dict_of_asmts 
        using sorted() function in descending order

        '''
        list_of_keys = []
        for key in self.dict_of_asmts:
            list_of_keys.append(key)
        list_of_keys = sorted(list_of_keys)
        list_of_keys = reversed(list_of_keys)
        new_dict = {}
        for i in list_of_keys:
            new_dict.update({i : self.dict_of_asmts[i]})

        self.dict_of_asmts_setter = new_dict

    
    def sort_by_priority_desc(self):
        '''
        sorts assignments' priorities of dict_of_asmts 
        using sorted() function in descending order
        '''
        list_of_keys = []
        for key in self.dict_of_asmts:
            if self.dict_of_asmts[key] == "Important":
                list_of_keys.insert(0,key)
            else:
                list_of_keys.append(key)
        list_of_keys = reversed(list_of_keys)
        new_dict = {}
        for i in list_of_keys:
            new_dict.update({i : self.dict_of_asmts[i]})

        self.dict_of_asmts_setter = new_dict



    
    def sort_by_priority_asc(self):
        '''
        sorts assignments' priorities of dict_of_asmts 
        using sorted() function in ascending order
        '''
        list_of_keys = []
        for key in self.dict_of_asmts:
            if self.dict_of_asmts[key] == "Important":
                list_of_keys.insert(0,key)
            else:
                list_of_keys.append(key)

        new_dict = {}
        for i in list_of_keys:
            new_dict.update({i : self.dict_of_asmts[i]})

        self.dict_of_asmts_setter = new_dict

