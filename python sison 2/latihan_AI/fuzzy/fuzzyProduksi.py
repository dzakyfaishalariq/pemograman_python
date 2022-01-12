import skfuzzy as fuzzy
import matplotlib.pyplot as plt


def fungsiperoduksi(reng, tepatan, titel, label1, label2):
    a = fuzzy.trapmf(reng, tepatan[0])
    b = fuzzy.trapmf(reng, tepatan[1])
    fig, pt = plt.subplots(nrows=1, figsize=(6, 3))
    pt.plot(reng, a, 'g', linewidth=1.5, label=label1)
    pt.plot(reng, b, 'r', linewidth=1.5, label=label2)
    pt.set_title(titel)
    pt.legend()
    pt.spines['top'].set_visible(False)
    pt.spines['right'].set_visible(False)
    pt.get_xaxis().tick_bottom()
    pt.get_yaxis().tick_left()
    plt.tight_layout()
    plt.axis([1, 1600, 0, 1])
    plt.grid()
    plt.show()
    return a, b
