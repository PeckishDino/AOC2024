from collections import deque
import heapq


def one():
    grid = [list(line.strip()) for line in open("input.txt")]
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                sr = r
                sc = c
                break

    pq = [(0, sr, sc, 0, 1)]
    seen = {(sr, sc, 0, 1)}

    while pq:
        cost, r, c, dr, dc = heapq.heappop(pq)
        seen.add((r, c, dr, dc))
        if grid[r][c] == "E":
            print(cost)
            break

        for (new_cost, nr, nc, ndr,
             ndc) in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr),
                      (cost + 1000, r, c, -dc, dr)]:
            if grid[nr][nc] == "#": continue
            if (nr, nc, ndr, ndc) in seen: continue
            heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))


def two():
    grid = [list(line.strip()) for line in open("input.txt")]
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                sr = r
                sc = c
                break

    pq = [(0, sr, sc, 0, 1,None,None,None,None)]
    lowest_cost = {(sr, sc, 0, 1): 0}
    backtrack = {}
    best_cost = float("inf")
    end_states = set()

    while pq:
        cost, r, c, dr, dc ,lr,lc,ldr,ldc= heapq.heappop(pq)
        if cost > lowest_cost.get((r, c, dr, dc), float("inf")): continue
        lowest_cost[(r, c, dr, dc)] = cost
        if grid[r][c] == "E":
            if cost > best_cost: break
            best_cost = cost
            end_states.add((r,c,dr,dc))
        if (r,c,dr,dc) not in backtrack: backtrack[(r,c,dr,dc)] = set()
        backtrack[(r,c,dr,dc)].add((lr,lc,ldr,ldc))

        for (new_cost, nr, nc, ndr,
             ndc) in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr),
                      (cost + 1000, r, c, -dc, dr)]:
            if grid[nr][nc] == "#": continue
            if cost > lowest_cost.get((nr, nc, ndr, ndc),float("inf")): continue
            heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc,r,c,dr,dc))

    print(backtrack)
    print(end_states)

    states = deque(end_states)
    seen = set(end_states)

    while states:
        key = states.popleft()
        for last in backtrack.get(key,[]):
            if last in seen: continue
            seen.add(last)
            states.append(last)
    print({(r,c) for r,c,_,_ in seen})
    print(len({(r,c) for r,c,_,_ in seen})-1)

two()