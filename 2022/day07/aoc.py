from anytree import Node, RenderTree, PreOrderIter


def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


def populate_sizes(node):
    if "size" not in node.__dict__:
        size = 0
        for c in node.children:
            c_size = populate_sizes(c)
            size += c_size
            node.size = size
        return size
    else:
        return node.size


def weird_sum(root):
    s = 0
    for node in PreOrderIter(root):
        if is_folder(node) and node.size <= 100_000:
            s += node.size
    return s


def is_folder(node):
    # obs: no children doesn't mean it is a folder, could be empty folder,
    # could add type (folder/file) to node
    return len(node.children) != 0


def get_tree(is_sample):
    lines = open(get_filename(is_sample)).read().strip().split("\n")
    root = Node("/")
    curr_folder = root
    for l in lines:
        if l.startswith("$ cd"):
            folder_name = l.split("$ cd ")[1]
            if folder_name == "..":
                curr_folder = curr_folder.parent
            elif folder_name in [c.name for c in curr_folder.children]:
                # nit: avoid double iteration
                try:
                    i = [c.name for c in curr_folder.children].index(folder_name)
                except ValueError:
                    raise Exception("index not found")
                curr_folder = curr_folder.children[i]
            elif folder_name == "/":  # nit: could avoid special case
                curr_folder = root
            else:
                tmp = Node(folder_name)
                curr_folder.children.__add__(tmp)
                curr_folder = tmp
        elif l.startswith("$ ls"):
            pass
        else:
            size, name = l.split(" ")
            if size == "dir":
                Node(name, parent=curr_folder)
            else:
                Node(name, parent=curr_folder, size=int(size))
    populate_sizes(root)

    return root


def print_tree(root):
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))


def part_one(is_sample=False):
    root = get_tree(is_sample)
    print(weird_sum(root))


def part_two(is_sample=False):
    root = get_tree(is_sample)
    available = 70_000_000
    needed = 30_000_000
    unused = available - root.size
    to_delete = needed - unused

    candidates = []
    for node in PreOrderIter(root):
        if is_folder(node) and node.size > to_delete:
            candidates.append(node)
    print(min(candidates, key=lambda c: c.size))


if __name__ == "__main__":
    part_one(False)  # 1297159 # 65 mins (45m parsing)
    part_two(False)  # 3866390 # 8 mins
