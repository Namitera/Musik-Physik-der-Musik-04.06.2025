from manim import *
import soundfile as sf
import os



class Thumbnail(Scene):
    def construct(self):
        #--disable_caching

        r = []
        d = ValueTracker(10)

        for i in range(0,27,1):
            r.append(0.38*i)
            
        def fx(x):
            y = -6.5/d.get_value()**2 * (x-d.get_value())**2 +6.5
            return y

        points = []
        for i in r:
            points.append([i,fx(i),0])

        ax = Axes(x_range=[0,16,1],x_length=16,y_range=[0,7,1],y_length=7).shift(RIGHT*1.5)
        sw = Tex("Physik").to_edge(UP).scale(2.1).shift(DOWN*1.9 + LEFT)
        sw2 = Tex("Physik").to_edge(UP).scale(2.15).move_to(sw).set_color(GRAY)
        rw = Tex("der Musik").to_edge(UP).scale(2.1).shift(DOWN*3+LEFT*0.1)
        rw2 = Tex("der Musik").to_edge(UP).scale(2.15).shift(DOWN*2.98+LEFT*0.1).set_color(GRAY)
        text = VGroup(sw,rw)
        textback = VGroup(sw2,rw2)
        eps = 0.00001
        rec = Rectangle(color=BLACK,fill_opacity=1).scale(10)

        # dots = VGroup(*[Dot(i) for i in points]).shift(LEFT*6.5 + DOWN*3.5)
        # j = -1
        # for i in dots:
        #     j += 1
        #     dots[j].add_updater(lambda mob, j=j: mob.set_y(fx(r[j])-3.5))

        op = 1


        for i in r:
            parab = ax.plot(lambda x: 0)
            self.add(parab)
            parab.add_updater(lambda mob, i=i: mob.become(ax.plot(lambda x: -(fx(i)/(i**2+eps)) * np.sin(x-i) +fx(i) )).set_color(BLUE))

            # parab2 = ax.plot(lambda x: 0)
            # self.add(parab2)
            # parab2.add_updater(lambda mob, i=i: mob.become(ax.plot(lambda x: -(fx(i)/(i**2+eps)) * (x-i)**2 +fx(i),stroke_opacity=op*np.floor(i)/15).set_color(BLUE)))

        #add parab
        self.add(ax,textback,text, parab)
        self.wait(frozen_frame=False)





