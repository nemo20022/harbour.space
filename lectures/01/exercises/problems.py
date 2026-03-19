"""Lecture 01 practice problems.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Keep implementations pure unless the function explicitly needs I/O.
- Use only the Python standard library.
"""



def normalize_username(name: str) -> str:
    return "_".join(name.strip().lower().split())
    """Return a normalized username.

    Rules:
    - Trim outer whitespace
    - Lowercase everything
    - Replace internal whitespace runs with a single underscore
    """
    raise NotImplementedError

def is_valid_age(age: int) -> bool:
    return 18 <= age <= 120
    """Return True if age is in [18, 120], otherwise False."""
    raise NotImplementedError


def truthy_values(values: list[object]) -> list[object]:
    """Return a new list containing only truthy values from input."""
    l=[]

    for i in values:
        if i:
            l.append(i)

    return l
    raise NotImplementedError


def sum_until_negative(numbers: list[int]) -> int:
    """Return sum of numbers until the first negative value (exclusive)."""
    total = 0
    for n in numbers:
        if n < 0:
            break
        total += n
    return total        
    raise NotImplementedError


def skip_multiples_of_three(numbers: list[int]) -> list[int]:
    l=[]
    for i in numbers:
        if i%3!=0:
            l.append(i)
    return l
    """Return numbers excluding values divisible by 3."""
    raise NotImplementedError


def first_even_or_none(numbers: list[int]) -> int | None:
    """Return the first even number, or None if no even number exists."""
    i=0
    for i in numbers:
        if i%2==0:
            return i
    return 
    raise NotImplementedError


def squares_of_even(numbers: list[int]) -> list[int]:
    """Return squares of all even numbers in input order."""
    # l=[]
    # for i in numbers:
    #     if i %2==0:
    #         l.append(i*i)
    # return l
    return [i*i for i in numbers if i%2==0]
    raise NotImplementedError


def word_lengths(words: list[str]) -> dict[str, int]:
    """Return dict mapping each word to its length."""
    d={}
    for i in words:
        d[i]=len(i)
    return d
    raise NotImplementedError

def zip_to_pairs(keys: list[str], values: list[int]) -> list[tuple[str, int]]:
    """Zip keys and values into list of pairs. Ignore extras in longer list."""
    l=[]
    for i,j in zip(keys,values):
        l.append((i,j))
    return l
    raise NotImplementedError


def build_user(name: str, role: str = "student", active: bool = True) -> dict[str, object]:
    """Build and return {'name': name, 'role': role, 'active': active}."""
    d={}
    d["name"]=name
    d["role"]=role
    d["active"]=active
    return d
    raise NotImplementedError


def append_tag_safe(tag: str, tags: list[str] | None = None) -> list[str]:
    """Append tag to tags safely (no shared mutable default across calls)."""
    if not tags:
        tags = []
    tags.append(tag)
    return tags
    raise NotImplementedError


def invert_dict(mapping: dict[str, int]) -> dict[int, str]:
    """Invert mapping. Assume values are unique."""
    d={}
    for key, value in mapping.items():
        d[value]=key
    return d
    raise NotImplementedError


def unique_sorted_tags(tags: list[str]) -> list[str]:
    """Return unique tags sorted ascending."""
    return sorted(set(tags))
    raise NotImplementedError

from collections import Counter,defaultdict,deque
def count_words(words: list[str]) -> dict[str, int]:
    """Count occurrences of each word using collections.Counter."""
    c= Counter(words)
    return dict(c)
    raise NotImplementedError


def group_scores(records: list[tuple[str, int]]) -> dict[str, list[int]]:
    """Group scores by student name using collections.defaultdict(list)."""
    d = defaultdict(list)
    for i,j in records:
        d[i].append(j)
    return dict(d)
    raise NotImplementedError

def rotate_queue(items: list[str], steps: int) -> list[str]:
    """Rotate queue to the right by steps using collections.deque and return as list."""
    d=deque(items)
    d.rotate(steps)
    return list(d)
    raise NotImplementedError


def safe_int(value: str) -> int | None:
    """Convert string to int, returning None if conversion fails."""
    try:
        return int(value)
    except ValueError:
        return None
    raise NotImplementedError


def read_lines(path: str) -> list[str]:
    """Read a text file with a context manager and return non-empty stripped lines."""
    with open(path, "r") as f:
        data=f.read()
    lines=[]
    for line in data.splitlines():
        line=line.strip()
        if line:
            lines.append(line)
    return lines
    raise NotImplementedError


def top_n_scores(scores: list[int], n: int = 3) -> list[int]:
    """Return top n scores in descending order."""
    scores=scores.copy()
    scores.sort(reverse=True)
    return scores[:n]
    raise NotImplementedError


def all_passed(scores: list[int], threshold: int = 50) -> bool:
    """Return True if every score is >= threshold."""
    for i in scores:
        if i<threshold:
            return False
    return True
    raise NotImplementedError