import skfuzzy as fuzzy
import matplotlib.pyplot as plt


def fungsiPermintaan(rang, tetapan, judul, label1, label2):
    a = fuzzy.pimf(rang, tetapan[0][0], tetapan[0][1],
                   tetapan[0][2], tetapan[0][3])
    b = fuzzy.pimf(rang, tetapan[1][0], tetapan[1][1],
                   tetapan[1][2], tetapan[1][3])
    fig, pt = plt.subplots(nrows=1, figsize=(6, 3))
    pt.plot(rang, a, 'g', linewidth=1.5, label=label1)
    pt.plot(rang, b, 'r', linewidth=1.5, label=label2)
    pt.set_title(judul)
    pt.legend()
    pt.spines['top'].set_visible(False)
    pt.spines['right'].set_visible(False)
    pt.get_xaxis().tick_bottom()
    pt.get_yaxis().tick_left()
    plt.axis([0, 1001, 0, 1])
    plt.tight_layout()
    plt.grid()
    plt.show()
    return a, b


def keanggotaan_permintaan(rang, turun, naik, nilai):
    _turun = fuzzy.interp_membership(rang, turun, nilai)
    _naik = fuzzy.interp_membership(rang, naik, nilai)
    return _turun, _naik
