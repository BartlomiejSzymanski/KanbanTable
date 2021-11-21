import assignment
import column
import table
import application
import kanban_exception
import pytest
import filesaver


def test_assignment_init():
    task = assignment.Assignment("Posprzątaj", "Wazne")

    assert task.name == "Posprzątaj"
    assert task.priority == "Wazne"

def test_ass_setters():
    task = assignment.Assignment()

    task.name_setter = "Wyprowadz psa"
    task.priority_setter = "Normal"

    assert task.name == "Wyprowadz psa"
    assert task.priority == "Normal"


def test_column_init():
    ToDo = column.Column("To Do")
    assert ToDo.column_name ==  "To Do"

def test_add_assignment():
    ToDo = column.Column("To Do")

    ToDo.add_assignment("Wyprowadz psa","Wazne")
    assert ToDo.dict_of_asmts == {"Wyprowadz psa" : "Wazne"}

    ToDo.add_assignment("Sprawdz kalendarz","Wazne")
    assert ToDo.dict_of_asmts == {"Wyprowadz psa" : "Wazne", "Sprawdz kalendarz" : "Wazne"}


def test_remove_assignment():
    ToDo = column.Column("To Do")

    ToDo.add_assignment("Wyprowadz psa","Wazne")
    ToDo.add_assignment("Sprawdz kalendarz","Wazne")
    ToDo.remove_assignment("Wyprowadz psa")

    assert ToDo.dict_of_asmts == {"Sprawdz kalendarz" : "Wazne"}
    
def test_sort_by_name_asc():
    ToDo = column.Column("To Do")
    ToDo.add_assignment("Wyprowadz psa","Wazne")
    ToDo.add_assignment("Sprawdz kalendarz","Wazne")

    ToDo.sort_by_name_asc()

    assert ToDo.dict_of_asmts == {"Sprawdz kalendarz" : "Wazne", "Wyprowadz psa" : "Wazne"}


def test_sort_by_name_desc():

    ToDo = column.Column("To Do")
    ToDo.add_assignment("A","Wazne")
    ToDo.add_assignment("B","Wazne")
    ToDo.add_assignment("C","Wazne")
    ToDo.sort_by_name_desc()
    assert ToDo.dict_of_asmts == {"C" : "Wazne","B" : "Wazne","A" : "Wazne"}


def test_sort_by_priority_asc():
    ToDo = column.Column("To Do")
    ToDo.add_assignment("A","Normal")
    ToDo.add_assignment("B","Normal")
    ToDo.add_assignment("C","Normal")
    ToDo.add_assignment("D","Important")
    ToDo.add_assignment("E","Important")
    ToDo.add_assignment("F","Important")

    ToDo.sort_by_priority_asc()
    
    assert ToDo.dict_of_asmts == {"E" : "Important", "F" : "Important", "D" : "Important","A" : "Normal", "B" : "Normal", "C" : "Normal" }

def test_sort_by_priority_desc():
    ToDo = column.Column("To Do")
    ToDo.add_assignment("A","Normal")
    ToDo.add_assignment("B","Normal")
    ToDo.add_assignment("C","Normal")
    ToDo.add_assignment("D","Important")
    ToDo.add_assignment("E","Important")
    ToDo.add_assignment("F","Important")

    ToDo.sort_by_priority_asc()
    
    assert ToDo.dict_of_asmts == {"C" : "Normal", "B" : "Normal", "A" : "Normal", "D" : "Important", "F" : "Important", "E" : "Important" }



def test_table_init():
    table_obj = table.Table()

    col0 =  table_obj.list_of_col[0]
    col1 =  table_obj.list_of_col[1]
    col2 =  table_obj.list_of_col[2]

    assert col0.column_name == "To Do"
    assert col1.column_name == "In Progress"
    assert col2.column_name == "Finished"

