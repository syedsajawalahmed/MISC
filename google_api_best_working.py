import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

# use creds to create a client to interact with the Google Drive API
# scope = ['https://spreadsheets.google.com/feeds']

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
spreadsheet = client.open('abcd')


# gc = gspread.authorize(credentials)
# spreadsheet = client.open("abcd").sheet1
sheet = spreadsheet.add_worksheet(title="Sheet_2", rows="100", cols="20")
sheet = client.open("abcd").worksheet('Sheet_2')

# r2 = sheet.row_values(2)
# c3 = sheet.col_values(3)
# cell = sheet.cell(2,2).value

# print(r2)
# print(c3)
# print("cell", cell)

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)


# rows
row = 0
row += 1

index = 2

a = sheet.title
print(a)
sheet.insert_row([0,1], index)

sheet.format('A3:B6', {'textFormat': {'bold': True}})

index +=1
sheet.insert_row([2,2], index)
index +=1
sheet.insert_row([3,3], index)

