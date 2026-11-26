from typing import List

def read_integers() -> List[int]:
    output = []
    for c in input().split(","):
        output.append(int(c))
    return output

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
