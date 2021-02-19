from tkinter import *

class Table:
    '''Mimic table for tkinter'''
    def __init__(self, root):
        for i in range(tot_rows):
            for j in range(tot_cols):
                self.e = Label(root, width=20, fg='#888',font=('Arial',16,'bold'), text=lst[i][j])
                self.e.grid(row=i, column=j)
                # self.e.insert(END, lst[i][j])
# lst = [
#     ('10000','|','23580'),
#     ('00000','|','92728'),
#     ('41250','|','78282'),
#     ('99999','|','09284')
# ]

# tot_rows = len(lst)
# tot_cols = len(lst[0])