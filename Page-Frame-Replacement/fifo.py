def fifo_page_replacement(pages, frame_size):
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

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3
print(f"FIFO Page Faults: {fifo_page_replacement(pages, frame_size)}")
