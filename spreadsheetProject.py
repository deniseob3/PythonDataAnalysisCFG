import csv
import statistics #mean & median
import matplotlib.pyplot as plt
import seaborn as sns

def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def run():
    data = read_data()
    sales = []
    months = []
    expenditures = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
        month = (row['month'])
        months.append(month)
        expenditure = int(row['expenditure'])
        expenditures.append(expenditure)

    sales_Statistics(sales, expenditures)
    salesPlot(months, sales)
    expenditurePlot(months, expenditures)
    #salesAndExpenditurePlot(months, sales, expenditures)

    boxplot(sales)
    barplot(sales, months)


# Percentage-function #
def percentage(part, whole):
    percentage = 100 * float(part) / float(whole)
    return percentage

def sales_Statistics (sales, expenditures):
    totalS = sum(sales)
    totalE = sum(expenditures)

    print('Total sales: {}'.format(totalS))
    print('Minimum sales amount: {}'.format(min(sales)))

    print("Median of yearly sales: {}".format(round(statistics.median(sales), 2)))  # mean can be skewed
    print("Mean of yearly sales: {}".format(round(statistics.mean(sales), 2)))  # actual "middle"

    # print('Percentage of total sales in January: {}'.format(round(sales[0] / total, 2)))

    print('Percentual difference of max & min sales per month: {} %'.format(
        round(percentage(min(sales), max(sales)), 2)))  # to see performance
    print('Percentage of total sales in January: {} %'.format(
        round(percentage(sales[0], totalS), 2)))  # with percent-function

    print('Total earnings: {}'.format(totalS - totalE))

def salesPlot(months, sales):
    x = months
    y = sales

    plt.plot(x, y)
    # giving title to the plot
    plt.title('Sales per month');
    # function to show plot
    plt.show()

def expenditurePlot(months, expenditures):
    x = months
    y = expenditures

    plt.plot(x,y)
    plt.title("Expenditure per month")
    plt.show()

def salesAndExpenditurePlot(months, sales, expenditures):
    x = months
    y = sales
    z = expenditures

    plt.plot(x,y, c="c")
    plt.plot(x,z, c="m")
    plt.title("Sales and expenditure per month")
    plt.show()

def boxplot(sales):
    sns.boxplot(sales)
    plt.title('BoxPlot of sales')
    plt.show()

def barplot(sales, months):
    sns.barplot(x= sales, y = months)
    plt.title('BoxPlot of sales')
    plt.show()

run()

