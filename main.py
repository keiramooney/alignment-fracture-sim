from agents.agents import create_initial_beliefs
from simulation.model import create_network, run_simulation
from eval.plot import plot_belief_drift, visualize_graph

# config 
num_agents = 10
num_timesteps = 10
aligned_value = 0.9
misaligned_value = 0.2
misaligned_index = 0
misalignment_threshold = 0.7
edge_probability = 0.1 
seed = 15

# setup
beliefs_initial = create_initial_beliefs(num_agents, aligned_value, misaligned_index, misaligned_value)
G, adj_matrix = create_network(num_agents, edge_probability, seed)

# simulate 
beliefs_over_time = run_simulation(num_agents, num_timesteps, beliefs_initial, adj_matrix, G)

# visualize results
plot_belief_drift(beliefs_over_time, misalignment_threshold)
visualize_graph(G, beliefs_initial, title="Initial Belief State")
visualize_graph(G, beliefs_over_time[-1], title="Belief State at Final Timestep")
