# 负采样函数(注意！！！要按照流行度进行采样)
    def nSample(data, ratio):
        new_data = {}
        # 正样本
        for user in data:
            if user not in new_data:
                new_data[user] = {}
            for item in data[user]:
                new_data[user][item] = 1
        # 负样本
        for user in new_data:
            seen = set(new_data[user])
            pos_num = len(seen)
            item = np.random.choice(items, int(pos_num * ratio * 3), pops)
            item = [x for x in item if x not in seen][:int(pos_num * ratio)]
            new_data[user].update({x: 0 for x in item})
        
        return new_data