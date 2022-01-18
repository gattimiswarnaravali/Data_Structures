import collections
class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x

    
# Your FreqStack object will be instantiated and called as such:
freqStack = FreqStack();
freqStack.push(5); 
freqStack.push(7); 
freqStack.push(5); 
freqStack.push(7); 
freqStack.push(4); 
freqStack.push(5); 
print(freqStack.pop())   
print(freqStack.pop())   
print(freqStack.pop())   
print(freqStack.pop())