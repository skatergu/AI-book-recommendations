import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

books = pd.read_csv('../data/books.csv')
# Clean up column names: strip spaces and convert to lowercase
books.columns = books.columns.str.strip().str.lower()
# Rename 'main genre' to 'genre' to simplify
books = books.rename(columns={'main genre': 'genre'})
# Convert price column from string with ₹ to a float
books['price'] = books['price'].replace({'₹': '', ',': ''}, regex=True).astype(float)
# Conversion rate from INR to USD 
conversion_rate = 84

# Convert the 'Price' column to USD
books['price'] = books['price'] / conversion_rate
books['price'] = books['price'].round(2)

books['author'] = books['author'].fillna('')


# Preprocess book genres for content-based filtering
count_vectorizer = CountVectorizer(stop_words='english')
count_matrix_main_genre = count_vectorizer.fit_transform(books['genre'])  # Use 'main genre' column
cosine_sim = cosine_similarity(count_matrix_main_genre, count_matrix_main_genre)
# print("Columns in the CSV file:", books.columns.tolist())

def get_books():
    return books

# Helper function to get recommendations based on filters (title, genre, author, etc.)
def recommend_by_filters(filters):
    filtered_books = books.copy()

    condition = pd.Series([True] * len(books))

    # Filter by title (finding similar titles)
    if filters.get('title'):
        print("filter by title")
        condition = condition & books['title'].str.contains(filters['title'], case=False, na=False)

    # Filter by genre
    if filters.get('genre'):
        print(f"Filtering by genre: {filters['genre']}")
        condition = condition & (books['genre'].str.lower() == filters['genre'].lower())
        print(f"Condition after genre filter: {condition.sum()} matches")

    # Filter by author
    if filters.get('author'):
        print(f"Filtering by author: {filters['author']}")
        condition = condition & (books['author'].str.lower() == filters['author'].lower())
        print(f"Condition after author filter: {condition.sum()} matches")

    # Filter by type (book format)
    if filters.get('type'):
        print(f"Filtering by type: {filters['type']}")
        condition = condition & (books['type'].str.lower() == filters['type'].lower())
        print(f"Condition after type filter: {condition.sum()} matches")

    # Filter by price range
    if 'price_range' in filters:
        min_price = filters['price_range'][0] if filters['price_range'][0] is not None else 0
        max_price = filters['price_range'][1] if filters['price_range'][1] is not None else float('inf')

        # Only apply price filter if it is specified with meaningful values
        if min_price != 0 or max_price != float('inf'):
            print(f"Filtering by price range: {min_price} - {max_price}")
            condition = condition & ((books['price'] >= min_price) & (books['price'] <= max_price))
            print(f"Condition after price filter: {condition.sum()} matches")

    # Filter by rating
    if filters.get('rating') is not None:
        condition = condition & (books['rating'] >= filters['rating'])

    # Apply AND condition based on the filters
    filtered_books = books[condition]

    # Sort by cosine similarity (if 'title' is provided and exists in the dataset)
    if filters.get('title') and filters['title'].lower() in books['title'].str.lower().values:
        title = filters['title'].lower()
        idx = books[books['title'].str.lower() == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]  # Exclude the first one because it's the same book
        book_indices = [i[0] for i in sim_scores]
        similar_books = books.iloc[book_indices]

        # Combine similarity-based recommendations with filtered books
        filtered_books = pd.concat([filtered_books, similar_books]).drop_duplicates()


    # If no books match, return an empty list
    if filtered_books.empty:
        print("No books matched the filters.")
        return []

    return filtered_books[['title', 'author', 'price']].to_dict(orient='records')


    # return filtered_books['title'].tolist()
    # return filtered_books.to_dict(orient='records')



# Helper function to get books by keyword
def get_books_by_keyword(keyword):
    keyword = keyword.lower()
    matching_books = books[books['title'].str.lower().str.contains(keyword)]

    if matching_books.empty:
        return f"No books found matching the keyword '{keyword}'."
    
    return matching_books['title'].tolist()

# Function to get available genres
def get_genres():
    return books['genre'].unique().tolist()

# Function to get available subgenres for a given genre
def get_subgenres(genre):
    return books[books['genre'].str.lower() == genre.lower()]['sub genre'].unique().tolist()
