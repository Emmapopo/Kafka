import uuid

def is_valid_uuid(value):
    """A function to check if a uuid is valid
       Receives a UUID and confirms if it's valid """   
    try:
        uuid.UUID(value)
        return True

    except ValueError:
        return False
