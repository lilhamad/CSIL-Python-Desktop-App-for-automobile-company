from tkinter import *
# from stringvariables import *
# from functionalties import *
from tkinter import messagebox, StringVar

import tkinter as tk


root=Tk()
sizex = 1000
sizey = 800
posx  = 0
posy  = 0
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
root.configure(bg='#000')
myframe=Frame(root,width=50,height=100,bd=0)
myframe.place(x=10,y=10)

canvas=Canvas(myframe)
canvas.configure(bg='#FF7F50')
frame=Frame(canvas)
frame.configure(bg='#FF7F50')
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

calculate_button = ''
replacement_charge_label = ''
replacement_charge_button = ''
generate_button = ''
more_row_entry = ''
replacement_charge_value = ''
current_end_row = 6
end =0
bg_orange = "#FF7F50"
# page.configure(bg='#FF7F50')
dana_list, open_list, foreign_list = [], [], []
space_one, error_label, total_dana_price_label, total_dana_price_entry, tw_percent_total_dana_label, tw_percent_total_dana_entry = '','','','','',''
total_open_price_label,total_open_price_entry, total_open_price_plus_label,total_open_price_plus_entry, fiv_percent_total_plus_open_label, fiv_percent_total_plus_open_entry, sev_percent_total_plus_open_plus_label, sev_percent_total_plus_open_plus_entry='','','','','','','',''



stringvar = StringVar()
name_0_value,name_1_value,name_2_value,name_3_value,name_4_value = StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
more_row_value = IntVar()
replacement_charge_value = IntVar()
dana_0_value,dana_1_value,dana_2_value,dana_3_value,dana_4_value = IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
foreign_0_value,foreign_1_value,foreign_2_value,foreign_3_value,foreign_4_value, = IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
open_0_value,open_1_value,open_2_value,open_3_value,open_4_value = IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
error_message = StringVar()

total_dana_price = IntVar()
tw_percent_total_dana = IntVar()
total_open_price = IntVar()
total_open_price_plus_l = IntVar()
sev_percent_total_plus_open_plus_l = IntVar()
fiv_percent_total_plus_open_l = IntVar()
page = frame

