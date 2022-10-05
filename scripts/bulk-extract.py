import sys, os, subprocess

dirname = sys.argv[1]
logfile = sys.argv[2]

with open(logfile, 'w') as log:
    for dirpath, dirnames, filenames in os.walk(os.path.join(dirname, 'Reading')):
        for filename in filenames:
            if filename.startswith('AK-PY0') and filename.endswith('.wav'):
                wav = os.path.join(dirpath, filename)
                tgs = wav.replace('Reading', 'FAVE_TextGrids').replace('wav', 'TextGrid')
                out = wav.replace('Reading', 'FAVE_Formants').replace('.wav', '')

                speakerfile = os.path.join(dirname, 'speakers', os.path.basename(dirpath) + ".speaker")

                if not os.path.exists(tgs):
                    print("Missing:", tgs)
                else:
                    os.makedirs(os.path.dirname(out), exist_ok=True)
                    cmd = [
                        'fave-extract',
                        '--speaker', speakerfile,
                        '--speechSoftware', 'praat_nogui',
                        wav,
                        tgs,
                        out
                    ]
                    print(out)
                    log.write(" ".join(cmd) + '\n')
                    log.write(out + '\n')
                    result = subprocess.run(cmd, capture_output=True)
                    log.write(result.stdout.decode('utf8'))
                    log.write(result.stderr.decode('utf8'))
                    log.write('--\n')
                    log.flush()