# https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
import numpy as np

tree = ET.parse('input.xml')
root = tree.getroot()

# print(root.tag, root.attrib)
# for child in root[:3]:
#     print(child.tag, child.attrib)

data = []
for i in range(len(root)):
    row = [root[i][j].text for j in range(4)]
    data.append(row)

np.savetxt("output.gz", data, fmt="%s")
