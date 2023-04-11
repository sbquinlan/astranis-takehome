from typing import Generator, List, Optional

ESCAPE = "|"
DOUBLE_ESCAPE = "||"
DOT = "."
ESCAPE_DOT = "|."


# Assume prefix is escaped already
def flatten_key(prefix: Optional[str], key: str) -> str:
    if isinstance(key, str) and (DOT in key or ESCAPE in key):
        key = key.replace(ESCAPE, DOUBLE_ESCAPE).replace(DOT, ESCAPE_DOT)
    return str(key) if prefix is None else f"{prefix}.{key}"


# Match '.' with either no or an even number of escapes in front. An odd number
# would mean an escaped '.' which we do not want to split on. Throw on empty
def _split_unescaped(key: str) -> Generator[str, None, None]:
    start_key = 0
    esc_count = 0
    for idx, char in enumerate(key):
        if char is DOT and esc_count % 2 == 0:
            yield key[start_key:idx]
            start_key = idx + 1
        esc_count = 0 if char is not ESCAPE else esc_count + 1
    yield key[start_key:]


def unflatten_key(key: str) -> List[str]:
    if DOT not in key:
        return [key]
    return [
        subkey.replace(ESCAPE_DOT, DOT).replace(DOUBLE_ESCAPE, ESCAPE)
        for subkey in _split_unescaped(key)
    ]
