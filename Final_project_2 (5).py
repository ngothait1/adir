
def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Exit")


def printEntry(id_user, name_user, age_user):
    print("ID: " + id_user)
    print("Name: " + name_user)
    print("Age: " + age_user)
    

def saveNewEntry(people_dict, sum_of_all_ages, id_list):
    user_id = input("ID: ")
    if not user_id.isdigit():
        print("Error: ID must be a number. " + user_id + " is not a number")
        return
    if user_id in people_dict:
        print("Error: ID already exists: " + str({"name": people_dict[user_id][0], "age": people_dict[user_id][1]}))
        return
    user_name = input("Name: ")
    user_age = input("Age: ")
    if not user_age.isdigit():
        print("Error: age must be a number. " + user_age + " is not a number")
        return
    people_dict[user_id] = [user_name, user_age]
    print("ID [" + user_id + "] saved successfuly")
    sum_of_all_ages[0] += int(user_age)
    id_list.append(user_id)


def search_ByID(people_dict): # O(1)
    user_id_search = input("Please enter the ID you want to look for: ")
    if not user_id_search.isdigit():
        print("Error: ID must be a number. " + user_id_search + " is not a number")
        return
    if user_id_search not in people_dict: 
        print("Error: ID " + user_id_search + " is not saved")
        return
    printEntry(user_id_search, people_dict[user_id_search][0], people_dict[user_id_search][1])


def printAgesAverage(people_dict, sum_of_all_ages): # O(1)
    if len(people_dict) == 0:
        print ("0")
        return
    print(sum_of_all_ages[0] / len(people_dict)) 


def printAllNames(people_dict): # O(N)
    for index, key in enumerate(people_dict): 
        print(str(index) + ". " + people_dict[key][0])


def printAllIds(people_dict): # O(N)
    for index, key in enumerate(people_dict): 
        print(str(index) + ". " + key)


def printAllEntries(people_dict): # O(N)
    for index, key in enumerate(people_dict):
        printEntry(str(index) + ". " + key, people_dict[key][0], people_dict[key][1])


def printEntryByIndex(people_dict, id_list): # O(1)
    index_entry_input = input("Please enter the index of the entry you want to print: ")
    if not index_entry_input.isdigit():
        print("Error: ID must be a number. " + index_entry_input + " is not a number")
        return
    if int(index_entry_input) >= len(id_list):
        print("Error: Index out of range. The maximum index allowed is " + str((len(id_list) - 1)))
        return
    printEntry(id_list[int(index_entry_input)], people_dict[id_list[int(index_entry_input)]][0], people_dict[id_list[int(index_entry_input)]][1])


def exitFromMenu():
    while True:
        exit_question_input = input("Are you sure? (y/n) ")
        if exit_question_input == "n":
            return "n"
        if exit_question_input == "y":
            print("Goodbye!")
            return "y"


records_database = {}
total_sum_ages = [0]
list_entries_ids = []

while True:
    printMenu()
    option_choise = input("Please enter your choise: ")
    flag = True
    if option_choise == "1":
        saveNewEntry(records_database, total_sum_ages, list_entries_ids)
    elif option_choise == "2":
        search_ByID(records_database)
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
        if exitFromMenu() == "y":
            break
        flag = False
    else:
        print("Error: Option [" + option_choise + "] does not exist. Please try again")
        flag = False

    if flag == True: 
        input("Press Enter to continue ")