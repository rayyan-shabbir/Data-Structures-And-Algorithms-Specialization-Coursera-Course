import heapq

def assign_jobs(n, jobs):
    # Initialize the heap with all threads having next_free_time = 0
    threads_heap = [(0, i) for i in range(n)]
    heapq.heapify(threads_heap)

    result = []

    for job in jobs:
        # Extract the thread with the smallest next_free_time
        next_free_time, thread_index = heapq.heappop(threads_heap)

        # Record the thread index and the start time (next_free_time)
        result.append((thread_index, next_free_time))

        # Update the thread's next_free_time by adding the job's duration
        heapq.heappush(threads_heap, (next_free_time + job, thread_index))

    return result


def main():
    n, m = map(int, input().split())
    jobs = list(map(int, input().split()))

    assigned_jobs = assign_jobs(n, jobs)

    for thread_index, start_time in assigned_jobs:
        print(thread_index, start_time)

if __name__ == "__main__":
    main()
