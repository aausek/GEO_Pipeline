# Developed by Ana Ausek
# Import NCBI data from GEO - Gene Expression Omnibus

# Import libraries
import urllib.request
import os
import time
from datetime import datetime
import csv
import json
# import pandas as pd


# Test with --> GSE37219 & GPL8321


def banner():
    print('''
         ██████╗ ███████╗ ██████╗         ██████╗ ██╗██████╗ ███████╗██╗     ██╗███╗   ██╗███████╗
        ██╔════╝ ██╔════╝██╔═══██╗        ██╔══██╗██║██╔══██╗██╔════╝██║     ██║████╗  ██║██╔════╝
        ██║  ███╗█████╗  ██║   ██║        ██████╔╝██║██████╔╝█████╗  ██║     ██║██╔██╗ ██║█████╗
        ██║   ██║██╔══╝  ██║   ██║        ██╔═══╝ ██║██╔═══╝ ██╔══╝  ██║     ██║██║╚██╗██║██╔══╝
        ╚██████╔╝███████╗╚██████╔╝███████╗██║     ██║██║     ███████╗███████╗██║██║ ╚████║███████╗
         ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝
    ''')


# Print ASCII banner
def inputMenu():
    # print('Enter search query. Enter exit to quit app.')
    while True:
        print('For full sample data download enter accession series code, and type FULL as query type. \n'
              'Type CUSTOM to specify custom query parameters.')

        # Add cases to test that these inputs are not blank
        acc = input('\nEnter acc component (gplxxx, gsmxxx or gsexxx): ')
        query_type = input('Enter "f" for full or "c" for custom query type: ')
        if query_type.lower() == 'f':
            targ = 'gsm'
            view = 'data'
            form = 'text'
            pullUrl(acc, targ, view, form)
        elif query_type.lower() == 'c':
            targ = input(
                'Enter targ component value (self, gsm, gpl, gse or all): ')
            view = input('Enter view component (brief, quick, data or full): ')
            form = input('Enter form component (text, html or xml): ')
            pullUrl(acc, targ, view, form)

        quit_app = input('\nQuit? Y/N: ')

        if quit_app.lower() == 'y':
            break
        elif quit_app.lower() == 'n':
            inputMenu()
        else:
            inputMenu()

    print('\nFor parameters clarification visit https://www.ncbi.nlm.nih.gov/geo/info/download.html')
    print('\nThanks for using GEO_Pipeline. See you next time!\n')
    exit(0)


# Prompt user for input on URL parameters
def pullUrl(acc, targ, view, form):
    # GEO request URL
    root_url = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?'
    # Construct request URL with input parameters
    request = root_url + 'acc=' + acc + '&targ=' + \
        targ + '&view=' + view + '&form=' + form

    self_targ = 'self'
    gpl_request = root_url + 'acc=' + acc + '&targ=' + \
        self_targ + '&view=brief' + '&form=text'
    print('\n' + request)
    print(gpl_request + '\n')

    # Parent Directory path
    os.getcwd()
    os.mkdir('output')
    parent_dir = './output/'
    date = datetime.today().strftime('%Y-%m-%d')

    # Path
    path = os.path.join(parent_dir, acc + '_' + date + '/')
    subfolder = os.path.join(path + targ + '/')

    # Create subfolders to drop gsm or gpl outputs
    if os.path.isdir(path):
        # os.mkdir(path + '-' + iterations)
        os.mkdir(subfolder)
    # elif os.path.isdir(subfolder):

    else:
        os.mkdir(path)
        os.mkdir(subfolder)

    extension = '.txt'
    sample_filename = acc + '_' + targ + '_' + \
        view + '_' + form + '_' + date + extension

    gpl_filename = acc + '_' + 'meta_' + date + extension

    # File and path name
    sample_filepath = os.path.join(subfolder, sample_filename)
    urllib.request.urlretrieve(request, sample_filepath)

    # File and path name
    gpl_filepath = os.path.join(subfolder, gpl_filename)
    urllib.request.urlretrieve(gpl_request, gpl_filepath)
    # head -10 filename.txt to display last 10 lines

    # full_path = os.path.join(path, filename)
    if targ == 'gsm':
        splitFiles(sample_filepath, subfolder, extension)
        #getGPL(gpl_filepath, subfolder, extension, root_url)


