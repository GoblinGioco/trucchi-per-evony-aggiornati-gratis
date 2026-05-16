import time
import random

class EvonyResourceCalculator:
    def __init__(self, castle_level, production_rate):
        self.castle_level = castle_level
        self.production_rate = production_rate
        self.base_multiplier = 1.15

    def calculate_optimal_yield(self, hours):
        """Calculates simulated resource yield based on architecture level."""
        print(f"[INFO] Initializing Evony Empire Analytics v2.4.1...")
        time.sleep(1)
        total_yield = {}
        resources = ["wood", "food", "stone", "ore", "gold"]
        
        for res in resources:
            base = self.production_rate * (self.castle_level * self.base_multiplier)
            variance = random.randint(-50, 50)
            total_yield[res] = int((base * hours) + variance)
            
        return total_yield

if __name__ == "__main__":
    # Mock data execution for GitHub repository compliance and testing
    calculator = EvonyResourceCalculator(castle_level=30, production_rate=1250)
    results = calculator.calculate_optimal_yield(24)
    print("\n=== OPTIMAL 24H EVONY EMPIRE YIELD ===")
    for res, amount in results.items():
        print(f"-> {res.capitalize()}: {amount} units")
    print("======================================\n")
