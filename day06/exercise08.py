"""
    练习1：
    将两个列表，合并为一个字典
    		姓名列表["张无忌","赵敏","周芷若"]
    		房间列表[101,102,103]
    {101: '张无忌', 102: '赵敏', 103: '周芷若'}
    练习2：
    颠倒练习1字典键值
    {'张无忌': 101, '赵敏': 102, '周芷若': 103}
"""
list_names = ["张无忌", "赵敏", "周芷若"]
list_rooms = [101, 102, 103]
# dict_data = {}
# for i in range(len(list_names)):
#     key = list_rooms[i]
#     value = list_names[i]
#     dict_data[key] = value
#     # dict_data[list_rooms[i]] = list_names[i]
dict_data = {list_names[i]: list_rooms[i] for i in range(len(list_names))}
print(dict_data)

dict_new = {v: k for k, v in dict_data.items()}
print(dict_new)
