import csv;

def read_tasks(filename):
    tasks = {};
    for row in csv.reader(open(filename)):
        number = int(row[0]);
        title = row[1];
        duration = float(row[2]);
        prerequisites = set(map(int,row[3].split()));
        tasks[number] = (title, duration, \
            prerequisites);
    return tasks;

# Test code- currently working 