import sys
import pandas as pd
from chemistryfuncs import molar_mass_calc, round_half_up

#Args (1st arg is chemical formula, 2nd arg is sig fig for amu)
formula = sys.argv[1]
decimals = 2

element_data = pd.read_csv("data/elements.csv", usecols=['Symbol', 'AtomicMass'])

symbol_list = element_data['Symbol']
atomic_mass_list = element_data['AtomicMass']

element_dict = {symbol_list[i]: round_half_up(float(atomic_mass_list[i]), decimals=decimals) for i in range(len(symbol_list))}

print(molar_mass_calc(formula, element_dict))