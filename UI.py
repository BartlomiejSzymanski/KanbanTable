import application
from tkinter import * 
#from tkinter.constants import BOTH, END, LEFT
from typing import Text

class UI:
    '''
    Presenter class, displays user graphic interface.
    Communicates with application.
    '''
    def __init__(self):
        #MAIN WIDGETS
        self.__app = application.Application()
        self.__root = Tk()
        self.__menu = Menu(self.__root)
        self.__window_flag = 0

        #LISTBOXES
        self.__ToDo = Listbox(self.__root,width=40,height = 30)
        self.__InProgress = Listbox(self.__root,width=40,height = 30)
        self.__Finished = Listbox(self.__root,width=40,height = 30)

        #BUTTONS

        self.__button_add_as = Button(self.__root, text = "Add Assignment", command = lambda: self.add_assignment()).grid(row = 4, column =1)
    @property
    def root(self):
        return self.__root


    def present(self):
        '''
        Initialization function, displays initialized widgets. Initializes new widgets.
        '''
        self.__root.config(menu=self.__menu)
        
        #DROPDOWN MENU INIT
        fileMenu = Menu(self.__menu)
        viewMenu = Menu(self.__menu)

        #DROPDOWN MENUS
        self.__menu.add_cascade(label= "File", menu= fileMenu)
        self.__menu.add_cascade(label = "View", menu = viewMenu)

        #MENU CONTENTS
        fileMenu.add_command(label = "Save", command = lambda: self.save_to_file())
        fileMenu.add_command(label = "Open", command = lambda: self.get_from_file())
        viewMenu.add_command(label = "Sort by name ascending",command = lambda: self.sort_by_name_asc())
        viewMenu.add_command(label = "Sort by name descending",command = lambda: self.sort_by_name_desc())
        viewMenu.add_command(label = "Sort by priority ascending",command = lambda: self.sort_by_priority_asc())
        viewMenu.add_command(label = "Sort by priority descending",command = lambda: self.sort_by_priority_desc())
        
        #MAIN WINDOW INIT
        self.__root.title("Tablica Kanban")
        self.__root.geometry("973x650")

        #LISTBOXES INIT
        self.__ToDo.grid(row=2, column=1)
        self.__InProgress.grid(row=2, column=2)
        self.__Finished.grid(row=2, column=3)
        
        ToDo_label = Label(self.__root,text="ToDo", width=10).grid(row=0, column=1)
        InProgress = Label(self.__root,text="InProgress", width=10).grid(row=0, column=2)
        Finished = Label(self.__root,text="Finished", width=10).grid(row=0, column=3)
        
        #BUTTONS INIT
        button_add_as = self.__button_add_as
        button_remove_as = Button(self.__root, text = "Del Assignment",command = lambda: self.del_ass_button()).grid(row = 4, column =2)
        button_shift_as =  Button(self.__root, text = "Shift Assignment", command = lambda: self.shift_ass_button()).grid(row = 4, column =3)




    def ok_button_pressed(self, box, name_en, priority):
        '''
        OK-button response command. Retrieves name (str) and Priority (str) from dialogbox, and passes to application.add_assignment
        '''
        name = name_en.get()
        priority = priority.get()
        self.__app.add_assignment(name, priority)
        

        self.update_presenter()
        
        
    def close_button_pressed(self,box):
        '''
        Close-button response command. Closes given dialogbox
        '''
        box.destroy()

    def shift_ass_button(self):
        '''
        Shift Assignment- button response command. Calls application methods. 
        '''
            
        box_dict = {self.__ToDo : self.__InProgress, self.__InProgress : self.__Finished}
        box_dict_controller = {self.__ToDo : 0, self.__InProgress : 1}

        curr_listbox = self.__root.focus_get()
        #GET NAME FROM SELECTED ITEM
        if isinstance(curr_listbox, Listbox):

            selected_str = curr_listbox.get(curr_listbox.curselection())
            ass_name = selected_str.replace("Important","")
            ass_name = ass_name.replace("Normal","")
            ass_name =  ass_name.strip(" ")
            

            #GET INDEX
            selected_index = curr_listbox.index(curr_listbox.curselection())
            
            if curr_listbox in box_dict:
                #CONTROLLER
                self.__app.shift_assignment(ass_name,box_dict_controller[curr_listbox]) # assignment name: selected_str, current column: dict[curr_listbox]
                #PRESENTER
                self.update_presenter()

            else:
                print("Cannot move further")
            

        

    def del_ass_button(self):
        '''
        Delete Assignment -button response. Calls application methods. 
        '''
        box_dict_of_indexes = {self.__ToDo : 0, self.__InProgress : 1, self.__Finished : 2}
        curr_listbox = self.__root.focus_get()
        print(curr_listbox)

        if isinstance(curr_listbox, Listbox):

            selected_index = curr_listbox.index(curr_listbox.curselection())
            
            selected_str = curr_listbox.get(curr_listbox.curselection())
            ass_name = selected_str.replace("Important","")
            ass_name = ass_name.replace("Normal","")
            ass_name =  ass_name.strip(" ")
            

            if curr_listbox in box_dict_of_indexes:
                #CONTROLLER
                self.__app.remove_assignment(ass_name,box_dict_of_indexes[curr_listbox])
                #PRESENTER
                self.update_presenter()
            else:
                print("Something went wrong")


    def add_assignment(self):
        '''
        Add Assignment -button response. Calls application methods. 
        '''

        if self.__window_flag == 0:
            self.__window_flag = 1
            print("add assignment")
            box = Tk()
            priority = StringVar(box)
            priority.set("Normal") # default value

            name = "New assignment"

            box.title("Wprowadz dane")
            box.geometry("300x200")

            name_lab = Label(box, text = "Name").grid(row = 0 , column =1)
            name_en = Entry(box, width = 35)
            name_en.grid(row = 2, column =1)
            prior_lab = Label(box, text = "Priority")
            prior_lab.grid(row = 3 , column =1)
            priority_en =OptionMenu(box, priority, "Normal", "Important").grid(row = 4, column =1)
            spacer  = Label(box, text = "").grid(row = 5, column =1)
            
            name = name_en.get()
            ok_button = Button(box, text = "add", command = lambda: self.ok_button_pressed(box, name_en, priority)).grid(row = 6, column =1)
            close_button = Button(box, text = "close", command = lambda: self.close_button_pressed(box)).grid(row = 7, column =1)


        
    
    def update_presenter(self):
        '''
        Presents contents of dict_of_asmts in every Column instance inside Table instance
        '''
        listboxes = [self.__ToDo, self.__InProgress, self.__Finished]

        for i in range(0,3):
            listboxes[i].delete(0,END)
            dict_of_asmts = self.__app.kanban_table.list_of_col[i].dict_of_asmts
            for asmt in dict_of_asmts:
                listboxes[i].insert(0,asmt + " " + dict_of_asmts[asmt])
        self.__app.print_all_column_contents()

    def save_to_file(self):
        '''
        Save - menu response.
        Calls application.save_to_file()
        '''
        print("ZAPISANO NASTEPUJACE DANE:   \n")
        self.__app.print_all_column_contents()
        self.__app.save_to_file()

    def get_from_file(self):
        '''
        Open - menu response.
        Calls application.get_from_file()
        '''
        self.__app.get_from_file()
        self.update_presenter()

    def sort_by_name_asc(self):
        '''
        Sort by name ascending - menu response.
        Calls application.sort_by_name_asc()
        '''
        
        self.__app.sort_by_name_asc()
        self.update_presenter()


    def sort_by_name_desc(self):
        '''
        Sort by name descending - menu response.
        Calls application.sort_by_name_desc()
        '''
        self.__app.sort_by_name_desc()
        self.update_presenter()

    def sort_by_priority_asc(self):
        '''
        Sort by priority ascending - menu response.
        Calls application.sort_by_priority_asc()
        '''
        self.__app.sort_by_priority_asc()
        self.update_presenter()

    def sort_by_priority_desc(self):
        '''
        Sort by priority descending - menu response.
        Calls application.sort_by_priority_desc()
        '''
        self.__app.sort_by_priority_desc()
        self.update_presenter()