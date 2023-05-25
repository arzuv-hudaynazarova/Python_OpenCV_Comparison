import cv2
import os
import time
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Belirtilen klasörden resimleri yükleris
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


# İki resim arasındaki benzerlik skorunu hesaplarıs
def calculate_similarity(imageA, imageB):
    imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # Görüntüler küçük olanın boyutlarına yeniden boyutlandırılır
    if imageA.shape != imageB.shape:
        height = min(imageA.shape[0], imageB.shape[0])
        width = min(imageA.shape[1], imageB.shape[1])
        imageA = cv2.resize(imageA, (width, height))
        imageB = cv2.resize(imageB, (width, height))

    return ssim(imageA, imageB)


# Görüntüler arasındaki benzerlik skorlarını bulurus
def find_similar_images(images):
    similarity_list = []
    for i in range(len(images)):
        for j in range(i + 1, len(images)):
            similarity = calculate_similarity(images[i], images[j])
            similarity_list.append((i, j, similarity))

    # Benzerlik skorlarına göre listeyi büyükten küçüğe sıralar
    similarity_list.sort(key=lambda x: x[2], reverse=True)

    return similarity_list

# Belirtilen klasördeki görüntüler arasında benzer olanları bulurus
def find_similar_images_in_folder(folder_path):
    images = load_images_from_folder(folder_path)
    similarity_list = find_similar_images(images)
    return similarity_list

folder_path =  r"C:\Users\leyla\Downloads\pythonProject2\ALGORTIMA_ANALIZI_ODEV_SOURCES"

baslama_zamani = time.time()
similarity_list = find_similar_images_in_folder(folder_path)
bitis_zamani = time.time()

# Benzerlik skoru tam 1 olan görüntü çiftlerini ekranda yazdırırıs
for i, j, score in similarity_list:
    if score == 1.0:
        print(f"Görüntüler {i} ve {j} benzerlik skoru {score} ile benzer.")

# Toplamda kaç karşılaştırma yapıldığını hesaplarıs
num_images = len(load_images_from_folder(folder_path))
comparisons = num_images * (num_images - 1) / 2
print(f"Görseller arasındaki toplam karşılaştırmalar: {int(comparisons)}")

# Hesaplamanın ne kadar süre aldığını yazdırırıs
print(f"Harcanan süre: {bitis_zamani - baslama_zamani} saniye")









