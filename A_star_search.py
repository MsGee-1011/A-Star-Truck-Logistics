import heapq
import time


# 1. Map of Mahikeng local municipality 
# complete the graph

graph = {
    "Disaneng": ["Mahikeng", "Madibogo"],
    "Mahikeng": ["Disaneng", "Mmabatho", "Slurry", "Bakerville", "Madibogo"],
    "Madibogo": ["Disaneng", "Mahikeng", "Sannieshof"],
    "Mmabatho": ["Mahikeng", "Slurry"],
    "Slurry": ["Mahikeng", "Mmabatho", "Zeerust", "Groot Marico", "Bakerville"],
    "Zeerust": ["Slurry", "Groot Marico"],
    "Groot Marico": ["Slurry", "Zeerust"],
    "Bakerville": ["Mahikeng", "Slurry", "Lichtenburg"],
    "Lichtenburg": ["Bakerville", "Coligny"],
    "Coligny": ["Lichtenburg", "Ottosdal"],
    "Ottosdal": ["Coligny", "Sannieshof"],
    "Sannieshof": ["Ottosdal", "Delareyville", "Madibogo"],
    "Delareyville": ["Sannieshof"]
}


# 2. Distance between areas (km/h)

weights = {
    ("Disaneng", "Mahikeng"): 25,
    ("Disaneng", "Madibogo"): 35,
    ("Mahikeng", "Mmabatho"): 10,
    ("Mahikeng", "Slurry"): 20,
    ("Mahikeng", "Bakerville"): 35,
    ("Mahikeng", "Madibogo"): 30,
    ("Mmabatho", "Slurry"): 15,
    ("Slurry", "Zeerust"): 35,
    ("Slurry", "Groot Marico"): 40,
    ("Slurry", "Bakerville"): 25,
    ("Zeerust", "Groot Marico"): 20,
    ("Bakerville", "Lichtenburg"): 20,
    ("Lichtenburg", "Coligny"): 30,
    ("Coligny", "Ottosdal"): 35,
    ("Ottosdal", "Sannieshof"): 25,
    ("Sannieshof", "Delareyville"): 30,
    ("Madibogo", "Sannieshof"): 35
}


# 3. Heuristic to goal = Coligny
# add the heuristics here 
heuristic = {
    "Disaneng": 120,
    "Mahikeng": 100,
    "Madibogo": 90,
    "Mmabatho": 95,
    "Slurry": 80,
    "Zeerust": 70,
    "Groot Marico": 65,
    "Bakerville": 60,
    "Lichtenburg": 30,
    "Coligny": 0,
    "Ottosdal": 20,
    "Sannieshof": 40,
    "Delareyville": 50

}


# 4. Undirected edge cost

def get_cost(a, b, weights):
    if (a, b) in weights:
        return weights[(a, b)]
    elif (b, a) in weights:
        return weights[(b, a)]
    else:
        raise ValueError(f"No weight found between '{a}' and '{b}'")


# A* Search code

def astar(graph, weights, heuristic, start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start))

    came_from = {}
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0

    f_score = {node: float("inf") for node in graph}
    f_score[start] = heuristic[start]

    visited_order = []

    while open_set:
        _, current = heapq.heappop(open_set)

        if current not in visited_order:
            visited_order.append(current)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, visited_order, g_score[goal]

        for neighbor in graph[current]:
            cost = get_cost(current, neighbor, weights)
            tentative_g = g_score[current] + cost

            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, visited_order, float("inf")


# 6. Run

start = "Disaneng"
goal = "Coligny"

path, visited_order, total_cost = astar(graph, weights, heuristic, start, goal)

print("Optimal Path:", path)
print("Visited Order:", visited_order)
print("Total Cost:", total_cost)
