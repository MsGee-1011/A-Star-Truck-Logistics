from A_star_search import astar, graph, heuristic, weights, simulate_path

# Define start and goal
start = "Disaneng"
goal = "Coligny"

# Run A*
path, visited_order, total_cost = astar(graph, start, goal)

# Print results
print("Optimal Path:", path)
print("Visited Order:", visited_order)
print("Total Cost:", total_cost)

# Run simulation
simulate_path(path, visited_order, total_cost)