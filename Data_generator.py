import os
import random
import shutil

def split_dataset(dataset_path, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    """
    Splits a dataset into training, validation, and testing sets based on the given ratios.

    Parameters:
    - dataset_path: Path to the dataset directory.
    - train_ratio: Proportion of the dataset to include in the train split.
    - val_ratio: Proportion of the dataset to include in the validation split.
    - test_ratio: Proportion of the dataset to include in the test split.
    """
    # Create directories for train, validation, and test sets
    train_dir = dataset_path + '/train'
    val_dir = dataset_path + '/val'
    test_dir = dataset_path + '/test'
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    print("Train, validation, and test directories created successfully.")

    class_folders = [folder for folder in os.listdir(dataset_path) if os.path.isdir(dataset_path+"/"+ folder)]

    # Split dataset for each class
    for class_folder in class_folders:
        class_path = dataset_path + "/" + class_folder
        images = os.listdir(class_path)
        random.shuffle(images)

        train_split = int(len(images) * train_ratio)
        val_split = train_split + int(len(images) * val_ratio)

        def copy_files(start_index, end_index, destination):
            for image in images[start_index:end_index]:
                src = class_path + "/" + image
                dst = destination + "/" + class_folder + "/" + image
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy(src, dst)

        copy_files(0, train_split, train_dir)
        copy_files(train_split, val_split, val_dir)
        copy_files(val_split, len(images), test_dir)

    print("Dataset split into train, validation, and test sets successfully.")

# Main function
def main():
    dataset_path = "./Multi-class Weather Dataset"
    split_dataset(dataset_path, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15)

if __name__ == "__main__":
    main()
