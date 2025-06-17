# Dev Notes

## Notes for 6/16/25
### Simulation setup
- network type: Erdos-Renyi graph
- edge probability: used between 0.1-0.5
- seed = 15
- 10 agents, aligned value = 0.9, misaligned value 0.1-0.2
- disconected notes excluded from belief updates (so their beliefs stay the same throughout)
- belief update rule: uniform avg of neighbors' beliefs (if connected)
- misalignment threshold = 0.7

### Observations
- misalignment spreads through sparse graphs depending on local connections
- some connected agents tend to trend toward misalignment if next to misaligned node
- disconnected nodes behave correctly (had to update code to account for this)
- when p is very low (0.1), misalignment spread is inconsistent and very topology-dependent
- when p is higher (0.4), belief convergence tends to dominate. misalignment is suppressed 

### Ideas to explore
- add stubbornness parameter: agents weigh their own individaul belief vs their neighbors'
- try diff graph types (barabasi-albert, watts-strogatz)
- multi-dimensional belief states?
- add noise/perturbations to belief updates
- track and plot
    - stdev of beliefs over time
    - num of agents below threshold each timestep
    - clusters of misalignent
- animation of belief evolution?
- log key metrics per run (like % misaligned)

### To do
- create metrics file to track mean/stdev over time
- support diff network types
- clean up main.py cli/config structure
- add command-line args for p, seed, misalignment threshold? 

