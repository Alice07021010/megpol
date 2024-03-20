import csv
with open ('space.2.0..csv',encoding='utf-8') as f:
    reader = list(csv.DictReader(f,delimiter='*',quotechar='"'))
    for i in range (len(reader)):
        j=i-1
        key=reader[i]
        while float(reader[j]['coord_place'] if reader[j]['coord_place']!='0' else 0)<float(key['coord_place'] if key['coord_place']!='0' else 0) and j>=0:
            reader [j+1]=reader[j]
            j-=1
            reader[j+1]=key

print('Название корабля')
k=1

for i in reader:
    if '0' in i['coord_place']:
        name,planet,direction=i['ShipName'].split()
        print(f"(k) Название корабля")
        k+=1
    if k==10:
        break