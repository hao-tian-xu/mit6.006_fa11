import rubik

###############
## SOLUTIONS ##
###############

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    if start == end:
        return []
    parents = ({start: None}, {end: None})
    frontiers = [[start], [end]]
    for i in range(14):
        switch = i % 2
        frontiers[switch], mid = BiBFS_next(
            frontiers[switch], 
            parents[switch], 
            parents[switch-1]
        )
        if mid:
            path_1 = Path(mid, parents[0])
            path_2 = Path(mid, parents[1], True)
            path_1.reverse()
            return path_1 + path_2
    return None

def BiBFS_next(frontier, parent, other_parent):
    """
    Using BFS to find next level vertices.
    If a node is also processed in the other direction, return it.
    """
    next = []
    mid = None
    for u in frontier:
        for pos, move in Next_pos(u):
            if pos not in parent:
                parent[pos] = (u, move)
                next.append(pos)
                if pos in other_parent:
                    mid = pos
                    return next, mid
    return next, mid

def Next_pos(position):
    """
    Generate rubik's next possible position and the move to it
    """
    for move in rubik.quarter_twists:
        new_pos = rubik.perm_apply(move, position)
        yield (new_pos, move)

def Path(pos, parent, reverse=False):
    """
    Given a collision position from a Bi-direction BFS.
    Return the path from it to one end.
    """
    path = []
    while parent[pos]:
        move = parent[pos][1]
        if reverse: move = rubik.perm_inverse(move)
        path.append(move)
        pos = parent[pos][0]
    return path

#########
## END ##
#########