import pandas as pd
import io
import re
from flask import Flask, jsonify, render_template, request
# Initialize the Flask application
app = Flask(__name__)

def clean_data():
    """Loads and cleans the Amazon dataset."""
    df = pd.read_csv('data/amazon.csv', keep_default_na=False, na_values=[""])
    
    # --- Data Cleaning and Preprocessing ---
    
    # Clean price columns
    for col in ['discounted_price', 'actual_price']:
        df[col] = df[col].str.replace('₹', '').str.replace(',', '').astype(float)
        
    # Clean rating and rating_count
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df['rating_count'] = df['rating_count'].str.replace(',', '', regex=False).astype(float)
    
    # Clean discount_percentage
    df['discount_percentage'] = df['discount_percentage'].str.replace('%', '').astype(float) / 100
    
    # Create a primary category column
    df['main_category'] = df['category'].str.split('|').str[0]
    
    # Drop rows with missing essential data
    df.dropna(subset=['rating', 'rating_count'], inplace=True)
    
    return df

# Load and clean data once on startup
df = clean_data()

# --- Flask Routes ---

@app.route('/')
def home():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/api/analyze')
def analyze():
    """Provides the data analysis results as JSON."""
    try:
        # 1. First 5 Rows (converted to HTML)
        head_html = df.head().to_html(classes='table-auto w-full text-left whitespace-no-wrap', border=0, index=False)
        head_html = re.sub(r'<tr style="text-align: right;">', '<tr>', head_html) # Align headers left
        
        # 2. Data Info (captured from buffer)
        buffer = io.StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()
        
        # 3. Missing Values
        missing_values = df.isnull().sum()
        missing_output = missing_values[missing_values > 0].to_frame(name='missing_count').to_html(classes='table-auto w-full', border=0)

        # 4. Descriptive Statistics
        describe_html = df.describe(include='number').to_html(classes='table-auto w-full', border=0)

        # 5. Top 10 Main Categories (as a dictionary for charting)
        top_categories = df['main_category'].value_counts().nlargest(10).to_dict()
        
        # 6. Average Rating for Top Categories (as a dictionary for charting)
        top_cat_list = list(top_categories.keys())
        avg_rating_categories = df[df['main_category'].isin(top_cat_list)].groupby('main_category')['rating'].mean().round(2).sort_values(ascending=False).to_dict()

        # 7. Discount vs. Rating Insight
        correlation = df['discount_percentage'].corr(df['rating'])
        insight = f"The correlation between discount percentage and rating is {correlation:.2f}. "
        if correlation > 0.1:
            insight += "This suggests a weak positive relationship: slightly higher discounts may be associated with slightly higher ratings."
        elif correlation < -0.1:
            insight += "This suggests a weak negative relationship: higher discounts might be associated with slightly lower ratings."
        else:
            insight += "This suggests there is no significant linear relationship between discounts and customer ratings."

        # Consolidate results into a JSON object
        return jsonify({
            'head': head_html,
            'info': info_str,
            'missing': missing_output if not missing_values[missing_values > 0].empty else "<p>No missing values found. Great!</p>",
            'describe': describe_html,
            'top_categories': top_categories,
            'avg_rating_categories': avg_rating_categories,
            'discount_rating_insight': insight
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)