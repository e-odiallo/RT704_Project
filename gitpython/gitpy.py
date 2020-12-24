#!/usr/bin/python3

from git import Repo 

#Repo.clone_from('https://github.com/Kinda00/OS_Project/','/home/rt704/test')

#repo = git.Repo('https://github.com/Kinda00/OS_Project/')

#for branch in repo.branches:
#    print(branch)
new_repo = Repo.init('test-gitpy')
my_repo = Repo('test-gitpy')

my_repo.index.add('README.md')

