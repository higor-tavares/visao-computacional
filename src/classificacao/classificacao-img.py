import cv2
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier
# Método auxiliar para transfomar, uma lista de listas, em uma lista
def transforma_lista(valores):
    lista = []
    aux = valores.tolist()
    for val in aux:
        lista.append(val[0])
    return lista
# Método que pega um conjunto de imagens e 
# retronar uma lista de caracteriticas invariaveis
def extrai_caracteristicas():
    caracteristicas = []
    for i in range(1,11):
        img = cv2.imread('../../img/treinamento/engrenagem-'+str(i)+'.bmp',0)
        moments = cv2.moments(img)
        hu_moments = cv2.HuMoments(moments)
        lista = -np.sign(hu_moments)*np.log10(np.abs(hu_moments))
        lista = transforma_lista(lista)
        caracteristicas.append(lista)
    return caracteristicas
# Utilizando um algoritimo de 
# classificação supervisionado
def main():
    classificacoes = [1,1,1,1,1,1,0,0,0,0]
    caracteristicas = extrai_caracteristicas()
    knn = KNeighborsClassifier(5)
    knn.fit(caracteristicas, classificacoes)
    # Objeto de teste 1
    p1 = cv2.imread('../../img/teste/coisa.bmp',0)
    m1 = cv2.moments(p1)
    hm1 = cv2.HuMoments(m1)
    l1 = -np.sign(hm1)*np.log10(np.abs(hm1))
    l1 = transforma_lista(l1)
    # Objeto de teste 2
    p2 = cv2.imread('../../img/teste/puzzle.bmp',0)
    m2 = cv2.moments(p2)
    hm2 = cv2.HuMoments(m2)
    l2 = -np.sign(hm2)*np.log10(np.abs(hm2))
    l2 = transforma_lista(l2)
    # tranformando l1 e l2 em uma lista de listas
    l1 = [l1]
    l2 = [l2]
    # Verifica se l1 é uma engrenagem
    t1 = 'Imagem p1 representa uma engrenagem? '+ (knn.predict(l1)[0]==1 and 'Sim' or 'Nao')
    # Verifica se l2 é uma engrenagem
    t2 = 'Imagem p2 representa uma engrenagem? '+(knn.predict(l2)[0]==1 and 'Sim' or 'Nao')
    cv2.imshow(t1,p1)
    cv2.imshow(t2,p2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()

