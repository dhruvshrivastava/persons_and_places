import os 
import pandas as pd

directory = "/mnt/disks/ldcil_test/all_text/"
places_output = []
for filename in os.listdir(directory):
    if 'Telugu' in filename and 'Place' in filename: 
        file_path = os.path.join(directory, filename)

        with open(file_path, 'r') as f:
            lines = f.readlines()
            line = lines[48]
            print("Done {0}".format(line))
            places_output.append(line)

df = pd.DataFrame(places_output, columns=['Place'])
df.to_csv('/mnt/disks/ldcil_test/telugu_places.csv')

person_output = []
for filename in os.listdir(directory):
    if 'Telugu' in filename and 'Person' in filename: 
        file_path = os.path.join(directory, filename)

        with open(file_path, 'r') as f:
            lines = f.readlines()
            line = lines[48]
            print("Done {0}".format(line))
            places_output.append(line)

df = pd.DataFrame(person_output, columns=['Place'])
df.to_csv('/mnt/disks/ldcil_test/telugu_persons.csv')
