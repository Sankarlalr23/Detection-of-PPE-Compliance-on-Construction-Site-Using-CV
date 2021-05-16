import os
import shutil
from os import path

def main():
    for i in range(424,892):
        # make a duplicate of an existing file
        if path.exists("worker ({}).jpg".format(i)):
    	# get the path to the file in the current directory
            src = path.realpath("worker ({}).jpg".format(i));

    	# rename the original file
            os.rename("worker ({}).jpg".format(i),"worker{}.jpg".format(i))

if __name__ == "__main__":
    main()
