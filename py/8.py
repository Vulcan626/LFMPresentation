# 训练
    P, Q = {}, {}
    for user in train:
        P[user] = np.random.random(K)
    for item in items:
        Q[item] = np.random.random(K)
            
    for s in trange(step):
        data = nSample(train, ratio)
        for user in data:
            for item in data[user]:
                eui = data[user][item] - (P[user] * Q[item]).sum()
                P[user] += lr * (Q[item] * eui - lmbda * P[user])
                Q[item] += lr * (P[user] * eui - lmbda * Q[item])
        lr *= 0.9 # 调整学习率