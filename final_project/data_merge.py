import os
import pandas as pd

# Folder where this script is located
script_dir = os.path.dirname(__file__)

# Build absolute paths
gender_path = os.path.join(script_dir, "gender_data.csv")
age_path = os.path.join(script_dir, "age_data.csv")
brand_path = os.path.join(script_dir, "brand_data.csv")
feedback_path = os.path.join(script_dir, "feedback_data.csv")

# Read each CSV as single column, no header
gender_df = pd.read_csv(gender_path, header=None, names=["gender"])
age_df = pd.read_csv(age_path, header=None, names=["age"])
brand_df = pd.read_csv(brand_path, header=None, names=["brand"])
feedback_df = pd.read_csv(feedback_path, header=None, names=["feedback"])

# Merge side by side
combined_df = pd.concat([gender_df, age_df, brand_df, feedback_df], axis=1)
combined_df.insert(0, "id", range(1, len(combined_df) + 1))

# Save to one CSV
output_path = os.path.join(script_dir, "coffeeX_feedback.csv")
combined_df.to_csv(output_path, index=False)

print(f"CSV file created at: {output_path}")
