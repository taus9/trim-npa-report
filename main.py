import csv

npa_report_filename = 'npa_report.csv'
new_report_filename = 'trimmed_npa_report.csv'

id_index = 0 # actual area code
assigned_index = 5 # is the area code currently in use
location_index = 8 # state or providence
country_index = 9 # country
timezone_index = 19 # what time zone(s) the area code is in

def load_csv(filename):
  rows = []
  with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # the first two rows are not needed
    next(csvreader) # date
    next(csvreader) # header
    
    for row in csvreader:
      rows.append(row)
  return rows
  
  
npa_report = load_csv(npa_report_filename)
print(npa_report[0])
