"""Reproducible portfolio benchmark added in October 2026."""
import argparse
import csv
import random
from astar import astar
from dijkstra import dijkstra
from grid import Grid


def run(output, trials):
    with open(output, 'w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=['seed','size','obstacle_probability','algorithm','reachable','path_length','expanded_nodes','runtime_seconds'])
        writer.writeheader()
        for size in (10,20,40,80):
            for density in (0.1,0.2,0.3,0.4):
                for trial in range(trials):
                    seed = size*10000 + int(density*100)*100 + trial
                    random.seed(seed)
                    world=Grid(size,size,density)
                    world.generate()
                    results=[('astar', astar(world)), ('dijkstra', dijkstra(world))]
                    assert results[0][1]['path_length']==results[1][1]['path_length'], 'Shortest path disagreement'
                    for name, result in results:
                        writer.writerow(dict(seed=seed,size=size,obstacle_probability=density,algorithm=name,reachable=bool(result['path']),path_length=result['path_length'],expanded_nodes=result['expanded_nodes'],runtime_seconds=result['runtime']))
    print(f'Wrote {32*trials} search results to {output}')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--trials',type=int,default=5)
    parser.add_argument('--output',default='results.csv')
    args=parser.parse_args()
    if args.trials<1: parser.error('--trials must be positive')
    run(args.output,args.trials)
