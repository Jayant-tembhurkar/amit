from csv import DictReader, DictWriter, reader, writer
import os

file = input("enter file to check:- ")
f = open(file)
csv_reader = DictReader(f)
file_data = list(csv_reader)
file_key = []
for row in file_data:
    for key1, value1 in row.items():
        file_key.append(key1)
        continue
    continue
file_key_set = set(file_key)
file_key_length = len(file_key_set)
file_keys = file_key[:file_key_length]
print(file_keys)
column = input("on which column you want to do opration :- ")
call = input(f"what opration you want to do on {column} \n date_scanner \n please type :- ")
def date_corrector(choose):
    value_headre = []
    header_key = []

    for row in file_data:
        for key, value in row.items():
            header_key.append(key)
            if "-" in value:
                value_headre.append(key)
            elif "/" in value:
                value_headre.append(key)
            continue
        if len(value_headre) == 0:
            continue

    header_key1 = set(header_key)
    header_key1_length = len(header_key1)
    header_key2 = header_key[:header_key1_length]

    for row in file_data:
        if len(row[choose]) == 0:
            with open(f'valid_{file}','a',newline='') as wf:
                csv_writer = DictWriter(wf,fieldnames=header_key2) 
                if os.stat(f'valid_{file}').st_size==0:
                    csv_writer.writeheader()
                csv_writer.writerow(row)
            continue
        k = []
        if "-" in row[choose]:
            k.append("-")
        else:
            k.append("/")
        def seprator():
            for l in k:
                return l
        m = row[choose].split(seprator())
        a = m[0]
        b= m[1]
        c = m[2]
        if int(a) > 31 or int(b) > 12 or len(c) != 4:
             with open(f'invalid_{file}','a',newline='') as wf:
                csv_writer = DictWriter(wf,fieldnames=header_key2)
                if os.stat(f'invalid_{file}').st_size==0:
                    csv_writer.writeheader()
                csv_writer.writerow(row)
        else:
            with open(f'valid_{file}','a',newline='') as wf:
                csv_writer = DictWriter(wf,fieldnames=header_key2) 
                if os.stat(f'valid_{file}').st_size==0:
                    csv_writer.writeheader()
                csv_writer.writerow(row)
    print(f"{file} has been checked and updated for date")    

""" calling function"""
if call == "date_scanner":
    calling = date_corrector(column)
else:
    print(f"you have not done any opration on {file}")