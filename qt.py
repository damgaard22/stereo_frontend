import tkinter as tk
from tkinter import ttk
import time
import sys

master = tk.Tk()

style = ttk.Style()

tree = ttk.Treeview(master, style="mystyle.Treeview")
next = 0

# while True:
#   replay_time = get_replay_time()
#   while replay_time < alerts[next][0]:
#       tree.insert(alerts[next])
#       try:
#           next += 1
#           alerts[next]

tree["columns"] = ("one", "two", "three", "four", "five", "six")
tree.column("#0", width=270, minwidth=270, stretch=tk.NO, anchor=tk.W)
tree.column("one", width=150, minwidth=150, stretch=tk.NO, anchor=tk.W)
tree.column("two", width=400, minwidth=200, anchor=tk.W)
tree.column("three", width=80, minwidth=50, stretch=tk.NO, anchor=tk.W)
tree.column("four", width=270, minwidth=270, stretch=tk.NO, anchor=tk.W)
tree.column("five", width=270, minwidth=270, stretch=tk.NO, anchor=tk.W)
tree.column("six", width=270, minwidth=270, stretch=tk.NO, anchor=tk.W)



tree.heading("#0", text="Time", anchor=tk.W)
tree.heading("one", text="Symbol", anchor=tk.W)
tree.heading("two", text="Price", anchor=tk.W)
tree.heading("three", text="Float", anchor=tk.W)
tree.heading("four", text="Volume 5% Chg", anchor=tk.W)
tree.heading("five", text="Relative Volume", anchor=tk.W)
tree.heading("six", text="Change (%)", anchor=tk.W)

tree.insert("", 1, "2", text="QQQ", values=("23-Jun-17 11:05","File folder","226GB"))
tree.insert("", 1, "3", text="VIX", values=("23-Jun-17 11:05","File folder","227GB"))
tree.insert("", 1, "4", text="UVXY", values=("23-Jun-17 11:05","File folder","228GB"))


tree.pack(side=tk.TOP, fill=tk.X)
master.mainloop()

