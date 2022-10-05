# Running FAVE inside a Docker container

This repository contains configuration and code patches to allow running
the FAVE align and extract tools inside a Docker container.  The container
is based on the [HTK docker configuration by Loreto Parisi](https://github.com/loretoparisi/htk), extended here to add the FAVE code.  A few patches are required to
allow these to work together.

## Building

Patching bug in HRec.c:

```bash
cd htk
patch -p 1 < ../htk.patch
```

From the main project directory, build the Docker image.

```bash
docker build -t htk-fave .
```

Once built, you can now start a shell prompt inside the container:

```bash
docker run -v ~/corpora/:/corpora -v `pwd`/FAVE:/root/FAVE -it htk-fave
```

To initalise the environment, you need to initialise poetry:

```bash
../.poetry/bin/poetry shell
```

Example commands for running `fave-extract` and `fave-align`: 

```bash
fave-extract '/corpora/NZ-Formants/Reading Passage wav-textgrid-txt files/Titirangi/Older/AK-TO01-P/AK-TO01-P01.wav' '/corpora/NZ-Formants/Reading Passage wav-textgrid-txt files/Titirangi/Older/AK-TO01-P/AK-TO01-P01.TextGrid' AK-TO01-P01.fm --speechSoftware praat_nogui
```

```bash
fave-align '/corpora/NZ-Formants/Reading Passage wav-textgrid-txt files/Papatoetoe/Younger/AK-PY01/AK-PY01-P02.wav' 'out/Papatoetoe/Younger/AK-PY01/AK-PY01-P02.trs' AK-PY01-P02.TextGrid
```

## Scripts

The repository includes some convenience scripts for running align and extract over 
a collection of files. These are written for our specific use case but could be adapted
for use on other collections. The scripts are in the `scripts` folder and are 
copied into the container as it is built.


