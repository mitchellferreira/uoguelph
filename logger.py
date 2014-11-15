#!/usr/bin/python

import os
from time import *

def logger(io_list[]):

	file_name = "logs/calc_" + strftime("%d_%m_%Y") + ".log"

	date = strftime("%d/%m/%Y")
	time = strftime("%H:%M:%S")
	msg_type = io_list[0]
	msg_text = io_list[1]
	output = "[" + msg_type + "] " + date + " " + time + " - " + msg_text + "\n"

	if os.path.isfile(file_name):
		f = open(file_name,"a")
	else:
		f = open(file_name,"w")

	f.write(output)
	if len(io_list) == 3:
		f.write(io_list[2])

	#assume io_list[2] is from format_exc(limit=1)

	f.close()


