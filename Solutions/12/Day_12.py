input_file ="sample.txt" if 0 else "input.txt"

with open(input_file) as inp:
    data = [row.split('-') for row in inp.read().split('\n')]
    graph = {}
    for a,b in data:
        if a not in graph.keys():
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph.keys():
            graph[b] = [a]
        else:
            graph[b].append(a)
    
    def step(paths, G):
        new_paths = []
        finished = []
        for path, visited_twice in paths:
            if path[-1] == 'end':
                finished += [path]
                continue
            for new_vertex in G[path[-1]]:
                if new_vertex != 'start':
                    if new_vertex == new_vertex.upper():
                        new_paths += [(path + [new_vertex], visited_twice)]
                    elif new_vertex in path and not visited_twice:
                        new_paths += [(path + [new_vertex], True)]
                    elif new_vertex not in path:
                        new_paths += [(path + [new_vertex], visited_twice)]
        return new_paths, finished
    
    final_paths = []
    unfinished_paths = [(['start'], False)]
    while len(unfinished_paths) > 0:
        unfinished_paths, ended = step(unfinished_paths, graph)
        final_paths += ended
    # print(*sorted(final_paths),sep='\n')
    print(len(final_paths))
                
    