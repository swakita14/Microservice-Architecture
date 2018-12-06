from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
POSTS = {
    "0": {
        "id": 0,
        "title": "How to String Concatinate in Python",
        "body": "Use the built-in python method str()",
        "link": True,
        "url": "api/post/0" ,
        "timestamp": get_timestamp(),
        "user_id": 4,
        "category_id": 2,
        "votes": 3,
        "version" : 2.0
    }


}

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [POSTS[key] for key in sorted(POSTS.keys())]

