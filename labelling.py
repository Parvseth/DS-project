import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer

# Step 1: Load the combined data
combined_data = pd.read_excel("combined_data.xlsx")

# Step 2: Separate features and target (artist label)
X = combined_data.drop('artist', axis=1)  # Features (all columns except 'artist')
y = combined_data['artist']  # Target variable (artist names)

# Step 3: Convert all columns in X to numeric (if applicable)
X = X.apply(pd.to_numeric, errors='coerce')  # Convert to numeric, invalid parsing will be NaN

# Step 4: Check for missing values
print(f"Number of missing values before imputation: {X.isna().sum().sum()}")

# Step 5: Impute missing values with a SimpleImputer
imputer = SimpleImputer(strategy='mean')  # Can change strategy to 'median' or 'most_frequent'
X_imputed = imputer.fit_transform(X)  # Impute missing values

# Step 6: Ensure there are no remaining missing values after imputation
print(f"Number of missing values after imputation: {pd.isna(X_imputed).sum().sum()}")

# Step 7: Convert column names to strings (if necessary)
X_imputed = pd.DataFrame(X_imputed, columns=X.columns)  # Convert back to DataFrame and retain column names

# Step 8: Label Encoding for artist names
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)  # Convert artist names to numerical labels

# Step 9: Feature Scaling (using StandardScaler)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)  # Apply scaling to the features

# Step 10: Train-Test Split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Output the sizes of the train-test sets
print(f"Training set size: {X_train.shape[0]} samples")
print(f"Test set size: {X_test.shape[0]} samples")
