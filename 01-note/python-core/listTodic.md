Python列表和字典是Python中用于存储数据的两个数据结构。 **Python列表是对象的有序序列，而字典是无序的。** 列表中的项目可以通过索引(基于它们的位置)来访问，而字典中的项目可以通过键而不是它们的位置来访问。

1. 将元组列表转换为字典

   + `dict()`构造函数直接从键值对序列中构建字典。

     ```python
     l1=[(1,'a'),(2,'b'),(3,'c'),(4,'d')]
     d1=dict(l1)
     print (d1)
     #Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
     ```

2. 将两个长度相同的列表转换为字典

   - 我们可以使用以下命令将两个相同长度的列表转换为字典 `zip()` 。

   - `zip()`将返回一个元组的迭代器。 我们可以使用以下方式将zip对象转换为字典 `dict()`构造函数。

     > “ `**zip** ( **iterables* )` *：*返回一个元组的迭代器，其中第i个元组包含每个参数序列或iterables中的第i个元素。 当最短的可迭代输入耗尽时，迭代器停止。 使用单个可迭代参数，它返回1元组的迭代器。 没有参数，它将返回一个空的迭代器。” — Python官方文档(https://docs.python.org/3.3/library/functions.html#zip)

     ```python
     l1=[1,2,3,4]
     l2=['a','b','c','d']
     d1=zip(l1,l2)
     print (d1)#Output:<zip object at 0x01149528>
     #Converting zip object to dict using dict() contructor.
     print (dict(d1))
     #Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
     ```

     

     

3. 将两个长度不同的列表转换为字典

4. 

5. 将字典列表转换为单个字典

6. 