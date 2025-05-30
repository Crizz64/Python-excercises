import pandas as pd

s=pd.Series(['Matematicas', 'Historia', 'Economia', 'Programación', 'Ingles'] dtype= 'string')
print(s)


#
import pandas as pd
s=pd.Series({'Matematicas': 6.0, 'Economia': 4.5, 'Progrmación': 8.5})
print(s)

import pandas as pd
s =pd.Series([1,2,2,3,3,3,4,4,4,4])
print(s.size)
print(s.index)
print(s.dtype)

print(s[0])


import pandas as pd
s=pd.Series({'Matematicas': 6.0, 'Economia': 4.5, 'Progrmación': 8.5})
print(s['Economia'])
print(s['Economia', 'Matematicas'])


import pandas as pd
s =pd.Series([1,2,2,3,3,3,4,4,4,4])
print(s.sum())
print(s.count())
print(s.cumsum())
print(s.value_count())
print(s.min())
print(s.max())
print(s.mean())
print(s.var())
print(s.std())
print(s.describe())


import pandas as pd
s=pd.Series({'Matematicas': 6.0, 'Economia': 4.5, 'Progrmación': 8.5})
print(s[s > 5])



import pandas as pd
s = pd.Series({'Matematicas': 6.0, 'Economia': 4.5, 'Progrmación': 8.5})
print(s.sort_values(ascending=True))
print(s.sort_index(ascending=False))


import pandas as pd
s = pd.Series({'lunes': 28, 'martes': 27, 'miercoles': 32, 'Jueves': 21, 'viernes': 25, 'sabado': 30, 'domingo': 24 })
print("La temperatura del miercoles es")
print(s[2])

print("la temperatura de promedio de la semana fue de")
print(s.mean())
print(s[s > 22])
print(s.drop('lunes')) 