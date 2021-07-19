# Developed by Ana Ausek
# Import NCBI data from GEO - Gene Expression Omnibus

# Import libraries
import urllib.request
import os
import time
from datetime import datetime


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
        acc = input('Enter acc component (gplxxx, gsmxxx or gsexxx): ')
        query_type = input('Enter F for full or C for custom query type: ')
        if query_type.lower() == 'f':
            targ = 'gsm'
            view = 'data'
            form = 'text'
            pullUrl(acc, targ, view, form)
        elif query_type.lower() == 'c':
            targ = input('Enter targ component value (self, gsm, gpl, gse or all): ')
            view = input('Enter view component (brief, quick, data or full): ')
            form = input('Enter form component (text, html or xml): ')
            pullUrl(acc, targ, view, form)

        quit_app = input('Quit? Y/N: ')

        if quit_app.lower() == 'y':
            break
        elif quit_app.lower() == 'n':
            inputMenu()
        else:
            inputMenu()

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
    print(request)
    print(gpl_request)

    # Parent Directory path
    parent_dir = 'output/'
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
        getGPL(gpl_filepath, subfolder, extension, root_url)


def splitFiles(sample_filepath, subfolder, extension):
    with open(sample_filepath, mode="r") as original_file:
        reader = original_file.read()
        token = '^SAMPLE = '

    samples = []
    for line in reader.splitlines():
        if token in line:
            sample_code = line.strip(token)
            print(sample_code)
            samples.append(sample_code)
            # print(samples)
    # Specify sample names
    for i, part in enumerate(reader.split(token)[1:]):
        filename = subfolder + "/Sample_" + str(i) + extension
        with open(filename, mode="w") as sample_file:
            sample_file.write(token + part)

        # Keep or remove original file?
    os.remove(sample_filepath)

# Parse 'self' GPL file


def getGPL(gpl_filepath, subfolder, extension, root_url):
    with open(gpl_filepath, mode="r") as original_file:
        reader = original_file.read()
        token = '!Series_platform_id = '

        for line in reader.splitlines():
            if token in line:
                gpl_code = line.strip(token)
                print(gpl_code)

                request = root_url + 'acc=' + gpl_code + \
                    '&targ=gpl' + '&view=full' + '&form=text'
                gpl_full = gpl_code + extension

                # File and path name
                gpl_full_path = os.path.join(subfolder, gpl_full)
                urllib.request.urlretrieve(request, gpl_full_path)
                # time.sleep(10)

        original_file.close()
        os.remove(gpl_filepath)

# Function to pair ID_REF with GPL files
# def probeMatch():


# Call main()
def main():
    banner()
    inputMenu()


# Invoke main
if __name__ == '__main__':
    main()
