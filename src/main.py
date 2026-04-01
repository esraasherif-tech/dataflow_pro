# main.py
import sys
from phase2_tracker import AppliedStepsTracker
from phase3_parser import DAXEvaluator
from phase4_buffer import LiveIngestionQueue
from phase5_trees import OrgChartAnalyzer

def main():
    print("==================================================")
    print("   Welcome to DataFlow Pro - NileMart ETL Engine  ")
    print("==================================================")

    tracker = AppliedStepsTracker()
    dax_engine = DAXEvaluator()
    buffer = LiveIngestionQueue()
    org_chart = OrgChartAnalyzer()

    while True:
        print("\nMain Menu:")
        print("1. Add ETL Step (Linked List)")
        print("2. Evaluate DAX Formula (Stack)")
        print("3. Ingest Live Data (Queue)")
        print("4. Analyze Org Chart Sales (Trees)")
        print("5. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            step = input("Enter transformation step: ")
            tracker.add_step(step)
            
        elif choice == "2":
            formula = input("Enter Postfix DAX expression: ")
            result = dax_engine.evaluate_postfix(formula)
            print(f"Result: {result}")
            
        elif choice == "3":
            buffer.enqueue_row({"txn": 1045, "branch": "Maadi", "amt_egp": 850})
            buffer.enqueue_row({"txn": 1046, "branch": "Smouha", "amt_egp": 3200})
            buffer.process_batch(2)
            
        elif choice == "4":
            org_chart.display_chart()
            total = org_chart.roll_up_sales(org_chart.vp_cairo)
            print(f"\nTotal Regional Sales for Tarek: {total:,} EGP")
            
        elif choice == "5":
            print("Shutting down DataFlow Pro. Masalama!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()