from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 그래프를 구성
        graph = defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))
        
        # 우선순위 큐 (현재 비용, 현재 노드, 남은 이동 횟수)
        priority_queue = [(0, src, k + 1)]
        # 각 노드까지의 최소 비용을 기록
        min_costs = {}
        
        while priority_queue:
            cur_cost, cur_node, remaining_moves = heapq.heappop(priority_queue)
            
            # 목적지에 도달했다면 현재 비용 반환
            if cur_node == dst:
                return cur_cost
            
            # 이동 횟수가 0이면 더 이상 진행 불가
            if remaining_moves > 0:
                for next_node, cost in graph[cur_node]:
                    next_cost = cur_cost + cost
                    # 더 적은 비용으로 해당 노드에 도달한 적이 없을 경우에만 탐색 확장
                    if (next_node, remaining_moves - 1) not in min_costs or next_cost < min_costs[(next_node, remaining_moves - 1)]:
                        min_costs[(next_node, remaining_moves - 1)] = next_cost
                        heapq.heappush(priority_queue, (next_cost, next_node, remaining_moves - 1))
        
        # 목적지까지 갈 수 없다면 -1 반환
        return -1
