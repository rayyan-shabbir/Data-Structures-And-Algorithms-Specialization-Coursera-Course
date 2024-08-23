def count_segments_containing_points(segments, points):
    # Create events for each segment and point
    events = []
    for (l, r) in segments:
        events.append((l, 'L'))
        events.append((r, 'R'))
    for i, point in enumerate(points):
        events.append((point, 'P', i))
   
    # Sort events by the position, then by type
    events.sort(key=lambda x: (x[0], x[1]))
    print(events)
   
    current_segments = 0
    result = [0] * len(points)
   
    # Traverse sorted events
    for event in events:
        if event[1] == 'L':
            current_segments += 1
        elif event[1] == 'R':
            current_segments -= 1
        else:  # event[1] == 'P'
            result[event[2]] = current_segments
   
    return result
 
# Get input from user
n, m = map(int, input().split())  # Number of segments and points
 
segments = []
for _ in range(n):
    l, r = map(int, input().split())  # Input each segment
    segments.append((l, r))
 
points = list(map(int, input().split()))  # Input all points
 
# Calculate the result
result = count_segments_containing_points(segments, points)
 
# Print the output
print(" ".join(map(str, result)))