class Opening(Scene):
    def construct(self):
        #--disable_caching

        r = []
        d = ValueTracker(10)

        for i in range(0,27,1):
            r.append(0.38*i)
            
        def fx(x):
            y = -6.5/d.get_value()**2 * (x-d.get_value())**2 +6.5
            return y

        points = []
        for i in r:
            points.append([i,fx(i),0])

        ax = Axes(x_range=[0,16,1],x_length=16,y_range=[0,7,1],y_length=7).shift(RIGHT*1.5)
        sw = Tex("Physik").to_edge(UP).scale(2.1).shift(DOWN*1.9 + LEFT)
        sw2 = Tex("Physik").to_edge(UP).scale(2.15).move_to(sw).set_color(GRAY)
        rw = Tex("der Musik").to_edge(UP).scale(2.1).shift(DOWN*3+LEFT*0.1)
        rw2 = Tex("der Musik").to_edge(UP).scale(2.15).shift(DOWN*2.98+LEFT*0.1).set_color(GRAY)
        text = VGroup(sw,rw)
        textback = VGroup(sw2,rw2)
        eps = 0.00001
        rec = Rectangle(color=BLACK,fill_opacity=1).scale(10)

        # dots = VGroup(*[Dot(i) for i in points]).shift(LEFT*6.5 + DOWN*3.5)
        # j = -1
        # for i in dots:
        #     j += 1
        #     dots[j].add_updater(lambda mob, j=j: mob.set_y(fx(r[j])-3.5))

        op = 1


        for i in r:
            parab = ax.plot(lambda x: 0)
            self.add(parab)
            parab.add_updater(lambda mob, i=i: mob.become(ax.plot(lambda x: -(fx(i)/(i**2+eps)) * np.sin(x-i) +fx(i) )).set_color(BLUE))

            # parab2 = ax.plot(lambda x: 0)
            # self.add(parab2)
            # parab2.add_updater(lambda mob, i=i: mob.become(ax.plot(lambda x: -(fx(i)/(i**2+eps)) * (x-i)**2 +fx(i),stroke_opacity=op*np.floor(i)/15).set_color(BLUE)))

        self.add_sound('music_frequency/Music/Opening.wav', time_offset=2.3)

        #add parab
        self.add(ax,textback,text)
        self.wait(frozen_frame=False)
        self.remove(textback)
        self.play(d.animate.set_value(1),Unwrite(text),rate_func=rate_functions.ease_in_quart,run_time=4)
        # self.play(FadeIn(rec))
        op = 0
        parab.suspend_updating()
        # parab2.suspend_updating()
        # self.remove(ax,text,textback,parab,rec)
        # self.wait(0.1,frozen_frame=False)
        # keine ahnung wieso DIESE methode geht, macht aber 5 min weniger renderzeit, parab gibts soviele ig.
        self.play(*[FadeOut(mob)for mob in self.mobjects],run_time=0.1)
        

        # self.add(NumberPlane())
        
        axes1 = Axes(x_range=[0, 6*PI , PI], y_range=[0, 28, 1], x_length=0.6666, y_length=6.45).shift(LEFT*4.5 +RIGHT*3.667*4) #8 triole
        axes2 = Axes(x_range=[0, 6*PI , PI], y_range=[0, 28, 1], x_length=2, y_length=6.45).shift(LEFT*4 +RIGHT*3.667*4) #4
        axes3 = Axes(x_range=[0, 6*PI , PI], y_range=[0, 28, 1], x_length=4, y_length=6.45).shift(LEFT*3 +RIGHT*3.667*4) #2
        g1 = axes2.plot(lambda x: np.sin(x) +1, color=YELLOW)
        g2 = axes2.plot(lambda x: np.sin(x) +3, color=YELLOW)

        g3 = axes1.plot(lambda x: np.sin(x) +24, color=BLUE).shift(RIGHT* 2)
        g4 = axes1.plot(lambda x: np.sin(x) +22, color=BLUE).shift(RIGHT* 2.666)
        g5 = axes1.plot(lambda x: np.sin(x) +25, color=BLUE).shift(RIGHT* 3.333)
        g6 = axes1.plot(lambda x: np.sin(x) +24, color=BLUE).shift(RIGHT* 4)
        g7 = axes1.plot(lambda x: np.sin(x) +22, color=BLUE).shift(RIGHT* 4.666)
        g8 = axes1.plot(lambda x: np.sin(x) +19, color=BLUE).shift(RIGHT* 5.333)

        g9 = axes2.plot(lambda x: np.sin(x) +18, color=YELLOW).shift(RIGHT* 6.1)

        g10 = axes3.plot(lambda x: np.sin(x) +18, color=RED).shift(RIGHT* 8)
        g11 = axes3.plot(lambda x: np.sin(x) +3, color=RED).shift(RIGHT* 8)

        g12 = axes2.plot(lambda x: np.sin(x) +9, color=YELLOW).shift(RIGHT* 12)
        g13 = axes2.plot(lambda x: np.sin(x) +7, color=YELLOW).shift(RIGHT* 14)
        g14 = axes2.plot(lambda x: np.sin(x) +5, color=YELLOW).shift(RIGHT* 16)

        g15 = axes1.plot(lambda x: np.sin(x) +9, color=BLUE).shift(RIGHT* 18)
        g16 = axes1.plot(lambda x: np.sin(x) +7, color=BLUE).shift(RIGHT* 18.666)
        g17 = axes1.plot(lambda x: np.sin(x) +11, color=BLUE).shift(RIGHT* 19.333)
        g18 = axes1.plot(lambda x: np.sin(x) +9, color=BLUE).shift(RIGHT* 20)
        g19 = axes1.plot(lambda x: np.sin(x) +7, color=BLUE).shift(RIGHT* 20.666)
        g20 = axes1.plot(lambda x: np.sin(x) +5, color=BLUE).shift(RIGHT* 21.333)

        g21 = axes2.plot(lambda x: np.sin(x) +1, color=YELLOW).shift(RIGHT* 22.1)

        g22 = axes3.plot(lambda x: np.sin(x) +3, color=RED).shift(RIGHT* 24)
        g23 = axes3.plot(lambda x: np.sin(x) +18, color=RED).shift(RIGHT* 28)



        allGs = VGroup(g1, g2, g3, g4, g5, g6, g7, g8,g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22, g23)
        self.add(axes1,axes2,axes3)
        self.add(allGs)
        #110 BPM



        height = 0.411
        height2 = 0.5*height
        width = 1.5
        width2 = 0.5*width
        w1 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)
        w2 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)
        w3 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)
        w4 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)
        w5 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)
        w6 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)
        w7 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)
        w8 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)
        w9 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)
        w10 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)
        w11 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)
        w12 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)
        w13 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)
        w14 = Rectangle(height=height, width=width, color=WHITE, fill_color=WHITE, fill_opacity=1)

        b1 = Rectangle(height=height2, width=width2, color=BLACK, fill_color=BLACK, fill_opacity=1)
        b2 = Rectangle(height=height2, width=width2, color=BLACK, fill_color=BLACK, fill_opacity=1)
        b3 = Rectangle(height=height2, width=width2, color=BLACK, fill_color=BLACK, fill_opacity=1)
        b4 = Rectangle(height=height2, width=width2, color=BLACK, fill_color=BLACK, fill_opacity=1).set_opacity(0)
        b5 = Rectangle(height=height2, width=width2, color=BLACK, fill_color=BLACK, fill_opacity=1)
        b6 = Rectangle(height=height2, width=width2, color=BLACK, fill_color=BLACK, fill_opacity=1)
        b7 = Rectangle(height=height2, width=width2, color=BLACK, fill_color=BLACK, fill_opacity=1).set_opacity(0)
        b8 = Rectangle(height=height2, width=width2, color=BLACK, fill_color=BLACK, fill_opacity=1)
        b9 = Rectangle(height=height2, width=width2, color=BLACK, fill_color=BLACK, fill_opacity=1)
        b10 = Rectangle(height=height2, width=width2, color=BLACK, fill_color=BLACK, fill_opacity=1)
        b11 = Rectangle(height=height2, width=width2, color=BLACK, fill_color=BLACK, fill_opacity=1).set_opacity(0)
        b12 = Rectangle(height=height2, width=width2, color=BLACK, fill_color=BLACK, fill_opacity=1)
        b13 = Rectangle(height=height2, width=width2, color=BLACK, fill_color=BLACK, fill_opacity=1)
        whites = VGroup(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14).shift(LEFT*5.8)
        blacks = VGroup(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13).shift(LEFT*5.4)
        whites.arrange_in_grid(rows=14,buff=0.05)
        blacks.arrange_in_grid(rows=13,buff=0.25)
        self.play(DrawBorderThenFill(whites), Write(blacks))       

        blackout = Rectangle(height=10, width=5, color=BLACK, fill_opacity=1).shift(LEFT*9.05)
        self.add(blackout)


        self.play(allGs.animate.shift(LEFT*3.667), rate_func=linear, run_time=1)
        self.play(allGs.animate.shift(LEFT*3.667), rate_func=linear, run_time=1)
        self.play(allGs.animate.shift(LEFT*3.667), rate_func=linear, run_time=1)
        self.play(allGs.animate.shift(LEFT*3.667), rate_func=linear, run_time=1)
        w14.set_color(YELLOW)
        w13.set_color(YELLOW)
        self.play(allGs.animate.shift(LEFT*1.999), rate_func=linear, run_time=0.5454)
        w14.set_color(WHITE)
        w13.set_color(WHITE)
        b2.set_color(BLUE)

        self.play(allGs.animate.shift(LEFT*0.666), rate_func=linear, run_time=0.1818)
        b3.set_color(BLUE)
        b2.set_color(BLACK)

        self.play(allGs.animate.shift(LEFT*0.666), rate_func=linear, run_time=0.1818)
        b3.set_color(BLACK)
        w2.set_color(BLUE)

        self.play(allGs.animate.shift(LEFT*0.666), rate_func=linear, run_time=0.1818)
        w2.set_color(WHITE)
        b2.set_color(BLUE)

        self.play(allGs.animate.shift(LEFT*0.666), rate_func=linear, run_time=0.1818)
        b2.set_color(BLACK)
        b3.set_color(BLUE)

        self.play(allGs.animate.shift(LEFT*0.666), rate_func=linear, run_time=0.1818)
        b3.set_color(BLACK)
        w5.set_color(BLUE)

        self.play(allGs.animate.shift(LEFT*0.666), rate_func=linear, run_time=0.1818)
        w5.set_color(WHITE)
        b5.set_color(YELLOW)

        self.play(allGs.animate.shift(LEFT*1.999), rate_func=linear, run_time=0.5454)
        b5.set_color(RED)
        w13.set_color(RED)

        self.play(allGs.animate.shift(LEFT*3.998), rate_func=linear, run_time=1.06)
        b5.set_color(BLACK)
        w13.set_color(WHITE)
        w10.set_color(YELLOW)

        self.play(allGs.animate.shift(LEFT*1.999), rate_func=linear, run_time=0.5454)
        w10.set_color(WHITE)
        w11.set_color(YELLOW)

        self.play(allGs.animate.shift(LEFT*1.999), rate_func=linear, run_time=0.5454)
        w11.set_color(WHITE)
        w12.set_color(YELLOW)

        self.play(allGs.animate.shift(LEFT*1.999), rate_func=linear, run_time=0.5454)
        w12.set_color(WHITE)
        w10.set_color(BLUE)

        self.play(allGs.animate.shift(LEFT*0.666), rate_func=linear, run_time=0.1818)
        w10.set_color(WHITE)
        w11.set_color(BLUE)

        self.play(allGs.animate.shift(LEFT*0.666), rate_func=linear, run_time=0.1818)
        w11.set_color(WHITE)
        w9.set_color(BLUE)

        self.play(allGs.animate.shift(LEFT*0.666), rate_func=linear, run_time=0.1818)
        w9.set_color(WHITE)
        w10.set_color(BLUE)

        self.play(allGs.animate.shift(LEFT*0.666), rate_func=linear, run_time=0.1818)
        w10.set_color(WHITE)
        w11.set_color(BLUE)

        self.play(allGs.animate.shift(LEFT*0.666), rate_func=linear, run_time=0.1818)
        w11.set_color(WHITE)
        w12.set_color(BLUE)

        self.play(allGs.animate.shift(LEFT*0.666), rate_func=linear, run_time=0.1818)
        w12.set_color(WHITE)
        w14.set_color(YELLOW)

        self.play(allGs.animate.shift(LEFT*1.999), rate_func=linear, run_time=0.5454)
        w14.set_color(WHITE)
        w13.set_color(RED)

        self.play(allGs.animate.shift(LEFT*3.998), rate_func=linear, run_time=1.06)
        w13.set_color(WHITE)
        b5.set_color(RED)

        self.play(allGs.animate.shift(LEFT*3.998), rate_func=linear, run_time=1.06)
        b5.set_color(BLACK)

        self.play(allGs.animate.shift(LEFT*3.667), rate_func=linear, run_time=1)
        self.play(FadeOut(whites), FadeOut(blacks), FadeOut(allGs), FadeOut(axes1), FadeOut(axes2), FadeOut(axes3), FadeOut(blackout), run_time=1)





