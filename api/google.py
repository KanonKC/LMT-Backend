import gspread

def getSheetScore():
    auth = gspread.service_account(filename="./service-account.json")
    doc = auth.open("TestScore")
    sheet = doc.worksheet('Sheet1')
    result = sheet.get('A2:B6')
    return [{'team':i[0],'score':int(i[1])} for i in result]