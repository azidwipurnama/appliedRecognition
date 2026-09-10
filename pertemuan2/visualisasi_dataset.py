import numpy as np
import matplotlib.pyplot as plt

def visualize_data(file_path):
    try:
        # Load the dataset
        data = np.load(file_path)
        print(f"Dataset loaded successfully with shape: {data.shape}")

        # Handling different potential shapes of the dataset
        if data.shape[1] == 2:
            x = data[:, 0]
            y = data[:, 1]
        elif data.shape[0] == 2:
            x = data[0, :]
            y = data[1, :]
        else:
            # Fallback if structure is unexpected
            print("Unexpected data shape, assuming index as X and values as Y")
            x = np.arange(len(data))
            y = data.flatten()

        # Create the visualization
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, alpha=0.5, color='blue', label='Dataset Points')
        plt.title('Visualisasi Data dari dataset_linier.npy')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.legend()

        # Save or show the plot
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    visualize_data('pertemuan2/dataset_linier.npy')
