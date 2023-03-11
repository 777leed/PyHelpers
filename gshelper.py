import pygsheets
from deep_translator import GoogleTranslator

# this return the translation of an expression from spanish to english
# return type : string
def myTranslator(exp):
    es = 'es'
    en = 'en'
    return GoogleTranslator(
        source=es, target=en
        ).translate(exp) 

# this return a list of the words in the file "weekly spanish"  
def getwords():
    with open(r'C:\Users\hp\Documents\Vault\Inbox\Weekly Spanish.md', 'r', encoding="utf-8") as f:
        text = f.read()
        text = text.translate({ord(i):None for i in '#123456789'})
        text = text.replace("day", '')
        lines = text.split('\n')
        non_empty_lines = [line for line in lines if line.strip() != ""]
        textdash = ''.join(non_empty_lines)
        lines = textdash.split('-')
        new_values = [lines[i+1] for i in range(len(lines)-1)]
        return new_values

# this returns a list of translated expressions after taking a list
def TranslationFactory(listofexp):     
    return [myTranslator(listofexp[i]) for i in range(len(listofexp))]   


# authorization
gc = pygsheets.authorize(service_file=r"C:\Users\hp\Downloads\sheetapi-380111-e9a36fa4aa50.json")
print("Logging in ...")

# open the Google spreadsheet by name
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1O6ZFndLUshc4BK5iyJNpMhUvDiB3ZL6cYTBXRfdilzo/edit?usp=sharing')
print("Opening the file ...")

# select the first sheet
worksheet = sh.sheet1
# get the values in the first column of the worksheet
# column1_values = worksheet.get_col(1)
# update the values in the first column with new values
new_values = getwords()
worksheet.update_col(1, new_values)
worksheet.update_col(2, TranslationFactory(new_values))
print("columns have been updated!")