def test_shift_assignment():

    table_obj = table.Table()

    col0 =  table_obj.list_of_col[0]
    col1 =  table_obj.list_of_col[1]
    col2 =  table_obj.list_of_col[2]

    col0.add_assignment("Wynies smieci", "Important")
    col1.add_assignment("Posprzataj pokoj", "Normal")
    col2.add_assignment("Pozmywaj naczynia", "Normal")

    table_obj.shift_assignment("Wynies smieci", 0)
    table_obj.shift_assignment("Posprzataj pokoj", 1)

    assert col0.dict_of_asmts == {}
    assert col1.dict_of_asmts == {"Wynies smieci" : "Important"}
    assert col2.dict_of_asmts == {"Pozmywaj naczynia" : "Normal","Posprzataj pokoj" : "Normal"}

    
    
def test_Last_Column_exception():
    table_obj = table.Table()

    col0 =  table_obj.list_of_col[0]
    col1 =  table_obj.list_of_col[1]
    col2 =  table_obj.list_of_col[2]

    col0.add_assignment("Wynies smieci", "Important")
    col1.add_assignment("Posprzataj pokoj", "Normal")
    col2.add_assignment("Pozmywaj naczynia", "Normal")

    with pytest.raises(kanban_exception.Last_Column):
        table_obj.shift_assignment("Pozmywaj naczynia", 2)




def test_application_init():

    app = application.Application()
    
    assert isinstance(app, application.Application)


def test_app_add_assignment():
    app = application.Application()

    app.add_assignment("Posprzataj pokoj", "Important")


    assert app.kanban_table.list_of_col[0].dict_of_asmts == {"Posprzataj pokoj" : "Important"}


def test_app_shift_assignment():
    app = application.Application()


    app.add_assignment("Wynies smieci", "Important")
    app.add_assignment("Posprzataj pokoj", "Normal")
    app.add_assignment("Pozmywaj naczynia", "Normal")

    app.shift_assignment("Wynies smieci", 0)
    app.shift_assignment("Posprzataj pokoj", 0)
    app.shift_assignment("Posprzataj pokoj", 1)


    assert app.kanban_table.list_of_col[0].dict_of_asmts == {"Pozmywaj naczynia" : "Normal"}
    assert app.kanban_table.list_of_col[1].dict_of_asmts == {"Wynies smieci" : "Important"}
    assert app.kanban_table.list_of_col[2].dict_of_asmts == {"Posprzataj pokoj" : "Normal"}


def test_app_remove_assignment():
    app = application.Application()

    app.add_assignment("Posprzataj pokoj", "Important")     # COL 3 del
    app.add_assignment("Wyprowadz psa", "Important")        # COL 1 del
    app.add_assignment("Napraw rower", "Important")         # COL 3 
    app.add_assignment("Podlej Kwiaty", "Important")        # COL 1
    app.add_assignment("Odrob lekcje", "Important")         # COL 2
    app.add_assignment("Odbierz paczke", "Important")       # COL 2 del


    app.shift_assignment("Posprzataj pokoj", 0)
    app.shift_assignment("Posprzataj pokoj", 1)

    app.shift_assignment("Napraw rower", 0)
    app.shift_assignment("Napraw rower", 1)
    
    app.shift_assignment("Odrob lekcje", 0)
    app.shift_assignment("Odbierz paczke", 0)
    
    
    app.remove_assignment("Wyprowadz psa", 0)
    app.remove_assignment("Posprzataj pokoj",2)
    app.remove_assignment("Odbierz paczke",1)



    assert app.kanban_table.list_of_col[0].dict_of_asmts == {"Podlej Kwiaty" : "Important"}
    assert app.kanban_table.list_of_col[1].dict_of_asmts == {"Odrob lekcje" : "Important"}
    assert app.kanban_table.list_of_col[2].dict_of_asmts == {"Napraw rower": "Important"}





