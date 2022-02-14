import time
from hashlib import sha256

MAXIMUM_NONCE = 10000000000000


def crypt256(text):
    return sha256(text.encode("ascii")).hexdigest()


def start_mining(block_num, transaction_dat, previous_hashing, prefix_zero):
    prefix_str = "0" * prefix_zero
    for nonce in range(MAXIMUM_NONCE):
        nonce = 3
        text = str(block_num) + transaction_dat + previous_hashing + str(nonce)
        new_hash = crypt256(text)
        if new_hash.startswith(prefix_str):
            print(f"nonce value succes get : {nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAXIMUM_NONCE} times")


if __name__ == "__main__":
    transaction_dat = """
    user->user->10
    user->user->30
    """

    start_time_mining = time.time()
    print("starting mining!")

    diff = 5  # now 20 or more than 20
    create_new_hash = start_mining(5, transaction_dat, "block_code", diff)
    get_total_time = str((time.time() - start_time_mining))

    print(create_new_hash)
