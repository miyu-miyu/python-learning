"""Typing test implementation"""

from operator import truediv
from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    para_list = [p for p in paragraphs if select(p)] 
    return para_list[k] if k<len(para_list) else ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def func(str):
        strs = split(lower(remove_punctuation(str))) # 去标点符号, 统一小写, 按逗号分开
        # print(strs)
        for element in topic:
            if element in strs:
                return True
        return False
    return func
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    typed_words_len = len(typed_words)
    if typed_words_len == 0:
        return 0.0
    length = min(typed_words_len, len(reference_words))
    correct_count = 0
    for i in range(length):
        if typed_words[i] == reference_words[i]:
            correct_count += 1
    return correct_count / typed_words_len * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return len(typed) / 5 / elapsed * 60
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word
    else:
        diff, word_to_select = limit+1, user_word
        for word in valid_words:
            if diff_function(user_word, word, limit) < diff:
                diff = diff_function(user_word, word, limit)
                word_to_select = word
        return word_to_select if diff <= limit else user_word
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'
    start_len = len(start)
    goal_len = len(goal)
    def recur(index, correct_num):
        if correct_num > limit:
            return limit + 1
        elif index >= min(start_len, goal_len):
            correct_num += max(start_len,goal_len) - index
            return correct_num if correct_num <= limit else limit + 1
        elif start[index] == goal[index]:
            return recur(index + 1, correct_num)
        else:
            return recur(index + 1, correct_num + 1)
    return recur(0, 0)   
        

        
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    """ 借鉴了学长的做法, 真的好厉害 """
    # assert False, 'Remove this line'
    if limit < 0: # 说明前面已经用了 limit 次了, 加上最开始的一次, 最终修改的结果会定格在 limit + 1
        # BEGIN
        return 0 
        # END
    elif len(start) == 0 or len(goal) == 0: # 有一个已经匹配完了, 剩下的要么是加, 要么是删
        # BEGIN
        return  len(start) + len(goal)
        # END
    elif start[0] == goal[0]: # matched
        return pawssible_patches(start[1:], goal[1:], limit)
    else: # 下面每种可行的修改都尝试一遍, 然后最后返回最需要修改最小的那个
        add_diff = pawssible_patches(start, goal[1:], limit - 1) 
        remove_diff = pawssible_patches(start[1:], goal, limit - 1)
        substitute_diff = pawssible_patches(start[1:], goal[1:], limit - 1)
        # BEGIN
        return 1 + min( add_diff, remove_diff, substitute_diff) # 前面 1 + 是本次修改的步骤记录
        # END


def final_diff(start, goal, limit): 
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'
    # 下面的太冗余, 而且效果也不好
    # 相同—>往下找
    # 不同：
    # 1. 如果start的下一个与 goal 相同，则删除
    # 2. 如果 goal 的下一个与 start 相同，则插入
    # 3. 如果二者长度相同，且 start 的下一个与 goal 的下一个相同，则替换
    start_len = len(start)
    goal_len = len(goal)
    def correct(index1, index2, steps):
        if steps > limit:
            return limit + 1
        elif index2 == goal_len: # goal match end
            return min(steps + start_len - index1, limit + 1)
        elif index1 == start_len: # start is end
            return min(steps + goal_len - index2, limit + 1)
        elif start[index1] == goal[index2]:
            return correct(index1 + 1, index2 + 1, steps)
        elif start_len - index1 == goal_len - index2: # 剩下的等长
            if index1 +1 < start_len: # 后面还有
                if start[index1 + 1] == goal[index2 + 1]: # substitue
                    return correct(index1 + 1, index2 + 1, steps + 1)
                elif start[index1 + 1] == goal[index2]: # delete
                    return correct(index1 + 2, index2 + 1, steps + 1)
                elif start[index1] == goal[index2 + 1]: # insert
                    return correct(index1, index2 + 1, steps + 1)
                else:
                    return correct(index1 + 1, index2 + 1, steps + 1)
            else: # 已经是最后一个了
                return correct(index1 + 1, index2 + 1, steps + 1)
        elif start_len - index1 < goal_len - index2: # start 短
            if start[index1] == goal[index2 + 1]: # insert
                return correct(index1, index2 + 1, steps + 1)
            else: # substitue
                return correct(index1 + 1, index2 + 1, steps + 1)
        else: # start 长
            if start[index1 + 1] == goal[index2]: # delete
                return correct(index1 + 2, index2 + 1, steps + 1)
            else: # substitue
                return correct(index1 + 1, index2 + 1, steps + 1)
    return correct(0,0,0)



###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    progress = 0
    for i in range(len(typed)):
        if typed[i] != prompt[i]:
            break
        progress += 1
    progress /= len(prompt)
    send({'id': user_id, 'progress': progress})
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    time = []
    for times_player in times_per_player:
        timer = [times_player[i + 1] - times_player[i] for i in range(len(times_player) - 1)]
        time.append(timer)
    return game(words, time)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    fastest = [[] for _ in player_indices]
    for word_i in word_indices:
        for player_i in player_indices:
            if player_i == 0 or word_time > time(game, player_i, word_i) or \
                (word_time == time(game, player_i, word_i) and sum_time_palyer(game, index) > sum_time_palyer(game, player_i)):
                index, word_time =player_i, time(game, player_i, word_i)
        fastest[index].append(word_at(game, word_i))
    return fastest
    
                
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]

def sum_time_palyer(game, player_index):
    """A selector function to return the tatol time the player_index player used"""
    return sum(all_times(game)[player_index])

def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)