# -----------------------------------------------------------------------------
# pdf_csv.py | converts a pdf to a csv
#
# Version 1.0 by JC on June 18, 2020
# Version 1.1 by JC on June 20, 2020
# Version 1.2 by JC on June 21, 2020
# -----------------------------------------------------------------------------


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
    print("[-+-] Purpose: script will import a pdf and convert it to a csv file \n")

    print("[-+-] default filenames:")
    pdf = "Bank_Report.pdf"
    csv = "Bank_Report.csv"
    print (pdf)
    print (csv + "\n")

    print("[-+-] default directory:")
    pdf_loc = os.getcwd()
    csv_loc = pdf_loc
    print (pdf_loc)
    print (csv_loc + "\n")

    print("[-+-] default file paths:")
    pdf_path = os.path.join(pdf_loc, pdf)
    csv_path = os.path.join(csv_loc, csv)
    print (pdf_path)
    print (csv_path + "\n")

    # check if a pdf exists at the default file path
    # TO DO create a loop to go through all pdfs and ask for user to select
    print("[-+-] looking for another pdf...")
    arr_pdf = [pdf_loc for pdf_loc in os.listdir() if pdf_loc.endswith(".pdf")]
    if len(arr_pdf) == 1:
        print("[-+-] pdf found: " + arr_pdf[0] + "\n")
        pdf_path = os.path.join(pdf_loc, arr_pdf[0])
    else:
        print("[-+-] pdf cannot be found, exiting script!")
        
    # check if csv exists at the default file path
    # if csv does not exist create a blank file at the default path
    # required for automatic script mode to function
    try:
        print("[-+-] checking if csv at default location...")
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

    print("[-+-] csv file can be found here: " + csv_path + "\n")

    print("[-+-] finished pdf_csv.py successfully!")
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# run the program
pdf_csv()
# -----------------------------------------------------------------------------
