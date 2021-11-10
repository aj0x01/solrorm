from solrorm.cores import Core

if __name__ == "__main__":
    my_core = Core(
    host='172.16.0.203', 
    port = 8983, 
    core_name = 'newsfeeds.sea_shipments',
    fields=['company_id','shipments', 'top_suppliers', 'recent_shipments'])

    results = my_core.objects\
        .query(company_id=69)\
        .get(start=0, rows=1)
    print(results.docs)