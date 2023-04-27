import csv;
import tkinter;
from tkinter.filedialog import askopenfile;

from collections import namedtuple;
Task = namedtuple("Task", ["title", "duration", "prerequisites"] );

def read_tasks(filename):
    tasks = {};
    for row in csv.reader(open(filename)):
        number = int(row[0]);
        title = row[1];
        duration = float(row[2]);
        prerequisites = set(map(int,row[3].split()));
        tasks[number] = Task(title, duration, \
            prerequisites);
    return tasks;

#adding logic 

def order_tasks(tasks):
    incomplete = set(tasks)
    completed = set()
    start_days = {}
    while incomplete:
        for task_number in incomplete:
            task = tasks[task_number]
            if task.prerequisites.issubset(completed):
                earliest_start_day = 0
                for prereq_number in task.prerequisites:
                    prereq_end_day = start_days[prereq_number] + \
                                     tasks[prereq_number].duration
                    if prereq_end_day > earliest_start_day:
                        earliest_start_day = prereq_end_day
                start_days[task_number] = earliest_start_day
                incomplete.remove(task_number)
                completed.add(task_number)
                break
    return start_days

# draw function for the chart thinking gnatt chart
def draw_chart()

# create open project functions and call draw function

def open_project():
    filename = askopenfilename(title="Open Project", initialdir=".",\
                                filetypes=[( "CSV Document","*.csv")])
    tasks = read_tasks(filename)
    draw_chart(tasks, canvas)
    


# create UI for project charts

root = tkinter.Tk()
root.title("Project Planner")
open_button = tkinter.Button(root, text="Open project...", \ 
                             command = open_project)
open_button.pack(side="top")
canvas = tkinter.Canvas(root,  width= 800, \
                         height= 400, bg="white")
canvas.pack(side="bottom")
tkinter.mainloop()
