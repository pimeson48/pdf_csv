# -----------------------------------------------------------------------------
# Version 1.0 by Jon Chuma (jchuma@westvancouver.ca) on June 18, 2020
# Version 1.1 by Jon Chuma on June 20, 2020
# -----------------------------------------------------------------------------

import os
import subprocess
import tkinter as tk
from tkinter import filedialog
import tabula  # Tabula: simple wrapper for tabula-java, read tables from PDF into DataFrame
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# ***IMPORTANT***

# Outlook rule downloads pdf, this needs to happen before Python script is run
# create Windows task schedule to run pdf_csv.py on a bi-weekly basis (Friday mornings)

# ***IMPORTANT***
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# open file explorer to view file
def startfile(filename):
    try:
        os.startfile(filename)
    except:
        subprocess.Popen(['xdg-open', filename])
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# open file dialogue window to select pdf file
def pdf_file():
    root = tk.Tk()
    root.withdraw()
    pf = filedialog.askopenfilename(title='select the pdf import file')
    return pf

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# open file dialogue window to select csv file
def csv_file():
    root = tk.Tk()
    root.withdraw()
    cf = filedialog.askopenfilename(title='select the csv output file')
    return cf
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# automatic or manual script mode
def choice(default):
    # set constants
    auto_num = 1
    man_num = 2
    auto_name = "automatic"
    man_name = "manual"
    auto_d = "Automatic (1)"
    man_d = "Manual (2)"
        
    if default == True:
        # Calls for an infinite loop that keeps executing until an exception occurs
        while True:
            try:
                AorM = int(input(auto_d + " or " + man_d + "  "))

            # If something else that is not the string version of a number is introduced, the ValueError exception will be called.
            except ValueError:
                # The cycle will go on until validation
                print("Error! This is not " + auto_d + " or " + man_d + ". Try again.")

            # When successfully converted to an integer, the loop will end.
            else:
                if AorM == auto_num:
                    AorM_name = auto_name
                elif AorM == man_num:
                    AorM_name = man_name
                break
    else:
        # manual only as default pdf bank report not available
        AorM = man_num 
        AorM_name = man_name 
    
    print(AorM_name + " script mode selected \n")
    return AorM
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# check if pdf file exists at default location
def pdf_exists(pdf_path):
    try:
        open(pdf_path, "r")
        default = True
        print ("found pdf at default location! \n")
    except IOError:
        print ("did not find default pdf! \n")
        default = False
    return default
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# convert pdf to csv
def pdf_csv():
    print ("starting pdf_csv.py...")
    print ("Purpose: script will import a pdf and convert it to a csv file")
    print ("Optional (manual mode only): csv output file can be moved to alternate destination folder")
    print ("Modes: automatic mode runs with no user input while manual allows edits to pdf and csv locations \n")

    # default filenames
    print ("default file names:")
    pdf = "Bank_Report.pdf"
    csv = "Bank_Report.csv"
    print (pdf)
    print (csv + "\n")
    # default file locations
    pdf_loc = os.getcwd()
    csv_loc = pdf_loc
    print ("default file locations:")
    print (pdf_loc)
    print (csv_loc + "\n")
    # default file paths
    pdf_path = os.path.join(pdf_loc, pdf)
    csv_path = os.path.join(csv_loc, csv)
    print ("default file paths:")
    print (pdf_path)
    print (csv_path + "\n")
    
    # check if pdf exists at the default file path
    print ("checking if pdf at default location...")
    default = pdf_exists(pdf_path)
    
    # check if a pdf exists at the default file path
    # TO DO create a loop to go through all pdfs and ask for user to select
    print("looking for another pdf...")
    arr_pdf = [pdf_loc for pdf_loc in os.listdir() if pdf_loc.endswith(".pdf")]
    if len(arr_pdf) == 1:
        pdf = arr_pdf[0]
        print("pdf found!")
        print("pdf filename: " + pdf + "\n")
        pdf_path = os.path.join(pdf_loc, pdf)
        default = True
    else:
        print("pdf cannot be found, will need to be manually selected!")
        
    #print ("selecting script mode...")
    # choose automatic or manual script modes
    #AorM = choice(default)
    if default == True:
        AorM = 1 # automatic
    else:
        AorM = 2 # manual
    
    if AorM == 1: # automatic
        # check if csv exists at the default file path
        # if csv does not exist create a blank file at the default path
        # required for automatic script mode to function
        try:
            print ("checking if csv at default location...")
            open(csv_path, "r")
            print ("csv found at default location!")
        except IOError:
            print ("did not find csv at default file path!")
            print ("creating a blank csv Bank Report file...\n")
            open(csv_path, "w")
        print ("automatic mode selected! \n")
        print ("pdf and csv files selected:")
        print (pdf_path)
        print (csv_path)
        print ("reminder: csv will be overwritten! \n")
    else:
        print ("automatic mode disabled, forcing manual...")
        print ("manual mode selected! \n")
        print ("select pdf import file...")
        pdf_path = pdf_file()

        # True if pdf actually selected
        pdf_ext = pdf_path.lower().endswith('.pdf')
        
        while True:
            if os.path.isfile(pdf_path) == True and pdf_ext == True:
                print ("pdf_path: " + pdf_path)
                break
            else:
                print ("pdf not selected, choose a pdf file \n")
                pdf_path = pdf_file() # pick another pdf
                pdf_ext = pdf_path.lower().endswith('.pdf')
        
        print ("select csv output file...")
        csv_choice = input ("use default csv file? y or n  ")

        if csv_choice == "y":
            try:
                open(csv_path, "r")
                print ("found csv at default location!")
                print ("csv will be overwritten!\n")
            except IOError:
                print ("did not find csv at default file path!")
                print ("creating a blank csv Bank Report file...\n")
                open(csv_path, "w")
        else:
            csv_path = csv_file()
        
            # True if pdf actually selected
            csv_ext = csv_path.lower().endswith('.csv')
            
            while True:
                if os.path.isfile(csv_path) == True and csv_ext == True:
                    print ("csv_path: " + csv_path + "\n")
                    break
                else:
                    print ("csv not selected, choose a csv file")
                    csv_path = csv_file() # pick another csv
                    csv_ext = csv_path.lower().endswith('.csv')
                       
    print ("converting pdf to csv...")
#    print ("testing suppressed pdf to csv conversion!\n")
    tabula.convert_into(pdf_path, csv_path, output_format="csv", pages="all")
    print ("pdf to csv conversion complete!\n")
        
    print ("csv file can be found here: " + csv_path + "\n")
#     if AorM == 2: # manual
#         print ("opening csv folder...\n")
#         csv_loc = os.path.dirname(csv_path)
#         startfile(csv_loc)
#     else:
#         print ("automatic mode suppressed opening csv location!\n")
    
    print ("finished pdf_csv.py successfully!")
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# run the program    
pdf_csv()
# -----------------------------------------------------------------------------