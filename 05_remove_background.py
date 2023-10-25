from rembg import remove
from PIL import Image

input_path = ''
output_path = ''
inp = Image.open(input_path)

output = remove(inp)
output.sabe(output_path)