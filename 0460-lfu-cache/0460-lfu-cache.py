from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        
        val, freq = self.key_to_val_freq[key]
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
        self.freq_to_keys[freq + 1][key] = None
        self.key_to_val_freq[key] = (val, freq + 1)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self.get(key)
            return
        
        if len(self.key_to_val_freq) >= self.capacity:
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last = False)
            del self.key_to_val_freq[evict_key]
        
        self.freq_to_keys[1][key] = None
        self.key_to_val_freq[key] = (value, 1)
        self.min_freq = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)