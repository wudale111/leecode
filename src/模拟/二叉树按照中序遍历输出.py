class Node:
	# 树节点
	# 对树结构体不了解的
	# 可看 二叉树相关算法：https://pycoder.blog.csdn.net/article/details/123502655
	# 实在不行直接跳过该题
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_node(c):
    # 判断是否是一个树节点
    # 不是树节点  创建节点返回
    if type(c) == Node:
        return c
    elif c:
        return Node(c)
    else:
        return None


def get_root(stack):
	# 构建树
	# 从最内层 开始 构建子树，如h{,I}
	# 将构建的子树 再放回 stack
	# 重新构建下一级
	# 类似 计算括号深度
    j = len(stack) - 1
    while j >= 0:
        if stack[j] == "{":
            break
        j -= 1

    if stack[j:][1] == ",":
        left_ = None
    else:
        left_ = get_node(stack[j:][1])

    if stack[j:][-1] == "," or "," not in stack[j:]:
        right_ = None
    else:
        right_ = get_node(stack[j:][-1])

    stack = stack[:j]
    root_ = get_node(stack.pop(-1))
    root_.left = left_
    root_.right = right_
    stack.append(root_)
    return stack


while 1:
    try:
        chars = input().replace(" ", "")

        # 构建树
        stack = []
        for c in chars:
            if c == "}":
                stack = get_root(stack)
            else:
                stack.append(c)

        dp = []

        # 中序输出
        # 树的前中后序、广度、深度
        # 可看 二叉树相关算法：https://pycoder.blog.csdn.net/article/details/123502655
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dp.append(root.val)
            dfs(root.right)

        dfs(stack[0])
        print("".join(dp))
    except Exception as e:
        break
