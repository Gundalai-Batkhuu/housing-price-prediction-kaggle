import re
import json
import re

# Define a function to parse the text and create the data dictionary
def parse_data_dictionary(text):
    data_dict = {}
    current_key = None
    category_dict = None
    lines = text.split('\n')

    for line in lines:
        # Match the attribute name followed by a colon and description
        match_attr = re.match(r"(\w+): (.+)", line)
        if match_attr:
            current_key = match_attr.group(1)
            data_dict[current_key] = {"Description": match_attr.group(2).strip()}
            continue

        # Match category entries (indicated by whitespace and a tab or space at the start of the line)
        match_category = re.match(r"\s{4,}(\S+)\s+(.+)", line)
        if match_category:
            if "Categories" not in data_dict[current_key]:
                data_dict[current_key]["Categories"] = {}
            data_dict[current_key]["Categories"][match_category.group(1)] = match_category.group(2)

    return data_dict


# Read the text file and parse it
with open("data_description.txt", "r") as file:
    data_dictionary_text = file.read()

data_dictionary = parse_data_dictionary(data_dictionary_text)

# Print the data dictionary (you can access attributes as needed)
for attribute, info in data_dictionary.items():
    print(f"Attribute: {attribute}")
    print(f"Description: {info['Description']}")
    if "Data Type" in info:
        print(f"Data Type: {info['Data Type']}")
    if "Categories" in info:
        print(f"Categories: {', '.join([f'{k} ({v})' for k, v in info['Categories'].items()])}")
    print()

# ... (Previous code for parsing the data dictionary)

# Save the data dictionary as a JSON file
with open("data_dictionary.json", "w") as json_file:
    json.dump(data_dictionary, json_file, indent=4)

print("Data dictionary saved as 'data_dictionary.json'")
