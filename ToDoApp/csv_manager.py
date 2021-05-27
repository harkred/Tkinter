import csv

def store_data(data, m):
    with open('tasks.csv', m) as file:
        write = csv.writer(file, dialect='excel')
        
        write.writerow(data)
        
def retrieve_data():
    with open('tasks.csv', 'r') as file:
        read = csv.reader(file, dialect='excel')
        
        return list(filter(lambda x: len(x) != 0, list(read)))