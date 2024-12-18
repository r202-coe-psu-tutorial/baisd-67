def count(words: list) -> dict:
    word_stat = dict()
    for word in words:
        if word not in word_stat:
            word_stat[word] = 0
        word_stat[word] += 1

    return word_stat


if __name__ == "__main__":
    nums = int(input("Word = "))
    words = [input(">>> ") for _ in range(nums)]

    results = count(words)
    print("Ans =>")
    print(len(results))
    print(" ".join([str(i) for i in results.values()]))
