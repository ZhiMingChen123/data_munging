from pandas import pd
from numpy import np


class DframeTools:
    # miss_data作为异常值列表传入类，将异常值作为空值进行处理
    def __init__(self,miss_data=[np.nan,'NS',999999,-999999],df=None,axis=0):
        self.axis = axis
        self.miss_data = miss_data
        #处理异常数据
        self.df = df[~df.isin(self.miss_data)]
    
    def method_mean(self):
        #获取平均值序列
        s_mean = self.df.apply(lambda x:x.mean(),axis=self.axis)
        #序列转换
        df_mean = s_mean.to_frame()
        return df_mean

    def method_median(self):
        #获取中位数
        s_med = self.df.apply(lambda x:x.median(),axis=self.axis)
        #序列转换
        df_median = s_med.to_frame()
        return df_median

    def method_max(self):
        #获取最大值
        s_max = self.df.apply(lambda x:x.max(),axis=self.axis)
        #序列转换
        df_max = s_max.to_frame()
        return df_max

    def method_min(self):
        #获取最小值
        s_min = self.df.apply(lambda x:x.min(),axis=self.axis)
        #序列转换
        df_min = s_min.to_frame()
        return df_min

    def method_count(self):
        #获取不同值计数
        s_count = self.df.apply(lambda x:len(x.count()),axis=self.axis)
        #序列转换
        df_count = s_count.to_frame()
        return df_count
    
    def method_variance(self):
        #获取方差数列
        s_variance = self.df.apply(lambda x:x.var(),axis=self.axis)
        #序列转换
        df_variance = s_variance.to_frame()
        return df_variance
        