class Begin(Scene):
    def construct(self):

        amplitude = ValueTracker(1)
        frequency = ValueTracker(1)
        phi = ValueTracker(0)

        axis = Axes(x_range=[-2,8,1], x_length=13, y_range=[-1,1,1], y_length=7, tips=False )
        g1 = axis.plot(lambda x: 0)
        g1.add_updater(lambda mob: mob.become(
            axis.plot(lambda x: amplitude.get_value() * np.sin(frequency.get_value() *PI/4* x + phi.get_value())
                      ).set_color(ManimColor((340- 85*frequency.get_value(),0,85*frequency.get_value() -85))))
            )
        g2 = Rectangle(height=3.5, width=0.02, color=GREEN, fill_color=GREEN, fill_opacity=1).shift(LEFT*1.28 + UP*1.75)	
        g3 = Rectangle(height=0.01, width=5.2, color=YELLOW, fill_color=YELLOW, fill_opacity=1).shift(LEFT*1.3)	
        g4 = Rectangle(height=0.01, width=2.6, color=YELLOW, fill_color=YELLOW, fill_opacity=1).shift(LEFT*0)	
        amp = MathTex(r"A = 1").next_to(g2, LEFT).shift(UP*0.1)
        lamda = MathTex(r"\lambda = 4").next_to(g3, DOWN).shift(UP*-0.1)
        lamda[0][0].set_color(YELLOW)
        lamda2 = MathTex(r"\lambda = 2").next_to(g3, DOWN).shift(UP*-0.1)
        lamda2[0][0].set_color(YELLOW)
        f1 = MathTex(r"f = \frac{v_{s}}{\lambda } = 171.5 Hz")
        f1[0][5].set_color(YELLOW)
        f1[0][2:4].set_color(GREEN)
        vs = MathTex(r"v_{s} = 343 \mathrm{m/s}").to_edge(UL)
        vs[0][0:2].set_color(GREEN)
        # self.add(NumberPlane())
        
        self.play(Write(axis), Write(g1), run_time=2)
        self.play(Write(g2),Write(amp), run_time=2)
        self.wait(7)
        self.play(phi.animate.set_value(0), frequency.animate.set_value(2), amp.animate.shift(LEFT*1.3), g2.animate.shift(LEFT*1.3), run_time=1)
        self.wait()
        self.play(Write(g3), Write(lamda), run_time=2)
        self.wait(10)
        self.play(frequency.animate.set_value(4), FadeOut(amp), FadeOut(g2), ReplacementTransform(g3,g4), ReplacementTransform(lamda,lamda2), run_time=1)
        self.wait(7)    
        f1.next_to(lamda2, DOWN*1.5)
        self.play(Write(f1), run_time=2)
        self.wait(1)
        self.play(Transform(f1.copy(), vs), run_time=2)
        self.wait()
        # self.play(phi.animate.set_value(0), frequency.animate.set_value(4), rate_func=linear, run_time=1)
        # self.wait()
        




