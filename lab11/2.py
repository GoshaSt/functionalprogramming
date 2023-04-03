import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)

canvas.create_oval(5, 90, 400, 310, fill='#0F9D58', outline='')

canvas.create_text(80, 200, text='G', font=('Product Sans', 140, 'bold'), fill='#4285F4')
canvas.create_text(175, 200, text='e', font=('Product Sans', 70, 'bold'), fill='#DB4437')
canvas.create_text(230, 200, text='o', font=('Product Sans', 70, 'bold'), fill='#F4B400')
canvas.create_text(275, 200, text='r', font=('Product Sans', 70, 'bold'), fill='#4285F4')
canvas.create_text(325, 200, text='g', font=('Product Sans', 70, 'bold'), fill='#DB4437')
canvas.create_text(360, 200, text='i', font=('Product Sans', 70, 'bold'), fill='#F4B400')
canvas.create_text(380, 200, text='i', font=('Product Sans', 70, 'bold'), fill='#4285F4')


canvas.pack()
root.mainloop()
