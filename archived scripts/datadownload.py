# Developed by Ana Ausek
# Import NCBI data from GEO - Gene Expression Omnibus

# Import libraries
import urllib.request, os

# main()
def main():
    inputMenu()
    
# Prompt user for input on URL parameters
def inputMenu():
    print('Enter search query. Enter ''exit'' to quit app.')
    acc = input('Enter acc component (gplxxx, gsmxxx or gsexxx): ')
    #targ = input('Enter targ component value (self, gsm, gpl, gse or all): ')
    #view = input('Enter view component (brief, quick, data or full): ')
    fileFormat = input('Enter format component (i.e. file): ')
    
    if acc == 'exit' or fileFormat == 'exit':
        exit(0)
    else:
        pullurl(acc, fileFormat)

# Funtion to access URL and download file
def pullurl(acc, fileFormat):
    # GEO request URL
    rootURL = 'https://www.ncbi.nlm.nih.gov/geo/download/?'
    # Construct request URL with input parameters
    rURL = rootURL + 'acc=' + acc + '&format=' + fileFormat
    print(rURL)
    # New output file path name
    path = 'output/'
    #extension = '.txt'
    filename = acc + '_RAW.tar'
    # File and path name
    filePath = os.path.join(path, filename)
    r = urllib.request.urlretrieve(rURL, filePath)
    # head -10 filename.txt to display last 10 lines

# Call main()
if __name__ == '__main__':
    main()