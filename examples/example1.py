from truth_table_generator import generate_table

f = lambda a, b, c: not(a) or (b and c)

t = generate_table(['a', 'b', 'c'], [('¬a(b ∧ c)', f)], table_name='table1', out_dir='./myTables/')