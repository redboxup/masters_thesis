#module for importing all the important functions


import numpy as np
import pandas as pd
from windy_gridworld_hor import *

#initialising the environment
env = WindyGridworldEnv()

#policy neural network

#let us define a function that will return z(s,a) matrices
def z(state,action):
  z_ = np.zeros([70,4])
  z_[state][action] = 1
  return z_

#let us now define the h function
def h(s_i,a_j,q):
  z_ = z(s_i,a_j)
  h_ = q[a_j][s_i]*z_[s_i][a_j]
  return h_

#now let us define the policy function
def policy(state,q):
  sum = 0
  p = []
  for j in range(4):
    sum += np.exp(h(state,j,q))
  #now probability corresponding to the action
  for j in range(4):
    p_ = np.exp(h(state,j,q))/sum
    p.append(p_)
  return p

#code to sample an action from given probability distribution
def sample_action(state,q):
  prob_action = policy(state,q)
  action = np.random.choice(np.arange(4),p = prob_action)
  return action
#convert state into is feature vector
def y(s):
  s_v = np.zeros(70)
  s_v[s] = 1
  return s_v  
  
  
#state-value function linear approximation
def v(w,s):
  s_v = y(s)
  return np.dot(w.T,s_v)

#gradient of state-value function
def grad_v(w,s):
  s_v = y(s)
  return s_v
  




#loop forever(for each episode)
def run_episode(q,w,alpha,gamma):
  #first state will be
  state = env.reset()
  is_done = False 
  I = 1
  #loop while S is not terminal for each time step
  no_step = 0
  total_reward = 0
  while is_done == False:
    #sample an action using the policy
    action = sample_action(state,q)
    #take the action A, observe S', R
    new_state, reward, is_done, _ = env.step(action)
    if is_done == True:
      delta = reward + gamma*0 -v(w,state)
    else:
      delta = reward + gamma*v(w,new_state) -v(w,state)
    #defining some important parameters
    r_exp = reward + v(w,new_state)
    beta = r_exp - v(w,state)
    #now we will update the weight parameters
    #using adam-algorithm we will write the standard stochastic gradient descent as
    z_times_policy = 0
    prob_action = policy(state,q)
    for i in range(4):
      z_times_policy += prob_action[i]*z(state,i)
    z_ = z(state,action)
    z_times_policy = z_times_policy.transpose()
    z_ = z_.transpose()
    q += alpha*beta*(z_-z_times_policy)
    w += alpha*beta*y(state)
    no_step += 1
    total_reward += reward
    #print(state,action,reward,no_step)
    state = new_state
  return no_step,total_reward



#to run an episode but not update its values
def run_episode_dont_update(q,w):
  state = env.reset()
  is_done = False
  #loop while S is not terminal for each time step
  no_step = 0
  total_reward = 0
  while is_done == False:
    action = sample_action(state,q)
    new_state, reward, is_done, _ = env.step(action)
    no_step += 1
    total_reward += reward
    state = new_state
  return no_step,total_reward














