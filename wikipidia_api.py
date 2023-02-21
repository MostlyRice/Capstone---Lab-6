import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('Die Hard')
print("Page - Exists: %s" % page_py.exists())


print("Page - Title: %s" % page_py.title)


print("Page - Summary: %s" % page_py.summary[0:60])
