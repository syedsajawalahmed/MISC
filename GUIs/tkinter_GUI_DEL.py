import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 400,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Automated Amazon Search Engined')
label1.config(font=('Times', 20))
canvas1.create_window(200, 20, window=label1)

label2 = tk.Label(root, text='Type SpreadSheet Name:')
label2.config(font=('Times', 15))
canvas1.create_window(200, 750, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

# def getSquareRoot ():
    
#     x1 = entry1.get()
    
#     label3 = tk.Label(root, text= 'The Square Root of ' + x1 + ' is:',font=('Times', 10))
#     canvas1.create_window(200, 210, window=label3)
    
#     label4 = tk.Label(root, text= float(x1)**0.5,font=('Times', 10, 'bold'))
#     canvas1.create_window(200, 230, window=label4)

def name_of_workspace():
    x1 = entry1.get()
    print(x1)
    
button1 = tk.Button(text='Google WorkSheet Name', command=name_of_workspace, bg='brown', fg='white', font=('Times', 9))
canvas1.create_window(200, 180, window=button1)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 220, window=entry1)

def search_keyword():
    x2 = entry1.get()
    print(x2)
    
button1 = tk.Button(text='Search Keyword', command=search_keyword, bg='brown', fg='white', font=('Times', 9))
canvas1.create_window(200, 250, window=button1)


root.mainloop()