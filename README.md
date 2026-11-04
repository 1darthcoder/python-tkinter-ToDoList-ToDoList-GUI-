# python-tkinter-ToDoList-ToDoList-GUI-
A basic beginner friendly desktop to-do list built with Python and tkinter. Add, Complete, Delete and Clear tasks. With commenting 
< screenshot>

--------------------------------------------------------------------------------------------------

Table of Contents
1. Why I built this
2. Why this app is useful
3. features
4. Getting started
5. How to use
6. How the code works
7. Proograming Concepts covered
8. Known limitations
9. Ideas for Future Improvements
10. Tech Stack
11. Author
12. Licence

----------------------------------------------------------------------------------------------------

Why I Built This

I built this project to move from writing simple command line scripts to building a real application with a graphical interface. A to-do list is a classic beginner project because it is small enough to finish, but still covers the core ideas behind almost every piece of software such as: storing data, reacting to user actions, updating what user sees and handling mistakes such as clicking the delete button with nothing is selected.

Building this also taught me how to read error messages and some basic debugging. Several early bugs were caused by small typos in names and options and fixing them showed me how strictly Python reads code. I also learnt a bit about classes and how they are structured as well as some basics when using the tkinter library.

----------------------------------------------------------------------------------------------------

Why this app is Useful
- keeps your tasks in one visible place so nothing gets forgotten
- shows progress at a simple glance. Every task has a clear status: done or not done
- Simple and distraction free. No sign-ups, no internet, no account required at all. it all runs locally on your computer
- Lightweight. It only uses Pythons built-in libraries so there is nothing extra to install at all
- A good learning base. Code i short, readable and comments slightly help explain what is going on.

---------------------------------------------------------------------------------------------------

Getting Started
Requirements 
 - python3.8 or newer
 - tkinter
(note) on some Linux systems tkinter must be installed separately:
sudo apt install python3-tk

Installation 
# 1. Clone the repository
git clone https://github.com/1darthcoder/python-tkinter-ToDoList-ToDoList-GUI-.git

# 2. Move into the project folder
cd python-tkinter-ToDoList-ToDoList-GUI-

# 3. Run the app
python To-Do-List_GUI.py

How to Use
1. To Add a new task: type in the text box, then click the Add Task button.
2. To Complete a task: click a task in the list to highlight it, then click Mark as Done.
3. To Delete a task: click a task to highlight it, then click Delete Task.
4. Starting fresh: click Clear All and confirm with Yes.

Note: The tasks do not get saved when you close the window.

How the Code Works

The whole program lives in one file, inside a single class called TodoApp.

Programming Concepts I Learnt

This project is small, but it helped me brush up on some basic coding fundamentals. Here is each concept, what it means, and where it appears in this app.

1. Modules and Imports

A module is a file of ready-made code you can reuse. import brings it into your program.

import tkinter as tk loads the GUI library and gives it the short nickname tk.
from tkinter import messagebox loads one specific part of the library (the pop-up dialogs) so you can use it directly by name.

2. Classes and Objects (Object-Oriented Programming)

A class is a blueprint. An object (or instance) is the thing that is built from that blueprint.

A class bundles together:
-Data (what the thing knows): the list of tasks, the widgets
-Methods (what the thing can do): add, delete, mark done

This keeps related code organised in one place instead of scattered across the file.

3. The Constructor (__init__)

__init__ is a special method in Python and runs automatically the moment an object is created. It is used to set up the object's starting state. In this app it creates the window settings and the empty task list.

Python only recognises the exact name __init__ (two underscores each side). A misspelling such as __innit__ is silently treated as a normal method and never runs. This was one of the bugs I hit.

4. self and Instance Variables

self means "this particular object". Anything stored as self.something is an instance variable: it belongs to the object and is remembered between method calls.

Because self.tasks belongs to the object, every method can reach the same list without it being passed around.

5. Return Values and None

return sends a result back from a function, or exits it early.

python
def get_selected_index(self):
    ...
    if not selection:
        return None        # nothing selected
    return selection[0]    # the selected row number

None is Python's value meaning "nothing". The calling code checks if index is None: to decide what to do. A bare return is also used to stop a function early (an "early exit" or "guard clause").

6. Lists

A list is an ordered collection of items (it always starts at 0).

python
self.tasks.append(...)    # add to the end
self.tasks.pop(index)     # remove the item at a position (and return it)
self.tasks.clear()        # remove everything
self.tasks[index]         # get the item at a position

7. Dictionaries

A dictionary stores labelled values as key: value pairs.

