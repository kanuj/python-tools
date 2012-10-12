"""
	@author: Kanuj Bhatnagar
	@description: Search git branches by wildcard and then checkout to them by index.
	@usage:	python checkout.list.py [SEARCH_TERM]
			Ex: 'python checkout.list.py production' will list all branches matching the word 'production'
	To switch to a branch, call python checkout.list.py production N to switch to Nth found branch
"""

import subprocess
import sys

if len(sys.argv) == 1:
	print 'Please provide atleast one search criteria.'
	exit(1)

arg = sys.argv[1]

index = ''

if len(sys.argv) == 3:
	index = sys.argv[2]

try:
	total_branches = subprocess.check_output("git branch | grep "+str(arg), shell=True)
	branch_list = total_branches.split('\n')
	branch_list = filter(None, branch_list)
	
	if index != '':
		switch_branch = branch_list[int(index)-1].replace('*','');
		subprocess.check_output("git checkout "+switch_branch, shell=True)
		exit(1)


	print str(len(branch_list))+' branches found: \n'

	i = 1;

	for branch in branch_list:

		print '\033[0m'+branch.strip()+' \033[92m['+str(i)+']'+'\033[0m'
		i = i+1

except subprocess.CalledProcessError:
	print 'No branches found matching the search criteria.'
	exit(1)
