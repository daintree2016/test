import sys
import mysql.connector
import pandas as pd

def callme():
    varr=sys.argv[1].split('##')[0]
    locc=sys.argv[1].split('##')[1]
    mydb = mysql.connector.connect(
    host="193.203.184.52", user="u666697439_peach",
    password="Peach@usa1", database="u666697439_pshipments")

    mycursor = mydb.cursor()
    global mydict
    mydict={}
    global mydict2
    mydict2={}
    mydict2['Indexx']=['PUID','Asin','Sku','title','Ship_no','Purch_Id','Purch_Price','Order_Id','Availability','Rack',
                    'Comments','Last_update','user','Reason','ord_history','Purch_Date','Vendor','location','Id']

    if locc.lower()=='all':
        mycursor.execute(f"SELECT * FROM warehouse")
    else:
        mycursor.execute(f"SELECT * FROM warehouse WHERE location = '{locc}' ")
    #print(str(sys.argv[1]))
    #print('yes')
    myresult = mycursor.fetchall()

    for x in myresult:    
        #time.sleep(1)
        #print(x[0])
        try:
            #print(mydict[x[1]])
            mydict[x[1]].append([x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16],x[17],x[18]])
        except Exception as e:
            print(e)
            mydict[x[1]]=[]
            mydict[x[1]].append([x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16],x[17],x[18]])
        
    #print(mydict['B01FYBDCXG'])

    list1={'Asin':[],'Sku':[],'Title':[],'Total Stock':[],'Proactive':[],'Restock':[],
        'Reactive':[],'Inactive':[],'Bin':[],'FBA':[],'Offline':[],'Last Purchase Date':[],'Last Purchase Price':[],'currentstock':[]}



    for i,j in mydict.items():
        #print(i,j)
        #print(j)
        #list1['Asin'].append(i)
        num=0
        num2=0
        num3=0
        num4=0
        num5=0
        num6=0
        num7=0
        for h in j:
            if h[8].lower()=='proactive':
                print(h)
                num=num+1
            elif h[8].lower()=='restock':
                print(h)
                num2=num2+1
            elif h[8].lower()=='reactive':
                print(h)
                num3=num3+1
            elif h[8].lower()=='inactive':
                print(h)
                num4=num4+1
            elif h[8].lower()=='bin':
                print(h)
                num5=num5+1
            elif h[8].lower()=='fba':
                print(h)
                num6=num6+1
            elif h[8].lower()=='offline':
                print(h)
                num7=num7+1
        total=num+num2+num3+num4+num5+num6+num7
        if total<=0:
            pass
        else:
            list1['Asin'].append(h[1])
            list1['Sku'].append(h[2])
            list1['Title'].append(h[3])
            list1['Proactive'].append(num)
            list1['Restock'].append(num2)
            list1['Reactive'].append(num3)
            list1['Inactive'].append(num4)
            list1['Bin'].append(num5)
            list1['FBA'].append(num6)
            list1['Offline'].append(num7)
            list1['Total Stock'].append(num+num2)
            list1['Last Purchase Date'].append(h[15])
            list1['currentstock'].append(num+num2+num3+num4+num6+num7)

            try:
                list1['Last Purchase Price'].append(float(h[6].replace('$','').replace(',','').strip()))
            except Exception:
                list1['Last Purchase Price'].append(h[6])
    print(list1)
    # # with open('stock.txt','r') as f:
    # #     dataa=str(f.read())

    # dataa=dataa.split(' ')
    # #print(dataa)
    # ioo=0
    # for a in dataa:
    #     #print(a)
    #     mydict2[ioo]=[a]
    #     func(asin=ioo,asinn=a)
    #     ioo=ioo+1
        #print(mydict2['B09BZ2SHQY'])
        #break
    #print(mydict2)


    df=pd.DataFrame.from_dict(list1,orient='index').transpose()
    #print(df)
    #writer = (r'total_stock.xlsx')
    #df.to_excel(writer,'Sheet5')
    #writer.close()
    df.to_csv(f"reports/{varr}_stock.csv")
    print("your file is now ready to be downloaded")

callme()