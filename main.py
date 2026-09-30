import csv


class Expense:
    def __init__(self, name, amount):
        if not name.strip():
            raise ValueError("Expense name cannot be empty.")

        if amount <= 0:
            raise ValueError("Expense amount must be greater than 0.")

        self.name = name
        self.amount = amount

    def get_category(self):
        return "General"

    def display(self):
        return f"{self.name}: ₹{self.amount:.2f} ({self.get_category()})"


class FoodExpense(Expense):
    def get_category(self):
        return "Food"


class TravelExpense(Expense):
    def get_category(self):
        return "Travel"


class EntertainmentExpense(Expense):
    def get_category(self):
        return "Entertainment"


def create_expense(name, category, amount):
    category = category.strip().lower()

    if category == "food":
        return FoodExpense(name, amount)

    elif category == "travel":
        return TravelExpense(name, amount)

    elif category == "entertainment":
        return EntertainmentExpense(name, amount)

    else:
        return Expense(name, amount)


def load_expenses(filename):
    expenses = []

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    name = row["name"].strip()
                    category = row["category"].strip()
                    amount = float(row["amount"])

                    expense = create_expense(name, category, amount)
                    expenses.append(expense)

                except (ValueError, KeyError) as e:
                    print(f"Skipping invalid row: {row} -> {e}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return expenses


def generate_report(expenses):
    if not expenses:
        print("No valid expenses found.")
        return

    total = sum(expense.amount for expense in expenses)
    average = total / len(expenses)
    highest = max(expenses, key=lambda expense: expense.amount)

    print("\n========== EXPENSE REPORT ==========")

    print(f"Number of expenses: {len(expenses)}")
    print(f"Total expenses: ₹{total:.2f}")
    print(f"Average expense: ₹{average:.2f}")

    print(
        f"Highest expense: {highest.name} "
        f"(₹{highest.amount:.2f})"
    )

    print("\nCategory-wise totals:")

    categories = {}

    for expense in expenses:
        category = expense.get_category()
        categories[category] = categories.get(category, 0) + expense.amount

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")

    print("\nAll expenses:")

    for expense in expenses:
        print(expense.display())

    print("====================================")


def main():
    print("===== Personal Expense Tracker =====")

    filename = input("Enter the CSV file name: ").strip()

    if not filename:
        print("Error: File name cannot be empty.")
        return

    expenses = load_expenses(filename)

    generate_report(expenses)


if __name__ == "__main__":
    main()