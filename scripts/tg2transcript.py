from fave import praat
import sys
import os


def process(filename, outdir):
    basename, ext = os.path.splitext(os.path.basename(filename))
    outfile = os.path.join(outdir, basename + '.trs')

    tg = praat.TextGrid()
    tg.read(filename)


    hasort = False
    t = []
    for tier in tg:
        if tier.name() in ['ORT', 'ORT-MAU']:
            hasort = True
            xmin = tier.xmin()
            xmax = tier.xmax()
            for interval in tier:
                word = interval.mark().strip(' \t-')
                t.append(word)

    text = ' '.join(t).strip() + '.'

    if hasort:
        os.makedirs(os.path.dirname(outfile), exist_ok=True)
        with open(outfile, 'w', encoding='utf8') as out:
            out.write("AB\tABC\t{xmin}\t{xmax}\t{text}\n".format(xmin=xmin, xmax=xmax, text=text))
    else:
        print("No ORT tier for", filename)

if __name__=='__main__':
    indir = sys.argv[1]
    outdir = sys.argv[2]

    for root, dirs, files in os.walk(indir):
        for f in files:
            filename = os.path.join(root, f)
            if filename.endswith('.TextGrid'):
                od = os.path.join(outdir, root.replace(indir, ''))
                process(filename, od)