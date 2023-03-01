import pandas
from tabulate import tabulate

keys = ('rsid', 'chromosome', 'position', 'genotype')

df = pandas.read_csv('137.23andme.58', sep='\t', dtype={'chromosome':str}, skiprows=15, names=keys)

eye_color_chr = ('rs12913832', 'rs1800407', 'rs12896399', 'rs16891982', 'rs1393350', 'rs12203592')
trombose_chr = ('rs6025', 'i3002432', 'rs8176719', 'rs2066865', 'rs2036914')  # i3002432 is for rs1799963
hiv_chr = 'i3003626'  # II normal, DD best
alcoholism_chr = 'rs1799971'  # AA normal, GG worst
milk_chr = 'rs4988235'  # TT best, CC worst

print('\nChromosomes for eye color \n')
print(tabulate(df[df.rsid.isin(eye_color_chr)], keys, showindex=False))
print('\nChromosomes for thrombosis risk\n')
print(tabulate(df[df.rsid.isin(trombose_chr)], keys, showindex=False))
print('\nPopular chromosomes \n')
print(tabulate(df[df.rsid == hiv_chr], tablefmt='plain', showindex=False))
print(tabulate(df[df.rsid == alcoholism_chr], tablefmt='plain', showindex=False))
print(tabulate(df[df.rsid == milk_chr], tablefmt='plain', showindex=False))
