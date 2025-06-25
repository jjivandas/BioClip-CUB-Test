import os
import json

data_dir = "CUB_200_2011"

# 1. Read train/test split
id_to_train_or_test_split = {}
with open(os.path.join(data_dir, "train_test_split.txt"), "r") as f:
    for line in f:
        image_id, is_train = line.strip().split()
        id_to_train_or_test_split[int(image_id)] = int(is_train)

# 2. Read image paths
id_to_image_path = {}
with open(os.path.join(data_dir, "images.txt"), "r") as f:
    for line in f:
        image_id, rel_path = line.strip().split()
        id_to_image_path[int(image_id)] = rel_path

# 3. Read class labels (image_id → class_id)
id_to_image_label = {}
with open(os.path.join(data_dir, "image_class_labels.txt"), "r") as f:
    for line in f:
        image_id, class_id = line.strip().split()
        id_to_image_label[int(image_id)] = int(class_id)

# 4. Read class names (class_id → name)
class_id_to_name = {}
with open(os.path.join(data_dir, "classes.txt"), "r") as f:
    for line in f:
        class_id, class_name = line.strip().split()
        class_id_to_name[int(class_id)] = class_name

# 5. Build list of test images
test_data = []
for image_id in id_to_train_or_test_split:
    if id_to_train_or_test_split[image_id] == 0:  # test
        rel_path = id_to_image_path[image_id]
        label_id = id_to_image_label[image_id]
        label_name = class_id_to_name[label_id]
        test_data.append({
            "image_id": image_id,
            "img_path": os.path.join(data_dir, "images", rel_path),
            "label_id": label_id,
            "label_name": label_name
        })

# 6. Save as JSON
with open("test_data.json", "w") as f:
    json.dump(test_data, f, indent=2)

print(f"Saved {len(test_data)} test examples to test_data.json ✅")
