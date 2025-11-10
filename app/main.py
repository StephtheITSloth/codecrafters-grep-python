import sys
import string

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    print('input_line:', input_line)
    print('pattern:', pattern)
    if len(pattern) == 1:
        return pattern in input_line

    elif pattern == r"\d":
        for char in input_line:
            if char.isdigit():
                return True
        return False
    
    elif pattern == r"\w":
        for char in input_line:
            if char in string.ascii_letters:
                return True
            elif char in string.digits:
                return True
            elif char == "_":
                return True
        return False
    
    elif pattern.startswith('[') and pattern.endswith(']'):
        new_pattern = pattern[1:-1]
        print(new_pattern)
        new_pattern = set(new_pattern)
        for char in input_line:
            if char in new_pattern:
                return True
        return False
    elif pattern.startswith('[^') and pattern.endswith(']'):
        new_pattern = pattern[2:-1]
        new_pattern = set(new_pattern)
        for char in input_line:
            if char not in new_pattern:
                return True
        return False
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")
 

def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    # TODO: Uncomment the code below to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
