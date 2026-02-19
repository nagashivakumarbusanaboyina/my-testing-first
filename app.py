# A simple task manager program

class Task:
    def __init__(self, name, priority="medium"):
        self.name = name
        self.priority = priority
        self.completed = False
    
    def mark_complete(self):
        self.completed = True
        print(f"Task '{self.name}' marked as complete!")
    
    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"{status} {self.name} (Priority: {self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, name, priority="medium"):
        task = Task(name, priority)
        self.tasks.append(task)
        print(f"Added task: '{name}'")
    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
            return
        
        print("\n=== Your Tasks ===")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print()
    
    def complete_task(self, task_number):
        try:
            task = self.tasks[task_number - 1]
            task.mark_complete()
        except IndexError:
            print("Invalid task number!")
    
    def delete_task(self, task_number):
        try:
            removed = self.tasks.pop(task_number - 1)
            print(f"Deleted task: '{removed.name}'")
        except IndexError:
            print("Invalid task number!")

# Main program
def main():
    manager = TaskManager()
    
    while True:
        print("\n=== Task Manager ===")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            name = input("Enter task name: ")
            priority = input("Enter priority (low/medium/high) [default: medium]: ").lower()
            if priority not in ["low", "medium", "high"]:
                priority = "medium"
            manager.add_task(name, priority)
        
        elif choice == "2":
            manager.list_tasks()
        
        elif choice == "3":
            manager.list_tasks()
            if manager.tasks:
                try:
                    num = int(input("Enter task number to complete: "))
                    manager.complete_task(num)
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == "4":
            manager.list_tasks()
            if manager.tasks:
                try:
                    num = int(input("Enter task number to delete: "))
                    manager.delete_task(num)
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
