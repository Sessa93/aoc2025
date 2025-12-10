import heapq
from typing import Any, Tuple, List

from src.base.abstract_problem import AbstractProblem

"""
Implement Kruskal-style unions over all pairwise distances,
stopping at the step that connects the final two components and returning the product of those junction boxes' X coordinates
"""


class Problem2Day8(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=8, problem_number=2, input=input)

    @staticmethod
    def parse_input(input_string: str) -> List[Tuple[int, int, int]]:
        lines = [
            line.strip() for line in input_string.strip().splitlines() if line.strip()
        ]
        points: List[Tuple[int, int, int]] = []
        for line in lines:
            parts = [part.strip() for part in line.split(",")]
            if len(parts) != 3:
                raise ValueError(f"Invalid coordinate line: {line}")
            points.append(tuple(int(part) for part in parts))  # type: ignore[arg-type]
        return points

    def answer(self) -> Any:
        data = self.input
        points = (
            self.parse_input(data) if isinstance(data, str) or data is None else data
        )

        n = len(points)

        heap: List[Tuple[int, int, int]] = []
        for i in range(n):
            x1, y1, z1 = points[i]
            for j in range(i + 1, n):
                x2, y2, z2 = points[j]
                dx = x1 - x2
                dy = y1 - y2
                dz = z1 - z2
                dist_sq = dx * dx + dy * dy + dz * dz
                heapq.heappush(heap, (dist_sq, i, j))

        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            return True

        components = n
        last_edge: Tuple[int, int] | None = None

        while components > 1 and heap:
            _, a, b = heapq.heappop(heap)
            if union(a, b):
                components -= 1
                last_edge = (a, b)

        if not last_edge:
            return 0

        a_idx, b_idx = last_edge
        return points[a_idx][0] * points[b_idx][0]
