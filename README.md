# truth-table-generator
Generate truth tables in html
## Usage
- Clone the repository
- Install the dependencies using the command:

 ```bash
 pip -r requirements.txt
 ```

- Use the `generate_table` function in your own code.
<details>
  <summary>generate_table</summary>

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

</details>

## Examples

#### Example 1
```python
from truth_table_generator import generate_table

f = lambda a, b, c: not(a) or (b and c)

t = generate_table(['a', 'b', 'c'], [('¬a(b ∧ c)', f)], table_name='table1', out_dir='./myTables/')
```
#### Output

<table>
    <tr>
        <th>a</th>
        <th>b</th>
        <th>c</th>
        <th>¬a(b ∧ c)</th>
    </tr>
    <tr>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
    </tr>
    <tr>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
    </tr>
</table>

<details>
  <summary>Image</summary>
<img src="https://github.com/vyper0016/truth-table-generator/assets/81050283/ce17f863-e805-4376-b4a5-70a7b0e05954" alt="table1">
</details>

---

#### Example 2

```python
from truth_table_generator import generate_table

o0 = lambda s1, s0, D: not(s1) and not(s0) and D
o1 = lambda s1, s0, D: not(s1) and s0 and D
o2 = lambda s1, s0, D: s1 and not(s0) and D
o3 = lambda s1, s0, D: s1 and s0 and D

t = generate_table(['S1', 'S0', 'D'], [('O0', o0), ('O1', o1), ('O2', o2), ('O3', o3)], 'table2', './myTables/')

```

#### Output

<table>
    <tr>
        <th>S1</th>
        <th>S0</th>
        <th>D</th>
        <th>O0</th>
        <th>O1</th>
        <th>O2</th>
        <th>O3</th>
    </tr>
    <tr>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
    </tr>
</table>

<details>
  <summary>Image</summary>
<img src="https://github.com/vyper0016/truth-table-generator/assets/81050283/f50d092b-f2c0-4633-b7fd-7811cfe93e9e" alt="table2">
</details>