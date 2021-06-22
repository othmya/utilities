import sys, os
import pandas as pd


def timeline_contacts(infile, outname):
    """
    Takes a .txt file generated from VMD's Timeline plot. Extract the contacts at all different
    frames for the different selected residues. Outputs a .csv dataframe named through the "outname"
    argument.
    """

    infile = open(infile, "r")
    rescontacts = []
    total_names = []

    contdict = {} # keys are identifiers, values are list of contact values

    # loop through the txt file

    for line in infile.readlines():
        if line.startswith("#") or "freeSelString" in line:
            pass
        elif "freeSelLabel" in line:
            elements = line.split(" ")
            resname = elements[1]
            resid = (str(elements[2]).split("=="))[0]
            name = resname + " " + resid
            total_names.append(name)
            contdict[name] = []
            rescontacts = []
        else:
            lines = line.rstrip().split(" ")
            contacts = lines[1]
            rescontacts.append(contacts)
            contdict[name] = rescontacts


    # save the df with pandas
    df = pd.DataFrame(contdict)
    df.to_csv(outname, index=False, header=True)


if __name__ == "__main__":

    input_file = sys.argv[1]
    output_name = sys.argv[2]

    timeline_contacts(input_file, output_name)


