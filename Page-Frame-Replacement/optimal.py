def optimal_page_replacement(pages, frame_size):
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

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3
print(f"Optimal Page Faults: {optimal_page_replacement(pages, frame_size)}")
