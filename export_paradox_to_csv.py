import pypxlib
import csv

db_file = 'Brutist.DB'
csv_file = 'Brutist.csv'

db = pypxlib.Table(db_file)
with open(csv_file, 'w', newline='', encoding='utf-8') as f:  
    writer = csv.writer(f)
    writer.writerow(db.fields)
    for record in db:
        row = [record[field] for field in db.fields]  
        writer.writerow(row)

print(f"Data successfully written to {csv_file}")
