import glob
import xml.etree.ElementTree as ET

# All XML files in the folder
xml_files = glob.glob("vale/*.xml")

# Create root element
dataset = ET.Element("dataset")

for xml_file in xml_files:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    dataset.append(root)

# Save merged XML
merged_tree = ET.ElementTree(dataset)
merged_tree.write("merged_annotations.xml")