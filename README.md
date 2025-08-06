# Amazon Product Data Explorer

This is a straightforward web application for doing Exploratory Data Analysis (EDA) on an Amazon sales dataset. The application has a Flask (Python) backend and a modern HTML/CSS/JavaScript frontend.

## Features

- **One-Click Analysis**: A simple user interface to start the data analysis.
- **Dynamic Visualizations**: Key insights appear in clear tables and interactive bar charts.
- **Comprehensive Overview**: The analysis includes:
    - A preview of the first few rows of data.
    - Data schema details and non-null counts.
    - A check for missing values.
    - Descriptive statistics for numerical columns.
    - A bar chart of the Top 10 product categories.
    - A bar chart showing the average user rating for those top categories.
    - An insight into how product discounts relate to ratings.

## How to Run

Follow these steps to run the application on your local machine.

### 1. Prerequisites

- Python 3.6 or newer
- `pip` for installing packages

### 2. Setup

**a. Clone the Repository (or create the files)**

If this were a Git repository, you would clone it. Since you have the files, just ensure they are organized as shown above.

**b. Download the Dataset**

- Download the dataset from **[Kaggle: Amazon Sale Dataset](https://www.kaggle.com/datasets/sohommajumder/amazon-sale-dataset)**.
- Rename the downloaded file to `amazon.csv`.
- Place it in the `data/` folder.

**c. Install Dependencies**

Open your terminal or command prompt, navigate to the project's root directory (`amazon-eda-project/`), and run:

```bash
pip install -r requirements.txt
