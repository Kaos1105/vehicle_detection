import os

# Define class ID mapping
class_id_mapping = {
    4: 0,
    5: 1,
    6: 2,
    7: 3
}

# Folder containing the annotation .txt files
folder_path = './train_20241023/nighttime'

# Iterate through each .txt file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        
        # Read the content of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Create a list to store the updated annotations
        updated_lines = []
        
        for line in lines:
            # Split the line into components
            parts = line.strip().split(' ')
            
            # Get the current class ID
            current_class_id = int(parts[0])
            
            # Update the class ID if it matches the mapping
            if current_class_id in class_id_mapping:
                parts[0] = str(class_id_mapping[current_class_id])
            
            # Reconstruct the line and add to the updated list
            updated_lines.append(' '.join(parts))
        
        # Write the updated lines back to the file
        with open(file_path, 'w') as file:
            file.write('\n'.join(updated_lines))
        
        print(f"Updated {filename}")

print("Class ID update complete.")
