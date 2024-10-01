from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from recommendation import recommend_by_filters, get_books, get_books_by_keyword, get_genres, get_subgenres
from utils import sort_books

app = Flask(__name__)
CORS(app)  

books = get_books()

@app.route('/')
def home():
    return render_template('index.html')

# Create a POST/GET route for book recommendations by title, genre, or other filters
@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    filters = {}
    # Handle POST requests (JSON or form)
    if request.method == 'POST':
        if request.is_json:  # If the request contains JSON
            print("request is json")
            filters = request.get_json() or {}
        elif request.form:  # If the request contains form data
            print("request form")
            filters['genre'] = request.form.get('genre')
            filters['author'] = request.form.get('author')
            filters['rating'] = float(request.form.get('rating')) if request.form.get('rating') else None
            
            # Check if price range is provided in the form
            min_price = request.form.get('min_price')
            max_price = request.form.get('max_price')
            if min_price or max_price:
                filters['price_range'] = [
                    float(min_price or 0), float(max_price or float('inf'))
                ]

    # Handle GET requests (Query parameters)
    elif request.method == 'GET':
        # Extract filters from query parameters
        genre = request.args.get('genre')
        author = request.args.get('author')
        rating = request.args.get('rating')
        min_price = request.args.get('min_price')
        max_price = request.args.get('max_price')

        # Add filters only if they are provided
        if genre:
            filters['genre'] = genre
        if author:
            filters['author'] = author
        if rating:
            filters['rating'] = float(rating) if rating else None
        
        # Only add the price range filter if either min_price or max_price is provided
        if min_price or max_price:
            filters['price_range'] = [
                float(min_price or 0), float(max_price or float('inf'))
            ]

    print(f"Filters received: {filters}")

    # Pass the filters to the recommendation function
    recommendations = recommend_by_filters(filters)
    return jsonify(recommendations)

# for searching books by keyword
@app.route('/search', methods=['GET'])
def search_books():
    # Retrieve the keyword from query parameters
    keyword = request.args.get('keyword', '').lower()

    if not keyword:
        return "Please provide a keyword in the query parameters, e.g., ?keyword=some_keyword"

    matching_books = get_books_by_keyword(keyword)

    # If the result is a string (error message), return it
    if isinstance(matching_books, str):
        return matching_books

    # Return the matching book titles as a JSON response
    return jsonify(matching_books)

# for retrieving all available authors
@app.route('/authors', methods=['GET'])
def authors():
    authors = books['author'].unique().tolist()
    return jsonify(authors)


# for retrieving available genres
@app.route('/genres', methods=['GET'])
def genres():
    return jsonify(get_genres())


if __name__ == '__main__':
    app.run(debug=True)
