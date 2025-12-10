import math
import heapq
from typing import Any, List, Tuple

from src.base.abstract_problem import AbstractProblem


class Problem1Day8(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=8, problem_number=1, input=input)

    def parse_input(self, input_string: str) -> List[Tuple[int, int, int]]:
        lines = [
            line.strip() for line in input_string.strip().splitlines() if line.strip()
        ]
        points: List[Tuple[int, int, int]] = []
        for line in lines:
            parts = [part.strip() for part in line.split(",")]
            points.append(tuple(int(part) for part in parts))  # type: ignore[arg-type]
        return points

    def answer(self) -> Any:
        data = self.input
        points = (
            self.parse_input(data) if isinstance(data, str) or data is None else data
        )

        n = len(points)
        max_pairs = n * (n - 1) // 2
        limit = min(1000, max_pairs)
        max_heap: List[Tuple[int, int, int]] = []

        if limit:
            for i in range(n):
                x1, y1, z1 = points[i]
                for j in range(i + 1, n):
                    x2, y2, z2 = points[j]
                    dx = x1 - x2
                    dy = y1 - y2
                    dz = z1 - z2
                    dist_sq = dx * dx + dy * dy + dz * dz
                    entry = (-dist_sq, i, j)
                    if len(max_heap) < limit:
                        heapq.heappush(max_heap, entry)
                    elif dist_sq < -max_heap[0][0]:
                        heapq.heapreplace(max_heap, entry)

        edges = sorted((-neg_d, i, j) for neg_d, i, j in max_heap)

        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        for _, a, b in edges:
            union(a, b)

        component_sizes = {}
        for idx in range(n):
            root = find(idx)
            component_sizes[root] = size[root]

        largest = sorted(component_sizes.values(), reverse=True)
        if not largest:
            return 0
        return math.prod(largest[:3])
