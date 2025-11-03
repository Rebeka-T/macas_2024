# Uzraksti programmu, kurā  dators izvēlas 100 skaitļus 
# robežās no 101 līdz 500. Izvēlētie skaitļi tiek izvadīti terminālī.

import random

for _ in range(100):
    print(random.randint(101,501), end="  ")
