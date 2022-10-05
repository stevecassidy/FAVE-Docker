# Notes on running FAVE

## Building

Patching bug in HRec.c:

```bash
cd htk
patch -p 1 < ../htk.patch
```

```bash
docker build -t htk-fave .
```


```bash
docker run -v ~/corpora/:/corpora -v `pwd`/FAVE:/root/FAVE -it htk-fave


../.poetry/bin/poetry shell


fave-extract '/corpora/NZ-Formants/Reading Passage wav-textgrid-txt files/Titirangi/Older/AK-TO01-P/AK-TO01-P01.wav' '/corpora/NZ-Formants/Reading Passage wav-textgrid-txt files/Titirangi/Older/AK-TO01-P/AK-TO01-P01.TextGrid' AK-TO01-P01.fm --speechSoftware praat_nogui


fave-align /corpora/NZ-Formants/Reading\ Passage\ wav-textgrid-txt\ files/Papatoetoe/Younger/AK-PY01/AK-PY01-P02.wav out/Papatoetoe/Younger/AK-PY01/AK-PY01-P02.trs AK-PY01-P02.TextGrid

```
