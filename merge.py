#!/usr/bin/python

import os
import sys
from PyPDF2 import PdfFileMerger
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox

def merge(input_folder = True, output_file = True, sort = True):
    Tk().withdraw() # keep the root window from appearing
    local_dir = askdirectory() # show an "Open" dialog box and return the path to the selected file
    if not local_dir: sys.exit()
    print('Directory: ' + str(local_dir))

    if input_folder: input_folder = local_dir
    if output_file: output_file = os.path.join(local_dir, 'MergePDF_output.pdf')
    # input_folder can be manually assigned
    input_files = os.listdir(input_folder)
    # ignore all non PDF files
    input_files = [f for f in input_files if f.endswith('.pdf') or f.endswith('.PDF')]
    if sort: input_files.sort()
        
    merger = PdfFileMerger()
    for pdf in input_files:
        merger.append(os.path.join(input_folder,pdf))
    merger.write(output_file)

    print('Files merged: '+str(input_files))
    print('Output file: '+str(output_file))
    
    messagebox.showinfo("MergePDF", str(len(input_files)) + ' PDF files merged into: ' + output_file)
    
if __name__ == '__main__':
    merge()
