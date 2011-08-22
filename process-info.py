#!/usr/bin/python2

import sys
import os.path
import subprocess

def get_description(command):
	if os.path.dirname(command) != '':
		command = os.path.basename(command)
	whatis = subprocess.Popen(["whatis", command], 
			stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].split()
	if whatis != []:
		if whatis[1] in ["(1)", "(6)", "(8)"]:
			return " ".join(whatis[3:])

def get_name_description(pid):
	com_file_path = "/proc/" + pid + "/comm"
	if os.path.exists(com_file_path):
		with open(com_file_path) as f:
			name = f.read().split()[0]
	description = get_description(name)
	return name, description

if __name__ == "__main__":
	command_to_query = sys.argv[1]
	if command_to_query.isdigit():
		command, description = get_name_description(command_to_query)
	else:
		description = get_description(command_to_query)
	if description:
		try:
			print command + ":", description
		except NameError:
			print description
	else:
		print "ERROR: no info found for", command_to_query
