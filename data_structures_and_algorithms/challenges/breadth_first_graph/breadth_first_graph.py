    def bfs(self, start_node):
        q = Queue()
        q.enqueue(start_node)
        while len(q):
            cur = q.dequeue()
            # mark the node as visited so you don't enqueue(visit) it again
            print(cur.value)
            neighbors = self._adjacency_list[cur]
            for n in neighbors:
                q.enqueue(n)