import matplotlib.pyplot as plt
import pathlib
import numpy as np
from utils import read_im, save_im, normalize
output_dir = pathlib.Path("image_solutions")
output_dir.mkdir(exist_ok=True)


im = read_im(pathlib.Path("images", "duck.jpeg"))


def convolve_im(im, kernel,
                ):
    """ A function that convolves im with kernel

    Args:
        im ([type]): [np.array of shape [H, W, 3]]
        kernel ([type]): [np.array of shape [K, K]]

    Returns:
        [type]: [np.array of shape [H, W, 3]. should be same as im]
    """
    assert len(im.shape) == 3
    flipped_kernel = np.flipud(np.fliplr(kernel))
    kernel_size = len(kernel)
    kernel_offset = int((kernel_size-1)/2)
    x_size = im.shape[0]
    y_size = im.shape[1]
    red = im[:,:,0]
    green = im[:,:,1]
    blue = im[:,:,2]

    convolved = np.zeros((x_size, y_size,3))
    for i in range(kernel_offset,x_size-kernel_offset):
        for j in range(kernel_offset,y_size-kernel_offset):
            convolved[i][j][0] = np.tensordot(kernel, red[i-kernel_offset:i+kernel_offset+1,j-kernel_offset:j+kernel_offset+1])
            convolved[i][j][1] = np.tensordot(kernel, green[i-kernel_offset:i+kernel_offset+1,j-kernel_offset:j+kernel_offset+1])
            convolved[i][j][2] = np.tensordot(kernel, blue[i-kernel_offset:i+kernel_offset+1,j-kernel_offset:j+kernel_offset+1])
    
    return convolved


if __name__ == "__main__":
    # Define the convolutional kernels
    h_b = 1 / 256 * np.array([
        [1, 4, 6, 4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1, 4, 6, 4, 1]
    ])
    sobel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])


    # Convolve images
    im_smoothed = convolve_im(im.copy(), h_b)
    save_im(output_dir.joinpath("im_smoothed.jpg"), im_smoothed)
    print("Done with smoothening")
    im_sobel = convolve_im(im, sobel_x)
    print(im_sobel)
    save_im(output_dir.joinpath("im_sobel.jpg"), im_sobel)

    # DO NOT CHANGE. Checking that your function returns as expected
    assert isinstance(
        im_smoothed, np.ndarray),         f"Your convolve function has to return a np.array. " + f"Was: {type(im_smoothed)}"
    assert im_smoothed.shape == im.shape,         f"Expected smoothed im ({im_smoothed.shape}" + \
        f"to have same shape as im ({im.shape})"
    assert im_sobel.shape == im.shape,         f"Expected smoothed im ({im_sobel.shape}" + \
        f"to have same shape as im ({im.shape})"
    
    plt.figure("Hej")

    plt.subplot(2, 2, 1)
    plt.imshow(normalize(im_smoothed))

    plt.subplot(2, 2, 2)
    plt.imshow(normalize(im_sobel))

    plt.subplot(2,2,3)
    plt.imshow(im)
    plt.show()
