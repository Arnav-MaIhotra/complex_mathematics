# complex_mathematics

---

**complex_mathematics is a Python module that can be used for many complex math related problems, with concepts from many different topics in mathematics, such as calculus, linear algebra, geometry, algebra, and more. It also has machine learning algorithms such as linear regression and K-Nearest-Neighbors.**

---

**To get started:**

---

Linear Algebra:

`from complex_mathematics.linalg import CLASS_NAME`

Eigenvectors:

```

from complex_mathematics.linalg import eigenvector
import numpy as np

mat = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])

eig = eigenvector(mat)

print(eig.eigenvalues)
print(eig.eigenvectors)

```

---

Machine Learning:

`from complex_mathematics.ml import CLASS_NAME`

Linear Regression (Stochastic gradient descent):

```

import numpy as np
import random
from complex_mathematics.ml import LinearRegression
    

X = np.array([[i] for i in range(-50, 51)])
y = np.array([2*i + 1 + random.uniform(-1, 1) for i in range(-50, 51)])

model = LinearRegression()

model.fit(X, y, True)

print(model.predict(10))

```

---

This module utilizes an MIT license so that it can be freely distributed with no restrictions
