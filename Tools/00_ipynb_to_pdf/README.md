### Get Ready to Use
pip install nbconvert[webpdf]  # may need more installation to use webpdf

pip install nbconvert
pip install jupyter_core
pip install jupyter_client
pip install nbformat
pip install ipykernel
pip install traitlets
pip install pygments
pip install jinja2
pip install pandoc  # may need pandoc also

---
### Code Explanation

import os: Used for file system path operations.

import subprocess: Used to execute external commands (in this case, jupyter nbconvert).

convert_ipynb_to_pdf() function:
os.getcwd(): Retrieves the path of the directory where the current script is being executed.

os.listdir(current_directory): Gets a list of all files and folders in the current directory.

f.endswith('.ipynb'): Filters only files ending with the .ipynb extension.

Loop for conversion: For each .ipynb file found, it performs the following:
os.path.splitext(ipynb_file)[0]: Gets the filename without its extension.

os.path.join(current_directory, f"{file_name_without_ext}.pdf"): Constructs the full path for the PDF file to be created.

subprocess.run(): Executes the jupyter nbconvert command.

--to webpdf: This option is the most recommended method for converting to PDF. It converts the notebook to PDF using web rendering, providing a clean output. This option requires a Chromium-based browser (like Chrome, Chromium, or Edge) to be installed on your system.

--to pdf: If webpdf doesn't work or is difficult to set up, you can use this option. However, this option requires a LaTeX distribution (e.g., TeX Live or MiKTeX) to be installed on your system to function correctly. An error will occur if LaTeX is not installed.

--output-dir current_directory: Specifies that the converted PDF file should be saved in the current directory.

Error Handling: Uses a try-except block to handle subprocess.CalledProcessError (when the command execution fails) and FileNotFoundError (when the jupyter command cannot be found).

---
### How to Use
Save the code above as a Python file, for example, convert_notebooks.py.

Navigate to the directory containing the .ipynb files you want to convert to PDF.

Execute the following command in your terminal or command prompt:

'''
python convert_notebooks.py
'''
