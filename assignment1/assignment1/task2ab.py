import matplotlib.pyplot as plt
import pathlib
from utils import read_im, save_im
output_dir = pathlib.Path("image_solutions")
output_dir.mkdir(exist_ok=True)


im = read_im(pathlib.Path("images", "duck.jpeg"))
plt.imshow(im)
def greyscale(im):
    """ Converts an RGB image to greyscale
    Args:
        im ([type]): [np.array of shape [H, W, 3]]

    Returns:
        im ([type]): [np.array of shape [H, W]]
    """
    for i, row in enumerate(im):
        for j, pixel in enumerate(row):
            R = im[i][j][0]
            G = im[i][j][1]
            B = im[i][j][2]
            grey = 0.212*R + 0.7152*G + 0.0722*B
            im[i][j] = grey
    return im


im_greyscale = greyscale(im)
save_im(output_dir.joinpath("gray_duck.jpeg"), im_greyscale, cmap="gray")
# plt.figure()
plt.imshow(im_greyscale, cmap="gray")
plt.show()

def inverse(im):
    """ Finds the inverse of the greyscale image

    Args:
        im ([type]): [np.array of shape [H, W]]

    Returns:
        im ([type]): [np.array of shape [H, W]]
    """
    for i, row in enumerate(im):
        for j, pixel in enumerate(row):
            grey = im[i][j]
            im[i][j] = 255 - grey
    return im

im_inverted = inverse(im_greyscale)
save_im(output_dir.joinpath("inverted_duck.jpeg"), im_inverted, cmap="gray")
exit()