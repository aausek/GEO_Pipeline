# Developed by Ana Ausek
# Import NCBI data from GEO - Gene Expression Omnibus

# Import libraries
import urllib.request, os, time

# main()
def main():
    inputMenu()
    
# Prompt user for input on URL parameters
def inputMenu():
    print('Enter search query')
    acc = input('Enter acc component (gplxxx, gsmxxx or gsexxx): ')
    targ = input('Enter targ component value (self, gsm, gpl, gse or all ): ')
    view = input('Enter view component (brief, quick, data or full): ')
    form = input('Enter form component (text, html or xml): ')
    pullurl(acc, targ, view, form)

# Funtion to access URL and download file
def pullurl(acc, targ, view, form):
    # GEO request URL
    rootURL = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?'
    rURL = rootURL + 'acc=' + acc + '&targ=' + targ + '&view=' + view + '&form=' + form
    path = 'output/'
    extension = '.txt'
    filename = acc + extension
    fileName = os.path.join(path, filename)
    r = urllib.request.urlretrieve(rURL, fileName)
    print(rURL)

# Call main()
main()    