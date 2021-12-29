import collections
import math


def estimate_shannon_entropy(dna_sequece):
    m = len(dna_sequece)
    bases = collections.Counter([tmp_base for tmp_base in dna_sequece])

    shannon_entropy_value = 0
    for base in bases:
        n_i = bases[base]
        p_i = n_i / float(m)

        entropy_i = p_i * (math.log(p_i, 2))
        shannon_entropy_value += entropy_i

    return shannon_entropy_value * -1


print(estimate_shannon_entropy("ATCTAGGAC"))
