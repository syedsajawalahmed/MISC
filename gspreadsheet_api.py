import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import sys

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
# spreadsheet = client.open('abcd')

# gc = gspread.authorize(credentials)
# spreadsheet = client.open("abcd").sheet1

# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)


class GSpreadSheet_API():

    row_counter = 1

    def __init__(self, sheet_name, worksheet_name="Amazon"):
        # self.sheet_name = sheet_name
        spreadsheet = client.open(worksheet_name)
        # try:
        #     client.open(worksheet_name).worksheet(sheet_name)
        #     print("Spread Sheet with this name Already Exists")
        #     print("Delete previous one or change SpreadSheet Name")
        # except:
        #     return

        self.sheet = spreadsheet.add_worksheet(title=sheet_name, rows='1000', cols='3')
        self.ss = client.open(worksheet_name)
        self.sheet = client.open(worksheet_name).worksheet(sheet_name)
        return

    def put_data(self, link, email_id, seller_disc):
        '''Columns
        Link - Email Id - Seller Description
        '''
        if self.row_counter == 1:
            self.sheet.insert_row(['Link', 'Email Id', 'Seller Description'], index=self.row_counter)
            self.sheet.format('A1', {'textFormat': {'bold': True}})
            self.sheet.format('B1', {'textFormat': {'bold': True}})
            self.sheet.format('C1', {'textFormat': {'bold': True}})
            self.row_counter += 1
        else:
            self.sheet.insert_row([link, email_id, seller_disc], index=self.row_counter)
            self.row_counter += 1


        ############# new  #################
        sheetId = self.sheet._properties['sheetId']
        body = {
                "requests": [
                    {
                        "updateDimensionProperties": {
                            "range": {
                                "sheetId": sheetId,
                                "dimension": "ROWS",
                                "startIndex": 0,
                                "endIndex": self.row_counter
                            },
                            "properties": {
                                "pixelSize": 21
                            },
                            "fields": "pixelSize"
                        }
                    },
                    {
                        "updateDimensionProperties": {
                            "range": {
                                "sheetId": sheetId,
                                "dimension": "COLUMNS",
                                "startIndex": 0,
                                "endIndex": self.row_counter
                            },
                            "properties": {
                                "pixelSize": 200
                            },
                            "fields": "pixelSize"
                        }
                    }
                ]
            }
        # body = {
        #         "requests": [
        #             {
        #                 "updateDimensionProperties": {
        #                     "range": {
        #                         "sheetId": sheetId,
        #                         "dimension": "COLUMNS",
        #                         "startIndex": 0,
        #                         "endIndex": self.row_counter
        #                     },
        #                     "properties": {
        #                         "pixelSize": 200
        #                     },
        #                     "fields": "pixelSize"
        #                 }
        #             }
        #         ]
        #     }
        res = self.ss.batch_update(body)
        ######################################
        return
        

if __name__ == "__main__":
    gs = GSpreadSheet_API('8')

    cont = """wow what a pleasant day \ni thought ikfask jkdf sfj skj fksd \ndfsf sdf  dfa s """

    for i in range(5):
        gs.put_data(i, i, cont)

    print("end")

# # rows
# row = 0
# row += 1

# index = 2

# a = sheet.title
# print(a)
# sheet.insert_row([0,1], index)

# sheet.format('A3:B6', {'textFormat': {'bold': True}})

# index +=1
# sheet.insert_row([2,2], index)
# index +=1
# sheet.insert_row([3,3], index)

