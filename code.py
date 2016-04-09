import pygame
from pygame.math import Vector2
import numpy as np
import random

class GameManager:
    def __init__(self, time_step, L, M_cart, M_bob, F):
    	pygame.init()
    	self.size = (500, 500)
    	self.screen = pygame.display.set_mode(self.size)

        self.colors = {'WHITE':(255,255,255), 'blue': (0,0,255), 'black': (0,0,0)}

        # Define the cart variables here
        self.t = time_step
        self.l = L
        self.m_cart = M_cart
        self.m_bob = M_bob
        self.g = 9.8
        self.cart = Vector2(0,0)
        
        #Learning parameters
        self.epsilon = 0.1 #Greedy 
        self.gamma = 0.8 #Discount factor
        self.Qvalues = {}
        self.actions = np.arange(-F,F, 10) #Amount of horizontal force
        
        
    def draw(self):
    	pygame.draw.rect(self.screen, self.colors['blue'], (self.cart.x, self.cart.y, self.cart.x+100, self.cart.y+100))

    # All the physics code will be added here
    def update(self):
        self.cart = self.cart + Vector2(1, 1)

    def run(self):
        self.screen.fill(self.colors['black'])

    	reward = self.update()

    	self.draw()

    	pygame.display.flip()
    
    def update_Qvalue(self, pstate, action, state, reward):
        max_qvalue = max([GameManager.get_Qvalue(self, state, a) for a in self.actions)])
        value = reward + self.gamma * max_qvalue
        old_qvalue = GameChanger.Qvalues.get(str(pstate), str(action), None)
        
        if old_qvalue = None:
            self.Qvalues[(str(pstate), str(action))] = reward
        else:
            self.Qvalues[(str(pstate), str(action))] = reward + self.gamma * (max_qvalue - old_value)
    
    def choose_actions(self):
        if random.random() <= self.epsilon:
            return self.actions[np.random.choice(len(self.actions))]
        else:
            q = [GameManager.get_Qvalue(self, state, a) for a in self.actions]
            maxQ = max(q)                
            count = q.count(maxQ)
        
        if count > 1:
            best = [i for i in range(len(self.actions)) if q[i] == maxQ]
            i = best[np.random.choice(len(best))]
        else:
            i = q.index(maxQ)

        action = self.actions[i]
        return action
            
    def get_Qvalue(self, state, action):
        return self.Qvalues.get(str(state), str(action), 0.0)
         
def main():
    gm = GameManager()

    for i in range(10000):
        gm.run()

if __name__ == "__main__":
    main()
