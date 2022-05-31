import turtle

window=turtle.Screen()
window.title("Ping Pong Game By Aseel Hodhod")#العنوان
window.setup(width=800,height=600)#طول وعرض الشاشة
window.tracer(0)#ما يعمل فاصل زمني اثناء اللعب
window.bgcolor(0.1,0.1,0.1)#لون الشاشة
#انشاء العنصو وهو الكرة
ball=turtle.Turtle()
ball.speed(0)  #سرعة الكرة
ball.shape("circle")    #شكل الكرة
ball.color("white")   #لون الكرة
ball.shapesize(stretch_len=1,stretch_wid=1)   #حجم الكرة ,, الطبيعي بيكون 20 بكسل
ball.goto(x=0,y=0)  # تبدا من نقطة الاصل
ball.penup()  # لمنع الخطوط اثناء الحركة تكون مثل سن القلم
#**************************
#التحكم في حركة الكرة
ball_dx,ball_dy=1,1
ball_speed=0.5
#************************************
#انشاء خط المنتصف
line=turtle.Turtle() # اي اشي بدي انشاه بستدعيه هيك بعدين بعطيه عناصر
line.speed(0)
line.shape("circle")
line.color("white")
line.shapesize(stretch_len=0.1,stretch_wid=25)
line.penup()
line.goto(0,0) #الخط يكون بالمنتصف
#**************************
#مضرب player one
player_one=turtle.Turtle()
player_one.speed(0)
player_one.shape("square")
player_one.color("red")
player_one.shapesize(stretch_len=1,stretch_wid=5)
player_one.penup()
player_one.goto(x=-350,y=0) # السالب عشان على الحافة اليسار
#**************************
#مضرب player two
player_two=turtle.Turtle()
player_two.speed(0)
player_two.shape("square")
player_two.color("blue")
player_two.shapesize(stretch_len=1,stretch_wid=5)
player_two.penup()
player_two.goto(x=350,y=0)
#***********************
#نص النتيجة في الاعلى
score=turtle.Turtle()
score.speed(0)
score.shape("circle")
score.color("red")
score.goto(x=0,y=260)
score.write("Player 1 : 0 , Player 2 : 0 ",align="center",font=("ِarial",14,"normal"))
score.hideturtle()
p1_score,p2_score=0,0
#***********************
#تحريك المضربين لاعلى او اسفل
def p1_move_up():
    player_one.sety(player_one.ycor()+20) #  لاعلى بمقدار 20 بكسل
def p1_move_down():
    player_one.sety(player_one.ycor()-20) #لاسفل بمقدار 20 بكسل

def p2_move_up():
        player_two.sety(player_two.ycor() + 20)  #for player 2

def p2_move_down():
        player_two.sety(player_two.ycor() - 20)
window.listen() # الاستجابة عند الغط على الكيبورد
window.onkeypress(p1_move_up,"a")
window.onkeypress(p1_move_down,"s")
window.onkeypress(p2_move_up,"Up")
window.onkeypress(p2_move_down,"Down")
#*******************
#تكرار للعبة
while True:    #تحديث للشاشة
    window.update()
    ball.setx(ball.xcor()+(ball_dx*ball_speed))
    ball.sety(ball.ycor()+(ball_dy*ball_speed))
    if (ball.ycor()>290):
         ball.sety(290)
         ball_dy *= -1
    if (ball.ycor() < -290):
        ball.sety(-290)
        ball_dy *= -1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (player_one.ycor() - 60) and ball.ycor() < (
            player_one.ycor() + 60):
        ball.setx(-340)
        ball_dx *= -1

        # collision with player 2
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (player_two.ycor() - 60) and ball.ycor() < (
            player_two.ycor() + 60):
        ball.setx(340)
        ball_dx *= -1
    if (ball.xcor() > 390):
        ball.goto(0, 0)
        ball_dx *= -1  
        score.clear()
        p1_score += 1
        score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",
                    font=("Courier", 14, "normal"))

    if (ball.xcor() < -390):
        ball.goto(0, 0)
        ball_dx *= -1
        score.clear()
        p2_score += 1
        score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",font=("arial", 14, "normal"))





