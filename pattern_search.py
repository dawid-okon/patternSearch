import timeit
import os

def naive_search(text, pattern):
    textLen = len(text)
    pattLen = len(pattern)
    results = []
    for i in range(textLen - pattLen + 1):
        if text[i:i + pattLen] == pattern:
            results.append(i)
    return results

def boyer_moore_search(text, pattern):
    textLen = len(text)
    pattLen = len(pattern)
    results = []
    bad_char = {}

    for i in range(pattLen):
        bad_char[pattern[i]] = i

    move = 0
    while move <= textLen - pattLen:
        pattIndex = pattLen - 1
        while pattIndex >= 0 and pattern[pattIndex] == text[move + pattIndex]:
            pattIndex -= 1
        if pattIndex < 0:
            results.append(move)
            move += (pattLen - bad_char.get(text[move + pattLen], -1) if move + pattLen < textLen else 1)
        else:
            move += max(1, pattIndex - bad_char.get(text[move + pattIndex], -1))

    return results

def compare_search(pattern):
  
    file = open('LoremIpsum.txt')
    text = file.read()

    startTime = timeit.default_timer()
    naiveResult = naive_search(text, pattern)
    naiveTime = timeit.default_timer() - startTime
    # print(f"Naive search results: {naiveResult}")
    # print(f"Naive search time: {naiveTime:.10f} seconds\n")

    startTime = timeit.default_timer()
    bmResult = boyer_moore_search(text, pattern)
    boyer_moore_time = timeit.default_timer() - startTime
    # print(f"Boyer-Moore search results: {bmResult}")
    # print(f"Boyer-Moore search time: {boyer_moore_time:.10f} seconds\n")

    if naiveTime < boyer_moore_time:
        print(f"Naive search was faster by {boyer_moore_time - naiveTime:.10f} seconds")
    else:
        print(f"Boyer-Moore search was faster by {naiveTime - boyer_moore_time:.10f} seconds")


pattern = "Duis"
for i in range(1,10):    
    compare_search(pattern)