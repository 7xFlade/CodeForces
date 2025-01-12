# n, t = map(int, input().split()) # input returns "n t"
# ints = list(map(int, input().split())) # split returns ['n', 't']
# cells = {1}

# for i in range(len(ints)):
#     i  += ints[i]+1
#     cells.add(i)
#     if t in cells:
#         print("YES")
#         break
#     elif i == n:
#         print("NO")
#         break
#     else:
#         continue
# print(cells)

n, t = map(int, input().split())
jumps = list(map(int, input().split()))

# Use a set to track all reachable cells
reachable = {1}  # Start at cell 1
current = {1}    # Current cells we're exploring from

while current:
    next_cells = set()  # New cells we can reach
    
    # Try jumping from each current cell
    for pos in current:
        # If we're not at the last cell, try using its portal
        if pos < n:
            # Calculate where we land after using portal at position pos
            next_pos = pos + jumps[pos-1]
            # If this is a valid cell and we haven't seen it yet
            if next_pos <= n and next_pos not in reachable:
                next_cells.add(next_pos)
                reachable.add(next_pos)
                
    # If we found our target, we're done
    if t in next_cells:
        print("YES")
        break
        
    # Update current cells to the new ones we found
    current = next_cells
else:
    # If we exit the while loop normally (current becomes empty)
    # and haven't found t, it's impossible
    print("NO")