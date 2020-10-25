"""
Good morning! Here's your coding interview problem for today.

This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
"""

def readN(n, file_path):
    with open(file_path) as file:
        f = file.read()
        while f:
            print(f[:n])
            f = f[n:]
        else:
            print()

readN(50, 'Daily-Coding-Problems\\txt.txt')