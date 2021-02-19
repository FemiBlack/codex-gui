import tkinter as tk
# from table import Table
from tkinter import ttk, messagebox

# validate
def callback_name(input):
    if input.isalpha():
        print(input)
        return True
    elif input == '':
        print(input)
        return True
    else:
        print(input)
        return False

def callback_key(input):
    if input.isdigit():
        print(input)
        return True
    elif input == '':
        print(input)
        return True
    else:
        print(input)
        return False

def version_info():
    messagebox.showinfo('Version Info','Codex\nVersion:1.0.0')
def xxx():
    messagebox.showinfo('TEMP','a new instance of the codex class would be called here!')
# name_var=tk.StringVar()
# pass_var=tk.StringVar()

# name=name_var.ge()
# pass=name_var.ge()

# Initialize window,set size
window = tk.Tk()
window.title("Welcome to XXX")
window.geometry('650x600')

# Create toolbar menu
menu = tk.Menu(window)
new_item = tk.Menu(menu) # tearoff=0
new_item.add_command(label='New', command=xxx)
new_item.add_separator()
new_item.add_command(label='Info', command=version_info)
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

# Create tabs
tab_ctrl = ttk.Notebook(window)
tab1 = ttk.Frame(tab_ctrl)
tab2 = ttk.Frame(tab_ctrl)
tab3 = ttk.Frame(tab_ctrl)
tab_ctrl.add(tab1,text="Tab1")
tab_ctrl.add(tab2,text="Tab2")
tab_ctrl.add(tab3,text="Tab3")
tab_ctrl.grid(row=0, column=1)

# Create different sections(frames)
txt_edit = tk.Text(tab1, width=60)
txt_rule = tk.Text(tab3, width=60, fg="green", font=('Cascadia Code', 10))
txt_rule.bind('<Key>', lambda e:'break')
fr_btns = tk.Frame(window)
fr_on = tk.Frame(window)

# Section One
codexlogo = tk.Label(fr_btns, text="CODEX", font=('Ar Destine', 30))
codexlogo.grid(row=1,column=0)


def find():
    txt_rule.tag_remove('highlight', '1.0', tk.END)
    s='Winner'
    if s:
        idx='1.0'
        while 1:
            idx=txt_rule.search(s,idx,nocase=1,stopindex=tk.END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(s))
            txt_rule.tag_add('found', idx, lastidx)
            idx= lastidx
        txt_rule.tag_config('found', foreground='red')
    
def quit_game():
    res = messagebox.askyesno('Exit Game', 'Are you sure you want to exit the game?!')
    if res:
        window.destroy()

def start_game():
    tab_ctrl.select(tab1)
    player1.focus()

def show_rules():
    txt_rule.configure(fg="red")
    txt_rule.delete('1.0', tk.END)
    t = txt_rule.get('1.0', tk.END)
    tab_ctrl.select(tab3)
    if t == '\n':
        in_file = open('resources/rules.txt', 'r', encoding='utf-8')
        content = in_file.read()
        txt_rule.insert(tk.END, content)
        in_file.close()

def show_record():
    txt_rule.configure(fg="green")
    txt_rule.delete('1.0', tk.END)
    t = txt_rule.get('1.0', tk.END)
    tab_ctrl.select(tab3)
    if t == '\n':
        in_file = open('resources/records.txt', 'r', encoding='utf-8')
        content = in_file.read()
        txt_rule.insert(tk.END, content)
        in_file.close()
    find()
start_btn = tk.Button(fr_btns, text="START GAME", bg="#ccc", fg="#444",
    height=2, width=10, font=('Ar Destine', 12), command=start_game)
start_btn.grid(row=2,column=0, sticky="ew", padx=5, pady=5)

record_btn = tk.Button(fr_btns, text="RECORDS", bg="#ccc", fg="#444",
    height=2, width=10, font=('Ar Destine', 12), command=show_record)
record_btn.grid(row=3,column=0, sticky="ew", padx=5, pady=5)

rules = tk.Button(fr_btns, text="RULES", bg="#ccc", fg="#444",
    height=2, width=10, font=('Ar Destine', 12), command=show_rules)
rules.grid(row=4,column=0, sticky="ew", padx=5, pady=5)

