# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def main():
    print("Program to create a savings calculator")
    months = int(input('How many months do you need to accumulate? '))
    salary = request_salary()
    threshold = request_savings_threshold()
    percent = request_percent()
    liv_expenses = request_living_expenses()
    monthly_savings = threshold * percent

    # display user information for user view
    print('====================Resource information====================')
    print(f'Your current salary is: {format_money(salary)}')
    print(f'Your current living expenses: {format_money(liv_expenses)}')
    print(f'Your chosen percent to salary to save: {percent}')
    print(f'Your saving threshold goal is: {format_money(threshold)}')
    print(f'Your monthly amount of savings will be: {format_money(monthly_savings)}')
    print(f'You will save this number of money in the following number of months : {months}')

    print('===========The following table shows your savings schedule===========')

    #   loop to calculate savings
    remaining_amount = threshold
    print('Month', 'Expenses', 'Amount Saved', 'Remaining Amount', 'Monthly Excess', sep='\t')
    for x in range(months):
        savings = compute_salary_savings(salary, liv_expenses, percent, threshold)
        if savings < 0:
            print('You cannot save for this month')
            break

        monthly_excess = savings - (liv_expenses + monthly_savings)
        remaining_amount = remaining_amount - monthly_savings

        # convert values to their dollar equivalent
        expenses_in_dol = format_money(liv_expenses)
        amt_sav_in_dol = format_money(monthly_savings)
        remain_in_dol = format_money(remaining_amount)
        excess_in_dol = format_money(monthly_excess)

        print(f'{x+1}\t', f'{expenses_in_dol}\t', f'{amt_sav_in_dol}\t', f'{remain_in_dol}\t\t\t', f'{excess_in_dol}', sep='\t')

    # confirm that the user wants to start again
    yes_list = ["yes", "y", "yeah"]
    restart = input("Do you want to start again?").lower()
    if restart in yes_list:
        main()
    else:
        exit()


def request_salary():
    _salary = float(input('Please enter your salary: '))
    return _salary


def request_savings_threshold():
    _savings_threshold = float(input('Please enter your savings threshold: '))
    return _savings_threshold


def format_money(val):
    return '$' + str("{:.2f}".format(val))


def request_living_expenses():
    _expense = float(input('Please enter your living expense: '))
    return _expense


def request_percent():
    _percent = float(input('Please enter your percent: '))
    return _percent


def compute_salary_savings(salary, living_expense, percent, savings_threshold):
    _savings = (salary/12) - (savings_threshold * percent) - living_expense
    return _savings

# Press the green button in the gutter to run the script.


if __name__ == '__main__':

    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
