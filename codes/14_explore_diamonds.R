# 加载包和数据集
library(ggplot2)
library(gcookbook)
diamonds

# 截取子集
set.seed(123)
# 从全部行中采样出1000行
diamonds <- diamonds[sample(nrow(diamonds), 1000),]

# 查看数据框的一些概要信息
summary(diamonds)
str(diamonds)

# 查看数据框的前几行或最后几行
head(diamonds)
tail(diamonds)

# 价格和克拉的关系
ggplot(diamonds) + geom_point(aes(x=carat, y=price))
# 加入color和cut的影响
ggplot(diamonds) + geom_point(aes(x=carat, y=price, color=color, shape=cut))

# 价格分布
ggplot(diamonds) + geom_histogram(aes(x=price))
# 加入cut的影响
ggplot(diamonds) + geom_histogram(aes(x=price, fill=cut))
# 分组直方图
ggplot(diamonds) + geom_histogram(aes(x=price, fill=cut), position="dodge")
# 百分比直方图
ggplot(diamonds) + geom_histogram(aes(x=price, fill=cut), position="fill")

# 纯净度分布
ggplot(diamonds) + geom_bar(aes(x=clarity))
# 加入color的影响
ggplot(diamonds) + geom_bar(aes(x=clarity, fill=color))

# 价格的概率分布
ggplot(diamonds) + geom_density(aes(x=price))
# 加入cut的影响
ggplot(diamonds) + geom_density(aes(x=price, color=cut))
# 加入color的影响
ggplot(diamonds) + geom_density(aes(x=price, color=color))

# 不同切工下价格的分布
ggplot(diamonds) + geom_boxplot(aes(x=cut, y=price))
# 加入color的影响
ggplot(diamonds) + geom_boxplot(aes(x=cut, y=price, fill=color))

# 坐标变换
ggplot(diamonds) + geom_point(aes(x=carat, y=price, color=color, shape=cut)) + scale_y_log10()

# 加上标题和坐标轴标签
ggplot(diamonds) + geom_point(aes(x=carat, y=price, color=color, shape=cut)) + scale_y_log10() + labs(x='克拉', y='价格', title='克拉和价格之间的关系') + theme(text=element_text(family='Microsoft YaHei'))

?theme