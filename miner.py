from hashlib import sha256
import time

MAX_NONCE = 100000000000

def  SHA256(text):
    """
    [A function to return SHA256 hash]

    [Returns sha256 hash encoded in ascii]

    Parameters
    ----------
    text : [A hash]
        [TODO:description]
    """
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeroes):
    """
    [A function to demonstrate how bitcoin mining works]

    [This method will iterate generating a new hash each time until we generate a hash that has {n} number of zeroes before te hash. N specifies difficulty setting]

    Parameters
    ----------
    block_number : [TODO:type]
        [TODO:description]
    transactions : [TODO:type]
        [TODO:description]
    previous_hash : [TODO:type]
        [TODO:description]
    prefix_zeroes : [TODO:type]
        [TODO:description]

    Raises
    ------
    [TODO:name]:
        [TODO:description]
    """
    prefix_str = '0'*prefix_zeroes
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Bitcoin mining successful with nonce value: {nonce}")
            return new_hash

    raise BaseException(f"Could not mine a bitcoin with nonce after {MAX_NONCE} number of attempts")


#Testing our code
if __name__=='__main__':
    transactions='''
    Alice->Bob->10
    Bob->Janet->60
    '''
    difficulty=5 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
    start = time.time()
    print("start mining")
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)

