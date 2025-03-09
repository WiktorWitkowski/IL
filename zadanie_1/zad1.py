
class HexList(list):
    def __repr__(self):
        return "[" + ", ".join(hex(x) for x in self) + "]"

    def __getitem__(self, index):
        chunk = super().__getitem__(index)
        if isinstance(chunk, list):
            return [hex(x) for x in chunk]
        return hex(chunk)


my_list = HexList([1, 15, 16, 25])
print(my_list)
print(my_list[0])
print(my_list[1])

my_list.append(100)
my_list.append(0x11)

print(my_list[0:2])
print(my_list[3:])
my_list.extend([0, 44])

print(my_list)
