from truth_table_generator import generate_table

o0 = lambda s1, s0, D: not(s1) and not(s0) and D
o1 = lambda s1, s0, D: not(s1) and s0 and D
o2 = lambda s1, s0, D: s1 and not(s0) and D
o3 = lambda s1, s0, D: s1 and s0 and D

t = generate_table(['S1', 'S0', 'D'], [('O0', o0), ('O1', o1), ('O2', o2), ('O3', o3)], 'table2', './myTables/')