def generate_initial_interface():
    colspan = 4
    dana_0_value.set(45),more_row_value.set(1),dana_1_value.set(45),dana_2_value.set(45),dana_3_value.set(45),dana_4_value.set(45)
    open_0_value.set(45),open_1_value.set(45),open_2_value.set(45),open_3_value.set(45),open_4_value.set(45)
    foreign_0_value.set(0.0),foreign_1_value.set(0.0),foreign_2_value.set(0.0),foreign_3_value.set(0.0),foreign_4_value.set(0.0)
    global dana_list
    global open_list
    global foreign_list
    dana_list = [dana_0_value, dana_1_value, dana_2_value, dana_3_value, dana_4_value]
    open_list = [open_0_value, open_1_value, open_2_value, open_3_value, open_4_value]
    foreign_list = [foreign_0_value, foreign_1_value, foreign_2_value, foreign_3_value, foreign_4_value]

    # headers and spaces
    csil_title = tk.Label(page, bg=bg_orange, font=(18),text='Combined System International Limited (CSIL) Pricing Software', pady=10).grid(row=1, column=3,columnspan=4)
    product_name_label = tk.Label(page, bg=bg_orange, text='Product Name').grid(row=2, column=2)
    dana_price_label = tk.Label(page, bg=bg_orange, text='Dana Price').grid(row=2, column=4)
    froreign_price_label = tk.Label(page, bg=bg_orange, text='Foreign Price').grid(row=2, column=6)
    open_market_price_label = tk.Label(page, bg=bg_orange, text='Open Market Price').grid(row=2, column=8)

    # input fields
    item_number = tk.Label(page, bg=bg_orange, text='Item 1').grid(row=3, column=1)
    product_name = tk.Entry(page,textvariable=name_0_value).grid(row=3, column=2)
    dana_price = tk.Entry(page,textvariable=dana_0_value).grid(row=3, column=4)
    open_price = tk.Entry(page,textvariable=foreign_0_value).grid(row=3, column=6)
    open_market_price = tk.Entry(page,textvariable=open_0_value).grid(row=3, column=8, pady=5)

    item_number = tk.Label(page, bg=bg_orange, text='Item 2').grid(row=4, column=1)
    product_name = tk.Entry(page, textvariable=name_1_value).grid(row=4, column=2)
    dana_price = tk.Entry(page,textvariable=dana_1_value).grid(row=4, column=4)
    foreign_price = tk.Entry(page,textvariable=foreign_1_value).grid(row=4, column=6)
    open_market_price = tk.Entry(page,textvariable=open_1_value).grid(row=4, column=8, pady=5)

    item_number = tk.Label(page, bg=bg_orange, text='Item 3').grid(row=5, column=1)
    product_name = tk.Entry(page, textvariable=name_2_value).grid(row=5, column=2)
    dana_price = tk.Entry(page, textvariable=dana_2_value).grid(row=5, column=4)
    foreign_price = tk.Entry(page, textvariable=foreign_2_value).grid(row=5, column=6)
    open_market_price = tk.Entry(page, textvariable=open_2_value).grid(row=5, column=8, pady=5)

    item_number = tk.Label(page, bg=bg_orange, text='Item 4').grid(row=6, column=1)
    product_name = tk.Entry(page, textvariable=name_3_value).grid(row=6, column=2)
    dana_price = tk.Entry(page,textvariable=dana_3_value).grid(row=6, column=4)
    foreign_price = tk.Entry(page,textvariable=foreign_3_value).grid(row=6, column=6)
    open_market_price = tk.Entry(page,textvariable=open_3_value).grid(row=6, column=8, pady=5)

    item_number = tk.Label(page, bg=bg_orange, text='Item 5').grid(row=7, column=1)
    product_name = tk.Entry(page, textvariable=name_4_value).grid(row=7, column=2)
    dana_price = tk.Entry(page,textvariable=dana_4_value).grid(row=7, column=4)
    foreign_price = tk.Entry(page,textvariable=foreign_4_value).grid(row=7, column=6)
    open_market_price = tk.Entry(page,textvariable=open_4_value).grid(row=7, column=8, pady=5)



    global replacement_charge_button
    global replacement_charge_label
    global calculate_button
    global generate_button
    global more_row_entry

    global space_one
    global error_label
    global total_dana_price_label
    global total_dana_price_entry
    global tw_percent_total_dana_label
    global tw_percent_total_dana_entry
    global total_open_price_label
    global total_open_price_entry
    global total_open_price_plus_label
    global total_open_price_plus_entry
    global fiv_percent_total_plus_open_label
    global fiv_percent_total_plus_open_entry
    global sev_percent_total_plus_open_plus_label
    global sev_percent_total_plus_open_plus_entry

    f = Frame(page, height=1, width=50, bg="black")
    f.grid(row=8, column=4, pady=2)

    replacement_charge_label = tk.Label(page, bg=bg_orange, pady=8, text='Replacement Charge')
    replacement_charge_label.grid(row=8, column=1,pady=8,)
    replacement_charge_button = tk.Entry(page, textvariable=replacement_charge_value)
    replacement_charge_button.grid(row=8, column=2)



    calculate_button = tk.Button(page, text="    Calculate    ", command=generate_result_interface)
    calculate_button.grid(row=9, column=2)
    more_row_entry = tk.Entry(page, width=3,  textvariable=more_row_value)
    more_row_entry.grid(row=9, column=4,padx=7, sticky=W)
    generate_button = tk.Button(page, text="More rows", command=add_some_more_rows)
    generate_button.grid(row=9, column=4, padx=7, pady=10, sticky=E)

    space_one = tk.Label(page, font=(16), bg=bg_orange, text='RESULTS')
    error_label = tk.Label(page, bg=bg_orange, fg='red', textvariable=error_message)

    total_dana_price_label = tk.Label(page, justify='left',bg=bg_orange, text='Total Dana Price is: ')
    total_dana_price_entry = tk.Entry(page, justify='left', bg='white', textvariable=total_dana_price)

    tw_percent_total_dana_label = tk.Label(page, justify='left',bg=bg_orange, text="22.5% of Total Dana Price is: ")
    tw_percent_total_dana_entry = tk.Entry(page, justify='left', textvariable=tw_percent_total_dana)

    total_open_price_label = tk.Label(page, justify='left',bg=bg_orange, text='Total Open Market Price is: ')
    total_open_price_entry = tk.Entry(page, bg='white', justify='left', textvariable=total_open_price)

    total_open_price_plus_label = tk.Label(page, bg=bg_orange,justify='left', text='Total OP + Total OP  + 22.5% of Total Dana Price is : ')
    total_open_price_plus_entry = tk.Entry(page, bg='white', justify='left', textvariable=total_open_price_plus_l)

    fiv_percent_total_plus_open_label = tk.Label(page, bg=bg_orange, justify='left',text='50% of Total OP + Total OP  + 22.5% of Total Dana Price is : ')
    fiv_percent_total_plus_open_entry = tk.Entry(page, bg='white', justify='left',textvariable=fiv_percent_total_plus_open_l)

    sev_percent_total_plus_open_plus_label = tk.Label(page, bg=bg_orange,justify='left',text='75% of Total OP + Total OP  + 22.5% of Total Dana Price is : ')
    sev_percent_total_plus_open_plus_entry = tk.Entry(page,  justify='left',textvariable=sev_percent_total_plus_open_plus_l)

    total_ai_label = tk.Label(page, bg=bg_orange,justify='left',text='Total A1 ')
    total_ai_entry = tk.Entry(page,  justify='left',textvariable=sev_percent_total_plus_open_plus_l)

    error_message.set('')
    space_one.grid(row=current_end_row + 3, column=2,sticky=W)
    error_label.grid(row=current_end_row + 3,column=2, sticky=E, columnspan=colspan,pady=4)
    total_dana_price_label.grid(row=current_end_row + 4, column=2, sticky=W)
    total_dana_price_entry.grid(row=current_end_row + 4, column=2, sticky=E, columnspan=colspan ,pady=4)
    tw_percent_total_dana_label.grid(row=current_end_row + 5, column=2, sticky=W)
    tw_percent_total_dana_entry.grid(row=current_end_row + 5, column=2, sticky=E, columnspan=colspan,pady=4)
    total_open_price_label.grid(row=current_end_row + 6, column=2, sticky=W)
    total_open_price_entry.grid(row=current_end_row + 6, column=2, sticky=E, columnspan=colspan,pady=4)
    total_open_price_plus_label.grid(row=current_end_row + 7, column=2, sticky=W)
    total_open_price_plus_entry.grid(row=current_end_row + 7, column=2, sticky=E, columnspan=colspan,pady=4)
    fiv_percent_total_plus_open_label.grid(row=current_end_row + 8,column=2, sticky=W)
    fiv_percent_total_plus_open_entry.grid(row=current_end_row + 8,column=2, sticky=E, columnspan=colspan,pady=4)
    sev_percent_total_plus_open_plus_label.grid(row=current_end_row + 9, column=2, sticky=W)
    sev_percent_total_plus_open_plus_entry.grid(row=current_end_row + 9, column=2, sticky=E, columnspan=colspan,pady=4)


