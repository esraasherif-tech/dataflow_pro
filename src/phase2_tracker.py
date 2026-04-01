# phase2_tracker.py

class Node:
    def __init__(self, step):
        self.step = step
        self.next = None
        self.prev = None  # For Doubly Linked List

class AppliedStepsTracker:
    """Tracks ETL steps with undo/redo capability."""
    def __init__(self):
        self.head = None
        self.current = None

    def add_step(self, step):
        new_node = Node(step)
        if not self.head:
            self.head = new_node
            self.current = new_node
        else:
            # Append to the end
            self.current.next = new_node
            new_node.prev = self.current
            self.current = new_node
        print(f"[Tracker] Added step: {step}")

    def undo_step(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"[Tracker] Undo to step: {self.current.step}")
        else:
            print("[Tracker] No previous step to undo.")

    def redo_step(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"[Tracker] Redo to step: {self.current.step}")
        else:
            print("[Tracker] No next step to redo.")