# main
from qa2hypo import *
import argparse

# parse the arguments of the program
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('root_dir')
    ARGS = parser.parse_args()
    return ARGS


if __name__ == "__main__":
    ############################
    # test on single sentence
    ############################
    # question = "how many potatoes does Mary now have ?"
    # answer = "0.5"
    # tree = get_parse_tree(question)
    # tree.pretty_print()
    # sent = qa2hypo(question, answer, True, False)

    ############################
    # test on all the sentence
    ############################
    a = get_args()
    qa_pairs_list = pre_proc(a, 'math_aida')
    # qa_pairs_list = pre_proc(a, 'math_rik')
    # res = qa2hypo_test(qa_pairs_list)
    # post_proc(a, res, 'math_rik') # includes writing to file