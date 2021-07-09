# Developed by Ana Ausek
# Import NCBI data from GEO - Gene Expression Omnibus

# Import libraries
import urllib.request
import os
from _datetime import datetime


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
        quit_app = input('Quit? Y/N: ')
        if quit_app.lower() == 'y':
            break
        acc = input('Enter acc component (gplxxx, gsmxxx or gsexxx): ')
        query_type = input('Enter FULL or CUSTOM query type: ')
        if query_type.lower() == 'full':
            targ = 'gsm'
            view = 'data'
            form = 'text'
            pullUrl(acc, targ, view, form)
        elif query_type.lower() == 'custom':
            targ = input('Enter targ component value (self, gsm, gpl, gse or all): ')
            view = input('Enter view component (brief, quick, data or full): ')
            form = input('Enter form component (text, html or xml): ')
            pullUrl(acc, targ, view, form)
        else:
            inputMenu()

    print('Thanks for using GEO_Pipeline. See you next time!')
    exit(0)


# Prompt user for input on URL parameters
def pullUrl(acc, targ, view, form):
    # GEO request URL
    root_url = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?'
    # Construct request URL with input parameters
    request = root_url + 'acc=' + acc + '&targ=' + targ + '&view=' + view + '&form=' + form
    print(request)

    # Parent Directory path
    parent_dir = 'output/'
    date = datetime.today().strftime('%Y-%m-%d')
    # Path
    path = os.path.join(parent_dir, acc + '_' + date + '/')
    os.mkdir(path)

    extension = '.txt'
    filename = acc + '_' + targ + '_' + view + '_' + form + '_' + date + extension
    # File and path name
    filepath = os.path.join(path, filename)
    r = urllib.request.urlretrieve(request, filepath)
    # head -10 filename.txt to display last 10 lines

    full_path = os.path.join(path, filename)
    splitFiles(full_path)


def splitFiles(filepath):

    token = '^SAMPLE'
    chunks = []
    current_chunk = []

    for line in open(filepath):
        if line.startswith(token) and current_chunk:
            chunks.append(current_chunk[:])
            current_chunk = []
        current_chunk.append(line)

    chunks.append(current_chunk)


# Call main()
def main():
    banner()
    inputMenu()


# Invoke main
if __name__ == '__main__':
    main()
