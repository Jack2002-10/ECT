# library
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt  # Import matplotlib for visualization
import processing_sample_5

# Updating these parameters if needed
filename = "test_0322.json"

# get the original data sets
x, z_real, z_imag = processing_sample_5.main(filename)
print("Data Loading Done!")

# Generate nice and neat x values with matching z_real and z_imag presentation
x_nice = []
z_nice_real = []
z_nice_imag = []
current = 0
while current <= 56:
    x_nice.append(round(current, 1))  # Round to 1 decimal place to avoid floating-point arithmetic issues


    for index in range(0, len(x)):
        x_raw = x[index]
        if x_raw > current:
            break
    # Subtract index by 1 to roll back to the previous value
    index -= 1
    z_nice_real.append(z_real[index])
    z_nice_imag.append(z_imag[index])

    current += 0.1

# Dataset for the real part
df_real = pd.DataFrame(z_nice_real)
df_flipped_real = df_real.T
df_flipped_real.columns = x_nice

# Dataset for the imaginary part
df_imag = pd.DataFrame(z_nice_imag)
df_flipped_imag = df_imag.T
df_flipped_imag.columns = x_nice

# Plot for the real part
plt.figure(figsize=(10, 8))
sns.heatmap(df_flipped_real)
plt.xlabel("Distance (cm)")
plt.ylabel("Channels")
plt.title("Real Impedance Defect Distribution")
plt.savefig("heatmap_real_distance.png", dpi=300)
plt.show()

# Plot for the imaginary part
plt.figure(figsize=(10, 8))  # Optional: Adjusts the size of the figure
sns.heatmap(df_flipped_imag)
plt.xlabel("Distance (cm)")
plt.ylabel("Channels")
plt.title("Imaginary Impedance Defect Distribution")
plt.savefig("heatmap_imaginary_distance.png", dpi=300)
plt.show()