class PitchFrequency(Scene):
    def construct(self):

        # self.add(NudmberPlane())
        axes = Axes(
            x_range=[0,10 , 1],
            y_range=[0, 4, 1],
            x_length=10,
            y_length=4,
            axis_config={"include_tip": False},
            tips=False
        ).shift(UP*1.4 + RIGHT*2)

        # ich weis nicht wieso aber diese linien sehen schief aus, optsiche täuschung
        g1 = axes.plot(lambda x: np.sqrt(x), color=YELLOW)
        g2 = axes.plot(lambda x: 1 +0*x)
        g3 = axes.plot(lambda x: 2 +0*x)

        g4 = axes.plot(lambda x: 1.16)
        g5 = axes.plot(lambda x: 1.33)
        g6 = axes.plot(lambda x: 1.5)
        g7 = axes.plot(lambda x: 1.66)
        g8 = axes.plot(lambda x: 1.83)
        g9 = axes.plot(lambda x: 2.0)
        g10 = axes.plot(lambda x: 2.16)
        g11 = axes.plot(lambda x: 2.33)
        g12 = axes.plot(lambda x: 2.5)
        g13 = axes.plot(lambda x: 2.66)
        g14 = axes.plot(lambda x: 2.83)
        g15 = axes.plot(lambda x: 3.0)
        graphs = VGroup(g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15)


        x_label = Tex("Frequenz (Hz)").shift(UP*-1.5 +5*RIGHT)
        y_label = Tex("Tonhöhe").scale(1).shift(-4.5*RIGHT + UP*3)

        f1 = MathTex("440 \mathrm{Hz}").shift(LEFT*2 + DOWN*1.3)
        f2 = MathTex("1760 \mathrm{Hz}").shift(LEFT*-1 + DOWN*1.3)
        f3 = MathTex("880 \mathrm{Hz}").shift(LEFT*-1 + DOWN*1.3)
        t1 = MathTex("1").shift(LEFT*3.5 + DOWN*-0.4)
        t2 = MathTex("2").shift(LEFT*3.5 + DOWN*-1.4)
        t3 = MathTex(r"\sqrt{2}").shift(LEFT*3.7 + DOWN*-1.4)
        # self.add(f1,f2,t1,t2,f3,t3)
 
        forumula1 = MathTex(r"f = 440 \cdot 2^{\frac{n}{12}}").to_corner(UL)
        forumula2 = MathTex(r"f = \sqrt[12]{2^{n}}").to_corner(UL)
        forumula3 = MathTex(r"440\sqrt[12]{2^{0}} = 440").to_corner(UL).shift(DOWN)
        forumula4 = MathTex(r"440\sqrt[12]{2^{1}} \approx 466").to_corner(UL).shift(DOWN*2)
        forumula5 = MathTex(r"440\sqrt[12]{2^{2}} \approx 493").to_corner(UL).shift(DOWN*3)
        forumula6 = MathTex(r"440\sqrt[12]{2^{3}} \approx 523").to_corner(UL).shift(DOWN*4)
        forumula7 = MathTex(r"440\sqrt[12]{2^{4}} \approx 554").to_corner(UL).shift(DOWN*5)
        forumula8 = MathTex(r"\vdots").next_to(forumula7, DOWN)
        forumula9 = MathTex(r"440\sqrt[12]{2^{12}} = 880").to_corner(UL).shift(DOWN*6.4)

        forumula2[0][7].set_color(YELLOW)
        forumula3[0][8].set_color(YELLOW)
        forumula4[0][8].set_color(YELLOW)
        forumula5[0][8].set_color(YELLOW)
        forumula6[0][8].set_color(YELLOW)
        forumula7[0][8].set_color(YELLOW)
        forumula9[0][8:10].set_color(YELLOW)


        # self.add(forumula1)

        self.wait()
        self.play(Write(axes), FadeIn(x_label), FadeIn(y_label), run_time=2)
        self.wait(3)
        self.play(Write(g1), run_time=2)
        self.wait()
        self.play(Write(g2), Write(f1), Write(t1), run_time=2)
        self.wait(3)
        self.play(Write(g3), Write(f2), Write(t2), run_time=2)
        self.wait(7)
        self.play(FadeOut(f2), FadeOut(t2))
        self.play(Write(f3), Write(t3), run_time=2)
        self.wait(7)
        self.play(FadeOut(y_label), FadeOut(t1), FadeOut(t3))
        self.wait(3)

        octave = Tex("Oktave").next_to(f1, RIGHT*0.5).shift(DOWN*0.2).set_color(YELLOW)
        self.play(Write(octave), run_time=2)
        self.wait(6)
        self.play(Unwrite(octave))

        self.wait(3)
        self.play(Write(forumula1), run_time=2)
        self.wait(25)
        self.play(ReplacementTransform(forumula1, forumula2), run_time=2)
        self.wait(3)
        self.play(Transform(forumula2.copy(), forumula3), run_time=2)
        self.play(Transform(forumula3.copy(), forumula4), run_time=2)
        self.play(Transform(forumula4.copy(), forumula5), run_time=2)
        self.play(Transform(forumula5.copy(), forumula6), run_time=2)
        self.play(Transform(forumula6.copy(), forumula7), run_time=2)
        self.play(Transform(forumula7.copy(), forumula8), run_time=2)
        self.play(Transform(forumula8.copy(), forumula9), run_time=2)
        self.wait(6)
        self.play(FadeOut(x_label), f3.animate.shift(RIGHT*5))
        self.play(Write(graphs), run_time=5)
        self.wait(1)



