# 이진 트리 직렬화 & 역직렬화 - 직렬화 & 역직렬화 구현
'''
이진트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능을 구현하라.
즉 다음과 같은 트리는 [1,2,3,null,null,4,5] 형태로 직렬화할 수 있을 것이다.
'''
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # 직렬화
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ['#']
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    # 역직렬화
    def deserialize(self, data: str) -> TreeNode:
        # 예외처리
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root
