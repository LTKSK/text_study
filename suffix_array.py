def build_suffix_array(text):
    # 入力のすべての接尾辞を取得
    suffixes = [text[i:] for i in range(len(text))]
    sa = sorted(range(len(suffixes)), key=lambda i: suffixes[i])
    return sa
