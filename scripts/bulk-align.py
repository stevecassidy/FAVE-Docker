import sys, os, subprocess

dirname = sys.argv[1]
logfile = sys.argv[2]

with open(logfile, 'w') as log:
    for dirpath, dirnames, filenames in os.walk(os.path.join(dirname, 'Reading')):
        for filename in filenames:
            if filename.endswith('.wav'):
                wav = os.path.join(dirpath, filename)
                trs = wav.replace('Reading', 'Transcripts').replace('wav', 'trs')
                out = wav.replace('Reading', 'FAVE_TextGrids').replace('wav', 'TextGrid')
                if not os.path.exists(trs):
                    print("Missing:", trs)
                else:
                    os.makedirs(os.path.dirname(out), exist_ok=True)
                    cmd = [
                        'fave-align',
                        wav,
                        trs,
                        out
                    ]
                    log.write(wav + '\n')
                    result = subprocess.run(cmd, capture_output=True)
                    log.write(result.stdout.decode('utf8'))
                    log.write(result.stderr.decode('utf8'))
                    log.write('--\n')
                    log.flush()