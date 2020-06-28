import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

#finding the values from cells
wksht1 = client.open("Medstore").worksheet("DrugWF")
wksht2 = client.open("Medstore").worksheet("DrugTally")
wksht3 = client.open("Medstore").worksheet("MaskWF")
wksht4 = client.open("Medstore").worksheet("MaskTally")
testwksht = client.open("Medstore").worksheet("testpage")

drugrowno = len(wksht1.col_values(1))
drugrowno = int(drugrowno)
maskrowno = len(wksht3.col_values(1))
maskrowno = int(maskrowno)

while True:
    drugrownocheck = len(wksht1.col_values(1))
    drugrownocheck = int(drugrownocheck)
    maskrownocheck = len(wksht3.col_values(1))
    maskrownocheck = int(maskrownocheck)

#Drug Section
    if drugrowno == drugrownocheck:
        time.sleep(1)
        pass

    else:
        drugname = wksht1.get('E2').first()
        drugvaldraw = wksht1.get('F2').first()
        drugcell = wksht2.find(drugname)
        drugrowval = int(drugcell.row)
        drugoldtally = wksht2.cell(drugrowval,6).value
        print(drugoldtally)

 #calculating the values and update cell
        drugvaldraw = int(drugvaldraw)
        drugoldtally = int(drugoldtally)
        drugnewtally = drugoldtally - drugvaldraw
        wksht2.update_cell(drugrowval,6, drugnewtally)
        drugrowno = drugrowno + 1
        time.sleep(1)

#Mask section

    if maskrowno == maskrownocheck:
        time.sleep(1)
        pass

    else:
        maskname = wksht3.get('E2').first()
        maskvaldraw = wksht3.get('F2').first()
        maskcell = wksht4.find(maskname)
        maskrowval = int(maskcell.row)
        maskoldtally = wksht4.cell(maskrowval,6).value
        print(maskoldtally)

 #calculating the values and update cell
        maskvaldraw = int(maskvaldraw)
        maskoldtally = int(maskoldtally)
        masknewtally = maskoldtally - maskvaldraw
        wksht4.update_cell(maskrowval,6, masknewtally)
        maskrowno = maskrowno + 1
        time.sleep(1)














#prototype(probably delete in later stage)
# (print("What do Obi Wan to do")
# BigAnswer = input("Answer:")
# if BigAnswer == ("Masks"):
#     #Value of Remainder
#     val = wksht1.acell('C2').value
#
#     #Questioning
#     print("What is your name?")
#     name = input("Name: ")
#     print("How many masks would you like to draw?")
#     qty = input("Answer: ")
#
#     #Values of masks subtraction
#     val = int(val)
#     qty = int(qty)
#     newval = val - qty
#
#     #inserting values
#     row = [name, qty, newval]
#     wksht1.insert_row(row,2)
#
# elif BigAnswer == ("Items"):
#     wksht2 = client.open("Medstore").worksheet("example2")
#     print("What do you want to draw?")
#     item = input("Answer: ")
#     if item == "C Collar":
#         cell = wksht2.find("C Collar")
#         rowval = int(cell.row)
#         oldval = wksht2.cell(rowval, 2).value
#         oldval = int(oldval)
#         print("How much do you want to use?")
#         quant = input("Answer: ")
#         quant = int(quant)
#         yes = oldval - quant
#         wksht2.update_cell(rowval, 2, yes)

# Updating of cells per month
