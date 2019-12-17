
def line_plot():
    # print(plt.style.available)
    # plt.xkdc()
    plt.style.use('fivethirtyeight')
    ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
    # plt.plot(ages_x, py_dev_y, color='b', linestyle ='-', marker='o', linewidth=3, label='Python')
    plt.plot(ages_x, py_dev_y, label='Python')

    js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
    # plt.plot(ages_x, js_dev_y, color='#adad3b', linestyle ='-', marker='o', linewidth=3, label='Javascript')
    plt.plot(ages_x, js_dev_y, label='Javascript')

    dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
    # plt.plot(ages_x, dev_y, 'k--', label = 'All Devs')
    # plt.plot(ages_x, dev_y, color='k', linestyle ='--', marker='.', label = 'All Devs')
    plt.plot(ages_x, dev_y, color='#444444', label = 'All Devs')

    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')
    plt.title('Median Salary by Age')

    plt.legend()

    # plt.grid(True)
    plt.tight_layout()

    plt.savefig('plot.png')

    plt.show()

def bar_plot():
    import numpy as np
    from matplotlib import pyplot as plt
    plt.style.use('fivethirtyeight')

    width = 0.25
    ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    x_indexes = np.arange(len(ages_x))

    dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
    plt.bar(x_indexes-width, dev_y, width=0.25, color='#444444', label = 'All Devs')

    py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
    plt.bar(x_indexes, py_dev_y, width=0.25, label='Python')

    js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
    plt.bar(x_indexes + width, js_dev_y, width=0.25, label='Javascript')

    plt.xticks(ticks=x_indexes, labels=ages_x)
    plt.title('Median Salary by Age')
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')

    plt.tight_layout()

    plt.show()

# line_plot():
bar_plot()