while True:
    weight = float(input())
    
    if weight == -1.0:
        break
        
    print("Objects weighing %.2f on Earth will weigh %.2f on the moon." % (weight, weight * 0.167))