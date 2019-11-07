import pytesseract
import sys
import re
from PIL import Image

print(re.search(r'[\dxX]{18}', pytesseract.image_to_string(Image.open(sys.argv[1])), re.I).group())
