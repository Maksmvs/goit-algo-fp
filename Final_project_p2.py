import turtle

def draw_pifagoras_tree(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length * level)
    t.right(45)
    draw_pifagoras_tree(t, branch_length * 0.7, level - 1)  
    t.left(90)
    draw_pifagoras_tree(t, branch_length * 0.7, level - 1)  
    t.right(45)
    t.backward(branch_length * level)

def main():
    
    level = int(input("Введіть рівень рекурсії, оптимальне число від 4 - 8: "))

    screen = turtle.Screen()
    screen.setup(width=800, height=800) 
    screen.bgcolor("white")
    screen.title("Дерево Піфагора")

    t = turtle.Turtle()
    t.speed(0) 
    t.color("blue")
    t.left(90)  

    t.penup()
    t.goto(0, -300)  
    t.pendown()

  
    draw_pifagoras_tree(t, 30, level)

    t.hideturtle()  
    screen.mainloop()

if __name__ == "__main__":
    main()
