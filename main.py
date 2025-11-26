import csv

npa_report_filename = 'npa_report.csv'
new_report_filename = 'trimmed_npa_report.csv'

id_index = 0 # actual area code
assigned_index = 5 # is the area code currently in use
location_index = 8 # state or providence
country_index = 9 # country
timezone_index = 19 # what time zone(s) the area code is in

# field names correspond with npa_report.csv
id_field_name = 'NPA_ID'
location_field_name = 'LOCATION'
country_field_name = 'COUNTRY'
timezone_field_name = 'TIME_ZONE'

def load_report(filename):
  rows = []
  with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # the first two rows are not needed
    next(csvreader) # date
    next(csvreader) # header
    
    for row in csvreader:
      rows.append(row)
  return rows
  
def trim_report(report):
  new_report = []
  for row in report:
    if row[assigned_index] == 'Yes':
      areacode = row[id_index]
      location = row[location_index]
      country = row[country_index]
      timezone = row[timezone_index]
      new_report.append([areacode, location, country, timezone])
  return new_report
  
def save_report(report, filename):
  fields = [
    id_field_name, 
    location_field_name, 
    country_field_name, 
    timezone_field_name,
  ]
  with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(report)
    
npa_report = load_report(npa_report_filename)
new_report = trim_report(npa_report)
save_report(new_report, new_report_filename)

print(f'{len(new_report)} area codes saved.')
