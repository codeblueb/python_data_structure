"""
    Hash your object: Immutable 

    then create a pair of hash & index 

    now you have O(1) to search for any object you have stored

    then you have O(1) to search for any object and do anything you want 

    therefore you have a O(2) operations 
"""
def find_object(obj: str | int) -> object:
    """
        O(1) to find index 
        O(1) to find the object 
    """
    if isinstance(obj, str):
        # get the index and then retrieve the object
    else:
        # retrieve the object
