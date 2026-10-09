from grid import Grid
from dijkstra import dijkstra
from astar import astar


def main():
    grid_obj = Grid(rows=10, cols=10, obstacle_prob=0.2)
    grid_obj.generate()

    print("Generated Grid:")
    grid_obj.print_grid()
    print()

    print("Running Dijkstra...")
    dijkstra_result = dijkstra(grid_obj)
    if dijkstra_result["path"]:
        print("Dijkstra found a path.")
        print(f"Path length: {dijkstra_result['path_length']}")
        print(f"Expanded nodes: {dijkstra_result['expanded_nodes']}")
        print(f"Runtime: {dijkstra_result['runtime']:.6f} seconds")
        grid_obj.print_grid(dijkstra_result["path"])
    else:
        print("Dijkstra could not find a path.")

    print("\n" + "=" * 40 + "\n")

    print("Running A*...")
    astar_result = astar(grid_obj)
    if astar_result["path"]:
        print("A* found a path.")
        print(f"Path length: {astar_result['path_length']}")
        print(f"Expanded nodes: {astar_result['expanded_nodes']}")
        print(f"Runtime: {astar_result['runtime']:.6f} seconds")
        grid_obj.print_grid(astar_result["path"])
    else:
        print("A* could not find a path.")


if __name__ == "__main__":
    main()