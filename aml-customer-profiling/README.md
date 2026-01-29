# AML Customer Profiling Project

This project focuses on customer profiling and segmentation using machine learning techniques. The goal is to identify distinct customer groups based on behavioral patterns and characteristics.

## Project Structure

- **data/**: Contains raw and processed data
  - `raw/`: Original dataset
  - `processed/`: Cleaned and processed datasets

- **notebooks/**: Jupyter notebooks for analysis and modeling
  - `01_data_understanding.ipynb`: Initial data exploration
  - `02_data_cleaning.ipynb`: Data cleaning and preprocessing
  - `03_eda.ipynb`: Exploratory data analysis
  - `04_customer_profiling.ipynb`: Customer profiling and segmentation
  - `05_modeling.ipynb`: Machine learning models

- **src/**: Python source code
  - `data_loader.py`: Data loading utilities
  - `cleaning.py`: Data cleaning functions
  - `features.py`: Feature engineering
  - `modeling.py`: Model training and prediction
  - `evaluation.py`: Model evaluation metrics

- **configs/**: Configuration files
  - `config.yaml`: Project configuration parameters

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start with the notebooks in order (01 through 05) for a complete analysis workflow.

3. Run individual scripts from the `src/` directory for specific tasks.

## Dataset

The project uses the AML (Anti-Money Laundering) customer profiling dataset:
- `PS_20174392719_1491204439457_log.csv`

## License

Project License Information Here
