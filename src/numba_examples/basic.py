import numba
import time


def without_numba(list_len: int = 100000000):
    big_list = list(range(list_len))


@numba.njit
def with_numba(list_len: int = 100000000):
    big_list = list(range(list_len))


if __name__ == "__main__":
    start_time = time.time()
    without_numba()
    print(f"Time elapsed: {(time.time() - start_time) * 1000} ms")
    start_time = time.time()
    with_numba()
    print(f"Time elapsed: {(time.time() - start_time) * 1000} ms")
