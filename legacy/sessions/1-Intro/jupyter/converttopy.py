import json

def convert(filename):
   with open(filename,'r') as file:
      ipynb_dict = json.load(file)
   with open("converted.py", 'w') as file:
      for cell in ipynb_dict["cells"]:
         if cell["cell_type"] == 'code':
            for line in cell["source"]:
               file.write(line)
            print(cell["source"])

convert("plenum.ipynb")
