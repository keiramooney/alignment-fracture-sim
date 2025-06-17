import numpy as np
import networkx as nx

def create_initial_beliefs(num_agents, aligned_value, misaligned_index, misaligned_value):
    """"
    Create initial beliefs for a set of agents.
    
    Parameters:
     - num_agents: int, number of agents
     - aligned_value: float, value for aligned agents
     - misaligned_index: int, index of the misaligned agent
     - misaligned_value: float, value for the misaligned agent
    
    Returns:
     - beliefs: np.ndarray, initial beliefs of agents
    """
    beliefs = np.ones(num_agents) * aligned_value
    beliefs[misaligned_index] = misaligned_value
    return beliefs
