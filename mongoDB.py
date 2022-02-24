def get_database():
    import pymongo

    # Initialize the database 
    client = pymongo.MongoClient("mongodb+srv://tscrivanich27:BostonSwim22@health-platform.6mb1k.mongodb.net/devices?retryWrites=true&w=majority")
    db = client.localhost

    # Return the database object
    return db
