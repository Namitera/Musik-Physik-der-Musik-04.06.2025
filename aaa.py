from manim import *



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

        
        self.add(axis, g1)
        # self.play(phi.animate.set_value(0), rate_func=linear, run_time=5)
        self.play(phi.animate.set_value(0), frequency.animate.set_value(2), rate_func=linear, run_time=1)
        self.wait()
        self.play(phi.animate.set_value(0), frequency.animate.set_value(3), rate_func=linear, run_time=1)
        self.wait()
        self.play(phi.animate.set_value(0), frequency.animate.set_value(4), rate_func=linear, run_time=1)
        self.wait()


class KonsonanzDissonanz(Scene):
    def construct(self):
        1
        

class PitchFrequency(Scene):
    def construct(self):

        # self.add(NumberPlane())
        axes = Axes(
            x_range=[0,10 , 1],
            y_range=[0, 4, 1],
            x_length=10,
            y_length=4,
            axis_config={"include_tip": False},
            tips=False
        ).shift(UP*1.4 + RIGHT)

        # ich weis nicht wieso aber diese linien sehen schief aus, optsiche täuschung
        g1 = axes.plot(lambda x: np.sqrt(x), color=YELLOW)
        g2 = axes.plot(lambda x: 1 +0*x)
        g3 = axes.plot(lambda x: 2 +0*x)

        x_label = Tex("Frequenz (Hz)").shift(UP*-1.5 +4*RIGHT)
        y_label = Tex("Tonhöhe").scale(1).shift(-5.5*RIGHT + UP*3)

        self.play(Write(axes), FadeIn(x_label), FadeIn(y_label), run_time=2)
        self.wait(3)
        self.play(Write(g1), run_time=2)
        self.play(Write(g2), run_time=2)
        self.play(Write(g3), run_time=2)













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


        self.add(ax,g1,nodes, antinodes_odd, antinodes_even)

        self.play(time.animate.set_value(2), rate_func=linear, run_time=2)
        lenght = 2
        n.set_value(lenght)
        self.play(time.animate.set_value(4), rate_func=linear, run_time=2)
        lenght = 3
        n.set_value(lenght)
        self.play(time.animate.set_value(6), rate_func=linear, run_time=2)
        lenght = 4
        n.set_value(lenght)
        self.play(time.animate.set_value(8), rate_func=linear, run_time=2)
        lenght = 5
        n.set_value(lenght)
        self.play(time.animate.set_value(10), rate_func=linear, run_time=2)








import soundfile as sf
import os

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