import csv
import os
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 185,
    "MSFT": 420,
    "NVDA": 875,
    "META": 510,
}


def show_available_stocks():
    print("\n--- Available Stocks ---")
    print(f"{'Symbol':<10} {'Price (USD)':>12}")
    print("-" * 24)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<10} ${price:>11,.2f}")
    print()


def build_portfolio():
    portfolio = {}
    print("\nEnter stock symbols and quantities (type 'done' when finished).")
    show_available_stocks()

    while True:
        symbol = input("Stock symbol: ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print(f"  ⚠  '{symbol}' not found. Available: {', '.join(STOCK_PRICES)}")
            continue
        try:
            qty = int(input(f"  Quantity of {symbol}: ").strip())
            if qty <= 0:
                print("  ⚠  Quantity must be a positive number.")
                continue
        except ValueError:
            print("  ⚠  Please enter a valid whole number.")
            continue

        if symbol in portfolio:
            portfolio[symbol] += qty
            print(f"  ✅ Updated {symbol} to {portfolio[symbol]} shares.")
        else:
            portfolio[symbol] = qty
            print(f"  ✅ Added {qty} share(s) of {symbol}.")

    return portfolio


def display_summary(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty.")
        return 0

    total = 0
    print("\n=============================")
    print("     PORTFOLIO SUMMARY       ")
    print("=============================")
    print(f"{'Stock':<8} {'Qty':>6} {'Price':>10} {'Value':>12}")
    print("-" * 40)

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        print(f"{symbol:<8} {qty:>6} ${price:>9,.2f} ${value:>11,.2f}")

    print("-" * 40)
    print(f"{'TOTAL':>26} ${total:>11,.2f}")
    print()
    return total


def save_to_csv(portfolio, total):
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price (USD)", "Value (USD)"])
        for symbol, qty in portfolio.items():
            price = STOCK_PRICES[symbol]
            writer.writerow([symbol, qty, price, price * qty])
        writer.writerow([])
        writer.writerow(["TOTAL", "", "", total])
    print(f"✅  Portfolio saved to '{filename}'")


def save_to_txt(portfolio, total):
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write("STOCK PORTFOLIO SUMMARY\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 40 + "\n")
        f.write(f"{'Stock':<8} {'Qty':>6} {'Price':>10} {'Value':>12}\n")
        f.write("-" * 40 + "\n")
        for symbol, qty in portfolio.items():
            price = STOCK_PRICES[symbol]
            value = price * qty
            f.write(f"{symbol:<8} {qty:>6} ${price:>9,.2f} ${value:>11,.2f}\n")
        f.write("-" * 40 + "\n")
        f.write(f"{'TOTAL':>26} ${total:>11,.2f}\n")
    print(f"✅  Portfolio saved to '{filename}'")


def main():
    print("\n=============================")
    print("   STOCK PORTFOLIO TRACKER   ")
    print("=============================")

    portfolio = build_portfolio()
    total = display_summary(portfolio)

    if portfolio:
        save = input("Save results? (csv / txt / no): ").strip().lower()
        if save == "csv":
            save_to_csv(portfolio, total)
        elif save == "txt":
            save_to_txt(portfolio, total)
        else:
            print("Results not saved.")


if __name__ == "__main__":
    main()
