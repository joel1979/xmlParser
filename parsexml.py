# Joel Pettersson

import xml.etree.ElementTree as ET
import json

# Set the input and output filenames
input_file = "input.xml"
output_file = "output.json"

# Set the element(s) and/or attribute(s) to extract
elements_to_extract = [""]
attributes_to_extract = [""]

try:
    # Parse the XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Initialize a dictionary to store the output
    output = {}

    # Loop through each element in the XML file
    for element in root.iter():

        # Check if the element is one of the ones to extract
        if element.tag in elements_to_extract:

            # Initialize a dictionary for the element
            element_dict = {}

            # Add any attributes to the dictionary
            if attributes_to_extract:
                attribute_dict = {}
                for attribute in attributes_to_extract:
                    if attribute in element.attrib:
                        attribute_dict[attribute] = element.attrib[attribute]
                if attribute_dict:
                    element_dict["attributes"] = attribute_dict

            # Add any sub-elements to the dictionary
            if list(element):
                sub_element_dict = {}
                for sub_element in element:
                    sub_element_dict[sub_element.tag] = sub_element.text
                if sub_element_dict:
                    element_dict["sub_elements"] = sub_element_dict

            # Add the element dictionary to the output dictionary
            output[element.tag] = element_dict

    # Write the output to the output file
    with open(output_file, "w") as f:
        json.dump(output, f)

    print("Output written to", output_file)

except Exception as e:
    print("Error:", e)
