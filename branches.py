#!/usr/bin/env python

import subprocess
import os

current_branch = subprocess.check_output("git rev-parse --abbrev-ref HEAD", shell=True)
subprocess.check_output("git fetch", shell=True)

try:
	total_branches = subprocess.check_output("git remote show origin | grep 'local out of date'", shell=True)
except subprocess.CalledProcessError:
	os.system('notify-send -u low "No new branches"')
	exit(1)

branches_list = total_branches.split("\n")

i = 0

for branch in branches_list:

	each_branch = branch.split("    ")	
	br = each_branch[1:2]
	if len(br) != 0:
		os.system("git checkout " + br.pop())
		os.system("git pull")
		i = i+1

subprocess.check_output("git checkout "+current_branch, shell=True) # return back to original branch
os.system("notify-send -u low 'Number of branches: "+str(i)+"'")