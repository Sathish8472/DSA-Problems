class Solution:

    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)

        def can_assign(k: int) -> bool:
            # Try assigning k tasks (hardest ones)
            available = deque()
            pills_left = pills
            worker_idx = m - 1

            for i in range(k - 1, -1, -1):  # hardest to easiest
                task = tasks[i]

                # Add eligible workers who can do the task with or without pill
                while worker_idx >= m - k and workers[worker_idx] + strength >= task:
                    available.appendleft(workers[worker_idx])
                    worker_idx -= 1

                if not available:
                    return False

                # Prefer worker who can do it without pill
                if available[-1] >= task:
                    available.pop()
                else:
                    if pills_left == 0:
                        return False
                    pills_left -= 1
                    available.popleft()  # give pill to weakest eligible

            return True

        # Binary search for max number of tasks
        left, right = 0, min(n, m)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result




    def maxTaskAssign1(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        count = 0
        tasks = deque(sorted(tasks))
        workers = deque(sorted(workers))

        print(f"tasks: {tasks}, workers: {workers}")

        while len(tasks) > 0:
            task = tasks.popleft()
            # worker = workers.popleft()

            worker = self.find_closest(workers, task)
            workers.remove(worker)

            print(f"task: {task}, worker: {worker}")
            
            if worker >= task:
                count += 1
            elif pills > 0 and worker + strength >= task:
                print("take pill")
                pills -= 1
                count += 1


            print(f"------ tasks: {tasks}, workers: {workers}")
            print("---------")
            
        
        return count
    
    def find_closest(self, arr, target):
            import bisect
            idx = bisect.bisect_left(arr, target)

            if not arr:
                return None  # Handle empty array case

            if idx == 0:
                return arr[0]
            elif idx == len(arr):
                return arr[-1]
            else:
                lower = arr[idx - 1]
                upper = arr[idx]
                dist_lower = abs(target - lower)
                dist_upper = abs(target - upper)

                if dist_lower < dist_upper:
                    return lower
                elif dist_upper < dist_lower:
                    return upper
                else:  # Distances are equal, prioritize upper
                    return upper