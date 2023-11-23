from prettytable import PrettyTable
import inspect
from html_table_csv import html_to_csv
# USAGE:
# generate_table(list of variables, list of tuples of (name, function))
    
def int_to_bin(x:int, n:int):
    s = '{0:b}'.format(x)
    s = '0'*(n-len(s)) + s
    return s

# [variable names], [(name, function)]
def generate_table(variables: list, functions: list, table_name:str = 'table', html: bool = True, html_name: str = None, csve: bool = True, csv_name = None):
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

    
    if html:
        html_name = html_name or table_name + '.html'
        with open('./tables/' + html_name, 'w', encoding='utf-8') as f:
            f.write('''<!DOCTYPE html>
                        <html>
                        <head>
                        <link rel="stylesheet" href="table.css">
                        </head>
                        <body>''' 
                        + t.get_html_string() +
                        '''</body>
                        </html>''')
        print(f'Exported table to {html_name}')
        
    
    if csve:
        csv_name = csv_name or table_name + '.csv'

        html_to_csv(t.get_html_string(), './tables/' + csv_name)
        print(f'Exported table to {csv_name}')
            
    return t

def implikation(a:bool, b:bool):
    return not a or b
