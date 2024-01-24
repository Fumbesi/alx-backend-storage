#!/usr/bin/env python3

"""
Cache module
"""

import redis
import uuid
from typing import Union

class Cache:
    """
    Cache class for storing data in Redis.
    """

    def __init__(self):
        """
        Initializes the Cache instance with a Redis client and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a random key and returns the key.

        Parameters:
        - data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
        - str: The generated random key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

if __name__ == "__main__":
    # Example usage in main.py
    cache = Cache()

    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))


#!/usr/bin/env python3

"""
Cache module
"""

import redis
import uuid
from typing import Union, Callable

class Cache:
    """
    Cache class for storing and retrieving data in/from Redis.
    """

    def __init__(self):
        """
        Initializes the Cache instance with a Redis client and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a random key and returns the key.

        Parameters:
        - data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
        - str: The generated random key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis using the provided key and applies the optional conversion function.

        Parameters:
        - key (str): The key used to retrieve data from Redis.
        - fn (Callable): Optional conversion function to apply to the retrieved data.

        Returns:
        - Union[str, bytes, int, float, None]: The retrieved data, optionally converted.
        """
        data = self._redis.get(key)
        if data is None:
            return None

        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieves data from Redis using the provided key and converts it to a UTF-8 string.

        Parameters:
        - key (str): The key used to retrieve data from Redis.

        Returns:
        - Union[str, None]: The retrieved data as a UTF-8 string, or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieves data from Redis using the provided key and converts it to an integer.

        Parameters:
        - key (str): The key used to retrieve data from Redis.

        Returns:
        - Union[int, None]: The retrieved data as an integer, or None if the key does not exist.
        """
        return self.get(key, fn=int)

if __name__ == "__main__":
    # Example usage in main.py
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value


#!/usr/bin/env python3

"""
Cache module
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps

class Cache:
    """
    Cache class for storing and retrieving data in/from Redis.
    """

    def __init__(self):
        """
        Initializes the Cache instance with a Redis client and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count the number of times a method is called.

        Parameters:
        - method (Callable): The method to be decorated.

        Returns:
        - Callable: The decorated method.
        """
        key = method.__qualname__

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            # Increment the count for the method key
            self._redis.incr(key)
            # Call the original method and return its result
            return method(self, *args, **kwargs)

        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a random key and returns the key.

        Parameters:
        - data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
        - str: The generated random key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis using the provided key and applies the optional conversion function.

        Parameters:
        - key (str): The key used to retrieve data from Redis.
        - fn (Callable): Optional conversion function to apply to the retrieved data.

        Returns:
        - Union[str, bytes, int, float, None]: The retrieved data, optionally converted.
        """
        data = self._redis.get(key)
        if data is None:
            return None

        return fn(data) if fn is not None else data

if __name__ == "__main__":
    # Example usage in main.py
    cache = Cache()

    cache.store(b"first")
    print(cache.get(cache.store.__qualname__))

    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))


#!/usr/bin/env python3

"""
Cache module
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps

class Cache:
    """
    Cache class for storing and retrieving data in/from Redis.
    """

    def __init__(self):
        """
        Initializes the Cache instance with a Redis client and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count the number of times a method is called.

        Parameters:
        - method (Callable): The method to be decorated.

        Returns:
        - Callable: The decorated method.
        """
        key = method.__qualname__

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            # Increment the count for the method key
            self._redis.incr(key)
            # Call the original method and return its result
            return method(self, *args, **kwargs)

        return wrapper

    @staticmethod
    def call_history(method: Callable) -> Callable:
        """
        Decorator to store the history of inputs and outputs for a particular function.

        Parameters:
        - method (Callable): The method to be decorated.

        Returns:
        - Callable: The decorated method.
        """
        key_inputs = "{}:inputs".format(method.__qualname__)
        key_outputs = "{}:outputs".format(method.__qualname__)

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            # Store input arguments in Redis
            self._redis.rpush(key_inputs, str(args))
            # Execute the wrapped function to retrieve the output
            output = method(self, *args, **kwargs)
            # Store the output in Redis
            self._redis.rpush(key_outputs, output)
            # Return the output
            return output

        return wrapper

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a random key and returns the key.

        Parameters:
        - data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
        - str: The generated random key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis using the provided key and applies the optional conversion function.

        Parameters:
        - key (str): The key used to retrieve data from Redis.
        - fn (Callable): Optional conversion function to apply to the retrieved data.

        Returns:
        - Union[str, bytes, int, float, None]: The retrieved data, optionally converted.
        """
        data = self._redis.get(key)
        if data is None:
            return None

        return fn(data) if fn is not None else data

if __name__ == "__main__":
    # Example usage in main.py
    cache = Cache()

    s1 = cache.store("first")
    print(s1)
    s2 = cache.store("second")
    print(s2)
    s3 = cache.store("third")
    print(s3)

    inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
    outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

    print("inputs: {}".format(inputs))
    print("outputs: {}".format(outputs))


#!/usr/bin/env python3

"""
Cache module
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps

class Cache:
    """
    Cache class for storing and retrieving data in/from Redis.
    """

    def __init__(self):
        """
        Initializes the Cache instance with a Redis client and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count the number of times a method is called.

        Parameters:
        - method (Callable): The method to be decorated.

        Returns:
        - Callable: The decorated method.
        """
        key = method.__qualname__

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            # Increment the count for the method key
            self._redis.incr(key)
            # Call the original method and return its result
            return method(self, *args, **kwargs)

        return wrapper

    @staticmethod
    def call_history(method: Callable) -> Callable:
        """
        Decorator to store the history of inputs and outputs for a particular function.

        Parameters:
        - method (Callable): The method to be decorated.

        Returns:
        - Callable: The decorated method.
        """
        key_inputs = "{}:inputs".format(method.__qualname__)
        key_outputs = "{}:outputs".format(method.__qualname__)

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            # Store input arguments in Redis
            self._redis.rpush(key_inputs, str(args))
            # Execute the wrapped function to retrieve the output
            output = method(self, *args, **kwargs)
            # Store the output in Redis
            self._redis.rpush(key_outputs, output)
            # Return the output
            return output

        return wrapper

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a random key and returns the key.

        Parameters:
        - data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
        - str: The generated random key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis using the provided key and applies the optional conversion function.

        Parameters:
        - key (str): The key used to retrieve data from Redis.
        - fn (Callable): Optional conversion function to apply to the retrieved data.

        Returns:
        - Union[str, bytes, int, float, None]: The retrieved data, optionally converted.
        """
        data = self._redis.get(key)
        if data is None:
            return None

        return fn(data) if fn is not None else data

    def replay(self, method: Callable) -> None:
        """
        Display the history of calls for a particular function.

        Parameters:
        - method (Callable): The method for which the history is displayed.

        Returns:
        - None
        """
        key_inputs = "{}:inputs".format(method.__qualname__)
        key_outputs = "{}:outputs".format(method.__qualname__)

        inputs = self._redis.lrange(key_inputs, 0, -1)
        outputs = self._redis.lrange(key_outputs, 0, -1)

        print("{} was called {} times:".format(method.__qualname__, len(inputs)))

        for input_args, output in zip(inputs, outputs):
            input_args = eval(input_args.decode('utf-8'))  # Convert string back to tuple
            print("{}{} -> {}".format(method.__qualname__, input_args, output.decode('utf-8')))

if __name__ == "__main__":
    # Example usage in main.py
    cache = Cache()

    cache.store("foo")
    cache.store("bar")
    cache.store(42)

    cache.replay(cache.store)
