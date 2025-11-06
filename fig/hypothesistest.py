# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,md:myst,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
# ---

# %%
# # Plots for Evaluation and Hypothesis Testing
#
# This script creates plot for the slides for one of the talks.
# It is made available as examples and as a source of ideas, to
# to showcase the constructions I use.

import numpy as np
import matplotlib.pyplot as plt

# %%
# We use `numpy` and `pyplot` as usual.
# We also need the statistics package from `scipy`, but only
# the binomial distribution, which is called `binom`.

from scipy.stats import binom

# %%
# ## One experiment 
# 
# Imagine that we make one experiment to test a classification model.
# In the experiment, we make a number of trials, say $n=50$, and
# for each trial we record either an error or a correct prediction.
# The result of the experiment is the number $X$ of observed errors.
#
# Since the experiment depends on random events, $X$ is a stochastic
# (that is random) variable.
# we want to understand how this variable is distributed under different
# True error rates $p_e$.
#
# We assume a particular error rate, say $p_e=0.1$, and try to model
# probability distribution of the 


# Define the data
n = 100
pe = 0.1
sig = 0.05

def mkplot1(n,pe,sig=0.05,colour="blue"):
   dist = binom(n,pe)

   m = int(n*pe*2)
   x = list(range(m))
   y = dist.pmf(x)

   plt.xlabel('Feiltal')
   plt.ylabel('Sannsyn')

   plt.xticks(range(0,m+1))
   plt.plot(x, y, color=colour, label=f'$n={n}$')

mkplot1( 50, 0.1 )
plt.savefig( "hyp0.svg" )
plt.figure()

# %%
# ## Hypothesis testing

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

plt.xlabel('Feilrate')
plt.ylabel('PDF')
plt.grid(True)

mkplot( 100, 0.1, 0.05 )
plt.legend()
plt.savefig( "hyp1.svg" )

mkplot( 1000, 0.1, 0.05, colour="red" )
mkplot( 10000, 0.1, 0.05, colour="green" )
plt.legend()
plt.savefig( "hyp2.svg" )