def add_x_more_entry(x):
    item_number = tk.Label(page, bg=bg_orange, text='Item '+str(x)).grid(row=x+2, column=1)
    product_name = tk.Entry(page, textvariable = 'name_'+str(x)+'value').grid(row=x+2, column=2)
    dana_price = tk.Entry(page, textvariable='dana_'+str(x)+'value')
    dana_price.grid(row=x+2, column=4)
    foreign_price = tk.Entry(page, textvariable='foreign_'+str(x)+'value')
    foreign_price.grid(row=x+2, column=6)
    open_market_price = tk.Entry(page, textvariable='open_'+str(x)+'value')
    open_market_price.grid(row=x+2, column=8, pady=5)
    dana_list.append(dana_price)
    open_list.append(open_market_price)
    foreign_list.append(foreign_price)

def add_some_more_rows():
    global end
    global current_end_row
    end = int(more_row_value.get())+current_end_row
    if end<300:
        for x in range(current_end_row, end):
            add_x_more_entry(x)

    current_end_row = end

    replacement_charge_label.grid(row=end +2, column=1)
    replacement_charge_button.grid(row=end +2, column=2)
    calculate_button.grid(row=end+3,column=3)
    more_row_entry.grid(row=end+3,column=4)
    generate_button.grid(row=end+3,column=5)

    space_one.grid(row=end+4, column=2,sticky=W)
    error_label.grid(row=end + 5,column=2, sticky=W)

    total_dana_price_label.grid(row=end + 6, column=2, sticky=W)
    total_dana_price_entry.grid(row=end + 6, column=3, sticky=W)
    tw_percent_total_dana_label.grid(row=end + 7, column=2, sticky=W)
    tw_percent_total_dana_entry.grid(row=end + 7, column=3, sticky=W)
    total_open_price_label.grid(row=end + 8, column=2, sticky=W)
    total_open_price_entry.grid(row=end + 8, column=3, sticky=W)
    total_open_price_plus_label.grid(row=end + 9, column=2, sticky=W)
    total_open_price_plus_entry.grid(row=end + 9, column=3, sticky=W)
    fiv_percent_total_plus_open_label.grid(row=end + 10,column=2, sticky=W)
    fiv_percent_total_plus_open_entry.grid(row=end + 10,column=3, sticky=W)
    sev_percent_total_plus_open_plus_label.grid(row=end + 11, column=2, sticky=W)
    sev_percent_total_plus_open_plus_entry.grid(row=end + 11, column=3, sticky=W)


def give_total_dana_price():
    total_dana_price_value = 0
    for y in range(current_end_row - 1):
        total_dana_price_value += float(dana_list[y].get())
    return total_dana_price_value


def give_total_open_price():
    total_open_price_value = 0
    for y in range(current_end_row - 1):
        total_open_price_value += float(open_list[y].get())
    return total_open_price_value


def give_total_foreign_price():
    total_foreign_price_value = 0
    for y in range(current_end_row - 1):
        total_foreign_price_value += float(foreign_list[y].get())
    return total_foreign_price_value


def generate_result_interface():
    try:
        error_message.set('')
        td = give_total_dana_price()
        total_dana_price.set(str(td))

        l = 0.225*td
        tw_percent_total_dana.set(str(l))

        # Ototal
        to = give_total_open_price()
        total_open_price.set(str(to))

        tf = give_total_foreign_price()

        total_open_price_plus_l.set(str((2*to)+l))
        print(replacement_charge_value.get())
        fiv_percent_total_plus_open_l.set(str((0.5*to)+to+l))

        sev_percent_total_plus_open_plus_l.set(str((0.75*to)+to+l))

    except TypeError:
        pass
    except ValueError:
        messagebox.showinfo('Error', 'Invalid value')
        error_message.set("Invalid value")

#
# class App(object):
#     def __init__(self):
#         generate_initial_interface()
#
# app = App()


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=960,height=650)


myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)
generate_initial_interface()
root.mainloop()