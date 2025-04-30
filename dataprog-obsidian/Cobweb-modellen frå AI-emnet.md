---
title: Game Theory
categories: session
---

# Reading

+ Cursory: [Dawid and Kopel 1998](https://link.springer.com/article/10.1007/s001910050066)
    - This is the simulation we will be working with, but it is not 
      necessary to read all the details of economics
+ R&N Chapter 6 on Game Theory
+ *Most importantly* review Genetic Algorithms and make sure that you
  can run and tune the solver to solve different optimisation problems


# Part 1.  Economic Simulation

## Briefing

- the population models a real population
    - we are interested in the behaviour of the population as a whole,
      not just one individual, optimal behaviour
    - related to agent-based simulation; we simulate a population of agents.
- payoff depends on all player strategies
    - as opposed to an externally given and static function
    - hence it is impossible to simulate a single agent; only a population
      makes sense
- goal: find equilibrium 
    - possibly with different co-existing solutions
- e.g. the cobweb model

## Cobweb Model

- famous market model
- $n$ companies produce the same good
- company $i$ can choose the quantity $q_{i,t}$ to produce
  in period $t$
- companies do not know the price $p_t$ when they decide $q_{i,t}$
- the price $p_t$ is determined as a function $p_t(q_t)$
  of the total production $q_t=\sum_i q_{i,t}$
- under some (but not any) conditions there is a unique, analytic equilibrium

## Exercise

+ Use the [demo at github](https://github.com/hgeorgsch/pygax/tree/main/Simulation)
+ [GASim.py](https://github.com/hgeorgsch/pygax/blob/main/Simulation/GASim.py)
  implements the CobWeb model according to
  [Dawid and Kopel 1998](https://link.springer.com/article/10.1007/s001910050066)
+ The `CobWeb` class is instantiated with Dawid and Kopel's parameters,
  $a$, $\alpha$, $\beta$, and $\gamma$
+ An analytic equilibrium exists if 
  $$\alpha < \frac{a^2\beta}{(2\beta+\gamma)^2}$$

### Your task

1. Review the code.  
    + How does the simulation work?
    + What differs from the regular GA optimisation?
2. There are a few new python features which may want to have a look at.
    + Command line arguments.  
      How are they parsed?  Why are they used?  What would be the alternative
      to using command line arguments?
    + Plotting.
      How do you plot data in python?
      How can you visualise performance data for algorithms and systems that
      you develop?
3. Run the experiment and produce the plots
    + What dos the plot tell you?
4. Dawid and Kopek report on two experiments, with $\alpha=0.25$ and
   $\alpha=1$, only the former has an analytic equilibrium.
    - Do the simulations behave differently?
5. The payoff is discontinuous at $q=0$, and such a point may have 
   particular interest.  Yet, as a random chromosome, it is no more
   probable than any other.
   Dawid and Kopek suggest modifying the encoding, adding an extra bit
   $b$ interpreted as follows 
    - if $b=0$, then $q=0$ regardless of the other bits.
    - if $b=1$, then $q$ is defined by the remaining bits as usual

   Implement this representation and check if it changes the behaviour
   of the population.  Reflect on your observations.  Are there other
   problems where a similar approach could be useful?


### Bonus Exercise

A different economic model, of land auctions, has been
simulated by 
[Balmann and Happe 2001](https://ir.library.oregonstate.edu/concern/conference_proceedings_or_journals/f4752h50s).

Can you replicate their experiment, using the demo code as a 
starting point?

# Part II. Simulating Games

## Midway brief.

### Game Theory

> What is a game?

+ Recall intelligent agents in adversarial games
    - minimax algorithm

> When is the minimax algorithm appropriate?

+ Other games may require different solutions
    - infinite games - who can survive indefinitely?
    - simultaneous moves
+ Repeating the game changes the dynamics
    - Particularly if the game is not zero-sum; e.g. Prisoner's Dilemma
    - Trust and Reputation (Psychology of Games)

> Monte Carlo simulation

### Simulation using Genetic Algorithms 

+ Survival of the fittest
    - bad strategies are killed off
    - good strategies are copied
+ Chromosomes can represent game strategies or move sequences
    - GA provides an alternative to the minimax algorithm
    - GA can also explore games where minimax is not appropriate

> What selection rules should be used?

+ Several scenarioes
    - optimisation
    - tournament selection playing a game
+ Many things can be optimised by GA
    - Action sequences 
    - Neural networks
    - Functions (e.g. inverse functions)


## The Centipede Game

**Source** [Investopedia](https://www.investopedia.com/terms/g/gametheory.asp)

> The [centipede game](https://www.investopedia.com/terms/c/centipede-game.asp)
 is an extensive-form game in game theory in which two players alternately get a chance to take the larger share of a slowly increasing money stash. It is arranged so that if a player passes the stash to their opponent who then takes the stash, the player receives a smaller amount than if they had taken the pot.

> The centipede game concludes as soon as a player takes the stash, with that player getting the larger portion and the other player getting the smaller portion. The game has a pre-defined total number of rounds, which are known to each player in advance.


(This game is also asymmetric. There is a difference between moving first
and moving last, even if the roles are otherwise equal.)

## Exercises

Implement the following version of the centipede game.

1.  Two players play, taking turns.
2.  The lot starts at zero and increases by £2 per turn.
3.  The player on turn can choose *take* or *pass*.
    - if he tskes, the players take half the lot each, and the player on turn
      gets £2 extra.
    - if he passes, the other player is on turn
4.  The game continuous for 128 turns.
5.  If the last player passes, they share the lot of £256.

The number of rounds passed constitutes a player strategy.

In this game, the payoff (cost) only makes sense when two players
are played against each other.  Thus, to evaluate the cost function,
the chromosomes must be paired and the game played.

Note that the players want to maximise their payoff,
not (primarily) beat the opponent.
Hence tournament selection based on playing
the game is hardly appropriate.

**Question**

1.  What is intuitively the optimal strategy?
1.  What is the analytically optimal strategy?  
    Is this different from your intuition?
    - What solution would the minimax algorithm find?
1.  What would be the optimal strategy in tournament selection?
1.  Design a GA simulation of the game.

## The Aberdeen Exercise

This game is asymmetric.  
One player is an incumbant firm and the other is a new entrant.
The incumbant firm is active in a market and has a steady income
therefrom.

The new entrant moves first, choosing whether or not to enter the
market.
The incumbant firm (the responder) can choose either to fight or
accept.
If they accepts, the two players share the profit from the market.
If they fight, they lose money by outbidding the new entrant, but
by virtue of superior capital they can bar the entrant who would
lose even more.
The payoff matrix could look like this, with payoff
given for new entrant/incumbant firm.

| | Accept | Fight |
| :- | :- | :- |
| abstain | 0/25 | 0/25 |
| enter  | 10/10 | -5/-2½ |

Regular minimax optimisation leads to the equilibrium of
enter/accept.  However, in practice, there are many markets
where we observe a fight strategy.  The rationale for this is
that if the incumbant firm can create an expectation that they
will fight, nobody dares enter, and they get their status quo
payoff as 25, which is optimal.

This behaviour only makes sense in a repeated game, where 
expectations can be built over time.

*Can you make a GA simulation of this game?* 
