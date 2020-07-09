def main():
    print("Enter a sequence of non-decreasing numbers.")
    count = 0

    last = float(input("Enter a num: "))
    first = last

    while first >= last:
        count += 1
        last = first
        first = float(input("Enter a num: "))

    print("Thanks for playing!")
    print("Sequence length: " + str(count))


if __name__ == "__main__":
    main()