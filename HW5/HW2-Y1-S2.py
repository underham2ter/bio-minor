import pandas

df_o = pandas.read_csv('Files/ressimple_somatic_mutation.open.COCA-CN.tsv.gz', sep='\t', usecols=['icgc_donor_id', 'gene_affected'])

id = "DO229010"

KRAS = "ENSG00000133703"
TP53 = "ENSG00000141510"
SMAD4 = "ENSG00000141646"
CDKN2A = "ENSG00000147889"
ARID1A = "ENSG00000117713"

patients = list(set(df_o.icgc_donor_id.values))
# print(patients)

# for p in patients:
#
#     df = df_o[df_o.icgc_donor_id == p]
#     n_kras = len(df[df.gene_affected == KRAS])
#     n_tp53 = len(df[df.gene_affected == TP53])
#     if n_tp53 > 0 and n_kras > 0:
#         print(p)
#         print("Mutations in KRAS gene: %s" % n_kras)
#         print("Mutations in TP53 gene: %s" % n_tp53)
#         print("Mutations in SMAD4 gene: %s" % len(df[df.gene_affected == SMAD4]))
#         print("Mutations in CDKN2A gene: %s" % len(df[df.gene_affected == CDKN2A]))
#         print("Mutations in ARID1A gene: %s" % len(df[df.gene_affected == ARID1A]))
#     else:
#         continue

df = df_o[df_o.icgc_donor_id == id]
n_kras = len(df[df.gene_affected == KRAS])
n_tp53 = len(df[df.gene_affected == TP53])

print("Mutations in KRAS gene: %s" % n_kras)
print("Mutations in TP53 gene: %s" % n_tp53)
print("Mutations in SMAD4 gene: %s" % len(df[df.gene_affected == SMAD4]))
print("Mutations in CDKN2A gene: %s" % len(df[df.gene_affected == CDKN2A]))
print("Mutations in ARID1A gene: %s" % len(df[df.gene_affected == ARID1A]))