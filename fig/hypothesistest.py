import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import binom

# Define the data
n = 100
pe = 0.1
sig = 0.05

def mkplot(n,pe,sig,colour="blue"):
   dist = binom(n,pe)

   m = int(n*pe*2)
   x0 = list(range(m))
   y0 = dist.pmf(x0)
   y = y0*n
   x = np.array(x0)/n

   c0 = dist.ppf(sig)
   p0 = dist.ppf(sig)/n
   c1 = round(c0+1)
   print( c0, p0 )

   plt.plot(x, y, color=colour, label=f'$n={n}$')

   plt.fill_between(x[:c1], y[:c1], color=colour, alpha=0.15) 

plt.xlabel('Feilsannsyn')
plt.ylabel('PDF')
plt.grid(True)

mkplot( 100, 0.1, 0.05 )
plt.legend()
plt.savefig( "hyp1.svg" )

mkplot( 1000, 0.1, 0.05, colour="red" )
mkplot( 10000, 0.1, 0.05, colour="green" )
plt.legend()
plt.savefig( "hyp2.svg" )
