
import column
import table
import filesaver




class Application:
    '''
    Controller class, connects modules column, table, filesaver together.
    Communicates with UI, decorates and uses methods from given modules
    '''
    def __init__(self):
        self.__KanbanTable = table.Table()
        self.__saver = filesaver.FileSaver("kanban_data.txt")
        


    @property
    def kanban_table(self):
        return self.__KanbanTable

    @kanban_table.setter
    def kanban_table_setter(self, table_object):
        self.kanban_table = table_object


    @property
    def filesaver(self):
        return self.__saver
    @filesaver.setter
    def filesaver(self, filename):
        self.__saver = filesaver.FileSaver(filename)


    def add_assignment(self,name, priority):
        '''
        Creates new name (key) - priority (value) pair for dict_of_asmts in ToDo (Column) instance
        '''
        self.kanban_table.list_of_col[0].add_assignment(name, priority)


    def remove_assignment(self,name, col_num):
        '''
        Removes assignment with given name (str), from current column col_num (int)
        '''        
        self.kanban_table.list_of_col[col_num].remove_assignment(name)

    def shift_assignment(self,name, col_num):
        '''
        Shifts assignment with given name (str), from current col_num (int) column to next (if not out of range)
        '''
        #col_num - number of column in which assignment is located
        self.kanban_table.shift_assignment(name, col_num)

    def sort_by_name_asc(self):
        '''
        Sorts assignments by name in ascending order
        '''
        self.kanban_table.list_of_col[0].sort_by_name_asc()
        self.kanban_table.list_of_col[1].sort_by_name_asc()
        self.kanban_table.list_of_col[2].sort_by_name_asc()
    def sort_by_name_desc(self):
        '''
        Sorts assignments by name in descending order
        '''
        self.kanban_table.list_of_col[0].sort_by_name_desc()
        self.kanban_table.list_of_col[1].sort_by_name_desc()
        self.kanban_table.list_of_col[2].sort_by_name_desc()

    def sort_by_priority_asc(self):
        '''
        Sorts assignments by priority in ascending order
        '''
        self.kanban_table.list_of_col[0].sort_by_priority_asc()
        self.kanban_table.list_of_col[1].sort_by_priority_asc()
        self.kanban_table.list_of_col[2].sort_by_priority_asc()
    
    def sort_by_priority_desc(self):
        '''
        Sorts assignments by priority in descending order
        '''
        self.kanban_table.list_of_col[0].sort_by_priority_desc()
        self.kanban_table.list_of_col[1].sort_by_priority_desc()
        self.kanban_table.list_of_col[2].sort_by_priority_desc()
    
    def save_to_file(self):
        '''
        Saves contents of dict_of_asmts in every Column instance inside Table instance
        '''
        self.__saver.save_to_file(self.kanban_table)
        
    def get_from_file(self):
        '''
        Reads contents into dict_of_asmts in every Column instance inside Table instance
        '''
        self.__saver.get_from_file(self.kanban_table)

    def print_all_column_contents(self):
        '''
        Displays contents of dict_of_asmts in every Column instance inside Table instance
        Helpful in troubleshooting and live database display
        '''
        print("ZAWARTOSC TABLICY KANBAN - CONTROLLER \n\n")
        print("To Do    ", self.kanban_table.list_of_col[0].dict_of_asmts)
        print("In Progress      ",self.kanban_table.list_of_col[1].dict_of_asmts)
        print("Finished     ", self.kanban_table.list_of_col[2].dict_of_asmts)
        print("\n\n")

