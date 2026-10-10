# Hashing

This folder is dedicated to learning and implementing hashing-based data structures in Python.

## What is hashing?

Hashing maps a key to an index in a table using a hash function. A hash table uses that index to store or find the value associated with the key.

Python's built-in `dict` and `set` are hash-based data structures.

## Common operations

- **Insert** a key-value pair
- **Search** for a value using its key
- **Update** the value associated with a key
- **Delete** a key-value pair

## Hash collisions

A collision happens when different keys map to the same table index. A hash table must handle collisions to store all keys correctly. Common strategies include:

- **Separate chaining:** keep multiple entries in a collection at each index.
- **Open addressing:** find another available table slot according to a probing rule.

## Time complexity

| Operation | Average case | Worst case |
|---|---:|---:|
| Search | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |

Average-case performance assumes a well-distributed hash function and a suitably sized table. The worst case can occur when many keys collide.

## Python key requirements

Dictionary and set keys must be hashable. A hashable object's hash value must remain stable while it is used as a key, and objects that compare equal must have the same hash value. Immutable types such as integers, strings, and tuples of hashable values are common keys; lists and dictionaries are not hashable.

## Files in this folder

- `implementation.py`: reserved for the Python hashing implementation and related examples.

This folder is intended for implementations, examples, and practice problems covering hashing and hash tables.
