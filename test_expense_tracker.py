from main import (
    Expense,
    FoodExpense,
    TravelExpense,
    EntertainmentExpense,
    create_expense
)


def test_food_expense():
    expense = FoodExpense("Lunch", 250)

    assert expense.get_category() == "Food"
    assert expense.amount == 250


def test_travel_expense():
    expense = TravelExpense("Bus Ticket", 80)

    assert expense.get_category() == "Travel"


def test_entertainment_expense():
    expense = EntertainmentExpense("Movie", 350)

    assert expense.get_category() == "Entertainment"


def test_inheritance():
    expense = FoodExpense("Lunch", 250)

    assert isinstance(expense, Expense)


def test_factory_function():
    expense = create_expense("Dinner", "food", 400)

    assert isinstance(expense, FoodExpense)


def test_invalid_amount():
    try:
        Expense("Test", -100)
        assert False
    except ValueError:
        assert True


print("All tests passed!")