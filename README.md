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

### Some Results
<p align = "center">
  <img src="https://github.com/redboxup/masters_thesis/blob/main/vicsek_model/order_parameter_vs_radius_interaction.png" />
  <img src="https://github.com/redboxup/masters_thesis/blob/main/vicsek_model/order_parameter_vs_noise.png" />
  <img src="https://github.com/redboxup/masters_thesis/blob/main/vicsek_model/order_parameter_vs_density.png" />
</p>



## Reinforcement learning
At the core of the project we want to study the decision making processes of individual agents to achieve certain goal. Our aim is to understand the general laws that these agents might be obeying to exhibit collective behaviour and to search for nutrient source in a turbulent environment.

We started by breaking down this problem into smaller problems to try and build a toy-model, which will be generalised later, to experiment with using some algorithms. Our goal is to probe, collective search in a turbulent flow. So we first devised a simple navigation problem, the agent neads to reach a terminal state from a starting state while it is being advected by underlying fluid flow. We were succesful in implementing a toy-model for the environment to test and caliberate an actor-critic algorithm for reinforcement learning. 

Second step, is to remove a terminal state and introduce chemotaxis. This was done by simply including a concentration field, and agent needs to "navigate and search" for the highest value of the concentration, which would be the source of the concentration. In the simple case, the concentration field would not be advected by underlying fluid flow, but in more complicated case, the field would be advected by fluid flow. Turbulent fluid flow would be introduced at the last stage.

Since a lot of the work is still being done and I might revise it in the future, I have not included it on the repository. This readme file is just so that it can give a flavour of what I am working on for the past couple of months (and will be working for good chunk of this year too).

## References


