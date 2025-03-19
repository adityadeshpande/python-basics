# tasks = []
# while True:
#     task = input("Enter a task (or 'quit' to exit): ")
#     if task == "quit":
#         break
#     tasks.append(task)
# print("Your tasks:", tasks)

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added!")

    def mark_completed(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            print(f"Task '{self.tasks[task_number]['task']}' marked as completed!")
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTo-Do List:")
            for idx, task in enumerate(self.tasks):
                status = "✔" if task["completed"] else "✘"
                print(f"{idx + 1}. [{status}] {task['task']}")

if __name__ == "__main__":
    todo = ToDoList()
    while True:
        print("\nOptions: 1) Add Task  2) Mark Completed  3) Show Tasks  4) Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.show_tasks()
            task_num = int(input("Enter task number to mark completed: ")) - 1
            todo.mark_completed(task_num)
        elif choice == "3":
            todo.show_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
