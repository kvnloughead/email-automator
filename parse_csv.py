import csv

def get_contacts(contacts):
    """Function to read contacts from a given file
    and return a list of names and email addresses"""
    # open file and establish headers
    f = open(contacts, 'r')
    reader = csv.reader(f)
    headers = next(reader, None)
    # build dictionary of contact info
    columns = {}
    for h in headers:
        columns[h] = []
    for row in reader:
        for h, v in zip(headers, row):
            columns[h].append(v)
    return columns

contacts = get_contacts('sample.csv')