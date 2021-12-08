# numpy.rfind() function

import numpy as np

a = np.array(["arfy", "slowy", "afdun"])

# counting a substring
print(np.char.rfind(a, "afdun"))

# counting a substring
print(np.char.rfind(a, "fo"))
