import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(0)

# Generate study time between 20 and 80
study_time = np.random.uniform(20, 80, 100)

# Generate marks between 0 and 100 with some noise
marks = 0.5 * study_time + np.random.normal(0, 10, 100)  # Linear relationship with noise

# Introduce some outliers in the marks
outlier_indices = np.random.choice(range(100), size=5, replace=False)
marks[outlier_indices] = np.random.uniform(0, 100, 5)  # Random outliers between 0 and 100

# Create a DataFrame
df = pd.DataFrame({
    'StudyTime': study_time,
    'Marks': marks
})

# Save to CSV
df.to_csv('study_time_marks.csv', index=False)

print("CSV file 'study_time_marks.csv' created successfully.")
