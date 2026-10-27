# CodeAlpha Internship
# Task 2: Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}

# Store user's selected stocks
portfolio = {}

print("\n===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price} per share")

print("\nEnter 'done' when you finish adding stocks.")

# Take input from user
while True:
    stock = input("\nEnter stock symbol: ").strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock symbol. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    # Add stock quantity to portfolio
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    print(f"{quantity} shares of {stock} added successfully.")

# Calculate total investment
total_investment = 0

print("\n===================================")
print("          PORTFOLIO REPORT")
print("===================================")

if not portfolio:
    print("No stocks were added.")

else:
    print(f"{'Stock':<10}{'Quantity':<10}{'Price':<10}{'Value':<10}")
    print("-" * 40)

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity

        total_investment += value

        print(
            f"{stock:<10}{quantity:<10}"
            f"${price:<9}${value:,.2f}"
        )

    print("-" * 40)
    print(f"Total Investment: ${total_investment:,.2f}")

    # Save portfolio report
    with open("portfolio_report.txt", "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 30 + "\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity

            file.write(
                f"{stock}: {quantity} shares x "
                f"${price} = ${value:,.2f}\n"
            )

        file.write(
            f"\nTotal Investment: ${total_investment:,.2f}\n"
        )

    print("\nReport saved to portfolio_report.txt")

print("\nThank you for using Stock Portfolio Tracker!")