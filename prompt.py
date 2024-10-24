def report_count(token):
    with open("corpus.txt", 'r', encoding='utf-8') as file:
            corpus = file.read()

        # Count the occurrences of the token
        token_count = corpus.count(token)

        # Output the result in the specified format
        print(f"The term [{token}] shows up in the corpus {token_count} times.")