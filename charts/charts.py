import matplotlib.pyplot as plt


def creaPieChart():
    labels = ["A", "B", "C", "D"]
    valores = [100, 45, 389, 29]

    fix, ax = plt.subplots()
    ax.pie(valores, labels=labels)
    plt.savefig('graficapastel.png')
    plt.close()