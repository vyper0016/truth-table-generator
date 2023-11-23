from prettytable import PrettyTable
import inspect
from html_table_csv import html_to_csv
import os

def int_to_bin(x:int, n:int):
    """
    Convert an integer to a binary string representation with a specified length.

    Args:
        x (int): The integer to convert.
        n (int): The desired length of the binary string.

    Returns:
        str: The binary string representation of the integer.
    """
    s = '{0:b}'.format(x)
    s = '0'*(n-len(s)) + s
    return s

def generate_table(variables: list, functions: list, table_name:str = 'table', out_dir: str = './tables/', html: bool = True, html_name: str = None, csve: bool = False, csv_name = None):
    """
    Generate a truth table based on the given variables and functions.

    Args:
        variables (list): A list of variable names.
        functions (list): A list of tuples containing the name and function for each column in the truth table: [variable names], [(name, function)]
        table_name (str, optional): The name of the table. Defaults to 'table'.
        out_dir (str, optional): The directory to save the table. Defaults to './tables/'.
        html (bool, optional): Whether to export the table as HTML. Defaults to True.
        html_name (str, optional): The name of the HTML file. Defaults to None.
        csve (bool, optional): Whether to export the table as CSV. Defaults to False.
        csv_name (str, optional): The name of the CSV file. Defaults to None.

    Returns:
        PrettyTable: The generated truth table.
    """
    for f in functions:
        assert isinstance(f, tuple), f'expected tuple, got {type(f)}'
        assert len(f) == 2, f'expected tuple of length 2, got {len(f)}'
        assert isinstance(f[0], str), f'expected string as first element of tuple, got {type(f[0])}'
        assert callable(f[1]), f'expected callable as second element of tuple, got {type(f[1])}'
        assert len(inspect.signature(f[1]).parameters) == len(variables), f'callable {f[1].__name__} expecting {len(inspect.signature(f[1]).parameters)} arguments, got {len(variables)}'
    for i in variables:
        assert isinstance(i, str), f'expected string, got {type(i)}'
    
    t = PrettyTable()
    t.field_names = variables + [f[0] for f in functions]
    
    for i in range(2**len(variables)):
        row = []
        vals = int_to_bin(i, len(variables))
        [row.append(j) for j in vals]
        for _, f in functions:
            row.append(int(f(*[bool(int(j)) for j in vals])))
        t.add_row(row)

    if html or csve:
        os.makedirs(out_dir, exist_ok=True)
    
    if html:
        html_name = html_name or table_name + '.html'
        with open('table.css', 'r') as f:
            css = f.read()
            
        with open(out_dir + html_name, 'w', encoding='utf-8') as f:
            f.write(f'''<!DOCTYPE html>
                        <html>
                        <head>
                        <style>{css}</style>
                        </head>
                        <body>''' 
                        + t.get_html_string() +
                        '''</body>
                        </html>''')
        print(f'Exported table to {out_dir + html_name}')
        
    if csve:
        csv_name = csv_name or table_name + '.csv'

        html_to_csv(t.get_html_string(), './tables/' + csv_name)
        print(f'Exported table to {csv_name}')
            
    return t

def implikation(a:bool, b:bool):
    """
    Compute the implication of two boolean values.

    Args:
        a (bool): The first boolean value.
        b (bool): The second boolean value.

    Returns:
        bool: The result of the implication.
    """
    return not a or b
