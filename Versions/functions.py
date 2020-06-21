# -----------------------------------------------------------------------------
# *** FUNCTIONS ***
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
# *** FUNCTIONS END ***
# -----------------------------------------------------------------------------
