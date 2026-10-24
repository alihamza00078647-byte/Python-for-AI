import pandas as pd
"""
** Interpolation is advance method compare to fillna() where we fill hardcoded or mean() vaule **
Types -> linear, polynomial, time --> *Check more*

1. __Advantages of Interpolation__
(i).    preserve data Integrity
(ii).   smooth Trends
(iii).  Avoid Data Loss

2. __Disadvantages of Interpolation__
(i). Can't Work with String values like (Name, ids)
"""
# Linear interpolation
# y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)

# Polynomial Interpolation
# P(x) = a₀ + a₁x + a₂x² + a₃x³ + ...

# Spline Interpolation
# S(x) = aᵢ + bᵢ(x-xᵢ) + cᵢ(x-xᵢ)² + dᵢ(x-xᵢ)³

# Time Interpolation
# y = y1 + (t - t1) / (t2 - t1) * (y2 - y1)

"""
import pandas as pd
import numpy as np

s = pd.Series([10, np.nan, np.nan, 40, np.nan, 60])

# 1. Linear (default) — seedhi line
s.interpolate(method='linear')
# [10, 20, 30, 40, 50, 60]  ← equal steps

# 2. Polynomial — curve fit
s.interpolate(method='polynomial', order=2)
# order = polynomial ki degree

# 3. Spline — smooth cubic curves
s.interpolate(method='spline', order=3)

# 4. Time — actual timestamps ke saath
s.index = pd.to_datetime(['2024-01', '2024-03', '2024-06',
                           '2024-07', '2024-09', '2024-12'])
s.interpolate(method='time')
# Gaps ke according weighted interpolation
"""


data = {
    "time" : [1, 2, 3, 4, 5],
    "value" : [10, None, 30, None, 50]
}

df = pd.DataFrame(data)
# interpolation(method, axis=0, )
df["value"] = df.interpolate(method="linear", axis=0)


