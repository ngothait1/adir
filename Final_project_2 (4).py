
def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Exit")

def pressEnterToContinue():
    press_enter = input("Press Enter to continue ")
    
def saveNewEntry():
    user_id = input("ID: ")
    if not user_id.isdigit():
        print("Error: ID must be a number. " + user_id + " is not a number")
    elif user_id in records_database:
        id_name_exist = records_database[user_id][0]
        id_age_exist = records_database[user_id][1]
        id_exist_record_dict = {"name": id_name_exist, "age": id_age_exist}
        print("Error: ID already exists: " + str(id_exist_record_dict))
    else:
        user_name = input("Name: ")
        user_age = input("Age: ")
        records_database[user_id] = [user_name, user_age]
        print("ID [" + user_id + "] saved successfuly")

        total_sum_ages[0] += (int(user_age))
        age_counter[0] += 1
        list_entries_ids.append(user_id)
        list_entries_names.append(user_name)
        list_entries_ages.append(user_age)


def search_ByID(): # O(1)
    user_id_search = input("Please enter the ID you want to look for: ")
    if not user_id_search.isdigit():
        print("Error: ID must be a number. " + user_id_search + " is not a number")
    elif user_id_search in records_database: 
        print("ID: " + user_id_search)
        print("Name: " + records_database[user_id_search][0])
        print("Age: " + records_database[user_id_search][1])        
    else:
        print("Error: ID " + user_id_search + " is not saved")
    pressEnterToContinue()


def printAgesAverage(): # O(1)
    if age_counter[0] == 0:
        print ("0")
    else:
        print(total_sum_ages[0] / age_counter[0]) 
    pressEnterToContinue()


def printAllNames(): # O(N)
    for index, key in enumerate(records_database): 
        print(str(index) + ". " + records_database[key][0])
    pressEnterToContinue()


def printAllIds(): # O(N)
    for index, key in enumerate(records_database): 
        print(str(index) + ". " + key)
    pressEnterToContinue()


def printAllEntries(): # O(N)
    for index, key in enumerate(records_database):
        print(str(index) + ". " + key)
        print("   Name: " + records_database[key][0])
        print("   Age: " + records_database[key][1])
    pressEnterToContinue()


def printEntryByIndex(): # O(1)
    index_entry_input = input("Please enter the index of the entry you want to print: ")
    if not index_entry_input.isdigit():
        print("Error: ID must be a number. " + index_entry_input + " is not a number")
    elif int(index_entry_input) >= len(list_entries_ids):
        print("Error: Index out of range. The maximum index allowed is " + str((len(list_entries_ids) - 1)))
    else:
        print("ID: " + list_entries_ids[int(index_entry_input)])
        print("Name: " + list_entries_names[int(index_entry_input)])
        print("Age: " + list_entries_ages[int(index_entry_input)])


def exitFromMenu():
    exit_question_input = input("Are you sure? (y/n) ")
    while True:
        if exit_question_input == "n":
            break
        elif exit_question_input == "y":
            print("Goodbye!")
            return "y"
        else:
            exit_question_input = input("Are you sure? (y/n) ")


age_counter = [0]
total_sum_ages = [0]
list_entries_ids = []
list_entries_names = []
list_entries_ages = []
records_database = {}



while True:
    printMenu()
    option_choise = input("Please enter your choise: ")
    if option_choise == "1":
        saveNewEntry()
        pressEnterToContinue()
    elif option_choise == "2":
        search_ByID()
    elif option_choise == "3":
        printAgesAverage()
    elif option_choise == "4":
        printAllNames()
    elif option_choise == "5":
        printAllIds()
    elif option_choise == "6":
        printAllEntries()
    elif option_choise == "7":
        printEntryByIndex()
        pressEnterToContinue()
    elif option_choise == "8":
        if exitFromMenu() == "y":
            break
    else:
        print("Error: Option [" + option_choise + "] does not exist. Please try again")