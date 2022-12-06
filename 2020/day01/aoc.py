def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


def complements_product(nums, target):
    complements = set()
    for n in nums:
        c = target - n
        complements.add(c)
        if n in complements:
            return n * c
    return None


def part_one(is_sample=False):
    nums = open(get_filename(is_sample)).read().strip().split("\n")
    nums = [int(n) for n in nums]
    print(complements_product(nums, 2020))


def part_two(is_sample=False):
    nums = open(get_filename(is_sample)).read().strip().split("\n")
    nums = [int(n) for n in nums]
    for i in range(0, len(nums)):
        curr = nums[i]
        remaining = nums[:i] + nums[i + 1 :]
        sub_complement = complements_product(remaining, 2020 - curr)
        if sub_complement:
            print(curr * sub_complement)
            return


if __name__ == "__main__":
    part_one(False)  # 494475 # 5 mins
    part_two(False)  # 267520550 # 10 mins
