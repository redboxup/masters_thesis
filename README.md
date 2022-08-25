# Master thesis: Collective Olfactory search using Reinforcement learning
All files,programs and code backup for working on my master's thesis

## Introduction
In nature many organisms use their olfactory senses to detect odor or chemical substances. This helps them in navigating towards or away from the source, this is called chemotaxis. It is essentially motion in response to chemical concentration gradients. Some examples of such phenomena include, sex pheromone trail detection by Lepidotera family or swimming of E. coli bacteria up the concentration gradients of nutrients etc.

To make the model more closely resemble real life, we must also include turbulence in the fluid flow. This is because, turbulence can greatly distort the pheromone signal, therefore a naive search strategy based on sensing the concentration gradients may fail or will be sub-optimal. Thus, here we will introduce reinforcement learning to evolve good search strategies.


## Vicsek model 
Collective motion or flocking is a ubiquitous phenomenon, which is observed in many different living systems in wide variety of length scales. These are very interesting systems and non-trivial at the same time, because they occur far from equilibrium. We enter into the domain of non-equilibrium statistical mechanics wherein the agents are _active_, that is they continously dissipate energy to move or perform any mechanical work. Such systems are active areas of research, where researchers are trying to find underlying principles. One interesting phenomena is _spontaneous breaking of a continuous symmetry_. The Vicsek model is perhaps the simplest model for displaying this phase transistion in collective motion.

The model can be simply described by the mathematical equations

$$ \textbf{r}_i^{t + \Delta t} = \textbf{r}_i^{t} + \Delta tv_o \textbf{s}_i^{t+\Delta t}$$

$$ \theta_{i}^{t + \Delta t} = Arg (\sum_{j} n_{ij}^{t} s^t_j) + \eta \xi_i^t$$


![alt text](https://github.com/redboxup/masters_thesis/blob/main/vicsek_model/order_parameter_vs_radius_interaction.png)




## Reinforcement learning
Implemented an actor-crtic algorithm for a windy grid world, which is basically a simplified navigation problem

## First update
uploading rest of the relevant files too


##References


