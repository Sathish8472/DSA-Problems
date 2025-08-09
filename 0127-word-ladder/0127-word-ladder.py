class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.wordSet = set(wordList)

        if endWord not in self.wordSet:
            return 0
        
        return self.bfs(beginWord, endWord)
    
    def bfs(self, beginWord: str, endWord: str) -> int:
        queue = deque([beginWord])
        distance = 1

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                current_word = queue.popleft()

                if current_word == endWord:
                    return distance
                
                for neighbor in self.get_neighbors(current_word):
                    queue.append(neighbor)
                    self.wordSet.remove(neighbor)
            
            distance += 1

        return 0
        
    def get_neighbors(self, word: str) -> List[str]:
        neighbors = []

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == word[i]:
                    continue

                new_word = word[:i] + c + word[i + 1:]
                if new_word in self.wordSet:
                    neighbors.append(new_word)
        
        return neighbors
