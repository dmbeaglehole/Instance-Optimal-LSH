import os

start = 0
num_trees = 10
for t in range(start, start + num_trees):
    tree_label = "tree" + str(t)
    dir_path = "../many_hash/trees/" + tree_label + "/"
    os.system("mkdir " + dir_path)
    os.system("mkdir " + dir_path + "dists/")
    os.system("mkdir " + dir_path + "hard_queries/")


    os.system("./tree_main " + str(t))
