# numpy.count() function

import numpy as np

a = np.array(["arfy", "slowy", "sayutod"])

# counting a substring
print(np.char.count(a, "sayutod"))

# counting a substring
print(np.char.count(a, "fo"))
