employees = {} 
def add_employee(): 
    name = input("Enter employee name: ") 
    if name in employees: 
        print("Employee already exists!") 
    else: 
        employees[name] = [] 
        print("Employee added successfully!") 
def assign_task(): 
    name = input("Enter employee name: ") 
    if name in employees: 
        task = input("Enter task: ") 
        employees[name].append({"task": task, "status": "Pending"}) 
        print("Task assigned successfully!") 
    else: 
        print("Employee not found!") 
def view_tasks(): 
    if not employees: 
        print("No employees found!") 
    else: 
        for name in employees: 
            print("\nEmployee:", name) 
            if not employees[name]: 
                print(" No tasks assigned") 
            else: 
                for i, t in enumerate(employees[name]): 
                    print(f" {i+1}. {t['task']} - {t['status']}") 
def complete_task(): 
    name = input("Enter employee name: ") 
    if name in employees: 
        if not employees[name]: 
            print("No tasks to update!") 
        else: 
            for i, t in enumerate(employees[name]): 
                print(f"{i+1}. {t['task']} - {t['status']}")     
            choice = int(input("Enter task number to mark complete: "))        
            if 1 <= choice <= len(employees[name]): 
                employees[name][choice-1]["status"] = "Completed" 
                print("Task marked as completed!") 
            else: 
                print("Invalid choice!") 
    else: 
        print("Employee not found!") 
while True: 
    print("\n--- Employee Task Tracker ---") 
    print("1. Add Employee") 
    print("2. Assign Task") 
    print("3. View Tasks") 
    print("4. Complete Task") 
    print("5. Exit") 
    option = input("Enter your choice: ") 
    if option == "1": 
        add_employee() 
    elif option == "2": 
        assign_task() 
    elif option == "3": 
        view_tasks() 
    elif option == "4": 
        complete_task() 
    elif option == "5": 
        print("Exiting program...") 
        break 
    else: 
        print("Invalid option! Try again.")