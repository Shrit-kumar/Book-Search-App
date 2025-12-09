import requests

print("***Book Search App***")
print("Type any book name to search\n")

while True:
    query = input("Search book: ").strip()

    if not query:
        print("Please type something.\n")
        continue

   
    url = "https://www.googleapis.com/books/v1/volumes"

   
    params = {
        "q": query,
        "maxResults": 5   
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
    except:
        print("Error fetching data from Google Books API.\n")
        continue

   
    items = data.get("items", [])

    if not items:
        print("No books found.\n")
        continue

    print(f"\nFound {len(items)} books:\n")

    
    i = 1
    for book in items:
        info = book.get("volumeInfo", {})

        title = info.get("title", "No Title")
        authors = info.get("authors", ["Unknown"])
        published = info.get("publishedDate", "Unknown")

        print(f"{i}. {title}")
        print("   Author(s):", ", ".join(authors))
        print("   Published:", published)
        print()
        i += 1

    print("----------------------------\n")

