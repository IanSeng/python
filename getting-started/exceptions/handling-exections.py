def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"Succeeeded")
    except KeyError:
        print("failed")
        x = -1
    return x


def main():
    convert(1)

if __name__ == '__main__':
    main()
