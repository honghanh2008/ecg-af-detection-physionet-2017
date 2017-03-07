import random
import numpy as np
import matplotlib.pyplot as plt

from qrs_detect import qrs_detect

plt.rcParams["figure.figsize"] = (20, 4)

seed = 42
random.seed(seed)
np.random.seed(seed)
print("Seed =", seed)

import loader
import preprocessing
import feature_extractor

(X, Y) = loader.load_all_data()
(Y, mapping) = preprocessing.format_labels(Y)
print('Input length', len(X))
print('Categories mapping', mapping)


def plot_with_detected_peaks(row):
    # r = feature_extractor.get_r_peaks_positions(row)
    (q, r, s) = qrs_detect(row)

    print('Q', q)
    print('R', r)
    print('S', s)
    plt.plot(range(len(row)), row, 'g-',
             q, [row[x] for x in q], 'bo',
             r, [row[x] for x in r], 'r^',
             s, [row[x] for x in s], 'mv',)

    plt.show()


plot_with_detected_peaks(X[0])
plot_with_detected_peaks(X[1])
plot_with_detected_peaks(X[2])
plot_with_detected_peaks(X[3])
