import cv2

def detect_people(image_file):
    # Load YOLO model
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    layers_names = net.getLayerNames()
    output_layers = [layers_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Read the image
    img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), -1)

    # Perform object detection
    height, width, _ = img.shape
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Analyze the results and count people
    people_count = 0
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and class_id == 0:  # Class 0 corresponds to people in COCO dataset
                people_count += 1

    return people_count
