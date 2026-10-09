# Grid Search Benchmark

A small Python comparison of A* and Dijkstra by Shiyu Chen, based on the saved CS 5100 course-project prototype. Both algorithms run on the same randomly generated four-neighbor grid, with identical start and goal cells. A* uses Manhattan distance; each traversable step costs one.

## Run

Python 3.10 or later; no third-party dependencies.

```sh
python main.py
python benchmark.py --trials 5 --output results.csv
```

The first command prints a single random grid and both paths. The benchmark uses deterministic seeds across four grid sizes and four obstacle densities, records reachability, path length, node expansions and elapsed time, and checks that both searches agree on shortest-path length.

## Files

- `grid.py`: obstacle generation and neighbor lookup.
- `astar.py`: heuristic search and path reconstruction.
- `dijkstra.py`: uniform-cost search and path reconstruction.
- `main.py`: original console demonstration.
- `benchmark.py`: repeatable experiment runner added during portfolio preparation.
- `results.csv`: a fresh October 2026 run, not the original course-report measurements.

## Scope

The four core modules preserve the saved course prototype. The benchmark script was added in October 2026 and is clearly separated from the original work. This copy does not contain the later path-smoothing implementation described in the course report, so it makes no claim to reproduce that report in full. Timing varies by machine; a small sample is not evidence of a universal speedup. Node expansions count queue removals as recorded by the original algorithms.

The project contains no assignment handouts, grades, private feedback or course solution files.