class TunedUntuned(Scene):
    def construct(self):

        def generate_tone(freq, duration=2.0, samplerate=44100, folder="music_frequency/TunedUntuned"):
            os.makedirs(folder, exist_ok=True)
            t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
            wave = 0.5 * np.sin(2 * np.pi * freq * t)
            filename = os.path.join(folder, f"{int(freq)}Hz.wav")
            sf.write(filename, wave, samplerate)

        frequencies = [440, 466, 493, 523, 554, 587, 622, 659, 698, 740, 784, 831, 880]
        frequencies2 = np.linspace(440, 880, 13)
        print(frequencies2)
        for freq in frequencies:
            generate_tone(freq, duration=0.25)
        for freq in frequencies2:
            generate_tone(freq, duration=0.25)
        # self.add(NumberPlane())

        freq_text = MathTex(r"f=").shift(DOWN*3 + LEFT*1)
        freq_number = DecimalNumber(440, num_decimal_places=0, include_sign=False).next_to(freq_text, RIGHT)
        freq_text2 = MathTex(r"\ \mathrm{Hz}").next_to(freq_number, RIGHT*1.3)

        r1 = Rectangle(height=0.05, width=10, color=BLUE, fill_color=BLUE, fill_opacity=1).shift(DOWN)

        axes = Axes(
            x_range=[0,10 , 1],
            y_range=[0, 4, 1],
            x_length=10,
            y_length=4,
            axis_config={"include_tip": False},
            tips=False
        )

        g1 = axes.plot(lambda x: np.sqrt(x), color=YELLOW)
        g2 = axes.plot(lambda x: 0.25*x + 0.75, color=YELLOW)
        self.wait(1)
        self.play(Write(axes), Write(g1), Write(freq_number), Write(freq_text), Write(freq_text2), Write(r1), run_time=2)
        self.wait(3)

        self.add_sound('music_frequency/TunedUntuned/440Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(440)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/466Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(466)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/493Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(493)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/523Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(523)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/554Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(554)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/587Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(587)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/622Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(622)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/659Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(659)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/698Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(698)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/740Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(740)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/784Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(784)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/831Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(831)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/880Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(880)
        r1.shift(UP*0.166)
        self.wait(1)
        self.play(ReplacementTransform(g1,g2), r1.animate.shift(DOWN*12*0.166), run_time=2)
        self.wait(5)

        self.add_sound('music_frequency/TunedUntuned/440Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(440)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/476Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(476)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/513Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(513)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/550Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(550)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/586Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(586)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/623Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(623)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/660Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(660)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/696Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(696)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/733Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(733)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/770Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(770)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/806Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(806)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/843Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(843)
        r1.shift(UP*0.166)
        self.wait(0.28)
        self.add_sound('music_frequency/TunedUntuned/880Hz.wav', gain=-15, time_offset=0)
        freq_number.set_value(880)
        r1.shift(UP*0.166)
        self.wait(1)





class ConssonanceDissonance(Scene):
    def construct(self):

        quinte = Tex("Quinte").set_color(YELLOW).shift(UP*1.5 + LEFT*3)
        tritone = Tex("Tritonus").set_color(YELLOW).shift(UP*1.5 + RIGHT*3)
        conssonance = Tex("Konsonanz").set_color(WHITE).shift(UP*2.5 + LEFT*3).scale(1.5)
        dissonance = Tex("Dissonanz").set_color(WHITE).shift(UP*2.5 + RIGHT*3).scale(1.5)
        c = MathTex(r" c\to 523.25Hz").to_edge(LEFT)
        f1 = MathTex(r"f = 523.25 \cdot 2^{\frac{n}{12}}").next_to(c, DOWN*2).to_edge(LEFT)
        f2 = MathTex(r"f = 523.25 \cdot 2^{\frac{7}{12}} \approx  783.98")
        f3 = MathTex(r"f = 523.25 \cdot 2^{\frac{6}{12}} \approx  739.98")
        f1[0][10].set_color(YELLOW)
        f2[0][10].set_color(YELLOW)
        f3[0][10].set_color(YELLOW)

        f4 = MathTex(r"2^{\frac{7}{12}} \approx  1.498")
        f5 = MathTex(r"2^{\frac{6}{12}} \approx  1.414")
        f6 = MathTex(r"2^{\frac{7}{12}} \approx  1.498 \approx \frac{3}{2}")
        f7 = MathTex(r"2^{\frac{6}{12}} \approx  1.414 \approx \frac{64}{45}")

        f4[0][1].set_color(YELLOW)
        f5[0][1].set_color(YELLOW)
        f6[0][1].set_color(YELLOW)
        f6[0][12:].set_color(GREEN)
        f7[0][1].set_color(YELLOW)
        f7[0][12:].set_color(RED)

        # self.add(NumberPlane())

        self.wait()
        self.play(Write(conssonance))
        self.wait(3)
        self.play(Write(dissonance))
        self.wait(3)
        self.play(Write(quinte))
        self.wait(3)
        self.play(Write(tritone))
        self.wait(3)
        self.play(Write(c))
        self.wait(6)
        self.play(Write(f1))
        self.wait(4)
        self.play(Unwrite(conssonance), Unwrite(dissonance))
        self.play(c.animate.to_corner(UL), f1.animate.to_corner(UL).shift(DOWN), run_time=2)
        self.play(quinte.animate.shift(LEFT*3 + DOWN), tritone.animate.shift(LEFT*2 +DOWN), run_time=2)

        self.wait()
        f2.next_to(quinte, DOWN).align_to(quinte, LEFT)
        f3.next_to(tritone, DOWN).align_to(tritone, LEFT)
        self.play(Write(f2))
        self.wait(4)
        self.play(Write(f3))
        self.wait(4)

        f4.next_to(f2, DOWN).align_to(f2, LEFT)
        f5.next_to(f3, DOWN).align_to(f3, LEFT)
        self.play(Write(f4))
        self.wait(4)
        self.play(Write(f5))
        self.wait(4)

        f6.move_to(f4).align_to(f4, LEFT)
        f7.move_to(f5).align_to(f5, LEFT)
        self.play(TransformMatchingShapes(f4,f6))
        self.wait(5)
        self.play(TransformMatchingShapes(f5,f7))
        self.wait(1)





class NodeAntiNode(Scene):
    def construct(self):

        time = ValueTracker(0)
        lenght = 1
        n = ValueTracker(lenght)
        ax_xlen = 13

        radius1 = 0.2
        n1 = Dot(color=BLUE, radius=radius1)
        n2 = Dot(color=BLUE, radius=radius1)
        n3 = Dot(color=BLUE, radius=radius1)
        n4 = Dot(color=BLUE, radius=radius1)
        n5 = Dot(color=BLUE, radius=radius1)
        n6 = Dot(color=BLUE, radius=radius1)
        nodes = VGroup(n1,n2,n3,n4,n5,n6)
        nodes.arrange(buff=ax_xlen * 1/lenght - 2*radius1)
        nodes.add_updater(lambda mob: mob.arrange(buff=ax_xlen * 1/lenght - 2*radius1).align_to(ax, LEFT))

        an1 = Dot(color=GREEN, radius=radius1)
        an2 = Dot(color=GREEN, radius=radius1)
        an3 = Dot(color=GREEN, radius=radius1)
        an4 = Dot(color=GREEN, radius=radius1)
        an5 = Dot(color=GREEN, radius=radius1)
        an6 = Dot(color=GREEN, radius=radius1)
        antinodes_odd = VGroup(an1,an3,an5)
        antinodes_even = VGroup(an2,an4,an6)
        antinodes_odd.arrange(buff=ax_xlen * 2/lenght - 2*radius1)
        antinodes_even.arrange(buff=ax_xlen * 2/lenght - 2*radius1)
        antinodes_odd.add_updater(lambda mob: mob.arrange(buff=ax_xlen * 2/lenght - 2*radius1).align_to(ax, LEFT).shift(RIGHT*0.5* ax_xlen/lenght+ UP* 3.1*np.cos(PI*n.get_value()*time.get_value())/np.sqrt(n.get_value()) ))
        antinodes_even.add_updater(lambda mob: mob.arrange(buff=ax_xlen * 2/lenght - 2*radius1).align_to(ax, LEFT).shift(RIGHT*0.5* ax_xlen/lenght +RIGHT*ax_xlen/lenght + UP* -3.1*np.cos(PI*n.get_value()*time.get_value())/np.sqrt(n.get_value()) ))

        ax = Axes(x_range=[0, 1, 1], x_length=ax_xlen, y_range=[-1.1, 1.1, 1], y_length=7, tips=False)
        nodes.align_to(ax, LEFT)
        antinodes_odd.align_to(ax, LEFT).shift(RIGHT*0.5* ax_xlen/lenght)
        antinodes_even.align_to(ax, LEFT).shift(RIGHT*0.5* ax_xlen/lenght +RIGHT*ax_xlen/lenght)

        g1 = ax.plot(lambda x: 0)
        g1.add_updater(lambda mob: mob.become(
            ax.plot(lambda x: np.cos(PI*n.get_value()*time.get_value())/np.sqrt(n.get_value()) * np.sin(n.get_value()*PI*x), color=YELLOW)
        ))
    
        node = Tex("Knoten").set_color(BLUE).next_to(n1, RIGHT*0.5).shift(DOWN)
        antinode_odd = Tex("Antiknoten").set_color(GREEN).shift(UP*2.4)
        lengh = MathTex(r"L").shift(DOWN).scale(2)
        lengh2 = MathTex(r"L=\frac{\lambda}{2}").shift(DOWN*2).scale(2)
        lengh3 = MathTex(r"L=\frac{\lambda n}{2}").shift(DOWN*2).scale(2)
        lengh4 = MathTex(r"L=\frac{\lambda n}{2} \rightarrow f_{n}=\frac{nv}{2L}").shift(DOWN*2).scale(2)
        brace = Brace(ax, DOWN, buff=0.1).shift(UP*3.5)
        count = MathTex(r"n = 1").next_to(brace, DOWN).shift(LEFT*0.5)
        count.add_updater(lambda mob: mob.become(MathTex(r"n = " + str(int(n.get_value()))).to_corner(UL).shift(RIGHT)))
        self.add(ax,g1,nodes, antinodes_odd, antinodes_even)

        # self.add(NumberPlane())
        self.play(Write(count),Write(ax))
        self.wait(10)
        self.play(time.animate.set_value(6), rate_func=linear, run_time=6)
        self.play(Write(node), Write(antinode_odd), run_time=2)
        self.wait(15)
        self.play(FadeOut(node), FadeOut(antinode_odd), run_time=1)
        self.play(Write(lengh),Write(brace), run_time=2)
        self.wait(3)
        self.play(ReplacementTransform(lengh, lengh2), run_time=2)
        self.wait(7)

        lenght = 2
        n.set_value(lenght)
        self.play(time.animate.set_value(12), rate_func=linear, run_time=6)
        self.wait(3)
        self.play(ReplacementTransform(lengh2, lengh3), run_time=2)
        self.wait(8)

        lenght = 3
        n.set_value(lenght)
        self.play(time.animate.set_value(14), rate_func=linear, run_time=2)
        lenght = 4
        n.set_value(lenght)
        self.play(time.animate.set_value(16), rate_func=linear, run_time=2)
        lenght = 5
        n.set_value(lenght)
        self.play(time.animate.set_value(18), rate_func=linear, run_time=2)
        self.wait(6)
        self.play(ReplacementTransform(lengh3, lengh4), run_time=3)
        self.wait(17)

        standingwave = Tex("stehende", " Welle").shift(UP*2.5).scale(2)
        standingwave[0].set_color(YELLOW)
        self.play(Write(standingwave))
        self.wait()





class Bell(Scene):
    def construct(self):

        off = 0.05
        volume = -10

        def generate_tone(freq, duration=3.0, samplerate=44100, folder="music_frequency/Bell"):
            os.makedirs(folder, exist_ok=True)
            t = np.linspace(0, duration, int(samplerate * duration))
            wave = 0.5 * np.sin(2 * np.pi * freq * t)
            filename = os.path.join(folder, f"{int(freq)}.wav")

            
            x_steps = int(len(wave))

            x_val = np.linspace(0, 0.7*duration, x_steps)
            curve =  freq/(8.1*np.log(list1[-1])) * (1- np.power(np.e, -x_val)) * np.power(np.e, 0.25*np.sqrt(freq) * -1 * x_val)
            wave *= curve
            sf.write(filename, wave, samplerate)

        listprep = [250, 499, 601, 749, 1000, 1500, 2075, 2421]
        list1 = []
        a = 0.24
        for i in range(len(listprep)):
            list1.append(listprep[i] - a*listprep[i])

        for f in list1:
            dura = 3
            generate_tone(f, duration=dura)


        axis = Axes(x_range=[-1,12,1], x_length=13, y_range=[-6,6,1], y_length=7, tips=False )
        
        l2 = []
        for i in range(len(list1)):
            l2.append(list1[i]/list1[0])


        g2 = axis.plot(lambda x: np.sin(x*l2[0])+ np.sin(x*l2[1]))
        g3 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]))
        g4 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]))
        g5 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]) + np.sin(x*l2[4]))
        g6 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]) + np.sin(x*l2[4]) + np.sin(x*l2[5]))
        g7 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]) + np.sin(x*l2[4]) + np.sin(x*l2[5]) + np.sin(x*l2[6]))
        g8 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]) + np.sin(x*l2[4]) + np.sin(x*l2[5]) + np.sin(x*l2[6]) + np.sin(x*l2[7]))
        g2.set_color(ManimColor((340- 85*l2[0],0,85*l2[0] -85)))
        g3.set_color(ManimColor((340- 85*l2[1],0,85*l2[1] -85)))
        g4.set_color(ManimColor((340- 85*l2[2],0,85*l2[2] -85)))
        g5.set_color(ManimColor((340- 85*l2[3],0,85*l2[3] -85)))
        g6.set_color(ManimColor((340- 85*l2[4],0,85*l2[4] -85)))
        g7.set_color(ManimColor((340- 85*l2[5],0,85*l2[5] -85)))
        g8.set_color(ManimColor((340- 85*l2[6],0,85*l2[6] -85)))


        freq_text = always_redraw(
            lambda: MathTex(r"f = " + str(int(list1[len(self.mobjects)-2])) + r"\ \mathrm{Hz}")
            .scale(0.8)
            .to_edge(DOWN)
            .shift(UP*0.6)
            .scale(2)
        )
        self.add(freq_text)

        self.play(Write(axis), Write(g2), run_time=2)
        self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        self.wait(3)
        self.play(ReplacementTransform(g2, g3), run_time=2)
        self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/456.wav', gain=volume, time_offset=off)
        self.wait(3)
        self.play(ReplacementTransform(g3, g4), run_time=2)
        self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/456.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/569.wav', gain=volume, time_offset=off)
        self.wait(3)
        self.play(ReplacementTransform(g4, g5), run_time=2)
        self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/456.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/569.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/760.wav', gain=volume, time_offset=off)
        self.wait(3)
        self.play(ReplacementTransform(g5, g6), run_time=2)
        self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/456.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/569.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/760.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/1140.wav', gain=volume, time_offset=off)
        self.wait(3)
        self.play(ReplacementTransform(g6, g7), run_time=2)
        self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/456.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/569.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/760.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/1140.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/1577.wav', gain=volume, time_offset=off)
        self.wait(3)
        self.play(ReplacementTransform(g7, g8), run_time=2)
        self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/456.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/569.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/760.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/1140.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/1577.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Bell/1839.wav', gain=volume, time_offset=off)
        self.wait(3)



