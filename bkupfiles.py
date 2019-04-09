
'''
backup files at 
- source folder, 
- destination folder where backup files to be stored

list of file name to be backup

e.g. 
file.ext --> file_yyyymmdd.ext

'''

import os
import shutil
import argparse
import time
import sys

parser = argparse.ArgumentParser(description='backup files specified list of files from source to destination folder')
parser.add_argument('src', type=str, help='the source folder where the files are to be backup')
parser.add_argument('dest', type=str, help='the destination of folder where backup files to be placed')
parser.add_argument('files', type=str, help='list of files separated with comma')

def toBackupName(srcfile):
    fname = os.path.splitext(srcfile)
    
    # print("*** fname: " , fname[0])
    dateformat = "_"+time.strftime('%Y%m%d')  

    return fname[0] + dateformat + fname[1]; 

try:
    status = True;

    args = parser.parse_args()

    src = args.src
    dest = args.dest 
    files = args.files
    files2backup = args.files.split(",")

    print("src: ",src)
    print("dest: ",dest)
    print("files2backup: ",files2backup)

    # print(os.path.isdir(dest))
    fnames = os.listdir(src)

    # check folder exist?
    if not os.path.isdir(dest):
        # create the folder
        print(dest," does not exist, creating it", file=sys.stdout)
        os.mkdir(dest)

    message = None
        
    # copy files in src folder to backup folder
    for f in files2backup:
        srcfile = src+f
        print("***",srcfile)
        exists = os.path.isfile(srcfile)
        if(exists == False):
            message = srcfile + " not found."
            status = False
            break

        shutil.copy(srcfile, dest)
        # rename the file to filename_yyyymmdd.ext
        destfile = dest+f
        # print("*** fname: " , toBackupName(destfile))

        # rename the files in backup folder
        os.rename(destfile,toBackupName(destfile))
        print(destfile, "is backup.")

except Exception as e:
    print(e.message, file=sys.stderr)
    status = False
    
finally:
    if(status):
        print(files2backup, "are backup successfully.", file=sys.stdout)
        sys.exit(0)
    else:
        print("files are backup with error: "+message, file=sys.stderr)
        sys.exit(1)