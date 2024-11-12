import os

# Path to the directory containing YOLO annotation files
ANNOTATIONS_DIR = 'D:/AfterGrad Ex/Computer Vision/Autonomous Driving car/train_20241023/daytime'

# Function to update a single annotation file
def update_annotation(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        parts = line.strip().split()
        if parts:  # Ensure it's not an empty line
            class_id = int(parts[0])
            # Update class IDs: 0 -> 1, 1 -> 2, 2 -> 3, 3 -> 4
            if class_id in range(4):  # Only update class IDs 0 to 3
                class_id += 1
            parts[0] = str(class_id)
            updated_lines.append(' '.join(parts) + '\n')

    # Write updated annotations back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

# Loop through all .txt files in the annotations directory
def update_all_annotations():
    for file_name in os.listdir(ANNOTATIONS_DIR):
        if file_name.endswith('.txt'):
            file_path = os.path.join(ANNOTATIONS_DIR, file_name)
            update_annotation(file_path)
            print(f'Updated {file_name}')

if __name__ == '__main__':
    update_all_annotations()
