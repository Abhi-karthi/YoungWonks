import tk_practice_2 as tk

root = tk.Tk()

entry = tk.Entry(root)
entry.insert(0, "Enter your nam

def disappear_text():
    entry.delete(0, tk.END)

entry.bind("<Button-1>", disappear_text)

entry.pack()

root.mainloop()
