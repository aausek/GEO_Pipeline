import GEOparse, os

# Main() to collect gene name input or exit
def main():
    userInput = input('Enter gene name or ''exit'' to quit app: ')
    if userInput == 'exit':
        sys.exit()
    else:
        # Call parser function to query GEO database
        parser(userInput)

# Query GEO database for gene samples
def parser(userInput):
    
    # User input used to query GEO and download to /output folder
    gse = GEOparse.get_GEO(geo=userInput, destdir="./output")
    
    print("\nGSM example:")
    
    for gsm_name, gsm in gse.gsms.items():
        print("Name: ", gsm_name)
        print("Metadata:",)
        for key, value in gsm.metadata.items():
            print(" - %s : %s" % (key, ", ".join(value)))
        print ("Table data:",)
        print (gsm.table.head())
        break

    print("\nGPL example:")
    for gpl_name, gpl in gse.gpls.items():
        print("Name: ", gpl_name)
        print("Metadata:",)
        for key, value in gpl.metadata.items():
            print(" - %s : %s" % (key, ", ".join(value)))
        print("Table data:",)
        print(gpl.table.head())
        break

# Call main()
if __name__ == '__main__':
    main()