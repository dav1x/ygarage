#!/usr/local/bin/python
# mac path fts
#!/bin/python

import os
import datetime
import random
import argparse
import sys

path = "/Users/dphillip/Desktop/Workouts/"
logdir = str(datetime.date.today()) 
workouts = path + "/workouts.list"
yes_answers = ['y', 'Y', 'yes', 'YES'] 

def addNewWorkout():
	print('\nInput text and end with Ctrl-d on a newline\n')
        newWorkout = sys.stdin.read()
	logWorkout(newWorkout)

def promptForWorkout():
	genRandomWorkout()
	
def genRandomWorkout():
	
	lines = open(workouts).read().splitlines()
	quickie = random.choice(lines)
 
	print quickie
		
	logWorkout(quickie)
	


def summarizeWorkouts():
	
        logname = (os.path.join(path, logdir)) + "/garage.log"

	print logname
        lines = open(logname, "r")
	for line in lines:
		print line.rstrip('\n')
	
        lines.close()

def logWorkout(quickie):

	if not os.path.exists(os.path.join(path, logdir)):
		os.mkdir(os.path.join(path, logdir))

        logname = (os.path.join(path, logdir)) + "/garage.log"
	
	if quickie:
                file = open(logname, "a")
                file.writelines(str(quickie))
                file.writelines('\n')
                file.close()

parser = argparse.ArgumentParser(description='ygarage will assign log and summarize your garage work')
parser.add_argument('--new', '-n', action='store_true')
parser.add_argument('--summary', '-s', action='store_true')
parser.add_argument('--repeat', '-r', action='store_true')
parser.add_argument('--add', '-a', action='store_true')

args = vars(parser.parse_args())

if args['new']:
	promptForWorkout()

if args['summary']:
	summarizeWorkouts()

if args['repeat']:
	print 'repeat last workout code here'

if args['add']:
	addNewWorkout()
