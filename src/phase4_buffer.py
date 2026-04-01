# phase4_buffer.py
from collections import deque

class LiveIngestionQueue:
    """Buffers live streaming sales data from NileMart branches before pushing to Power BI."""
    
    def __init__(self):
        self.buffer = deque()

    def enqueue_row(self, row_data: dict) -> None:
        self.buffer.append(row_data)
        print(f"[Buffer] Enqueued live data from POS: {row_data}")

    def process_batch(self, batch_size: int) -> list:
        processed_data = []
        for _ in range(batch_size):
            if self.buffer:
                processed_data.append(self.buffer.popleft())
        print(f"[Buffer] Processed {len(processed_data)} transactions. Pushing to NileMart Power BI Datasets...")
        return processed_data