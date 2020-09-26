punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@', '?']


# strips a sentence of all the punctuations defined previously
def strip_punctuation(string):
    word = str(string)
    for item in punctuation_chars:
        if item in word:
            word = word.replace(item, "")
    return word


# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


# number of how much positive words are used in a sentence
def get_pos(sentences):
    matched_pos_words = []
    sentence = str(sentences).lower()
    s_sen = strip_punctuation(sentence)
    for item in positive_words:
        if item in s_sen.split(" "):
            matched_pos_words.append(item)
    return len(matched_pos_words)


# list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


# number of how much negative words are used in a sentence
def get_neg(sentences):
    matched_neg_words = []
    sentence = str(sentences).lower()
    s_sen = strip_punctuation(sentence)
    for item in negative_words:
        if item in s_sen.split(" "):
            matched_neg_words.append(item)
    return len(matched_neg_words)


with open("project_twitter_data.csv", "r") as project_twitter_data:
    data_list = project_twitter_data.readlines()
    data_list.remove(data_list[0])
    with open("resulting_data.csv", "w") as resulting_data:
        resulting_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
        resulting_data.write("\n")
        for itm in data_list:
            if "\n" in itm:
                itm = itm.replace("\n", "")
            itm_list = itm.split(",")
            resulting_data.write(
                "{}, {}, {}, {}, {}".format(itm_list[1], itm_list[2], get_pos(itm_list[0]),
                                            get_neg(itm_list[0]), get_pos(itm_list[0]) - get_neg(itm_list[0])))
            resulting_data.write("\n")
