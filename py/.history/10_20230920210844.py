class Experiment():  
    def __init__(self, M, N, ratio=1,K=100, lr=0.02, step=100, lmbda=0.01, fp='../dataset/ml-1m/ratings.dat'):
        ''':params: M, 进行多少次实验 :params: N, TopN推荐物品的个数
        :params: ratio, 正负样本比例  :params: K, 隐语义个数
        :params: lr, 学习率          :params: step, 训练步数
        :params: lmbda, 正则化系数    :params: fp, 数据文件路径'''
        self.M = M
        self.K = K
        self.N = N
        self.ratio = ratio
        self.lr = lr
        self.step = step
        self.lmbda = lmbda
        self.fp = fp
        self.alg = LFM