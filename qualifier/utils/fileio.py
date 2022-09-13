# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath,saveFile):
    with open(csvpath, "w", newline='') as csvfile: 

        csvwriter = csv.writer(csvfile, delimiter=",")
        header = ["Lender,Max Loan Amount,Max LTV,Max DTI,Min Credit Score,Interest Rate"]

        if header:
            #add header to new csv file
            csvwriter.writerow(header)

        # inputs data in each row of new csv file
        csvwriter.writerows(saveFile)
        print(
            f"the list of qualifying loans has now been saved to: {str(csvpath)}")