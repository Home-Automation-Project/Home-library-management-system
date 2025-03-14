How It Works
	1.	Google Books API: Checks first for book details.
	2.	Open Library API: Used as a fallback if Google Books has no data.
	3.	Returns:
	•	Title
	•	Authors
	•	Publisher
	•	Published Date
	•	Description
	•	Page Count
	•	Categories
	•	Thumbnail (Cover Image URL)

import requests

def get_book_info(isbn: str):
    """Fetch book details using Google Books API and Open Library API."""
    
    # Try Google Books API first
    google_url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    google_response = requests.get(google_url).json()
    
    if "items" in google_response:
        book = google_response["items"][0]["volumeInfo"]
        return {
            "title": book.get("title"),
            "authors": book.get("authors", []),
            "publisher": book.get("publisher"),
            "published_date": book.get("publishedDate"),
            "description": book.get("description"),
            "page_count": book.get("pageCount"),
            "categories": book.get("categories", []),
            "thumbnail": book.get("imageLinks", {}).get("thumbnail")
        }

    # If Google Books API fails, try Open Library API
    openlib_url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    openlib_response = requests.get(openlib_url).json()
    
    if f"ISBN:{isbn}" in openlib_response:
        book = openlib_response[f"ISBN:{isbn}"]
        return {
            "title": book.get("title"),
            "authors": [author["name"] for author in book.get("authors", [])],
            "publisher": [publisher["name"] for publisher in book.get("publishers", [])] if "publishers" in book else None,
            "published_date": book.get("publish_date"),
            "page_count": book.get("number_of_pages"),
            "categories": book.get("subjects", []),
            "thumbnail": book.get("cover", {}).get("medium")
        }
    
    return {"error": "Book not found"}

# Example Usage
isbn = "9780131103627"  # Example ISBN (The C Programming Language)
book_info = get_book_info(isbn)
print(book_info)

return
{
    "title": "The C Programming Language",
    "authors": ["Brian W. Kernighan", "Dennis M. Ritchie"],
    "publisher": "Prentice Hall",
    "published_date": "1988",
    "description": "This second edition...",
    "page_count": 274,
    "categories": ["Computers"],
    "thumbnail": "http://books.google.com/books/content?id=...",
}
