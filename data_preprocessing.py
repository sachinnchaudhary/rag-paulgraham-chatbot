import re
import json

#this is function for cleaning the essay data 
def clean_essaydata(essays):
    essays = re.sub(r'\d{4}', '', essays)  # Remove years
    essays = re.sub(r'\n+', ' ', essays)  # Remove newlines

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    for month in months:

        if month in essays:
            essays = re.sub(rf"{month}", "", essays)

    stamps = ["[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]", "[9]", "[10]", "[11]", "[12]", "[13]", "[14]",
              "[15]", "[16]", "[17]", "[18]", "[19]", "[20]", "[21]", "[22]", "[23]", "[24]", "[25]", "[26]", "[27]",
              "[28]", "[29]", "[30]"]

    for stamp in stamps:
        if stamp in essays:
            essays = re.sub(rf"{stamp}", "", essays)
            print(f"deleting the {stamp}")

    essays = re.sub(r'\[]', "", essays)

    essays = re.sub("  ", "", essays)

    print(essays)
    return essays


with open("....name of file....", "r", encoding="utf-8") as file:
    data = json.load(file)

# Get an iterator over the dictionary items
essay_iterator = iter(data.items())

# Function to fetch the next essay
def print_next_essay(iterator):
    try:
        essay_title, essay_text = next(iterator)
        return essay_text, essay_title
    except StopIteration:
        return None, None

# Write the processed essays to a text file

with open("....name of file....", "w", encoding="utf-8") as output_file:
    for i in range(221):
        essay_title, essay_text = print_next_essay(essay_iterator)
        if essay_title is None or essay_text is None:
            break
        cleaned_text = clean_essaydata(essay_text)
        output_file.write(f"Title: {essay_title}\nCleaned Essay Text: {cleaned_text}\n\n")

print("Essays added flawlessly to text file.")
