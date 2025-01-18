
import pandas as pd

# Load the dataset
file_path = 'portfolio_data.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Convert the "Date" column to a proper datetime format for better compatibility with Tableau
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')

# Save the cleaned data to a new CSV file for Tableau use
output_path = 'cleaned_portfolio_data.csv'  # Replace with your desired output path
data.to_csv(output_path, index=False)

print(f'Cleaned data saved to {output_path}')
