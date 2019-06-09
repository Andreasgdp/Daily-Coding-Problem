import sys
import os

# path = '../{}/'.format(str(sys.argv[1]))

assignment = '../{}/{}'.format(str(sys.argv[1]), 'ASSIGNMENT.md')
f1 = open(assignment, 'a')
f1.write('# Assignment ({})'.format(str(sys.argv[1])))
f1.close()

notes = '../{}/{}'.format(str(sys.argv[1]), 'NOTES.md')
f2 = open(notes, 'a')
f2.write('# Notes ({})'.format(str(sys.argv[1])))
f2.close()