def splitFiles(sample_filepath, subfolder, extension):
    with open(sample_filepath, mode="r") as original_file:
        reader = original_file.read()
        token = '^SAMPLE = '

    samples = []
    print('Samples:')
    for line in reader.splitlines():
        if token in line:
            sample_code = line.strip(token)
            print(sample_code)
            samples.append(sample_code)
            # print(samples)

    # Specify sample names
    for i, part in enumerate(reader.split(token)[1:]):
        fname = "Sample_" + samples[i]
        filename_ = subfolder + fname + '_' + extension
        filename_final = subfolder + fname + extension
        
        with open(filename_, mode="w") as sample_file:
            sample_file.write(token + part)
        
        with open(filename_, "r") as file_input:
            with open(filename_final, "w") as file_output: 
                for line in file_input:
                    if line.strip("\n") != "!sample_table_end":
                        file_output.write(line)
        os.remove(filename_)
        probeMatch(subfolder, filename_final, samples[i])
        # Keep or remove original file?
    os.remove(sample_filepath)
    
    
# Download GPL file
def getGPL(gpl_filepath, subfolder, extension, root_url):
    with open(gpl_filepath, mode="r") as original_file:
        reader = original_file.read()
        token = '!Series_platform_id = '

        for line in reader.splitlines():
            if token in line:
                gpl_code = line.strip(token)
                print(gpl_code)

                request_txt = root_url + 'acc=' + gpl_code + \
                    '&targ=gpl' + '&view=data' + '&form=text'
                gpl_full = gpl_code + extension

                # File and path name
                gpl_full_path = os.path.join(subfolder, gpl_full)
                urllib.request.urlretrieve(request_txt, gpl_full_path)
                # time.sleep(10)
                #convertGPL(gpl_full_path)

        original_file.close()
        os.remove(gpl_filepath)
        probeMatch(subfolder)


# Convert GPL file into dictionary
# TODO - How to deal with GSM files that lead to multiple GPLs
def convertGPL(gpl_full_path):
    with open(gpl_full_path, mode="r") as original_file:
        reader = original_file.read()
        token = ' ID '

    # Specify sample names
    for i, part in enumerate(reader.split(token)):
        filename = gpl_full_path
        with open(filename, mode="w") as file:
            file.write(token + part)

    os.remove(gpl_full_path)
    probeMatch()


# Function to pair ID_REF with GPL files
# Parse 'self' GPL file
# TODO - Remove this function?
def probeMatch(subfolder, filename_final, sample_code):

    # text will be stored
    dict1 = {}
    
    filename = 'Sample_GSM913972.txt'
    #subfolder = './output/GSE37219_2021-08-02/gsm/'
    # fields in the sample file 
    fields =['ID_REF', 'VALUE',	'P-VAL']
    # creating dictionary
    with open(filename_final) as fh:
        # lines = fh.readlines()
        # lines = lines[:-1]
        l = 1
        for _ in range(6):
            next(fh)
        for line in fh:
            
            # reads each line and trims of extra the spaces
            # and gives only the valid words
            description = list( line.strip().split(None, 3))
            print(description)
            
            sno ='ID_' + str(l)
            # loop variable
            i = 0
            # intermediate dictionary
            dict2 = {}
            while i < len(fields):
                # creating dictionary for each record
                dict2 [fields[i]] = description[i]
                i = i + 1
            # appending the record of each record to
            # the main dictionary
            dict1[sno] = dict2
            l = l + 1

    # creating json file
    # the JSON file is named as test1
    json_file = sample_code + ".json"
    out_file = open(subfolder + json_file, "w")
    json.dump(dict1, out_file, indent = 3)
    out_file.close()


# Driver code
def main():
    banner()
    inputMenu()

# Invoke main
if __name__ == '__main__':
    main()
