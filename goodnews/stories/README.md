Running 'add_new_articles.py' will grab article urls from RSS_feeds.txt, process the articles with newspaper into a json object, append the json object to articles.jsonl, and append the processed urls to extracted_article_urls.txt

The article jsons are stored in a jsonlines file because I did not see an easy way to append json objects to a list stored in a txt file. Otherwise the whole txt file would have to be overwritten each time.  

The jsonlines file can easily be converted to a list of json objects though.
