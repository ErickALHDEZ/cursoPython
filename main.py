from packages.mod_1 import func_1, func_2
import packages.mod_1
from packages.mod_2 import func_3, func_4

print(func_1())
print(func_2())

import packages
print(packages.URL)
print(packages.mod_1.func_1())