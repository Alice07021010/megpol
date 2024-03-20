import csv
with open ("C:\Users\sulej\Downloads\space.2.0.csv",encoding='utf-8') as f:
    f=csv.DictReader(f,delimiter='*',quotecher='"')
    d=sorted(reader,key=lambda x:x['ShipName'])
shp_nm=input()

while (shp_nm!='stop'):
    shp_nm=int(shp_nm)
    for i in d:
        if int(i['ShipName'])==shp_nm:
            name,planet,direction=i['ShipName'].split()
            print(f"Корабль (i['shp_nm'] был отправлен с планеты: (plane[0]) и его направление движения было: (direction)")
            break
    else:
        print('error.. er.. ror..')
    shp_nm=input()


