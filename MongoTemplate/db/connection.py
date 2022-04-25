import mongoengine



def get_db():
    conn = mongoengine.connect(db = "mycompany",
        host = "mongodb+srv://cluster0.x1lm7.mongodb.net",
        port = 27017,
        username = "sabari",
        password = "Password123",
        retrywrites = True
    )
    return conn
