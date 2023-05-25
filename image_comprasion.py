import cv2
import os
import time
import numpy as np
from skimage.metrics import structural_similarity as ssim

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def calculate_similarity(imageA, imageB):
    imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    return ssim(imageA, imageB)

def find_similar_images(images):
    similarity_list = []
    for i in range(len(images)):
        for j in range(i + 1, len(images)):
            similarity = calculate_similarity(images[i], images[j])
            similarity_list.append((i, j, similarity))

    # Sort the list in descending order of similarity
    similarity_list.sort(key=lambda x: x[2], reverse=True)

    return similarity_list

def find_similar_images_in_folder(folder_path):
    images = load_images_from_folder(folder_path)
    similarity_list = find_similar_images(images)
    return similarity_list

folder_path =  r"C:\Users\leyla\Downloads\pythonProject2\ALGORTIMA_ANALIZI_ODEV_SOURCES"

baslama_zamani = time.time()
similarity_list = find_similar_images_in_folder(folder_path)
bitis_zamani = time.time()

for i, j, score in similarity_list:
    print(f"Görüntüler {i} ve {j} benzerlik skoru {score} ile benzer.")

num_images = len(load_images_from_folder(folder_path))
comparisons = num_images * (num_images - 1) / 2
print(f"Görseller arasındaki toplam karşılaştırmalar: {int(comparisons)}")

print(f"Harcanan süre: {bitis_zamani - baslama_zamani} saniye")




