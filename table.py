import column 
import kanban_exception



class Table:
    '''
    Container class, holds a list() of Column type objects
    '''
    def __init__(self):
  
        self.list_of_col_setter = list()
        Finished = column.Column("Finished")
        InProgress = column.Column("In Progress")
        ToDo = column.Column("To Do")

        self.list_of_col.append(ToDo)
        self.list_of_col.append(InProgress)
        self.list_of_col.append(Finished)

    @property
    def list_of_col(self):
        return self.__list_of_col

    @list_of_col.setter 
    def list_of_col_setter(self, list_of_col):
        self.__list_of_col = list_of_col


    def shift_assignment(self,name, col_num):
        '''
        Takes name (str) and current column index col_num (int)
        If next column index within range, shifts assignment
        to newly selected column
        '''
        
        list_of_columns = self.list_of_col
        current_dict = list_of_columns[col_num].dict_of_asmts

        if name in current_dict:
            priority = current_dict[name]
            
            if col_num + 1 <= 2:
                list_of_columns[col_num + 1].add_assignment(name,priority)
                list_of_columns[col_num].remove_assignment(name)
            else:
                raise kanban_exception.Last_Column

