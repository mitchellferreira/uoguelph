#!/usr/bin/python

from Tkinter import *


#Calculator Screen
def std_gui():

	root = Tk()
	root.geometry("500x500")
	root.title("Calculator")

	frame_holder = Frame(root)
	frame_holder.config(width=500, height=500)
	frame_holder.pack(fill=BOTH, expand=1)
	frame_holder.columnconfigure(1, weight=1)
	frame_holder.columnconfigure(3, pad=7)
	frame_holder.rowconfigure(3, weight=1)
	frame_holder.rowconfigure(5, pad=7)

	list_box = Listbox(frame_holder)
	list_box.config(width=55, height=16)
	list_box.grid(row=0, column=0, rowspan=4, columnspan=2, padx=5)

	entry_box = Entry(frame_holder)
	entry_box.config(width=55)
	entry_box.place(x=10, y=450)
	entry_box.grid(row=4, column=0, columnspan=2, padx=5)

	def equals_command():
		in_String = get_entry_box()
		insert_to_listbox(in_String)
		io_list[] = ["std",in_String]
		#io_list[] = inputHandler(io_list)

	def graph_command():
		in_String = get_entry_box()
		insert_to_listbox(in_String)
		io_list[] = ["graph",in_String]
		#io_list[] = inputHandler(io_list)

	def get_entry_box():
		in_String = entry_box.get()
		entry_box.delete(0,END)
		return in_String

	def insert_to_listbox(in_String):
		list_box.insert(END, in_String)

	def insert_error(in_String):
		in_String = "ERROR: " + in_String
		insert_to_listbox(in_String)


	equals_button = Button(frame_holder, text="Equals", command=equals_command)
	equals_button.grid(row=4 ,column=2, padx=5)

	graph_button = Button(frame_holder, text="Graph", command=graph_command)
	graph_button.grid(row=3, column=2, padx=5)

	mainloop();


