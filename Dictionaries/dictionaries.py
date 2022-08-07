

class Tabelas:
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.current_size = 0
        self.keys = [None] * self.max_size
        self.values = [None] * self.max_size

    def search(self, key) -> int:
        for i in range(self.current_size):
            if self.keys[i] == key:
                return i

    def __len__(self) -> int:
        return self.current_size


    def __repr__(self) -> str:
        r = ""
        for i in range(self.current_size):
            r += self.keys[i] + " = " + self.values[i] + "\n"
        return r

    def has_free_space(self):
        if self.current_size < self.max_size:
            return True
        else:
            return False

    def insert(self, key, value) -> bool:
        if self.has_free_space():
            searched_key = self.search(key)
            if searched_key == None:
                self.keys[self.current_size] = key
                self.values[self.current_size] = value
                self.current_size += 1
                return True
            else:
                self.values[searched_key] = value
                return True
        else:
            return False

    def remove(self, key):
        item_pos = self.search(key)
        
        if self.keys[item_pos] == self.keys[-1]:
            self.current_size -= 1
        
        for i in range(item_pos, self.current_size - 1):

            if i == self.current_size:
                break
            
            self.keys[i] = self.keys[i + 1]
            self.values[i] = self.values[i + 1]
        
        self.current_size -= 1

    def delete(self):
        self.current_size = 0
             

            
    


    
