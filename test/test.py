import cv2
from skimage.metrics import structural_similarity as ssim

# 
def calculate_similarity(imageA_path, imageB_path):
    # 이미지 받아오기
    # cv2.IMREAD_GRAYSCALE <- 조건
    # 회색조로 불러와서 저장
    imageA = cv2.imread(imageA_path, cv2.IMREAD_GRAYSCALE)
    imageB = cv2.imread(imageB_path, cv2.IMREAD_GRAYSCALE)
    
    # 이미지 A, B 모양 비교
    if imageA.shape != imageB.shape:
        # 세로, 가로 빼와서 비교하겠단거
        heigth, width = imageA.shape
        # 이미지 B를 리사이즈 하는거(리사이즈란? -> 사이즈 맞추는거..?
        # (해상도는 그대로), crop -> 자르는거)

        imageB = cv2.resize(imageB, (width, heigth))

    # 유사도 검사해주는 함수(유사도 검사 후 변수에 저장)
    similarity_index = ssim(imageA, imageB)
    
    # 유사도 출력(소수점 2자리까지)
    print(f"이미지 유사도 : {similarity_index * 100:.2f}%")

imageA_path = '0.jpg'
imageB_path = '1.jpg'

calculate_similarity(imageA_path, imageB_path)