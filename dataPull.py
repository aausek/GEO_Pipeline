# Developed by Ana Ausek
# Import NCBI data from GEO - Gene Expression Omnibus

# Import libraries
import urllib.request, os

# main()
def main():
    inputMenu()
    
# Prompt user for input on URL parameters
def inputMenu():
    print('Enter search query. Enter exit to quit app.')
    acc = input('Enter acc component (gplxxx, gsmxxx or gsexxx): ')
    targ = input('Enter targ component value (self, gsm, gpl, gse or all): ')
    view = input('Enter view component (brief, quick, data or full): ')
    form = input('Enter form component (text, html or xml): ')
    if input() == 'exit':
        sys.exit()
    else:
        pullurl(acc, targ, view, form)

# Funtion to access URL and download file
def pullurl(acc, targ, view, form):
    # GEO request URL
    rootURL = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?'
    # Construct request URL with input parameters
    rURL = rootURL + 'acc=' + acc + '&targ=' + targ + '&view=' + view + '&form=' + form
    print(rURL)
    # New output file path name
    path = 'output/'
    extension = '.txt'
    filename = acc + extension
    # File and path name
    filePath = os.path.join(path, filename)
    r = urllib.request.urlretrieve(rURL, filePath)
    # head -10 filename.txt to display last 10 lines

# Call main()
if __name__ == '__main__':
    main()