def test_app_sorting():
    app = application.Application()

    app.add_assignment("Posprzataj pokoj", "Important")     # COL 3 del
    app.add_assignment("Wyprowadz psa", "Normal")        # COL 1 del
    app.add_assignment("Napraw rower", "Normal")         # COL 3 
    app.add_assignment("Podlej Kwiaty", "Important")        # COL 1
    app.add_assignment("Odrob lekcje", "Normal")         # COL 2
    app.add_assignment("Odbierz paczke", "Important")       # COL 2 del
    app.add_assignment("Umyj okna", "Normal")


    app.shift_assignment("Posprzataj pokoj", 0)
    app.shift_assignment("Posprzataj pokoj", 1)
    app.shift_assignment("Umyj okna", 0)
    app.shift_assignment("Umyj okna", 1)

    app.shift_assignment("Napraw rower", 0)
    app.shift_assignment("Napraw rower", 1)
    
    app.shift_assignment("Odrob lekcje", 0)
    app.shift_assignment("Odbierz paczke", 0)

    app.sort_by_name_asc()
    assert app.kanban_table.list_of_col[0].dict_of_asmts == {"Podlej Kwiaty" : "Important","Wyprowadz psa" : "Normal"}
    assert app.kanban_table.list_of_col[1].dict_of_asmts == {"Odbierz paczke": "Important", "Odrob lekcje" : "Normal"}
    assert app.kanban_table.list_of_col[2].dict_of_asmts == {"Napraw rower" : "Normal", "Posprzataj pokoj" : "Important", "Umyj okna" : "Normal"}

    app.sort_by_name_desc()
    assert app.kanban_table.list_of_col[0].dict_of_asmts == {"Wyprowadz psa" : "Normal","Podlej Kwiaty" : "Important"}
    assert app.kanban_table.list_of_col[1].dict_of_asmts == {"Odrob lekcje" : "Normal","Odbierz paczke": "Important"}
    assert app.kanban_table.list_of_col[2].dict_of_asmts == {"Umyj okna" : "Normal", "Posprzataj pokoj" : "Important", "Napraw rower" : "Normal"}

    app.sort_by_priority_asc()
    assert app.kanban_table.list_of_col[0].dict_of_asmts == {"Podlej Kwiaty" : "Important","Wyprowadz psa" : "Normal"}
    assert app.kanban_table.list_of_col[1].dict_of_asmts == {"Odbierz paczke": "Important", "Odrob lekcje" : "Normal"}
    assert app.kanban_table.list_of_col[2].dict_of_asmts == {"Posprzataj pokoj" : "Important", "Napraw rower" : "Normal", "Umyj okna" : "Normal"}

    app.sort_by_priority_desc()
    assert app.kanban_table.list_of_col[0].dict_of_asmts == {"Wyprowadz psa" : "Normal","Podlej Kwiaty" : "Important"}
    assert app.kanban_table.list_of_col[1].dict_of_asmts == {"Odrob lekcje" : "Normal","Odbierz paczke": "Important"}
    assert app.kanban_table.list_of_col[2].dict_of_asmts == {"Napraw rower" : "Normal","Umyj okna" : "Normal", "Posprzataj pokoj" : "Important"}


def test_save_to_file():
    with open("filesaver_test.txt", "w") as ff:
        ff.write("")
        ff.close()
    app = application.Application()
    app.filesaver = "filesaver_test.txt"
    
    app.add_assignment("Wyprowadz psa","Important")
    app.add_assignment("Posprzataj pokoj", "Normal")
    app.shift_assignment("Posprzataj pokoj",0)

    app.save_to_file()

    with open("filesaver_test.txt", "r") as ff:
        package = ff.read()
        ff.close()
    assert package == "{'Wyprowadz psa': 'Important'}LF{'Posprzataj pokoj': 'Normal'}LF{}LF"
    
def test_get_from_file():
    with open("filesaver_test.txt", "w") as ff:
        ff.write("{'Wyprowadz psa': 'Important'}LF{'Posprzataj pokoj': 'Normal'}LF{}LF")
        ff.close()
    app = application.Application()  
    app.filesaver = "filesaver_test.txt"      
    app.get_from_file()

    assert app.kanban_table.list_of_col[0].dict_of_asmts == {"Wyprowadz psa": "Important"}
    assert app.kanban_table.list_of_col[1].dict_of_asmts == {"Posprzataj pokoj": "Normal"}
    assert app.kanban_table.list_of_col[2].dict_of_asmts == {}
        