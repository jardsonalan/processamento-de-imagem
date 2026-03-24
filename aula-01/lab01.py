# Bibliotecas
import os
import cv2
import matplotlib.pyplot as plt

# Carregar imagem
base_dir = os.path.dirname(__file__) # Armazena o diretório do arquivo
img_path = os.path.join(base_dir, 'images', 'image.png') # Cria o caminho até a imagem
img = cv2.imread(img_path, 0)

# Validação de carregamento da imagem
if img is None:
  print('Erro ao carregar a imagem.')
  exit()

# Detectar bordas
sobel = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=5)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
canny = cv2.Canny(img, 100, 200)

# Imprimir resultados
plt.subplot(1, 3, 1); plt.title('Sobel'); plt.imshow(sobel, cmap='gray')
plt.subplot(1, 3, 2); plt.title('Laplacian'); plt.imshow(laplacian, cmap='gray')
plt.subplot(1, 3, 3); plt.title('Canny'); plt.imshow(canny, cmap='gray')

plt.show()