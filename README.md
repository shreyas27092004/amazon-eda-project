
## Amazon Product Data Explorer

A simple web application for performing **Exploratory Data Analysis (EDA)** on an Amazon sales dataset.
The backend is built with **Flask (Python)** and the frontend uses **HTML, CSS, and JavaScript**.

---

### **Features**

* **One-Click Analysis**: Start analyzing the dataset instantly from the web interface.
* **Dynamic Visualizations**: View clear tables and interactive bar charts.
* **Comprehensive Overview**:

  * Preview of the first few rows of data.
  * Dataset schema with column names and non-null counts.
  * Missing value detection.
  * Descriptive statistics for numerical columns.
  * Bar chart of **Top 10 product categories**.
  * Bar chart of **average user ratings** for those top categories.
  * Insights into the relationship between **discounts** and **ratings**.

---

### **How to Run**

#### **1. Prerequisites**

* Python **3.6+**
* `pip` (Python package installer)

#### **2. Setup**

**a. Organize the Project**
Ensure your files are structured like this:

```
amazon-eda-project/
│
├── app.py
├── requirements.txt
├── static/
├── templates/
├── data/
│   └── amazon.csv
```

**b. Download the Dataset**

1. Download the dataset from **Kaggle**: [Amazon Sale Dataset](https://www.kaggle.com/datasets)
2. Rename the downloaded file to:

```
amazon.csv
```

3. Place it inside the `data/` folder.

**c. Install Dependencies**
In your terminal or command prompt, navigate to the project folder and run:

```bash
pip install -r requirements.txt
```

---

#### **3. Run the Application**

```bash
python app.py
```

#### **4. Open in Browser**

Go to:

```
http://127.0.0.1:5000
```

You’ll now be able to explore the Amazon dataset interactively.

---
