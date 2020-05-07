import sqlite3
from pathlib import Path

conn = sqlite3.connect('Project.db')
c = conn.cursor()

depon = [250601, 'depon', 'Headache', 'Paracetamol', 2506, 0.4, 0.58, 0, 200]
panadol = [230602, 'panadol', 'Headache', 'Paracetamol', 2306, 0.56, 0.81, 0, 200]
livial = [220604, 'livial', 'Climacteric', 'Tibolone', 2206, 7.57, 10.43, 0, 200]
villamos = [230605, 'villamos', 'Antipsychotics', 'Olanzapine', 2306, 21.08, 29.04, 0, 200]
dalacinc = [250606, 'dalacinc', 'Infections', 'Clindamycin', 2506, 3.38, 4.66, 0, 200]
zinadol = [230607, 'zinadol', 'Otitis', 'Cefuroxime', 2306, 5.6, 7.72, 0, 200]
blocatens = [230608, 'blocatens', 'Arterial hypertension', 'bisoprolol', 2306, 2.88, 3.96, 0, 200]
tamiflu = [270609, 'tamiflu', 'Influenza treatment', 'Oseltamivir carboxylate', 2706, 12.73, 17.54, 0, 200]
vibramycin = [230610, 'vibramycin', 'Acinetobacter', 'Doxycycline', 2306, 1.34, 1.84, 0, 200]
plaquenil = [230611, 'plaquenil', 'Arthritis', 'hydroxychloroquine', 2306, 2.71, 3.73, 0, 200]
rafazil = [220612, 'rafazil', 'Alzheimer', 'donepezil', 2206, 15.04, 20.72, 0, 200]
raberen = [220613, 'rabaren', 'Esophageal disease', 'rabeprazole', 2206, 3.39, 4.68, 0, 200]
xagrid = [240614, 'xagrid', 'idiopathic thrombocytosis', 'anagrelide', 2406, 305.15, 355.81, 0, 200]
xeloda = [230615, 'xeloda', 'colon cancer stage', 'capecitabine', 2306, 21.32, 29.38, 0, 200]
kanilad = [230616, 'kanilad', 'seizures', 'lacosamide', 2306, 41.47, 57.14, 0, 200]

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Medicine(ID INTEGER, Name TEXT, Catergory TEXT, Active Ingredient TEXT, Exp Date INTEGER, Purchase Cost INTEGER, Selling Price INTEGER, Placebo INTEGER, Quantity INTEGER)')

def data_entry():
    c.execute("INSERT INTO Medicine VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")
    conn.commit()
    c.close()
    conn.close()

data_entry()
create_table()

    
#     depon = [250601, 'depon', 'Headache', 'Paracetamol', 2506, 0.4, 0.58, 0, 200]
#     panadol = [230602, 'panadol', 'Headache', 'Paracetamol', 2306, 0.56, 0.81, 0, 200]
#     livial = [220604, 'livial', 'Climacteric', 'Tibolone', 2206, 7.57, 10.43, 0, 200]
#     villamos = [230605, 'villamos', 'Antipsychotics', 'Olanzapine', 2306, 21.08, 29.04, 0, 200]
#     dalacinc = [250606, 'dalacinc', 'Infections', 'Clindamycin', 2506, 3.38, 4.66, 0, 200]
#     zinadol = [230607, 'zinadol', 'Otitis', 'Cefuroxime', 2306, 5.6, 7.72, 0, 200]
#     blocatens = [230608, 'blocatens', 'Arterial hypertension', 'bisoprolol', 2306, 2.88, 3.96, 0, 200]
#     tamiflu = [270609, 'tamiflu', 'Influenza treatment', 'Oseltamivir carboxylate', 2706, 12.73, 17.54, 0, 200]
#     vibramycin = [230610, 'vibramycin', 'Acinetobacter', 'Doxycycline', 2306, 1.34, 1.84, 0, 200]
#     plaquenil = [230611, 'plaquenil', 'Arthritis', 'hydroxychloroquine', 2306, 2.71, 3.73, 0, 200]
#     rafazil = [220612, 'rafazil', 'Alzheimer', 'donepezil', 2206, 15.04, 20.72, 0, 200]
#     raberen = [220613, 'rabaren', 'Esophageal disease', 'rabeprazole', 2206, 3.39, 4.68, 0, 200]
#     xagrid = [240614, 'xagrid', 'idiopathic thrombocytosis', 'anagrelide', 2406, 305.15, 355.81, 0, 200]
#     xeloda = [230615, 'xeloda', 'colon cancer stage', 'capecitabine', 2306, 21.32, 29.38, 0, 200]
#     kanilad = [230616, 'kanilad', 'seizures', 'lacosamide', 2306, 41.47, 57.14, 0, 200]