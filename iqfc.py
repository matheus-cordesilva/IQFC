import numpy as np
import pandas as pd

data = np.random.uniform(size=(50, 5))

df = pd.DataFrame(data=data)

print(df)