exit_game = tk.Button(fr_btns, text="QUIT", bg="#ccc", fg="#444",
    height=2, width=10, font=('Ar Destine', 12), command=quit_game)
exit_game.grid(row=5,column=0, sticky="ew", padx=5, pady=5)


footer = tk.Label(fr_btns, text="::made by femiiblack ©", font=('Cascadia Code', 8))
footer.grid(row=6, column=0)

txt_p1 = tk.Label(fr_on, text="Player One", padx=50)
txt_p1.grid(row=0, column=0)

txt_p2 = tk.Label(fr_on, text="Secret Key", state='disabled')
txt_p2.grid(row=0, column=1)

txt_p3 = tk.Label(fr_on, text="Player Two", padx=50, state='disabled')
txt_p3.grid(row=2, column=0)

txt_p4 = tk.Label(fr_on, text="Secret Key")
txt_p4.grid(row=2, column=1)

txt_moves = tk.Label(fr_on, text="Moves", padx=50)
txt_moves.grid(row=0, column=2)


reg_n = fr_on.register(callback_name)
reg_k = fr_on.register(callback_key)

player1 = tk.Entry(fr_on, bg="#ccc", width=10)
player1.grid(row=1, column=0)
player1.config(validate='key', validatecommand=(reg_n, '%P'))

key1 = tk.Entry(fr_on, bg="#ccc", width=10, show='*')
key1.grid(row=1, column=1)
key1.config(validate='key', validatecommand=(reg_k, '%P'))

player2 = tk.Entry(fr_on, bg="#ccc", width=10)
player2.grid(row=3, column=0)
player2.config(validate='key', validatecommand=(reg_n, '%P'))

key2 = tk.Entry(fr_on, bg="#ccc", width=10, show='*')
key2.grid(row=3, column=1)
key2.config(validate='key', validatecommand=(reg_k, '%P'))
def count():
    count_ln = len(open('resources/game.txt', encoding='utf-8').readlines())
    lbl_move.config(text=(count_ln-2))
    fr_on.after(500,count)

lbl_move = tk.Label(fr_on, fg="red")
lbl_move.grid(row=1, column=2)
count()
lbl_win = tk.Label(fr_on, text='Mr.Black', fg="green")
lbl_win.grid(row=3, column=2)

txt_winner = tk.Label(fr_on, text="Winner")
txt_winner.grid(row=2, column=2)

fr_btns.grid(row=0,column=0, sticky="ns")
fr_on.grid(row=7,column=1, sticky="w")
txt_edit.grid(row=0, column=1, sticky="n")
txt_rule.grid(row=0, column=1, sticky="n")


# Tab2

class Table:
    '''Mimic table for tkinter'''
    def __init__(self, root):
        for i in range(tot_rows):
            for j in range(tot_cols):
                self.e = tk.Label(root, width=10, fg='#888',font=('Arial',16,'bold'), text=lst[i][j])
                self.e.grid(row=i, column=j)

lst = [
    ('PLAYER 1','PLAYER 2'),
    ('10000','23580'),
    ('00000','92728'),
    ('41250','78282'),
    ('99999','09284')
]

tot_rows = len(lst)
tot_cols = len(lst[0])

tabular = Table(tab2)

# Tab3

window.mainloop()






# window.rowconfigure(0, minsize=500, weight=1)
# window.columnconfigure(1, minsize=500, weight=1)


# frame_a = tk.Frame()
# frame_b = tk.Frame()

# lbl = tk.Label(frame_b, text="Hello")# font=('Arial Bold', 50))
# lbl.pack()
# lbl.grid(column=0, row=0)

# canvas = tk.Canvas(height=500, width=500, bg="#263d42")
# canvas.pack()
# txt = tk.Entry(frame_b, bg="#ccc", width=10) # state='disabled'
# txt.pack()
# txt.grid(column=1, row=0)
# # txt.focus()
# def clicked():
#     res = 'Welcome to ' + txt.get()
#     lbl.configure(text=res)

# btn.grid(column=2, row=0)
# frame_a.grid()
# frame_b.pack()

# showwarning
# showerror
# askquestion
# askyesno
# askyesnocancel
# askokcancel
# askretrycancel
