# This is wrong when exported to kappa
prot(name='lacZ', loc='cyt', dna=None, met=None, prot=None, rna=None, up=None, dw=1) %
prot(name='lacZ', loc='cyt', dna=None, met=None, prot=None, rna=None, up=1, dw=None) +
prot(name='lacZ', loc='cyt', dna=None, met=None, prot=None, rna=None, up=None, dw=1) %
prot(name='lacZ', loc='cyt', dna=None, met=None, prot=None, rna=None, up=1, dw=None)

# This is correct when exported to kappa
prot(name='lacZ', loc='cyt', dna=None, met=None, prot=None, rna=None, up=None, dw=1) %
prot(name='lacZ', loc='cyt', dna=None, met=None, prot=None, rna=None, up=1, dw=None) +
prot(name='lacZ', loc='cyt', dna=None, met=None, prot=None, rna=None, up=None, dw=2) %
prot(name='lacZ', loc='cyt', dna=None, met=None, prot=None, rna=None, up=2, dw=None)
