# A-Star-Truck-Logistics
A Python implementation of the A* Search algorithm for truck logistics route optimization, finding the most efficient path from Disaneng to Coligny with cost calculation and route simulation.
Algorithm Explanation

The A* Search algorithm combines:

g(n): Actual cost from the start node
h(n): Heuristic estimate to the goal
f(n) = g(n) + h(n): Total estimated cost

The algorithm always expands the node with the lowest f(n), ensuring an optimal and efficient solution.

Problem Setup
Start Node: Disaneng
Goal Node: Coligny

The map consists of multiple towns connected by weighted edges representing travel distances.

Results
🔹 Optimal Path

Disaneng → Mahikeng → Bakerville → Lichtenburg → Coligny

🔹 Total Cost

110 km

🔹 Visited Nodes

Disaneng → Madibogo → Sannieshof → Ottosdal → Mahikeng → Bakerville → Lichtenburg → Coligny

How to Run the Program
Open Command Prompt

Navigate to the project folder:

cd "OneDrive\Desktop\CMPG 313\lab 5"

Run the main program:

python A_star_search.py

Optional (test file):

python A_star_search_testcase.py
Simulation Feature

The program includes a simulation that visually shows the truck traveling along the optimal route step-by-step.

Example output:

Truck is now at: Disaneng
Truck is now at: Mahikeng
Truck is now at: Bakerville
Truck is now at: Lichtenburg
Truck is now at: Coligny

Destination reached!
