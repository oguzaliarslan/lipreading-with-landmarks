"""
Varios util functions are stored here

"""

def char_to_num(char):
    vocab = "abcdefghijklmnopqrstuvwxyz'?!123456789 "
    return vocab.index(char) if char in vocab else -1

def num_to_char(num):
    if num == -1:
        return " "
    vocab = "abcdefghijklmnopqrstuvwxyz'?!123456789 "
    return vocab[num] if num < len(vocab) else -1

def return_vocab_size():
    return len("abcdefghijklmnopqrstuvwxyz'?!123456789")