import csv
import os

basedir = '/corpora/NZ-formants/speakers'
os.makedirs(basedir, exist_ok=True)

with open("speaker_deets.csv") as fd:

    reader = csv.DictReader(fd)
    for row in reader:
        outfile = os.path.join(basedir, row['spk'] + ".speaker")
        print(outfile)
        with open(outfile, 'w') as out:
            out.write('--sex\n')
            out.write(row['sex'])
            out.write('\n--age\n')
            if row['age'] == 'Y':
                out.write('25')
            else:
                out.write('55')
            out.write('\n')