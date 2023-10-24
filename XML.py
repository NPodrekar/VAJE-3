import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("person")

# Create sub-elements and set their values
name = ET.SubElement(root, "name")
name.text = "Alice"

age = ET.SubElement(root, "age")
age.text = "30"

address = ET.SubElement(root, "address")
street = ET.SubElement(address, "street")
street.text = "Dunajska"

city = ET.SubElement(address, "city")
city.text = "Ljubljana"

married = ET.SubElement(root, "married")
married.text = "True"

# Serialize to XML file
tree = ET.ElementTree(root)
tree.write("./person.xml")


# Parse the XML file
tree = ET.parse('./person.xml')
root = tree.getroot()

# Update age and married status
root.find("age").text = "31"
root.find("married").text = "False"

# Write the manipulated data back to the same XML file
tree.write("./person.xml")