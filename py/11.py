# 定义单次实验
    @timmer
    def worker(self, train, test):
        '''
        :params: train, 训练数据集
        :params: test, 测试数据集
        :return: 各指标的值
        '''
        getRecommendation = self.alg(train, self.ratio, self.K, 
                                     self.lr, self.step, self.lmbda, self.N)
        metric = Metric(train, test, getRecommendation)
        return metric.eval()