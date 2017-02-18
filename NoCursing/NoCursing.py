import urllib


def read_text():
   quotes = open("C:\Users\Personal\Desktop\udacity\NoCursing\CursingFile.txt")
   contents_of_file = quotes.read()
   #print (contents_of_file)
   quotes.close()
   checkProfanity(contents_of_file)

def checkProfanity(txt_to_check):
    connection =  urllib.urlopen("http://www.wdylike.appspot.com/?q=" + txt_to_check )
    output = connection.read()
   # print (output)
    connection.close()
    if "true" in output:
        print ("Curse Words detected.Watch Out")
    elif "false" in output:
        print ("Smooth sailing.(jesus approved)No curse words detected ")
    else:
        print ("Unable to scan the file")
read_text()
