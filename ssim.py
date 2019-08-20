from SSIM_PIL import compare_ssim
from PIL import Image
import time
import csv


def find_similarity(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    value = compare_ssim(image1, image2)
    return round((1 - value), 6)


def process_csv_file_images(input_path, output_path):
    with open(input_path) as input_file, open(
            output_path, "w+") as output_file:
        input_reader = csv.reader(input_file, delimiter=",")
        result_writer = csv.writer(output_file)
        header = ['image1', 'image2', 'similar', 'elapsed']
        result_writer.writerow([g for g in header])

        for i, x in enumerate(input_reader):
            if len(x) == 2:
                start_time = time.time()
                result = find_similarity(x[0], x[1])
                end_time = time.time() - start_time
                result_writer.writerow([x[0], x[1], result, end_time])
                print("processing time : ", result, end_time)
            else:
                print("Ignoring csv line ", x)
