'''
Want to make a script to read pdfs because edge's reader is trash
Needs to clean up text and then read what is there min x2.5 speed

Maverick Reynolds
ContentReader.py
01.20.2023

'''

import re
import pyttsx3
from unidecode import unidecode


class Speeds:
    SLOW = 200
    BRISK = 300
    QUICK = 450
    FASTEST = 500

# A bunch of heuristics to help the TTS engine read efficiently
SUBSTITUTION_DICT = {
    '\"': '',           # Quotes
    '\.\.\.': '',       # Ellipses
    '[\[\]\(\)]': '',   # Brackets or parentheses
    'http\S+': '',      # Websites
    '\S+\.pdf': '',     # pdfs
    '[p|P]age \d+': '', # Page numbers
    '_+': '',           # Line breaks or general underscores
    '[\.\:]': ','       # Make these punctuation markers have slight pause
}


# Reads from a file that the user will copy/paste into
def get_raw_text():
    with open('RAW.txt', 'r', encoding='utf-8') as f:
        return f.read()


# Split year for 1987 -> 19 87
# Say 14 hundred if 1400 (nice touch!)
def split_yr(match: re.Match):
    suffix = match.group(2)
    if suffix == '00':
        suffix = 'hundred'
    
    return match.group(1) + ' ' + suffix


def clean_text(txt, *, remove_newlines=True):
    # Remove unicode chars
    txt = unidecode(txt)

    # Remove newlines if requested
    if remove_newlines:
        txt = re.sub('\n', ' ', txt)

    # Make substitions as provided, need re.MULTILINE if newlines not removed
    for key, value in SUBSTITUTION_DICT.items():
        txt = re.sub(key, value, txt)

    # Change year format slightly
    txt = re.sub('(\d{2})(\d{2})', split_yr, txt)

    # Remove tabs then repeated whitespace  
    txt = re.sub('\t+', ' ', txt)
    txt = re.sub('\s{2,}', ' ', txt)

    return txt


def write_to_script_file(txt):
    with open('SCRIPT.txt', 'w') as f:
        f.write(txt)
    
def read(txt, speed=500):
    rdr = pyttsx3.init()
    rdr.setProperty('rate', speed)
    rdr.say(txt) # Put text into queue
    rdr.runAndWait()


def main():
    script = clean_text(get_raw_text(), remove_newlines=True)
    write_to_script_file(script)
    print(script)
    read(script, speed=400)

if __name__ == '__main__':
    main()