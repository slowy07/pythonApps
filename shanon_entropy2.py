import collections
import math


def estimate_shannon_entropy(dna_sequence):
    m = len(dna_sequence)
    bases = collections.Counter([tmp_base for tmp_base in dna_sequence])

    shannon_entropy_value = 0
    for base in bases:
        n_i = bases[base]
        p_i = n_i / float(m)
        entropy_i = p_i * (math.log(p_i, 2))

        shannon_entropy_value += entropy_i

    return shannon_entropy_value * -1


print(estimate_shannon_entropy("ENTRYPSHNNON"))
