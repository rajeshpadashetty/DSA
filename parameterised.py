def fun(i,sum):
    if i<0:
        print(sum)
        return
    fun(i-1,sum+i)
fun(5,0)
