# Book Recommendation System

This project is a similarity-based book recommendation system that provides personalized book recommendations based on various filters such as title, genre, author, price, and rating. It also allows users to list available genres and authors for easier selection.

## Features

- **Filter by Title, Genre, Author, Rating, and Price**: Get personalized book recommendations using multiple filters.
- **Content-Based Recommendations**: Uses cosine similarity to recommend books similar to a selected one.
- **Search by Keyword**: Find books by searching for keywords in the title.
- **List Available Genres and Authors**: Retrieve available genres and authors for easier selection.
- **Display of Available Filters**: Buttons to display available genres and authors, dynamically loaded via the UI.
- **Interactive Form**: Users can enter filters through an easy-to-use form to get recommendations.
- **Flexible Filtering**: Users can input any combination of filters (title, genre, author, rating, and price range) to get recommendations. Filters are case-insensitive and support partial matching.

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
