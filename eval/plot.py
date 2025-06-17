import matplotlib.pyplot as plt
import networkx as nx


def plot_belief_drift(num_agents, beliefs_over_time, misalignment_threshold = 0.7, title = "Belief Drift Over Time"):
  """
  Plot the belief values of each agent over time.

  Parameters: 
   - beliefs_over_time: np.array of shape (num_timesteps, num_agents)
   - misalignment_threshold: float, threshold for misalignment
    - title: str, title of plot
  """
  plt.figure(figsize = (10, 6))
  
  for agent in range(num_agents):
    plt.plot(beliefs_over_time[:, agent], label = f'Agent {agent}')

  plt.xlabel('Timestep')
  plt.ylabel('Belief Alignment')
  plt.axhline(misalignment_threshold, color="pink", label = "Misalignment Threshold")
  plt.legend()
  plt.title(title)
  plt.show()


def visualize_graph(G, beliefs_current, threshold=0.7, title="Agent Influence Graph"):
    """
    Visualize agent network with node colors based on belief alignment.
    
    Parameters:
    - G: networkx Graph
    - beliefs: list or array of belief values at current timestep
    - threshold: alignment cutoff
    """
    pos = nx.spring_layout(G, seed=15)

    # color nodes based on belief
    node_colors = []
    for belief in beliefs_current:
        if belief < threshold:
            node_colors.append("pink")  # misaligned
        else:
            node_colors.append("lightblue")  # aligned

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color = node_colors, node_size=800)
    plt.title(title)
    plt.axis("off")
    plt.show()
