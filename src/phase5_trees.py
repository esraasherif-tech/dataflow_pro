# phase5_trees.py
from anytree import Node, RenderTree

# ----------- BST for Customers ------------
class BSTNode:
    def __init__(self, national_id: int, name: str):
        self.national_id = national_id
        self.name = name
        self.left = None
        self.right = None

class DimensionIndex:
    def __init__(self):
        self.root = None

    def insert(self, national_id, name):
        # TODO: Implement BST insertion
        pass

    def search(self, national_id):
        # TODO: Implement BST search
        pass

# ----------- Org Chart ------------
class OrgChartAnalyzer:
    def __init__(self):
        self.ceo = Node("Omar (Global CEO)", sales=0)
        self.vp_cairo = Node("Tarek (VP Cairo & Giza)", parent=self.ceo, sales=0)
        self.vp_alex = Node("Salma (VP Alex & Delta)", parent=self.ceo, sales=0)

        Node("Aya (Maadi Branch Rep)", parent=self.vp_cairo, sales=150000)
        Node("Mahmoud (Zayed Branch Rep)", parent=self.vp_cairo, sales=270000)
        Node("Kareem (Smouha Branch Rep)", parent=self.vp_alex, sales=180000)
        Node("Nour (Mansoura Branch Rep)", parent=self.vp_alex, sales=120000)

    def display_chart(self):
        print("\n[Org Chart] NileMart Hierarchy:")
        for pre, _, node in RenderTree(self.ceo):
            print(f"{pre}{node.name} (Direct Sales: {node.sales:,} EGP)")

    def roll_up_sales(self, node: Node) -> int:
        total = node.sales + sum(self.roll_up_sales(child) for child in node.children)
        return total