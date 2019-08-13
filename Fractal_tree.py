import turtle

def tree(branchLen,t):
    if branchLen > 1:
        if branchLen < 10:
            t.color("green")     
        else:
            t.color("brown")
        t.down()
        t.forward(branchLen)
        t.right(30)
        tree(branchLen-10,t)
        t.left(60)
        tree(branchLen-10,t)
        t.right(30)
        t.up()
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75,t)
    myWin.exitonclick()

main()