python
{"task": "Buy milk", "done": False}

You read a value by its key: task["done"]. Using dictionaries lets each task carry several related pieces of information together.

8. Data Structures: a List of Dictionaries

Combining the two gives a simple "table" of data: the list is the table, each dictionary is a row, and each key is a column. This pattern is extremely common in real applications (and is very close to how JSON data looks).

9. Booleans and Truthiness

A boolean is True or False.

Empty things ("", [], (), None) count as False.
Non-empty things count as True.
python
if not task_text:        # True when the text box is empty
if not self.tasks:       # True when the list is empty

10. Conditionals (if / else)

Conditionals let code make decisions.

python
if not task_text:
    # show a warning and stop

There is also a one-line version, the conditional expression:

python
status = "✅" if task["done"] else "❌"

11. Loops

A for loop repeats code for each item in a collection.

python
for index, task in enumerate(self.tasks, start=1):

enumerate hands you a counter and the item together. start=1 makes the counter begin at 1 so humans see "1." rather than "0.".

12. Strings and String Methods

Strings are pieces of text. Useful methods used here:

.strip() removes spaces from the start and end
.get() (on the Entry widget) reads the text typed in

13. f-Strings

An f-string lets you place values directly inside text. Anything in { } is replaced by its value.

python
display_text = f"{index}. {task['task']} [{status}]"

14. Event-Driven Programming

A GUI program does not run top-to-bottom and finish. It waits for events (clicks, key presses) and reacts. root.mainloop() is the event loop: it keeps the window alive and listens until you close it.

15. Callbacks

A callback is a function you hand to something else to be called later, when an event occurs.

command=self.add_task

Note there are no brackets. Writing self.add_task() would run it immediately; writing self.add_task passes the function itself so the button can run it on click.

16. GUI Widgets and Layout
- Widgets are the visual building blocks: Label, Entry, Button, Listbox, Scrollbar, Frame.
- Frames are invisible containers used to group widgets into rows.
- .pack() is a layout manager that places widgets. Options like side, padx, pady, fill and expand control position and spacing.
- Widgets can be configured with keyword arguments such as bg= (background colour) and font=.

17. Keyword Arguments
Many options are passed by name rather than position:

tk.Button(text="Delete Task", bg="#c0392b", fg="white", command=self.delete_task)

Names make the code readable, but they must be spelled exactly right. A single typo causes an error.

18. Message Boxes (User Feedback and Confirmation)
messagebox.showinfo(...) tells the user something. messagebox.askyesno(...) asks a question and returns True or False, which the program uses to decide whether to continue. Confirming before a destructive action is good user-experience design.

19. Input Validation
Never trust user input. The app checks that a task is not empty before adding it, and checks that something is selected before deleting or marking. This prevents crashes and bad data.

20. Separation of Data and Display
The data (self.tasks) is kept separate from how it is shown (refresh_listbox). Changing one does not require rewriting the other. This idea underlies major design patterns such as MVC (Model-View-Controller).

21. Helper Methods and DRY (Don't Repeat Yourself)
get_selected_index() is a helper method: both mark_done and delete_task need the same selection logic, so it is written once and reused. Avoiding repeated code makes programs shorter and easier to fix.

22. The if __name__ == "__main__": Guard
This line means "only run the following when this file is run directly". It lets the file be imported by other programs without launching the window.

23. Code Comments and Readability
Comments (#like this) explain why code exists. Clear names (add_task, refresh_listbox) and consistent formatting make code understandable months or years later.

24. Debugging and Reading Error Messages
The most valuable skill this project teaches. Every bug I hit was a typo (__innit__, paddy, slide, commmand, resizeable, self.task vs self.tasks). The approach that works:

Read the last line of the error message.
Find the exact misspelled name it mentions.
Check spelling, capitalisation and consistency in the code.

Known Limitations
- Tasks are not saved. They disappear when the window is closed.
- A task's text cannot be edited after it has been added.
- Only one task can be selected at a time.
- Pressing Enter in the text box does not add the task; you must click the button.

Ideas for Future Improvements
-Save and load tasks using Python's json module
-Add a task by pressing Enter
-Edit an existing task (e.g. double-click)
-Add due dates and priorities
-Colour or strike through completed tasks
-Undo the last deletion
-Filter by done / not done

Tech Stack
-Language: Python 3
-GUI library: tkinter (Python standard library)
-Dependencies: none

Author
Miekaeel GitHub: @1darthcoder

License
This project is licensed under the MIT License. See the LICENSE file for details.
