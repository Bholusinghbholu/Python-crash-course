mya = ["apple","mango","banana"]
ya = mya[:]
mya.append("grapes")
ya.append("jamun")
print("my fav fruits are:")
for fr in mya:
    print(fr)
print("\nmy least fav fruits are:")
for yr in ya:
    print(yr)
    
for i in ya,mya:
    print(i)
