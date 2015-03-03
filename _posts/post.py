import datetime
import sys
import string

def filenameConvert(name):
    name = name.lower()
    name = name.replace(' ','-')
    return name

now = datetime.datetime.now()
dateString = now.strftime('%y-%m-%d') 

if len(sys.argv) == 0:
    print('Defaulting to standard name')
    title = 'Hello World'
else:
    title = sys.argv[1]
    print('The title is: ',title)
# Open file
fo = open(dateString + '-' + filenameConvert(title) + ".md","w")
fo.write("---\n")
fo.write("layout: post\n")
fo.write("title: " + title +"\n")
fo.write("date: " + dateString  + "\n")
fo.write("categories: \n")
fo.write("---\n")
fo.close()
