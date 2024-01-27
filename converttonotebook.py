
import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell
from nbformat import write

def py_to_ipynb(py_file, ipynb_file):
    # Read the Python script
    with open(py_file, 'r') as f:
        lines = f.readlines()

    # Create a new Jupyter Notebook
    nb = nbformat.v4.new_notebook()

    # Initialize a variable to track the current code cell
    current_code_cell = None

    # Iterate through each line in the Python script
    for line in lines:
        if line.startswith("# In["):
            # If a new code cell is encountered, create a new code cell in the Jupyter Notebook
            if current_code_cell is not None:
                nb.cells.append(current_code_cell)
            # Create a new code cell with the current line as the source
            current_code_cell = new_code_cell(source=line)
        else:
            # If not a code cell marker, add the line to the source of the current code cell
            if current_code_cell is not None:
                current_code_cell['source'] += line

    # Append the last code cell to the Jupyter Notebook
    if current_code_cell is not None:
        nb.cells.append(current_code_cell)

    # Write the Jupyter Notebook to a file
    with open(ipynb_file, 'w') as f:
        write(nb, f, 4)

# Replace 'your_script.py' with the path to your Python script
# Replace 'output_notebook.ipynb' with the desired name for the Jupyter Notebook
py_to_ipynb('filename.py', 'output_notebook.ipynb')
