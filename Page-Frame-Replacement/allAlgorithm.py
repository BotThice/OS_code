import time
import matplotlib.pyplot as plt

def test_algorithm(algorithm, frame, pages):
    start_time = time.perf_counter()
    page_faults = algorithm(frame, pages.copy())
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return page_faults, execution_time

def run_tests(algorithm, frames, pages):
    # results = {frame: (0, 0) for frame in frames}
    results = {}
    
    for frame in frames:
        page_faults, execution_time = test_algorithm(algorithm, frame, pages)
        results[frame] = (page_faults, execution_time)
        print(f"Frame Size: {frame}, Page Faults: {page_faults}, Execution Time: {execution_time:.6f}s")
    
    return results

def plot_results(results, title):
    frames = list(results.keys())
    faults = [results[f][0] for f in frames]
    times = [results[f][1] for f in frames]
    
    fig, ax1 = plt.subplots()
    ax1.set_xlabel('Number of Frames')
    ax1.set_ylabel('Page Faults', color='tab:red')
    ax1.plot(frames, faults, 'ro-', label='Page Faults')
    ax1.tick_params(axis='y', labelcolor='tab:red')
    
    ax2 = ax1.twinx()
    ax2.set_ylabel('Execution Time (s)', color='tab:blue')
    ax2.plot(frames, times, 'bo-', label='Execution Time')
    ax2.tick_params(axis='y', labelcolor='tab:blue')
    
    plt.title('Performance of ' + title)
    plt.show()

def fifo(frame_size, pages) :
    frame = []
    page_faults = 0

    for page in pages:
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            page_faults += 1

    return page_faults

def lru(frame_size, pages):
    frame = []
    page_faults = 0

    for page in pages:
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                lru_page = min(frame, key=lambda p: pages[:pages.index(page)].count(p))
                frame.remove(lru_page)
                frame.append(page)
            page_faults += 1
        else:
            frame.remove(page)
            frame.append(page)

    return page_faults

def optimal(frame_size, pages):
    frame = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                future_uses = [pages[i+1:].index(p) if p in pages[i+1:] else float('inf') for p in frame]
                frame.pop(future_uses.index(max(future_uses)))
                frame.append(page)
            page_faults += 1

    return page_faults

# main part
frames = [8, 16, 25, 32]

pages1 = [  
            7, 12, 8, 3, 7, 22, 21, 30, 15, 20, 26, 8, 3, 12, 27, 28, 7, 5,
            8, 3, 25, 10, 15, 24, 23, 29, 7, 3, 8, 30
        ]

pages2 = [  
            40, 5, 14, 10, 1, 25, 1, 9, 1, 30, 50, 41, 42, 43, 57, 20, 9, 5,
            5, 54, 1, 9, 9, 46, 45, 52, 44, 9, 48, 56, 35, 47, 1, 53, 15,
            20, 51, 1, 55, 10, 1, 14, 30, 9, 35, 10, 20, 5, 15, 5, 9, 9, 
            20, 5, 15, 14, 10, 5, 9, 49
        ]

pages3 = [
            22, 67, 2, 18, 10, 40, 12, 6, 18, 90, 2, 10, 51, 92, 22, 6, 80,
            28, 50, 34, 66, 22, 77, 68, 63, 62, 12, 40, 86, 16, 6, 82, 2, 
            28, 22, 89, 85, 47, 53, 75, 6, 93, 64, 34, 16, 10, 79, 61, 78, 
            84, 87, 22, 57, 22, 81, 2, 6, 65, 76, 6, 18, 6, 88, 10, 18, 2, 
            83, 18, 2, 6, 6, 22, 12, 67, 40, 2, 28, 6, 22, 91, 16, 18, 22, 
            10, 18, 6, 28, 34, 22, 40, 10, 16, 2, 6, 22, 10, 2, 6, 28, 12
        ]

# results = run_tests(fifo, frames, pages1)
# plot_results(results, "FIFO of first set")
# results = run_tests(fifo, frames, pages2)
# plot_results(results, "FIFO of second set")
# results = run_tests(fifo, frames, pages3)
# plot_results(results, "FIFO of third set")

# results = run_tests(optimal, frames, pages1)
# plot_results(results, "Optimal of first set")
# results = run_tests(optimal, frames, pages2)
# plot_results(results, "Optimal of second set")
# results = run_tests(optimal, frames, pages3)
# plot_results(results, "Optimal of third set")

# results = run_tests(lru, frames, pages1)
# plot_results(results, "LRU of first set")
# results = run_tests(lru, frames, pages2)
# plot_results(results, "LRU of second set")
results = run_tests(lru, frames, pages3)
plot_results(results, "LRU of third set")


