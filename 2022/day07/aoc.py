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
    curr_folder = root = Node("/")
    for l in lines:
        match l.split():
            case ['$', 'cd', '/']:
                curr_folder = root
            case ['$', 'cd', '..']:
                curr_folder = curr_folder.parent
            case ['$', 'cd', folder_name]:
                curr_folder = next((c for c in curr_folder.children if c.name == folder_name), None)
            case ['$', 'ls']:
                pass
            case ['dir', folder_name]:
                Node(folder_name, parent=curr_folder)
            case [size, file_name]:
                Node(file_name, parent=curr_folder, size=int(size))
            case _:
                raise
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
