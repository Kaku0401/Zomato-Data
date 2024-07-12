# Zomato Data Analysis

This project involves the analysis of a Zomato dataset to gain insights into various attributes such as restaurant types, votes, ratings, online orders, and approximate costs for two people. The analysis includes data cleaning, visualization, and summarization of key findings.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Analysis](#analysis)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/zomato-data-analysis.git
    ```

2. Navigate to the project directory:
    ```bash
    cd zomato-data-analysis
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place the Zomato dataset CSV file in the project directory.
2. Update the `file_path` variable in the script with the path to your CSV file.
3. Run the script:
    ```bash
    python analysis.py
    ```

The script will perform the following steps:
- Load the dataset.
- Clean and preprocess the data.
- Visualize the data through various plots.
- Summarize key findings.

## Dataset

The dataset used for this analysis should be a CSV file containing Zomato data with the following columns:
- `name`
- `rate`
- `votes`
- `online_order`
- `approx_cost(for two people)`
- `listed_in(type)`

## Analysis

The analysis includes the following steps:

1. **Loading the Dataset**: The script attempts to load the CSV file. If the file is not found or contains errors, appropriate error messages are displayed.

2. **Data Preprocessing**:
   - The `rate` column is cleaned by converting the ratings to float and handling non-numeric values.

3. **Data Visualization**:
   - **Count of Restaurant Types**: A count plot of different types of restaurants.
   - **Votes by Type of Restaurant**: A line plot showing the sum of votes for each restaurant type.
   - **Restaurant(s) with Maximum Votes**: Identification of the restaurant(s) with the highest votes.
   - **Count of Online Orders**: A count plot showing the distribution of online orders.
   - **Ratings Distribution**: A histogram showing the distribution of ratings.
   - **Approximate Cost for Two People**: A count plot of approximate costs for two people.
   - **Boxplot of Online Orders vs Rate**: A boxplot showing the relationship between online orders and ratings.
   - **Heatmap of Online Orders by Restaurant Type**: A heatmap showing the distribution of online orders across different restaurant types.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
