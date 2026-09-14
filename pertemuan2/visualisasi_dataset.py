import numpy as np
import matplotlib.pyplot as plt

def visualize_data(file_path):
    try:
        # Load the dataset
        data = np.load(file_path)
        print(f"Dataset loaded successfully with shape: {data.shape}")

        # The dataset stores rows as (y, x), so column 0 is y, column 1 is x
        x = data[:, 1]
        y = data[:, 0]

        # Create the visualization with a dark background style
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(10, 6), facecolor='black')
        ax.set_facecolor('black')

        # Scatter plot with cyan points, similar to the reference image
        scatter = ax.scatter(x, y, c='#00FFFF', alpha=0.6, s=30, edgecolors='none', zorder=3)

        # Axis and grid styling for dark background
        ax.set_title('Dataset Linier', color='white', fontsize=14, fontweight='bold')
        ax.set_xlabel('X', color='white', fontsize=12)
        ax.set_ylabel('Y', color='white', fontsize=12)
        ax.tick_params(colors='white', which='both')

        # Grid lines styled for visibility on black
        ax.grid(True, linestyle='--', alpha=0.3, color='gray')

        # Spines in white
        for spine in ax.spines.values():
            spine.set_color('white')
            spine.set_linewidth(0.5)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    visualize_data('pertemuan2/dataset_linier.npy')