class Guitar(Scene):
    def construct(self):

        off = 0.05
        volume = -4

        def generate_tone(freq, duration=3.0, samplerate=44100, folder="music_frequency/Guitar"):
            os.makedirs(folder, exist_ok=True)
            t = np.linspace(0, duration, int(samplerate * duration))
            wave = 0.5 * np.sin(2 * np.pi * freq * t)
            filename = os.path.join(folder, f"{int(freq)}.wav")

            
            x_steps = int(len(wave))

            x_val = np.linspace(0, 0.7*duration, x_steps)
            curve =  (21.373 * (1- np.power(np.e, -x_val)) * np.power(np.e, 7.37* -1 * x_val))/(0.2*np.sqrt(freq))
            wave *= curve
            sf.write(filename, wave, samplerate)

        listprep = [196,392,587,784,980,1176,1372,1568,1764,1960,2156,2352]
        list1 = []
        a = 0.603
        for i in range(len(listprep)):
            list1.append(listprep[i] - a*listprep[i])


        for f in list1:
            dura = 1.5
            generate_tone(f, duration=dura)

        axis = Axes(x_range=[-1,12,1], x_length=13, y_range=[-6,6,1], y_length=7, tips=False )
        
        l2 = []
        for i in range(len(list1)):
            l2.append(list1[i]/list1[0])

        g2 = axis.plot(lambda x: np.sin(x*l2[0])+ np.sin(x*l2[1]))
        g3 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]))
        g4 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]))
        g5 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]) + np.sin(x*l2[4]))
        g6 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]) + np.sin(x*l2[4]) + np.sin(x*l2[5]))
        g7 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]) + np.sin(x*l2[4]) + np.sin(x*l2[5]) + np.sin(x*l2[6]))
        g8 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]) + np.sin(x*l2[4]) + np.sin(x*l2[5]) + np.sin(x*l2[6]) + np.sin(x*l2[7]))
        g9 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]) + np.sin(x*l2[4]) + np.sin(x*l2[5]) + np.sin(x*l2[6]) + np.sin(x*l2[7]) + np.sin(x*l2[8]))
        g10 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]) + np.sin(x*l2[4]) + np.sin(x*l2[5]) + np.sin(x*l2[6]) + np.sin(x*l2[7]) + np.sin(x*l2[8]) + np.sin(x*l2[9]))


        g2.set_color(ManimColor((340- 85*l2[0],0,85*l2[0] -85)))
        g3.set_color(ManimColor((340- 85*l2[1],0,85*l2[1] -85)))
        g4.set_color(ManimColor((340- 85*l2[2],0,85*l2[2] -85)))
        g5.set_color(ManimColor((340- 85*l2[3],0,85*l2[3] -85)))
        g6.set_color(ManimColor((340- 85*l2[4],0,85*l2[4] -85)))
        g7.set_color(ManimColor((340- 85*l2[5],0,85*l2[5] -85)))
        g8.set_color(ManimColor((340- 85*l2[6],0,85*l2[6] -85)))
        g9.set_color(ManimColor((340- 85*l2[7],0,85*l2[7] -85)))
        g10.set_color(ManimColor((340- 85*l2[8],0,85*l2[8] -85)))
        g11 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]) + np.sin(x*l2[4]) + np.sin(x*l2[5]) + np.sin(x*l2[6]) + np.sin(x*l2[7]) + np.sin(x*l2[8]) + np.sin(x*l2[9]) + np.sin(x*l2[10]))
        g11.set_color(ManimColor((340- 85*l2[9],0,85*l2[9] -85)))
        g12 = axis.plot(lambda x: np.sin(x*l2[0]) + np.sin(x*l2[1]) + np.sin(x*l2[2]) + np.sin(x*l2[3]) + np.sin(x*l2[4]) + np.sin(x*l2[5]) + np.sin(x*l2[6]) + np.sin(x*l2[7]) + np.sin(x*l2[8]) + np.sin(x*l2[9]) + np.sin(x*l2[10]) + np.sin(x*l2[11]))
        g12.set_color(ManimColor((340- 85*l2[10],0,85*l2[10] -85)))

        freq_text = always_redraw(
            lambda: MathTex(r"f = " + str(int(list1[len(self.mobjects)-2])) + r"\ \mathrm{Hz}")
            .scale(0.8)
            .to_edge(DOWN)
            .shift(UP*0.6)
            .scale(2)
        )
        self.add(freq_text)

        self.play(Write(axis), Write(g2), run_time=2)
        self.add_sound('music_frequency/Guitar/77.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/155.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/233.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/311.wav', gain=volume, time_offset=off)
        self.wait(2.5)
        self.play(ReplacementTransform(g2, g3), run_time=2)
        self.add_sound('music_frequency/Guitar/77.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/155.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/233.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/311.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/389.wav', gain=volume, time_offset=off)
        self.wait(2.5)
        self.play(ReplacementTransform(g3, g4), run_time=2)
        self.add_sound('music_frequency/Guitar/77.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/155.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/233.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/311.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/389.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/466.wav', gain=volume, time_offset=off)
        self.wait(2.5)
        self.play(ReplacementTransform(g4, g5), run_time=2)
        self.add_sound('music_frequency/Guitar/77.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/155.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/233.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/311.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/389.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/466.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/544.wav', gain=volume, time_offset=off)
        self.wait(2.5)
        self.play(ReplacementTransform(g5, g6), run_time=2)
        self.add_sound('music_frequency/Guitar/77.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/155.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/233.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/311.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/389.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/466.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/544.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/622.wav', gain=volume, time_offset=off)
        self.wait(2.5)
        self.play(ReplacementTransform(g6, g7), run_time=2)
        self.add_sound('music_frequency/Guitar/77.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/155.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/233.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/311.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/389.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/466.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/544.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/622.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/700.wav', gain=volume, time_offset=off)
        self.wait(2.5)
        self.play(ReplacementTransform(g7, g8), run_time=2)
        self.add_sound('music_frequency/Guitar/77.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/155.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/233.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/311.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/389.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/466.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/544.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/622.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/700.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/778.wav', gain=volume, time_offset=off)
        self.wait(2.5)
        self.play(ReplacementTransform(g8, g9), run_time=2)
        self.add_sound('music_frequency/Guitar/77.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/155.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/233.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/311.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/389.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/466.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/544.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/622.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/700.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/778.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/855.wav', gain=volume, time_offset=off)
        self.wait(2.5)
        self.play(ReplacementTransform(g9, g10), run_time=2)
        self.add_sound('music_frequency/Guitar/77.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/155.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/233.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/311.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/389.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/466.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/544.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/622.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/700.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/778.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/855.wav', gain=volume, time_offset=off)
        self.add_sound('music_frequency/Guitar/933.wav', gain=volume, time_offset=off)
        self.wait(2.5)





