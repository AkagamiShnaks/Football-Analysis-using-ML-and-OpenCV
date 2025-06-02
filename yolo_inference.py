from ultralytics import YOLO

model = YOLO(r"models\best.pt")


results = model.predict("input videos/C35bd9041_0 (39).mp4",save=True)
print(results[0])
print("--------------------------------")

for box in results[0].boxes:
        print(box)


