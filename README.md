# Student Sleep & Productivity Analyzer

## Overview
This project explores the relationship between sleep habits, screen time, caffeine intake, and student productivity using Python-based data analysis. The goal is to identify trends and correlations that impact academic focus and performance.

## Motivation
Sleep deprivation and excessive screen time are common issues among college students. This project analyzes lifestyle factors to better understand how daily habits may influence productivity and overall well-being.

## Dataset
The dataset used in this project is **synthetic student lifestyle data**, generated to reflect realistic behavioral patterns, including:
- Sleep duration
- Screen time
- Caffeine intake
- Study hours
- Self-reported productivity scores
- Mood indicators

Synthetic data was used to avoid privacy concerns while allowing controlled and reproducible analysis.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git & GitHub

## Analysis Performed
- Data loading and validation
- Exploratory data analysis
- Scatter plot visualizations
- Correlation analysis between lifestyle factors and productivity

## Key Findings
- Higher sleep duration generally correlates with higher productivity scores
- Increased screen time shows a mild negative relationship with productivity
- Caffeine intake does not fully offset the effects of insufficient sleep

## Project Structure
sleep-productivity-analyzer/
├── data/
│ └── sleep_data.csv
├── analysis.ipynb
├── generate_data.py
├── requirements.txt
└── README.md


## How to Run
1. Clone the repository
2. Install dependencies:
    pip install -r requirements.txt
3. Generate synthetic data:
    python3 generate_data.py
4. Launch Jupyter Notebook:
    jupyter notebook
5. Open `analysis.ipynb`

## Future Improvements
- Apply regression models to predict productivity
- Expand dataset with real survey data
- Build an interactive dashboard for visualization
- Perform statistical significance testing

## Author
Sam Inala
