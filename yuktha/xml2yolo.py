import xml.etree.ElementTree as ET
import os

# Path to your merged_annotations.xml
xml_file = "merged_annotations.xml"
output_dir = "label1"

# Create labels folder if not exists
os.makedirs(output_dir, exist_ok=True)

# Class mapping (add all classes you want YOLO to detect)
class_mapping = {
    "left_arrow": 0,
    "right_arrow": 1
}

tree = ET.parse(xml_file)
root = tree.getroot()

# Iterate over all <annotation> tags
for annotation in root.findall("annotation"):
    filename = annotation.find("filename").text
    image_width = int(annotation.find("size/width").text)
    image_height = int(annotation.find("size/height").text)
    
    # Create corresponding YOLO txt file
    txt_filename = os.path.splitext(filename)[0] + ".txt"
    txt_path = os.path.join(output_dir, txt_filename)
    
    with open(txt_path, "w") as f:
        for obj in annotation.findall("object"):
            class_name = obj.find("name").text.strip()
            
            if class_name not in class_mapping:
                print(f"Skipping unknown class: {class_name}")
                continue  # skip if the class is not in mapping
            
            class_id = class_mapping[class_name]
            
            xmin = int(obj.find("bndbox/xmin").text)
            ymin = int(obj.find("bndbox/ymin").text)
            xmax = int(obj.find("bndbox/xmax").text)
            ymax = int(obj.find("bndbox/ymax").text)
            
            # Convert to YOLO format
            x_center = ((xmin + xmax) / 2) / image_width
            y_center = ((ymin + ymax) / 2) / image_height
            width = (xmax - xmin) / image_width
            height = (ymax - ymin) / image_height
            
            f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

print("Conversion complete! YOLO labels are saved in 'labels/' folder.")