class Frequency(Scene):
    def construct(self):

        pic = ImageMobject("music_frequency/pictures/frequency.png").scale(1.3)
        self.add(pic)





class ASound(Scene):
    def construct(self):
        
        def generate_tone(freq, duration=2.0, samplerate=44100, folder="music_frequency/Sound"):
            os.makedirs(folder, exist_ok=True)
            t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
            wave = 0.5 * np.sin(2 * np.pi * freq * t)
            filename = os.path.join(folder, f"{int(freq)}Hz.wav")
            sf.write(filename, wave, samplerate)

        frequencies = [300,600,900,1200]
        for freq in frequencies:
            generate_tone(freq, duration=3)

        sound = ImageMobject("music_frequency/pictures/sound.png").scale(2)
        self.add(sound)
        self.add_sound('music_frequency/Sound/300Hz.wav', gain=-10, time_offset=0)
        self.add_sound('music_frequency/Sound/600Hz.wav', gain=-10, time_offset=0)
        self.add_sound('music_frequency/Sound/900Hz.wav', gain=-10, time_offset=0)
        self.add_sound('music_frequency/Sound/1200Hz.wav', gain=-10, time_offset=0)
        self.wait(3)





class ANoise(Scene):
    def construct(self):
        
        def generate_tone(freq, duration=2.0, samplerate=44100, folder="music_frequency/Noise"):
            os.makedirs(folder, exist_ok=True)
            t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
            wave = 0.5 * np.sin(2 * np.pi * freq * t)
            filename = os.path.join(folder, f"{int(freq)}Hz.wav")
            sf.write(filename, wave, samplerate)

        frequencies = [x * 300 for x in [1,2.8,3.2,4.1,5.2,6.6,7.33,8.94,9.12,10.2]]
        for freq in frequencies:
            generate_tone(freq, duration=1)

        sound = ImageMobject("music_frequency/pictures/noise.png").scale(1.5)
        self.add(sound)
        self.add_sound('music_frequency/Noise/300Hz.wav', gain=-10, time_offset=0)
        self.add_sound('music_frequency/Noise/840Hz.wav', gain=-10, time_offset=0)
        self.add_sound('music_frequency/Noise/960Hz.wav', gain=-10, time_offset=0)
        self.add_sound('music_frequency/Noise/1230Hz.wav', gain=-10, time_offset=0)
        self.add_sound('music_frequency/Noise/1560Hz.wav', gain=-10, time_offset=0)
        self.add_sound('music_frequency/Noise/1980Hz.wav', gain=-10, time_offset=0)
        self.add_sound('music_frequency/Noise/2199Hz.wav', gain=-10, time_offset=0)
        self.add_sound('music_frequency/Noise/2682Hz.wav', gain=-10, time_offset=0)
        self.add_sound('music_frequency/Noise/2735Hz.wav', gain=-10, time_offset=0)
        self.add_sound('music_frequency/Noise/3060Hz.wav', gain=-10, time_offset=0)
        self.wait(3)





