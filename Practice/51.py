def calculate_total(price: float, discount: float) -> float:
        # Lots of complex math happening here...
        total = price - (price * discount)
        breakpoint()
        final_price = total / 0  # CRASH HAPPENS HERE
        return final_price

def main():
    calculate_total(100.0, 0.2)

if __name__ == "__main__":
      main()