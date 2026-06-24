import cv2
import time
from collections import Counter
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def run_detection(duration):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("카메라를 찾을 수 없습니다.")
        return

    detected = []
    start = time.time()

    while True:
        elapsed = time.time() - start
        if elapsed >= duration:
            break

        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)
        annotated = results[0].plot()

        remaining = int(duration - elapsed)
        cv2.putText(annotated, f"Time left: {remaining}s", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Object Detection", annotated)

        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            detected.append(label)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if not detected:
        print("탐지된 객체가 없습니다.")
        return

    most_common = Counter(detected).most_common(1)[0][0]
    print(f"\n객체는 {most_common} 입니다.")
    print("프로그램 종료")

def main():
    answer = input("객체 탐색을 시작하시겠습니까? (y/n): ").strip().lower()
    if answer != "y":
        print("프로그램 종료")
        return

    while True:
        try:
            duration = int(input("몇 초 동안 탐지하시겠습니까? (1~30): ").strip())
            if 1 <= duration <= 30:
                break
            print("1~30 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")

    print(f"\n{duration}초 동안 탐지를 시작합니다...\n")
    run_detection(duration)

if __name__ == "__main__":
    main()