class Jadelith7(Scene):
    # This scene is a placeholder for the Jadelith7 scene.
    # It is a video rendered by Jadelith7.
    # The link to the video is provided in the Ending scene under his github.
    42 # :)





class Ending(Scene):
    def construct(self):

        self.add_sound(sound_file="music_frequency/Music/MusicEnding.wav",time_offset=0)

        banner = ManimBanner().scale(0.5)
        bannertxt = Tex("https://www.manim.community/")
        musicimg = ImageMobject("music_frequency/pictures/3b1bmusiclogo.jpg").scale(0.8).set_z_index(-1)
        musicimgtxt = Tex("https://vincerubinetti.bandcamp.com/album/the-music-of-3blue1brown").scale(0.85)
        
        page1 = VGroup(banner,bannertxt,musicimgtxt)

        download = Tex("Download zum Vortrag, Skript, Code:")
        download2 = Tex("https://github.com/Namitera/Musik-Physik-der-Musik-05.06.2025").scale(0.85).shift(DOWN)
        download3 = Tex("https://github.com/Jadelith7/AroundTheFire").scale(0.85).shift(DOWN)
        desmos = Tex("https://www.desmos.com/?lang=en").scale(0.9)

        page2 = VGroup(desmos,download,download2,download3)

        self.wait()
        self.play(banner.create())
        self.play(banner.expand())
        self.play(banner.animate.to_corner(UL))
        self.play(FadeIn(bannertxt))
        self.play(bannertxt.animate.next_to(banner,DOWN).align_to(banner,LEFT))
        self.wait(3)
        self.play(FadeIn(musicimg))
        self.play(musicimg.animate.to_edge(LEFT).shift(DOWN+LEFT*0.5))
        self.play(FadeIn(musicimgtxt))
        self.play(musicimgtxt.animate.next_to(musicimg,DOWN).align_to(musicimg,LEFT).shift(RIGHT*0.5+UP*0.3))
        self.wait(5)
        self.play(FadeOut(page1),FadeOut(musicimg))
        self.wait()


        self.play(FadeIn(desmos))
        self.play(desmos.animate.to_corner(UL).shift(DOWN*0+LEFT*0.2))
        self.play(FadeIn(download))
        self.play(download.animate.to_corner(UL).shift(DOWN*3+LEFT*0.2))
        self.play(FadeIn(download2))
        self.play(download2.animate.to_corner(UL).shift(DOWN*4+LEFT*0.2))
        self.play(FadeIn(download3))
        self.play(download3.animate.to_corner(UL).shift(DOWN*5+LEFT*0.2))
        self.wait(5)
        self.play(FadeOut(page2))
        self.wait()




        
class E1(Scene):
    def construct(self):

        banner = ManimBanner().scale(0.5)
        bannertxt = Tex("https://www.manim.community/")
        musicimg = ImageMobject("music_frequency/pictures/3b1bmusiclogo.jpg").scale(0.8).set_z_index(-1)
        musicimgtxt = Tex("https://vincerubinetti.bandcamp.com/album/the-music-of-3blue1brown").scale(0.85)
        
        self.play(banner.create())
        self.play(banner.expand())
        self.play(banner.animate.to_corner(UL))
        self.play(FadeIn(bannertxt))
        self.play(bannertxt.animate.next_to(banner,DOWN).align_to(banner,LEFT))
        self.wait(3)
        self.play(FadeIn(musicimg))
        self.play(musicimg.animate.to_edge(LEFT).shift(DOWN+LEFT*0.5))
        self.play(FadeIn(musicimgtxt))
        self.play(musicimgtxt.animate.next_to(musicimg,DOWN).align_to(musicimg,LEFT).shift(RIGHT*0.5+UP*0.3))





class E2(Scene):
    def construct(self):

        download = Tex("Download zum Vortrag, Skript, Code:")
        download2 = Tex("https://github.com/Namitera/Musik-Physik-der-Musik-05.06.2025").scale(0.85).shift(DOWN)
        download3 = Tex("https://github.com/Jadelith7/AroundTheFire").scale(0.85).shift(DOWN)
        desmos = Tex("https://www.desmos.com/?lang=en").scale(0.9)

        self.play(FadeIn(desmos))
        self.play(desmos.animate.to_corner(UL).shift(DOWN*0+LEFT*0.2))
        self.play(FadeIn(download))
        self.play(download.animate.to_corner(UL).shift(DOWN*3+LEFT*0.2))
        self.play(FadeIn(download2))
        self.play(download2.animate.to_corner(UL).shift(DOWN*4+LEFT*0.2))
        self.play(FadeIn(download3))
        self.play(download3.animate.to_corner(UL).shift(DOWN*5+LEFT*0.2))