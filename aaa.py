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

class Ist(Scene):
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
            # print(x_steps)
            # print(x_val)
            # print(len(wave))
            # print(freq)
            curve =  freq/(8.1*np.log(list1[-1])) * (1- np.power(np.e, -x_val)) * np.power(np.e, 0.25*np.sqrt(freq) * -1 * x_val)
            print(curve)
            wave *= curve
            print(len(wave))
            sf.write(filename, wave, samplerate)

        listprep = [250, 499, 601, 749, 1000, 1500, 2075, 2421]
        # listprep = [250]
        list1 = []
        a = 0.24
        for i in range(len(listprep)):
            list1.append(listprep[i] - a*listprep[i])


        # print(list1)
        for f in list1:
            dura = 3
            generate_tone(f, duration=dura)


        # self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        # self.wait(4)
        # self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        # self.wait(4)
        # self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/456.wav', gain=volume, time_offset=off)
        # self.wait(4)
        # self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/456.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/569.wav', gain=volume, time_offset=off)
        # self.wait(4)
        # self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/456.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/569.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/760.wav', gain=volume, time_offset=off)
        # self.wait(4)
        # self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/456.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/569.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/760.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/1140.wav', gain=volume, time_offset=off)
        # self.wait(4)
        # self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/456.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/569.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/760.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/1140.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/1577.wav', gain=volume, time_offset=off)
        # self.wait(4)
        # self.add_sound('music_frequency/Bell/190.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/379.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/456.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/569.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/760.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/1140.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/1577.wav', gain=volume, time_offset=off)
        # self.add_sound('music_frequency/Bell/1839.wav', gain=volume, time_offset=off)
        # self.wait(4)