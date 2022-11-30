import feedparser


rss_feed = feedparser.parse(r'https://www.asahi.com/rss/asahi/politics.rdf')

print(rss_feed.feed.title)
print(rss_feed.feed.link)