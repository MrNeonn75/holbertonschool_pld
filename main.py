""" Group 6920 """
import argparse
import cmd

class Task:
    id = 0
    
    def __init__(self, title, description):
        Task.id += 1
        self.id = Task.id
        self.title = title
        self.description = description
        self.completed = False
    
    def mark_as_completed(self):
        self.completed = True
    
class TaskManager:
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks[new_task.id] = new_task
        
    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print("Task was removed")
        else:
            print("Task not found")
    
    def mark_task_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].mark_as_completed()
            print("Task marked as completed")
        else:
            print("Task not found")
        
    def list_tasks(self):
        for key, value in self.tasks.items():
            print(f"{key}: {value.title} {value.completed}")
    
    def find_task(self, task_id):
        if task_id in self.tasks:
            return self.tasks[task_id]
        else:
            return None
        
class TaskConsole(cmd.Cmd):
    new_task = TaskManager()
    
    def do_quit(self, line):
        return True
    
    def do_add(self, line):
        parser = argparse.ArgumentParser(description="Add a new task")
        parser.add_argument("--title", required=True, help="Title of the task")
        parser.add_argument("--description", required=True, help="Description of the task")
        args = parser.parse_args(line.split())
        
        self.new_task.add_task(args.title, args.description)
        
    def do_remove(self, line):
        parser = argparse.ArgumentParser(description="Remove a task")
        parser.add_argument("--id", type=int, required=True, help="ID of the task to be removed")
        args = parser.parse_args(line.split())
        
        self.new_task.remove_task(args.id)
        
    def do_completed(self, line):
        parser = argparse.ArgumentParser(description="Mark a task as completed")
        parser.add_argument("--id", type=int, required=True, help="ID of the task to be marked as completed")
        args = parser.parse_args(line.split())
        
        self.new_task.mark_task_completed(args.id)
        
    def do_list(self, line):
        self.new_task.list_tasks()
    
    def do_find(self, line):
        parser = argparse.ArgumentParser(description="Find a task")
        parser.add_argument("--id", type=int, required=True, help="ID of the task to find")
        args = parser.parse_args(line.split())
        
        task = self.new_task.find_task(args.id)
        if task:
            print(task)
        else:
            print("Task not found")

if __name__ == "__main__":
    TaskConsole().cmdloop()
