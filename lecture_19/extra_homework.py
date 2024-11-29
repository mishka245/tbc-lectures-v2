from contextlib import contextmanager


@contextmanager
def transaction(db: dict):

    yield db


# Simulated database
database = {}

# Example usage
try:
    with transaction(database) as db:
        db["user1"] = "Alice"
        db["user2"] = "Bob"
        print("Before error:", db)
        # Simulate an error
        raise ValueError("Something went wrong!")
        db["user3"] = "Charlie"  # This won't execute
except ValueError:
    pass

print("After rollback:", database)

with transaction(database) as db:
    db["user3"] = "Charlie"
    print("Final state before commit:", db)

print("Final database state:", database)

