# Developed by Ana Ausek
# Import NCBI data from GEO - Gene Expression Omnibus

# Import libraries
import urllib.request, os, time

# Prompt user for input on URL parameters
def inputMenu():
    print('Enter search query')
    acc = input('Enter acc component (gplxxx, gsmxxx or gsexxx):')
    targ = input('Enter targ component value (self, gsm, gpl, gse or all ):')
    view = input('Enter view component (brief, quick, data or full):')
    form = input('Enter form component (text, html or xml): ')

# Funtion to access URL and download file
def pullurl():
    # GEO request URL
    rootURL = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?'
    # acc = ''
    # targ = 'self'
    # view = 'full'
    # form = 'text'
    