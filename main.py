import csv


# Read data from the spreadsheet
def read_data():
    data = []
    with open("sales.csv", "r") as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


# Collect all the sales from each month into a single list
def get_monthly_sales():
    data = read_data()
    sales_list = []
    for row in data:
        sales = (row["sales"])
        sales_list.append(sales)
    return sales_list


# Total annual sales
def get_total_sales():
    sales_list = get_monthly_sales()
    total_sales = sum(map(float, sales_list))
    return total_sales


# Quarterly sales
def get_quarterly_sales():
    data = read_data()
    quarterly_sales = {
            "Q1": 0,
            "Q2": 0,
            "Q3": 0,
            "Q4": 0,
        }

    for row in data:
        month = row["month"]
        sales = int(row["sales"])
        if month in ["jan", "feb", "mar"]:
            quarterly_sales["Q1"] += sales
        elif month in ["apr", "may", "jun"]:
            quarterly_sales["Q2"] += sales
        elif month in ["jul", "aug", "sep"]:
            quarterly_sales["Q3"] += sales
        elif month in ["oct", "nov", "dec"]:
            quarterly_sales["Q4"] += sales
    return f"Quarterly sales: {quarterly_sales}"


# Average sales
def get_average_sales():
    sales_list = get_monthly_sales()
    average_sales = sum(map(float, sales_list)) / len(sales_list)
    return f"{average_sales:.2f}"


# The lowest monthly sales of the year
def get_lowest_sales():
    sales_list = get_monthly_sales()
    lowest_sales = min(map(float,sales_list))
    return f"The lowest sales: {lowest_sales}"


# The highest monthly sales of the year
def get_highest_sales():
    sales_list = get_monthly_sales()
    highest_sales = max(map(float, sales_list))
    return f"The highest sales: {highest_sales}"


# Collect expenses from each month into a single list
def get_expenditure_list():
    data = read_data()
    expenditure_list = []
    for row in data:
        expenditure = (row["expenditure"])
        expenditure_list.append(expenditure)
    return expenditure_list


# Total annual expenditure
def get_total_expenditure():
    expenditure_list = get_expenditure_list()
    total_expenditure = sum(map(float, expenditure_list))
    return total_expenditure


# Average expenditure
def get_average_expenditure():
    expenditure_list = get_expenditure_list()
    total_expenditure = sum(map(float, expenditure_list))
    average_expenditure = total_expenditure / len(expenditure_list)
    return f"{average_expenditure:.2f}"


# Net profit for the year
def get_net_profit():
    total_sales = get_total_sales()
    total_expenditure = get_total_expenditure()
    net_profit = total_sales - total_expenditure
    return f"Net profit: {net_profit}"


# Identify months with sales below and above the average
def categorize_sales():
    sales_categories = {
        "Low sales months": [],
        "High sales months": [],
    }
    average_sales = get_average_sales()
    data = read_data()

    sales_categories["Low sales months"] = [row["month"] for row in data if row["sales"] < average_sales]
    sales_categories["High sales months"] = [row["month"] for row in data if row["sales"] > average_sales]

    response = ""
    for key, value in sales_categories.items():
        response += f"{key}: {value}\n"

    return response


def print_menu():
    print("SALES DATA / 2018")
    print("1. Total sales")
    print("2. Quarterly sales")
    print("3. Average sales")
    print("4. The highest and lowest sales month of the year")
    print("5. Total expenditure")
    print("6. Average expenditure")
    print("7. Net profit")
    print("8. Performance categorization: low/high")
    print("9. Exit the program")


def select_option():
    option = input("\nChoose an option (1-9): ")
    return option


def execute_selected_option(choice):
    if choice == "1":
        print(get_total_sales())
    elif choice == "2":
        print(get_quarterly_sales())
    elif choice == "3":
        print(get_average_sales())
    elif choice == "4":
        print(get_highest_sales())
        print(get_lowest_sales())
    elif choice == "5":
        print(get_total_expenditure())
    elif choice == "6":
        print(get_average_expenditure())
    elif choice == "7":
        print(get_net_profit())
    elif choice == "8":
        print(categorize_sales())
    elif choice == "9":
        print("Program exited successfully.")
    else:
        print("Incorrect value")


def run():
    while True:
        print_menu()
        user_choice = select_option()
        execute_selected_option(user_choice)
        if user_choice == "9":
            break
        else:
            input("\nPress any key to continue...\n")


run()
