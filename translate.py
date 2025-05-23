import os
import sys
from deep_translator import GoogleTranslator

if len(sys.argv) < 3:
    print("Usage: python script.py /home/Downloads/subtitle_filename subtitle_filename")
    sys.exit(1)

file = sys.argv[1]
filename = sys.argv[2]

GET_FOLDER = 'subtitles'
os.makedirs(GET_FOLDER, exist_ok=True)

with open(f"{file}.srt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    
translated = []
for line in lines:
    if "-->" in line or line.strip().isdigit() or line.strip() == "":
        translated.append(line)
    else:
        translated.append(GoogleTranslator(source='auto', target='pt').translate(line))

with open(f"{GET_FOLDER}/{filename}_traduzida.srt", "w", encoding="utf-8") as f:
    f.writelines(translated)

print("Translation finalised.")