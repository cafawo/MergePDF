#!/usr/bin/python

import os
from PyPDF2 import PdfFileMerger
    
def mergePDF(input_folder = True, output_file = True, sort = True):
    local_dir = os.path.dirname(__file__)
    if input_folder: input_folder = os.path.join(local_dir, 'input')
    if output_file: output_file = os.path.join(local_dir, 'mergePDF_output.pdf')
    # input_folder can be manually assigned
    input_files = os.listdir(input_folder)
    # ignore all non PDF files
    input_files = [f for f in input_files if f.endswith('.pdf') or f.endswith('.PDF')]
    if sort: input_files.sort()
        
    merger = PdfFileMerger()
    for pdf in input_files:
        merger.append(os.path.join(input_folder,pdf))
    merger.write(output_file)

    print(input_files)
    
if __name__ == '__main__':
    mergePDF()