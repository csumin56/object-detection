# 카메라 기반 실시간 사물 인식

YOLOv8 모델을 이용해 카메라에서 실시간으로 사물을 인식하는 프로그램입니다.

## 환경 설정

```bash
pip install -r requirements.txt
```

## 실행 방법

```bash
python main.py
```

- 실행하면 카메라 화면이 열리고 인식된 사물에 박스와 라벨이 표시됩니다.
- `q`를 누르면 종료됩니다.
- YOLOv8 모델 파일(`yolov8n.pt`)은 최초 실행 시 자동으로 다운로드됩니다.

## 사용 모델

- **YOLOv8n** (nano): ultralytics에서 제공하는 경량 모델
- COCO 데이터셋 기준 80가지 사물 인식 가능 (사람, 자동차, 의자 등)

## 파일 구조

```
object-detection/
├── main.py            # 메인 프로그램
├── requirements.txt   # 필요 라이브러리
└── .gitignore
```
