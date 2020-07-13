import pandas as pd
import xlrd as xl
import matplotlib.pyplot as plt


print("welcome to SMART BUY")
print("admin login")
count=3
while(count>0):
    a=int(input('enter the password:'))
    if a != 12345678:
        print("wrong password")
        count -= 1
        print("you have only ",count,"chances")
    else:
        print("sucessfully logined")
        print("####The products in the stocks####\n")

        """ reading excel file"""
        filename = 'C:/Users/student/Downloads/bse.xlsx'
        sheet_no = 0
        wb = xl.open_workbook(filename)
        sheet = wb.sheet_by_index(sheet_no)
        norows = sheet.nrows
        nocol = sheet.ncols

        """serial number of items"""
        sno = []
        for i in range(1, norows):
            x = int(sheet.cell_value(i, 0))
            sno.append(x)

        """items of in the stock"""
        items = []
        for i in range(1, norows):
            x = sheet.cell_value(i, 1)
            items.append(x)

        """prices of items extraction"""
        price = []
        for i in range(1, norows):
            x = int(sheet.cell_value(i, 2))
            price.append(x)

        """quantites of items in stocks: extraction"""
        quantity = []
        for i in range(1, norows):
            x = int(sheet.cell_value(i, 3))
            quantity.append(x)

        """expiry dates  of items in stocks: extraction"""
        expiry = []
        for i in range(1, norows):
            x = sheet.cell_value(i, 4)
            expiry.append(x)
        print(expiry)

        df1 = pd.DataFrame({'SNO': [i for i in sno], 'items': [i for i in items], 'price': [i for i in price],
                            'quantity': [i for i in quantity]})
        print(df1)

        print('\n### new items arrieved to the stock ###')
        arrived = int(input('enter  newly arrived items count->'))
        for i in range(0, arrived):
            status = int(input("enter\n\t'1' if item is already in stock\n\n\t'0' if item is not in stock\n\t->"))
            if status == 1:
                ab = int(input('enter the serial number of item->'))
                for j in range(0, len(sno)):
                    if sno[j] == ab:
                        q_ab = int(input('enter the quantity of item->'))
                        quantity[j] += q_ab
            else:
                s_ab = sno[len(sno) - 1] + 1
                sno.append(s_ab)
                new_item = input('enter the item name->')
                items.append(new_item)
                new_price = int(input('enter the price(:1) of item->'))
                price.append(new_price)
                new_quantity = int(input('enter the quantity of item->'))
                quantity.append(new_quantity)
                new_expiry = input('enter the expiry date')
                expiry.append(new_expiry)

        print('\n### updated stock ###')
        df2 = pd.DataFrame({'SNO': [i for i in sno], 'items': [i for i in items], 'price': [i for i in price],
                            'quantity': [i for i in quantity]})
        print(df2)

        """ billing input"""

        totalbill = 0
        cust_items = int(input('\nenter number of items taken by cutomer->'))
        cust_list = []


        """" cust_list  contain [item,price,quantity,price*quantity] """
        
        while (cust_items > 0):
            print(sno)
            cust_sno = int(input('enter the serial number of item->'))
            cust_quantity = int(input('enter the quantity->'))
            for i in range(0, len(sno)):
                if sno[i] == cust_sno:
                    cust_list.append([items[i], price[i], cust_quantity, (price[i] * cust_quantity)])
                else:print('enter the correct serial number ')
            cust_items -= 1
            

        df3 = pd.DataFrame(cust_list, columns=['item', 'price(:1)', 'quantity', 'p*q'])
        print(df3)
        for i in range(len(cust_list)):
            totalbill += cust_list[i][3]

        print('\n %%% BILLAMOUNT %%%%->', totalbill)

        """###UPDATING THE EXCEL FILE###"""

        df2.to_excel('C:/Users/student/Downloads/updatedbs.xlsx',index=False)
        
        print('#### THANKS FOR VISITING ####')
              
        break

""" DATA VISUVALISATION FOR 5 DAYS OF SALES """
print('\n####SALES  ANALYSIS####')
data_sales=[]
n=int(input('\nFor no. of days'))
print('### data visualization FOR {0} DAYS ###'.format(n))
for i in range(n):
    ax=int(input('enter the sales of day:{0}->'.format(i+1)))
    data_sales.append(ax)

print(data_sales)
x = [i for i in range(1,n+1)]

"""create bar graphs"""

plt.bar(x,data_sales,label = 'Sales per day', color ='red')
plt.legend()
plt.xlabel('DAYS')
plt.ylabel('SALES AMOUNT')
plt.title('SALES FOR {0} DAYS'.format(n))
plt.show()


