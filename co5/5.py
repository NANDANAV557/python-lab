import scv
csv_col=['Roll no.','Name','Address']
dict_data=[{'Roll no.':1,'Name':alan,'Address':palakkad(po)678621},
           {'Roll no.':2,'Name':tony,'Address':idukki(po)764532},
           {'Roll no.':3,'Name':liya,'Address':kannur(po)234566},
           {'Roll no.':4,'Name':aline,'Address':wayyanda(po)567890},
           {'Roll no.':5,'Name':david,'Address':kozhikode(po)123456},
           {'Roll no.':6,'Name':mark,'Address':thrissur(po)234567}]
           
csv_file="student.csv"
try:
    with oprn(csv_file,'w')as file1:
        writer=csv.Dictwriter(file1,filednames=csv_col)
        writer.writeheader()
        for data1 in dict_data:
            writer.writerow(data1)
except IOError:
    print("I/O error")
data1=csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data1:
    print(row)
