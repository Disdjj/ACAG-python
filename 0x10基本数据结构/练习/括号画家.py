# https://www.acwing.com/problem/content/152/
quote_str = input()
quote_dict = {
    "(": 1,
    ")": -1,
    "{": 2,
    "}": -2,
    "[": 3,
    "]": -3,
}


def process(quote: str):
    res = 0
    index_stack = []
    for index in range(len(quote)):
        if not index_stack:
            index_stack.append(index)
        else:
            now_quote = quote_dict[quote[index]]
            if now_quote < 0 and now_quote + quote_dict[quote[index_stack[-1]]] == 0:
                index_stack.pop()
            else:
                index_stack.append(index)
        if index_stack:
            res = max(res, index - index_stack[-1])
        else:
            res = max(res, index + 1)
    return res


print(process(quote_str))
