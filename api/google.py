import gspread

auth = gspread.service_account(filename="./service-account.json")
doc = auth.open_by_key("1LragT8P41KwjRvdixHr1i5e_XbvytzSH-yHiRckTg6o")

def getSheetScore():
    worksheet = doc.get_worksheet(0)
    result = sorted(worksheet.get_all_records(),key=lambda item: item['Score'],reverse=True)
    
    return [{'team':i['Team'],'score':i['Score'],'color':i['Color']} for i in result]