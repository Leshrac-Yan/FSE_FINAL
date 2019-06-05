def profit(price):
    days=len(price)
    if days<=1:
        return 0
    else:
        templist=[0]
        for i in range(1,days-1):
            buyin=int(price[0])
            sellout=int(price[i])
            templist.append(sellout-buyin+profit(price[i+1:days]))
        buyin=int(price[0])
        sellout=int(price[days-1])
        templist.append(sellout-buyin)
        maxlist=max(templist)
        temppro=profit(price[1:days])
        if temppro>maxlist:
            return temppro
        else:
            return maxlist


inpstr=input()
inpstr=inpstr[1:-1]
price=inpstr.split(",")
print(profit(price))