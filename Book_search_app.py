import requests

print("***Book Search App***")
print("Type any book name to search (type 'exit' to quit)\n")

while True:
    query = input("Search book: ").strip()

    if query.lower() == "exit":
        print("Goodbye!")
        break

    if not query:
        print("Please type something.\n")
        continue

    # API endpoint
    url = "https://www.googleapis.com/books/v1/volumes"

    # Parameters sent to API
    params = {
        "q": query,
        "maxResults": 5   # Show only 5 results
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
    except:
        print("Error fetching data from Google Books API.\n")
        continue

    # 'items' contains book results
    items = data.get("items", [])

    if not items:
        print("No books found.\n")
        continue

    print(f"\nFound {len(items)} books:\n")

    # Loop through results
    for i, book in enumerate(items, start=1):
        info = book.get("volumeInfo", {})

        title = info.get("title", "No Title")
        authors = info.get("authors", ["Unknown"])
        published = info.get("publishedDate", "Unknown")

        print(f"{i}. {title}")
        print("   Author(s):", ", ".join(authors))
        print("   Published:", published)
        print()

    print("----------------------------\n")
