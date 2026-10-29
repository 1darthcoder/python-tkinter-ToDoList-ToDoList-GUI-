#TO-DO-LIST with a GUI (Python + tkinter)
#========================================
#WHAT THIS PROGRAM IS 
#   A small desktop window where you can add tasks, mark them as done,
#   delete them or clear the whole list. 
import tkinter as tk
from tkinter import messagebox

# self inside a class means "this particular  app" 
#anything saved as self.-- is remembered and can be used in every method in app
class TodoApp:
    def __init__(self, root): #constructer #root is main window
        self.root = root
        self.root.title("To-Do-List") #Window title
        self.root.geometry("500x450") #window size
        self.root.resizable(False, False) #stops user from resizing window
        self.root.configure(bg = "#f0f4f7")

        self.tasks = [] #real data of the whole app {"task": "buy milk", "done": False}
        self.setup_ui()

   
    def setup_ui(self):
        #padx- horizontal spacing around widget #pady - vertical spacing around widget
        #Setup for a widget for title at the top 
        title_label = tk.Label(
            self.root,  #sits on the main window
            text= "To-Do-List",
            font = ("Arial", 22, "bold"),
            bg = "#f0f4f7",
            fg = "#333"
        )
        #.pack() places widget on window 
        #pady=10 makes 10 pixels of empty space above and below it.
        title_label.pack(pady=10)

        # Frame is invisible container used to group text box and buttoon so can sit tg
        input_frame = tk.Frame(self.root, bg ="#f0f4f7")
        input_frame.pack(pady=10)


        # Entry is one line text box where user types a taask
        #sacce it as self.task_entry bcs add_task needs 
        #read frm it later. 
        self.task_entry =tk.Entry(
            input_frame, #sits inside input row
            font = ("Arial", 12),
            width = 30
        )
        #puts in te left row, padx(0,10)= 0 pixls on left, 10 on right
        self.task_entry.pack(side="left", padx=(0,10))


        #ADD TASK BUTTON
        add_button = tk.Button(
            input_frame, 
            text = "Add Task",
            font = ("Arial", 12),
            bg = "#27ae60",
            fg = "white",  
            padx = 10,
            # command = what to run when button is clicked
            #self.add_task = "callback"
            command = self.add_task # bcs theres no () hands over function to itseld, so buttom can run later when clicks
        )
        add_button.pack(side="left")

        # TASK LIST (listbox +scrollbar)
        #frame holding ^
        list_frame = tk.Frame(self.root, bg="#f0f4f7")
        # fill = both and expand= true lets area stretch ot use all
        #spare space in window
        list_frame.pack(pady=10, fill = "both", expand=True)

        #LISTBOX shows tasks one per row, lets user click
        # to select it. Saved as self.task_listbox bcs methods 
        #need to read from it or change it. 
        self.task_listbox = tk.Listbox(
            list_frame,
            font = ("Arial", 12),
            width = 45,         
            height = 10, 
            activestyle = "none" #no dotted underline on the selected row.
        )
        self.task_listbox.pack(side="left", fill="both", expand=True)

        #The scrollbar, placed on right side of list
        #fill y stretches it from top to bottom of list 
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        #LINKS list and scrollbar
        #lists tells scrollbar wher it is so scrollbar ahngles move when the list moves.
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        #scrollbar tells list to scrol when user drags handle
        scrollbar.config(command=self.task_listbox.yview)


        #MESSAGE LINE (feedback to the user)
        #label under list 
        self.info_label = tk.Label(
            self.root,
            text = "",
            font = ("Arial", 11),
            bg =  "#f0f4f7",
            fg = "#007acc"
        )
        self.info_label.pack(pady=5)


        #BOTTOM ROW OF BUTTONS
        #frame to hold three buttons side by side
        button_frame = tk.Frame(self.root, bg = "#f0f4f7")
        button_frame.pack(pady=10)

        #MARK DONE button runs 
        mark_done_button = tk.Button(
            button_frame,
            text = "Mark as Done" ,
            font = ("Arial", 11, "bold"),
            bg = "#2980b9",
            fg = "white",
            padx = 10,
            command=self.mark_done
        )
        mark_done_button.pack(side="left", padx=5)


        #DELETE TASK button. runs self.delete_task when clicked.
        delete_button = tk.Button(
            button_frame,
            text = "Delete Task",
            font = ("Arial", 11, "bold"),
            bg = "#c0392b",
            fg = "white",
            padx = 10,
            command=self.delete_task
        )
        delete_button.pack(side="left", padx=5)

        #CLEAR ALL Button. runs self.clear_all when clicked
        clear_button = tk.Button(
            button_frame,
            text = "Clear All",
            font = ("Arial", 11, "bold"),
            bg = "#7f8c8d",
            fg = "white",
            padx=10,
            command = self.clear_all
        )
        clear_button.pack(side="left", padx=5)

    #self.task is ereal data 
    #this methhod throws old pic away draws fresh one from
    #current data. called after every change to self.tasks
    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END) #delete every row currently shown #delete(first,last): 0 is the first row, tk.End means the last row 
        #loops through every task in data 
        #enumerate -> gives index - counter, task - dictionary for that task
        for index, task in enumerate(self.tasks, start=1):
            status = "✅" if task["done"] else "❌"
            display_text = f"{index}.{task['task']} [{status}]"
            self.task_listbox.insert(tk.END, display_text)

    def add_task(self):
        #read what user typed in text box
        #.get() -> returns the text in the box
        #.strip() -> removes spaces at start and end, 
        #containing only spaces counts as empty 
        task_text = self.task_entry.get().strip()

        #VALIDATION- never trust user input
        # if not task_text is True when the text is empty
        #empty tect counts as false, so not flips to true. 
        if not task_text:
            self.info_label.config(text = "Please enter a task first.")
            #return exits the method immediately, so nothing below runs
            #no empty task is added. - early exit
            return

        #add new task to end of the list 
        #new task alwats start as not done(false)
        self.tasks.append({"task" : task_text, "done" : False})
        
        #empty tect box ready for next task
        #delete(o,Tk.END) removes everything from 1st char
        #to the end 
        self.task_entry.delete(0, tk.END)

        #Show confirmation message under the list 
        self.info_label.config(text = f"Task '{task_text}' added!")
        #redraw list so new task appears on screen 
        self.refresh_listbox()

    #HELPER METHOD
    #works which user clicked list 
    #needed by both mark_done and delete_task
    #Returns:
    #row num
    #none if nothing selected
    def get_selected_index(self):

        #.curselection() turns selected row into tuple
        #if nothing selected return empty tuple()
        selection = self.task_listbox.curselection()
        
        #empty tuple count false 
        if not selection:
            messagebox.showinfo("No Selection", "Please select a task first.")
            return None
        return selection[0]

    #Mark done when clicked 
    def mark_done(self):

        #index asks helper wich row selected 
        index = self.get_selected_index()
        if index is None:
            return 

        #select task dictionary
        #cahnges it done val to true
        self.tasks[index]["done"] = True

        #tell user then redraw X to check
        self.info_label.config(text = "Task marked as done!")
        self.refresh_listbox()

    #delete task 
    def delete_task(self):
        index = self.get_selected_index()
        #sME START AS MARK_DONE: FINDS SELECTED ROW, STOP IF NONE
        if index is None:
            return

        #.POP(INDEX) 2 things at once
        #1 remove irem at that posit from list
        #2 gives removed item back
        removed = self.tasks.pop(index)
        #removed is task dict so removed['task'] is text
        self.info_label.config(text= f"Deleted task: {removed['task']}")
        self.refresh_listbox()

    #clear_all when Clear All BUTTOn clicked
    def clear_all(self):
        if not self.tasks:
            self.info_label.config(text = "No tasks to clear.")
            return

        #askyesno show pop up wih YES NO buttons 
        #It gives true if cilck yes, false if clicked no
        #so code inside this if only run when click yes
        #ask before destroying act pevent acciden
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            #.clear() remove every item from the list
            self.tasks.clear()
            self.refresh_listbox()
            self.info_label.config(text = "All tasks cleared!")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
