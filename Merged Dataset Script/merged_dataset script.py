import os
import glob

# Define dataset paths
datasets_root = "/content/"
dataset_paths = [
    "Dataset-for-YOLO-CSE-233--5",
    "data-2"
]

# Define the class mappings (update based on both datasets)
label_map = {
    "Dataset-for-YOLO-CSE-233--5": {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5},  # Existing dataset mapping
    "data-2": {0: 6, 1: 6}  # Boat -> 6, Ship -> 6 (Both merged into 'ship')
}

# Iterate through all dataset directories
for dataset in dataset_paths:
    for split in ["train", "valid", "test"]:
        labels_dir = os.path.join(datasets_root, dataset, split, "labels")

        # Ensure label directory exists
        if not os.path.exists(labels_dir):
            print(f" Skipping {dataset}/{split}, labels not found.")
            continue

        # Iterate over all `.txt` annotation files
        label_files = glob.glob(os.path.join(labels_dir, "*.txt"))

        for label_file in label_files:
            new_lines = []
            with open(label_file, "r") as f:
                lines = f.readlines()

            # Update class IDs based on mapping
            for line in lines:
                parts = line.strip().split()
                old_class = int(parts[0])

                if old_class in label_map[dataset]:
                    new_class = label_map[dataset][old_class]
                    parts[0] = str(new_class)  # Update class ID
                    new_lines.append(" ".join(parts))

            # Overwrite the file with updated labels
            with open(label_file, "w") as f:
                f.write("\n".join(new_lines))

            print(f"Updated labels in {label_file}")

print("\n Label Update Completed Successfully! All 'boat' labels are now 'ship'.")
