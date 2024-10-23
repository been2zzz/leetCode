class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # n 노드 갯수, k 시작 노드
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2],time[1]))
        costs = {}
        priority_queue = []
        heapq.heappush(priority_queue, (0, k)) # start node set
        
        while priority_queue:
            cur_cost, cur_node = heapq.heappop(priority_queue)
            if cur_node not in costs:
                costs[cur_node] = cur_cost
                for cost, next_node in graph[cur_node]:
                    next_cost = cur_cost + cost
                    heapq.heappush(priority_queue, (next_cost, next_node))

        for node in range(1, n+1):
            if node not in costs:
                return -1
        
        return max(costs.values())