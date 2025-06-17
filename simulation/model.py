import numpy as np
import networkx as nx

def create_network(num_agents, edge_probability, seed):
    """
    Create a random network of agents.
    
    Parameters:
     - num_agents: int, number of agents in the network
     - edge_probability: float, probability of edge creation between agents
     - seed: int, random seed for reproducibility
    
    Returns:
     - G: networkx.Graph, the generated random graph
     - adj_matrix: np.ndarray, adjacency matrix of the graph
    """
    G = nx.erdos_renyi_graph(num_agents, edge_probability, seed)

    adj_matrix = nx.to_numpy_array(G)
    sum_rows = adj_matrix.sum(axis = 1, keepdims = True)
    sum_rows[sum_rows == 0] = 1 # prevent division by 0
    adj_matrix = adj_matrix / sum_rows # weighted average 

    return G, adj_matrix

def run_simulation(num_agents, num_timesteps, beliefs_initial, adj_matrix, G):
    """
    Simulate the fracture process over a number of timesteps.
    
    Parameters:
     - num_agents: int, number of agents
     - num_timesteps: int, number of timesteps to simulate
     - beliefs_initial: np.ndarray, initial beliefs of agents
     - adj_matrix: np.ndarray, adjacency matrix of the network
     - G: networkx.Graph, the network of agents
    
    Returns:
     - beliefs_over_time: np.ndarray, beliefs of agents over time
    """
    beliefs_over_time = [beliefs_initial.copy()]
    beliefs_current = beliefs_initial.copy()

    for _ in range(num_timesteps):
        # to prevent disconnected nodes from being updated 
        beliefs_new = np.zeros(num_agents)

        for agent in range(num_agents):
            if G.degree[agent] == 0:
                beliefs_new[agent] = beliefs_current[agent]
            else:
                beliefs_new[agent] = adj_matrix[agent] @ beliefs_current
    
        beliefs_over_time.append(beliefs_new.copy())
        beliefs_current = beliefs_new
    
    return np.array(beliefs_over_time)