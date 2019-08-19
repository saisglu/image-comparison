from ssim import find_similarity
import logging


def test_similarity():
    logging.info("must be true if list is empty")
    image1_path = "/Users/SaiKumarShailu/Desktop/pyprojects/image-comparison/21.jpeg"
    image2_path = "/Users/SaiKumarShailu/Desktop/pyprojects/image-comparison/23.jpeg"
    expect_similar_value = 0.5
    result = find_similarity(image1_path, image2_path)
    assert result == expect_similar_value
