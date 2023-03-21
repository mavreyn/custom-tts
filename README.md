# Custom TTS Reader

I made this simple script in January 2023 after being frustrated with chromium's tts reader. I could not make it read faster than 200% speed and it would say goofy things that semantically made no sence (e.g. underscore underscore underscore underscore underscore underscore...) instead of ignoring or removing the line break.

## Wishlist

I wanted to make a script that allowed me to 'clean' the text before giving it to the tts reader. My solution was a simple dictionary of substitutions `SUBSTITUTION_DICT` that I could use regex to find. I also learned that re.sub may take a callable as one of its parameters, which accepts a match object and returns a string, so that the contents of the match can be manipulated and reinserted to the text. This is seen with the `split_yr` function

I also have some preset speeds in the `Speeds` class that I often use.

## Use

To use the reader, copy text into `RAW.txt`. After running `ContentReader.py`, the content will be cleaned and saved to `SCRIPT.py` and the pyttsx3 reader will speak aloud the script. The user also has the option of removing newlines in the main function if he/she desires.
