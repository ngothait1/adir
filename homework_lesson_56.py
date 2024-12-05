import os
import json
import pandas as pd
from Student import Student
from Employee import Employee


def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Save all data")
    print("9. Exit")


def checkNumber(user_input, string_print):
    if user_input.isdigit():
        return True
    print("Error: " + string_print + " must be a number. " + user_input + " is not a number")
    return False


#1
def saveNewEntry(people_dict, sum_of_all_ages, id_list):
    user_id = input("ID: ")
    if not checkNumber(user_id, "ID"):
        return
    if user_id in people_dict:
        print("Error: ID already exists")
        return
    user_name = input("Name: ")
    user_age = input("Age: ")
    if not checkNumber(user_age, "age"):
        return
    which_class = input("Are you a student or an employee?\nPress s for student \ Press e for employee: ") # <==
    if which_class == "s" or which_class == "S":
        user_field_of_study = input("Field of study: ")
        user_year_of_study = input("Year of study: ")
        if not checkNumber(user_year_of_study, "Year of study"):
            return    
        student = Student(user_id, user_name, user_age, user_field_of_study, user_year_of_study)
        people_dict[student.getID()] = student
    elif which_class == "e" or which_class == "E":
        user_field_of_work = input("Field of work: ")
        user_salary = input("Salary: ")
        if not checkNumber(user_salary, "Salary"):
            return  
        employee = Employee(user_id, user_name, user_age, user_field_of_work, user_salary)
        people_dict[employee.getID()] = employee
    else:
        print("Error: you need to choose the letter s or e")
        return
    print("ID [" + user_id + "] saved successfuly")
    sum_of_all_ages[0] += int(user_age)
    id_list.append(user_id)


#2
def searchByID(people_dict): # O(1)
    user_id_search = input("Please enter the ID you want to look for: ")
    if not checkNumber(user_id_search, "ID"):
        return
    if user_id_search not in people_dict: 
        print("Error: ID " + user_id_search + " is not saved")
        return
    id = user_id_search
    entry = people_dict[id]
    people_dict[user_id_search].printMyself()
    


#3
def printAgesAverage(people_dict, sum_of_all_ages): # O(1)
    if len(people_dict) == 0:
        print(0)
        return
    print(sum_of_all_ages[0] / len(people_dict)) 


#4
def printAllNames(people_dict): # O(N)
    for index, key in enumerate(people_dict): 
        print(str(index) + ". " + people_dict[key].getName())


#5
def printAllIds(people_dict): # O(N)
    for index, key in enumerate(people_dict): 
        print(str(index) + ". " + key)


#6
def printAllEntries(people_dict): # O(N)
    for index, key in enumerate(people_dict):
        print("*********")
        print(index)
        people_dict[key].printMyself()


#7
def printEntryByIndex(people_dict, id_list): # O(1)
    index_entry_input = input("Please enter the index of the entry you want to print: ")
    if not checkNumber(index_entry_input, "index"):
        return
    if int(index_entry_input) >= len(id_list):
        print("Error: Index out of range. The maximum index allowed is " + str((len(id_list) - 1)))
        return
    id = id_list[int(index_entry_input)]
    entry = people_dict[id]
    people_dict[id].printMyself()


#8
def saveAllData(people_dict):
    path = os.path.join("C:\\", "Users", "adirv", "Videos", "קורס תכנות עם נדב גוטהייט", "קורס פייתון", "קבצים", "advance_files")
    data_entries = []
    conf_file = {}
    for key, value in people_dict.items():
        data_entries.append(value.getDictionary()) # <===
    df = pd.DataFrame(data_entries)
    csv_file_name = input("What is your output file name? ")
    if not csv_file_name.endswith(".csv"):
        csv_file_name = csv_file_name + ".csv"
    df.to_csv(os.path.join(path, csv_file_name), index=False)


#9
def exitFromMenu():
    while True:
        exit_question_input = input("Are you sure? (y/n) ")
        if exit_question_input == "n":
            return "n"
        if exit_question_input == "y":
            print("Goodbye!")
            return "y"


def main():
    records_database = dict()
    total_sum_ages = [0]
    list_entries_ids = list()
    while True:
        printMenu()
        option_choise = input("Please enter your choise: ")
        if option_choise == "1":
            saveNewEntry(records_database, total_sum_ages, list_entries_ids)
        elif option_choise == "2":
            searchByID(records_database)
        elif option_choise == "3":
            printAgesAverage(records_database, total_sum_ages)
        elif option_choise == "4":
            printAllNames(records_database)
        elif option_choise == "5":
            printAllIds(records_database)
        elif option_choise == "6":
            printAllEntries(records_database)
        elif option_choise == "7":
            printEntryByIndex(records_database, list_entries_ids)
        elif option_choise == "8":
            saveAllData(records_database)
            continue
        elif option_choise == "9":
            if exitFromMenu() == "y":
                return
            continue
        else:
            print("Error: Option [" + option_choise + "] does not exist. Please try again")
            continue
        input("Press Enter to continue ")


main()