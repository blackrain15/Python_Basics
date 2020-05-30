import xml.etree.ElementTree as ET
import csv

tree = ET.parse("product.xml")
root = tree.getroot()

f = open('product.csv', 'w')

csvwriter = csv.writer(f)

count = 0

head = ['id','productName','cost','weight']

csvwriter.writerow(head)

for item in root.findall('product'):
    row = []
    ID = item.find('id').text
    row.append(ID)
    prod_name = item.find('productName').text
    row.append(prod_name)
    cost = item.find('cost').text
    row.append(cost)
    wt = item.find('weight').text
    row.append(wt)
    csvwriter.writerow(row)

f.close()

f_in = open("product.csv", "r")
print(f_in.read())
f_in.close()