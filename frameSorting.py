import random

class Frame:
    def __init__(self,seqNo,data=None):
        self.seqNo = seqNo
        self.data = data

n = int(input("Enter the number of frames:  "))

seqList = []
for _ in range(n):
    r = random.randint(1,n*100)
    while r in seqList:
        r = random.randint(1,n*100)
    seqList.append(r)

frames = []
for _ in range(n):
    ch = random.choice(seqList)
    frames.append(Frame(ch))
    seqList.remove(ch)

for i in range(n):
    frames[i].data = input(f"Enter frame data for sequence number {frames[i].seqNo}:  ")

frames.sort(key=lambda x:x.seqNo)

print("\n---SORTED FRAMES----")
for frame in frames:
    print(f"{frame.seqNo} - {frame.data}")
print()
