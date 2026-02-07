class AutoInputs:
    def __init__(self, enabled: bool):
        self.enabled = enabled

    def input(self, inputs):
        if self.enabled:
            return getAutoInput(inputs)
        else:
            return numList(input())
        
def numList(txt):
    return list(map(int, txt.split()))

start = 0
def getAutoInput(inputs):
    global start
    nums = ""
    for i in range(start, len(inputs)):
        char = inputs[i]

        if char == 'p':
            return numList(input())
        
        if char == "\n":
            start = i + 1
            print("AUTOINPUT:", nums:= numList(nums))
            return nums
            
        nums += char