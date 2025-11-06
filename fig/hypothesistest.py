import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import binom

# Define the data
n = 100
m = int(n/5)
x0 = list(range(m))
y = binom.pmf(x0,n,0.05)
x = np.array(x0)/n

# Create the plot
plt.plot(x, y, color='blue', label='$f(x)$')

# Fill the area under the curve
# y2 defaults to 0 if not specified, filling down to the x-axis
# plt.fill_between(x, y, color='lightblue', alpha=0.5) 

# Add labels and title
plt.xlabel('Feilsannsyn')
plt.ylabel('PDF')
# plt.title('Area Under a Curve')
# plt.legend()
plt.grid(True)
plt.savefig( "hyp1.svg" )
