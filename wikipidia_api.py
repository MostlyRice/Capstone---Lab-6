# Import the wikipediaapi library
import wikipediaapi

# Create a Wikipedia object for the English language
wiki_wiki = wikipediaapi.Wikipedia('en')

# Retrieve the Wikipedia page for the movie "Die Hard"
page_py = wiki_wiki.page('Die Hard')

# Check if the page exists and print the result
print("Page - Exists: %s" % page_py.exists())

# Print the title of the page
print("Page - Title: %s" % page_py.title)

# Print the first 60 characters of the page summary
print("Page - Summary: %s" % page_py.summary[0:60])

# Print the full URL of the page
print(page_py.fullurl)
# Note: This URL is not related to the "Die Hard" page, but rather to the Python programming language page.
