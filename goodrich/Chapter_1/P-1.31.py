def make_change(m_charged, m_given):
    
    if m_given > 1000:
        print("Error: value is above 1000")
        return None
        
    diff = m_given - m_charged
    bills = [10, 20, 50, 100, 500, 1000]
    coins = [1, 2, 5]
    
    while diff >= 10:
        for i in range(len(bills)):
            if diff == bills[i]:
                print("return one note of {}".format(bills[i]))
                diff = diff - bills[i]
                if diff == 0:
                    break                
            else:
                if diff < bills[i]:
                    print("return one note of {}".format(bills[i-1]))
                    diff = diff - bills[i-1]
                    break
                
    while diff >= 1:
        for i in range(len(coins)):
            if diff == coins[i]:
                print("return one coin of {}".format(coins[i]))
                diff = diff - coins[i]
                if diff == 0:
                    break
            else: 
                if diff < coins[i]:
                    diff = diff - coins[i-1]
                    print("return one coin of {}".format(bills[i-1]))
                    diff = diff - bills[i-1]
                    break
