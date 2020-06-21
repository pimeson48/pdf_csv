# pdf_csv.py | converts a pdf to a csv
#
# Version 1.0 by JC on June 18, 2020
# Version 1.1 by JC on June 20, 2020
# Version 1.2 by JC on June 21, 2020
# -----------------------------------------------------------------------------
__version__ = '1.2'

print("[-+-] starting defaults.py...")
print("[-+-] set defaults for pdf_csv.py")
# -----------------------------------------------------------------------------
print("[-+-] importing required packages for defaults.py...")
import os
print("[-+-] defaults.py packages imported!")
#-----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def defaults(): # set defaults for pdf_csv.py
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

    return pdf, csv, defaultdir, pdf_path, csv_path
# -----------------------------------------------------------------------------
