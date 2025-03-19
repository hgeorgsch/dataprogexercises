"""
Skript som går igjennom src_folder, finner alle .ipynb-filer og konverterer de til ren kode (.py)
og lagrer de i dest_folder med samme struktur

Ment for plagiatkontroll
"""

import os
import shutil
import json

skips = 0
skips_name = []
def process_notebook(input_path, output_path):
   global skips, skips_name
   """
   Henter alle kodeceller i input_path (.ipynb) 
   og limer de sammen i 1 *.py fil
   """
   with open(input_path,'r', encoding="utf-8") as file:
      try:
         ipynb_dict = json.load(file)
         with open(output_path, 'w', encoding="utf-8") as file:
            for cell in ipynb_dict["cells"]:
               if cell["cell_type"] == 'code':
                  for line in cell["source"]:
                     file.write(line)
      except:
         skips += 1
         skips_name.append(input_path)
         print(f"Skipping:{input_path}")

def copy_and_process_notebooks(src_dir, dest_dir):
    """
    Recursively find all *.ipynb files in src_dir, process them,
    and save only the code cells as Python scripts in dest_dir while maintaining the directory structure.
    """
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".ipynb") and not "checkpoint" in root and not "__MAC" in root:
                # Construct full paths
                input_path = os.path.join(root, file)

                # Change the file extension to .py for the output
                relative_path = os.path.relpath(input_path, src_dir)
                output_path = os.path.join(dest_dir, os.path.splitext(relative_path)[0] + ".py")

                # Ensure the output directory exists
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Process and save the notebook
                print(f"Processing {input_path} -> {output_path}")
                process_notebook(input_path, output_path)

if __name__ == "__main__":
    # Specify the source and destination directories
    src_folder = "InsperaAssessment_1308938588/"
    dest_folder = "InsperaAssessment_1308938588/Besvarelser-PY"

    # Ensure the destination folder exists
    os.makedirs(dest_folder, exist_ok=True)

    # Process the notebooks
    copy_and_process_notebooks(src_folder, dest_folder)

    print("ERRORS", skips)
    print("Folders skipped:", skips_name)
