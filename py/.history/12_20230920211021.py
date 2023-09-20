    @timmer # 多次实验取平均
    def run(self):
        metrics = {'Precision': 0, 'Recall': 0, 
                   'Coverage': 0, 'Popularity': 0}
        dataset = Dataset(self.fp)
        for ii in range(self.M):
            train, test = dataset.splitData(self.M, ii)
            print('Experiment {}:'.format(ii))
            metric = self.worker(train, test)
            metrics = {k: metrics[k]+metric[k] for k in metrics}
        metrics = {k: metrics[k] / self.M for k in metrics}
        print('Average Result (M={}, N={}, ratio={}): {}'.format(\
                              self.M, self.N, self.ratio, metrics))
    # LFM实验
    M, N = 8, 10
    for r in [1, 2, 3, 5, 10, 20]:
        exp = Experiment(M, N, ratio=r)
        exp.run()