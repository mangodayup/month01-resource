# 练习：根据下列文字，提取变量，使用字符串格式化打印信息
# 湖北确诊67802人,治愈63326人,治愈率0.99
region = "湖北"
confirmed = 67802
cure = 63326
rate_cure = 0.99
print("%s确诊%d人,治愈%s人,治愈率%.2f" % (region, confirmed, cure, rate_cure))

# 70秒是01分零10秒
total_second = 70
print("%s秒是%.2d分零%.2d秒" % (total_second, total_second // 60, total_second % 60))
