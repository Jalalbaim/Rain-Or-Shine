import os
import random
import shutil

def split_dataset(dataset_path, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    # Create train, validation, and test directories
    train_dir = os.path.join(dataset_path, 'train')
    val_dir = os.path.join(dataset_path, 'val')
    test_dir = os.path.join(dataset_path, 'test')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    print("Train, validation, and test directories created successfully.")

    # Get class folders
    class_folders = [folder for folder in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, folder))]

    # Split dataset for each class
    for class_folder in class_folders:
        class_path = os.path.join(dataset_path, class_folder)
        images = os.listdir(class_path)
        random.shuffle(images)

        # Calculate split indices
        train_split = int(len(images) * train_ratio)
        val_split = train_split + int(len(images) * val_ratio)

        # Move images to train directory
        for image in images[:train_split]:
            src = os.path.join(class_path, image)
            dst = os.path.join(train_dir, class_folder, image)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy(src, dst)

        # Move images to validation directory
        for image in images[train_split:val_split]:
            src = os.path.join(class_path, image)
            dst = os.path.join(val_dir, class_folder, image)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy(src, dst)

        # Move images to test directory
        for image in images[val_split:]:
            src = os.path.join(class_path, image)
            dst = os.path.join(test_dir, class_folder, image)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy(src, dst)

    print("Dataset split into train, validation, and test sets successfully.")

def __main__():
    dataset_path = "./Multi-class Weather Dataset"
    split_dataset(dataset_path, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15)


if __name__ == "__main__":
    __main__()
