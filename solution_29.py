if __name__ == '__main__':
    all_terms = set()
    for a in range(2, 101):
        for b in range(2, 101):
            all_terms.add(a**b)
    print(len(all_terms))
