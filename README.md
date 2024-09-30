# AI-Based Book Recommendation System

This project is an AI-driven book recommendation system that provides personalized book recommendations based on filters such as genre, author, price, and rating.

## Features

- **Filter by Genre, Author, Rating, and Price**: Get book recommendations based on multiple filters.
- **Content-Based Recommendations**: Uses cosine similarity to recommend books similar to a selected one.
- **Search by Keyword**: Find books by searching for keywords in the title.
- **List Available Genres and Subgenres**: Retrieve available genres and subgenres for easier selection.

## Installation

### Prerequisites

- Python 3.8 or higher

### Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/book-recommendation-system.git
    cd book-recommendation-system
    ```

2. **Set up a virtual environment** (optional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Prepare the Dataset**:
   Place the `books.csv` file in the `data/` directory.

5. **Run the Application**:
    ```bash
    python app.py
    ```

6. **Access the Application**:
   Visit `http://127.0.0.1:5000/` in your browser.

## Endpoints

- **/recommend (GET/POST)**: Get book recommendations based on filters.
- **/search (GET)**: Search for books by keyword in the title.
- **/genres (GET)**: List all available genres.
- **/subgenres (GET)**: Get subgenres for a given genre.
