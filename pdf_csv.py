# -----------------------------------------------------------------------------
# pdf_csv.py | converts a pdf to a csv
#
# Version 1.0 by JC on June 18, 2020
# Version 1.1 by JC on June 20, 2020
# Version 1.2 by JC on June 21, 2020
# -----------------------------------------------------------------------------
__version__ = '1.2'

# -----------------------------------------------------------------------------
# import required packages that must be done before FUNCTIONS are created
print("[-+-] importing required packages...")
import os
#import tabula  # simple wrapper for tabula-java, read tables from PDF into DataFrame
print("[-+-] packages imported!")
#-----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# convert pdf to csv
def pdf_csv():
    print("[-+-] starting pdf_csv.py...")
    print("[-+-] import a pdf and convert it to a csv \n")

    # TODO allow pdf name selection with minimal interaction
    print("[-+-] default filenames:")
    filename = "Bank_Report"
    pdf = filename + ".pdf"
    csv = filename + ".csv"
    print (pdf)
    print (csv + "\n")

    print("[-+-] default directory:")
    print("[-+-] (based on current working directory of python file)")
    defaultdir = os.getcwd()
    print (defaultdir + "\n")

    print("[-+-] default file paths:")
    pdf_path = os.path.join(defaultdir, pdf)
    csv_path = os.path.join(defaultdir, csv)
    print (pdf_path)
    print (csv_path + "\n")

    # check if a pdf exists at the default file path
    print("[-+-] looking for default pdf...")
    if os.path.exists(pdf_path) == True:
        print("[-+-] pdf found: " + pdf + "\n")
    else:
        print("[-+-] looking for another pdf...")
        arr_pdf = [defaultdir for defaultdir in os.listdir() if defaultdir.endswith(".pdf")]
        if len(arr_pdf) == 1: # there has to be only 1 pdf in the directory
            print("[-+-] pdf found: " + arr_pdf[0] + "\n")
            pdf_path = os.path.join(defaultdir, arr_pdf[0])
        elif len(arr_pdf) > 1:
            print("[-+-] more than 1 pdf found, exiting script!")
            # TODO add option to select from available pdfs
        else:
            print("[-+-] pdf cannot be found, exiting script!")

    # check if csv exists at the default file path
    # if csv does not exist create a blank file at the default path
    try:
        print("[-+-] looking for default csv...")
        open(csv_path, "r")
        print("[-+-] csv found: " + csv + "\n")
    except IOError:
        print("[-+-] did not find csv at default file path!")
        print("[-+-] creating a blank csv file: " + csv + "... \n")
        open(csv_path, "w")

#    print ("converting pdf to csv...")
    print("[-+-] pdf to csv conversion suppressed! \n")
#    tabula.convert_into(pdf_path, csv_path, output_format="csv", pages="all")
#    print ("pdf to csv conversion complete!\n")

#    print("[-+-] converted csv file can be found here: " + csv_path + "\n")
    
    print("[-+-] finished pdf_csv.py successfully!")
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# run the program
pdf_csv()
# -----------------------------------------------------------------------------
