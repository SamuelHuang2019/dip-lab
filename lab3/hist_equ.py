import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize


def hist_equ(raw_img=None, file_name=None):
    """
    Implement the histogram equalization to the input images Q3_1_1.tif and Q3_1_2.tif
    """

    if raw_img is None:
        raw_img = cv.imread(file_name, cv.IMREAD_GRAYSCALE)

    norm = Normalize(vmin=0, vmax=255)
    L = 2 ** 8
    bins = range(L + 1)
    # row, col = raw_img.shape

    # input_hist = np.zeros(L, int)
    # for i in raw_img.flat:
    #     input_hist[i] += 1

    # input_hist = histogram(raw_img)
    input_hist, _ = np.histogram(raw_img.flat, bins=bins, density=True)
    # print(file_name, 'raw', np.count_nonzero(input_hist))

    # s = np.zeros(L, int)
    # for k in range(L):
    #     s[k] = (L - 1) * sum(input_hist[:k + 1])

    s = np.array([(L - 1) * sum(input_hist[:k + 1]) for k in range(L)])

    out_img = np.array([s[r] for r in raw_img], int).reshape(raw_img.shape)
    # output_hist = histogram(out_img)
    output_hist, _ = np.histogram(out_img.flat, bins=bins, density=True)
    # print(file_name, 'equalized', np.count_nonzero(output_hist))

    # %% plots
    '''
    plt.subplot(121)
    plt.imshow(raw_img, cmap='gray', norm=norm)
    plt.title("Raw " + file_name)

    plt.subplot(122)
    plt.imshow(out_img, cmap='gray', norm=norm)
    plt.title("Equalized " + file_name)
    # plt.savefig(file_name + "_comparison.png")
    plt.show()

    plt.title("Histogram of " + file_name)
    plt.bar(range(L), input_hist)
    plt.bar(range(L), output_hist)
    plt.legend(('raw image', 'equalized image'))
    # plt.savefig(file_name + "_histogram.png")
    plt.show()

    plt.plot(range(L), s)
    plt.title("Histogram equalization transformation for " + file_name)
    plt.xlabel('$r_k$')
    plt.ylabel('$s_k$')
    plt.show()
    '''

    return out_img, output_hist, input_hist, s


# %%

*_, trans_1 = hist_equ(file_name="Q3_1_1.tif")
*_, trans_2 = hist_equ(file_name="Q3_1_2.tif")

plt.plot(range(2 ** 8), trans_1)
plt.plot(range(2 ** 8), trans_2)
plt.title("Histogram equalization transformation")
plt.xlabel('$r_k$')
plt.ylabel('$s_k$')
plt.legend(('Q3_1_1.tif', 'Q3_1_2.tif'))
# plt.savefig("Q3_1_trans.png")
plt.show()
