from solrorm.cores import Core

# defining my new core
# its that simple.
# will integrate it to settings module, so that host, port wont have to be repeated.
my_core = Core(
    host='<SOLR_HOST_HERE>', 
    port = 8983, 
    core_name = '<SOLR_CORE_NAME_HERE>', 
    fields = ['title', 'authors'])

def add_title_length(doc):
    """
    A transformation function to add the title length in the response
    """
    return len(doc["title"])

def append_title(doc, a):
    """
    A transformation function to append a string to the response
    """
    return doc["title"] + a

if __name__ == "__main__":

    # querying data using the core created above
    # note that the field names are already defined in the core object.
    # we are querying for a specific org, which DOES NOT have source_tag as it_news
    results = my_core.objects\
        .query(organizations="twitter inc", __s_tag ="it_news", sentiment="Positive")\
        .get(start=10, rows=10)

    # transforming result to append a custom string to the already existing title
    # transform funtion taskes the new field name, a callback and the args required by callback as its args
    # here, title is an already existing field, so it is replaced byour new title
    results.transform("title", append_title, " added by user")

    # transforming result by adding a new field called 'title_length'
    # pretty useful for mutating responsed in graphql
    results.transform("title_length", add_title_length)

    #printing the docs
    print(results.docs)