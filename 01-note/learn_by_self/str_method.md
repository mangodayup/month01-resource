## 判断

**[isspace()](http://www.runoob.com/python3/python3-string-isspace.html)**

如果字符串中只包含空白，则返回 True，否则返回  False.

[**startswith(substr,  beg=0,end=len(string))**](http://www.runoob.com/python3/python3-string-startswith.html)

检查字符串是否是以指定子字符串  substr 开头，是则返回 True，否则返回 False。如果beg 和 end  指定值，则在指定范围内检查。

[**endswith(suffix,  beg=0, end=len(string))**](http://www.runoob.com/python3/python3-string-endswith.html)

检查字符串是否以 obj 结束，如果beg 或者 end  指定则检查指定的范围内是否以 obj 结束，如果是，返回  True,否则返回 False.

## 查找

[**find(str,  beg=0 end=len(string))**](http://www.runoob.com/python3/python3-string-find.html)

检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1

[**rfind(str,  beg=0,end=len(string))**](http://www.runoob.com/python3/python3-string-rfind.html)

类似于 find()函数，不过是从右边开始查找.

[**count(str,  beg= 0,end=len(string))**](http://www.runoob.com/python3/python3-string-count.html)

返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

## 修改

[**replace(old,  new [, max\])**](http://www.runoob.com/python3/python3-string-replace.html)

把  将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。

[**lstrip()**](http://www.runoob.com/python3/python3-string-lstrip.html)

截掉字符串左边的空格或指定字符。

[**rstrip()**](http://www.runoob.com/python3/python3-string-rstrip.html)

删除字符串字符串末尾的空格.

[**strip([chars\])**](http://www.runoob.com/python3/python3-string-strip.html)

在字符串上执行 lstrip()和  rstrip()

[**lower()**](http://www.runoob.com/python3/python3-string-lower.html)

转换字符串中所有大写字符为小写.

[**upper()**](http://www.runoob.com/python3/python3-string-upper.html)

转换字符串中的小写字母为大写

[**swapcase()**](http://www.runoob.com/python3/python3-string-swapcase.html)

将字符串中大写转换为小写，小写转换为大写

## 对齐

[**center(width,  fillchar)**](http://www.runoob.com/python3/python3-string-center.html)

返回一个指定的宽度 width 居中的字符串，fillchar  为填充的字符，默认为空格。

[**zfill  (width)**](http://www.runoob.com/python3/python3-string-zfill.html)

返回长度为 width 的字符串，原字符串右对齐，前面填充0

[**ljust(width[,  fillchar\])**](http://www.runoob.com/python3/python3-string-ljust.html)

返回一个原字符串左对齐,并使用 fillchar 填充至长度  width 的新字符串，fillchar 默认为空格。