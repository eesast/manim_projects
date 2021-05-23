from manim import *
import numpy as np


class EESASTLogo(Scene):
    """
    绘制 EESAST logo
    注释部分为绘制时的辅助点、线、圆
    """

    def construct(self):
        base_circle = Circle(radius=3, color=WHITE)

        p0 = base_circle.point_at_angle(210 * DEGREES)
        p1 = base_circle.point_at_angle(150 * DEGREES)
        p2 = base_circle.point_at_angle(90 * DEGREES)
        p3 = base_circle.point_at_angle(30 * DEGREES)
        p4 = base_circle.point_at_angle(330 * DEGREES)
        p5 = base_circle.point_at_angle(270 * DEGREES)

        dot0 = Dot().move_to(p0)
        dot1 = Dot().move_to(p1)
        dot2 = Dot().move_to(p2)
        dot3 = Dot().move_to(p3)
        dot4 = Dot().move_to(p4)
        dot5 = Dot().move_to(p5)

        big_circle_0 = Circle(radius=3, color=WHITE)
        big_circle_1 = Circle(radius=3, color=WHITE)
        big_circle_2 = Circle(radius=3, color=WHITE)
        big_circle_3 = Circle(radius=3, color=WHITE)
        big_circle_4 = Circle(radius=3, color=WHITE)
        big_circle_5 = Circle(radius=3, color=WHITE)

        big_circle_0.shift(1.5 * DOWN).shift(1.5 * np.sqrt(3) * LEFT)
        big_circle_1.shift(1.5 * UP).shift(1.5 * np.sqrt(3) * LEFT)
        big_circle_2.shift(3 * UP)
        big_circle_3.shift(1.5 * UP).shift(1.5 * np.sqrt(3) * RIGHT)
        big_circle_4.shift(1.5 * DOWN).shift(1.5 * np.sqrt(3) * RIGHT)
        big_circle_5.shift(3 * DOWN)

        frame_0 = Line(dot0, dot1)
        frame_1 = Line(dot1, dot2)
        frame_2 = Line(dot2, dot3)
        frame_3 = Line(dot3, dot4)
        frame_4 = Line(dot4, dot5)
        frame_5 = Line(dot5, dot0)

        tiny_circle_0 = Circle(radius=0.3, color=ORANGE).move_to(p0)
        tiny_circle_0_p0 = tiny_circle_0.point_at_angle(90 * DEGREES)
        tiny_circle_0_p1 = tiny_circle_0.point_at_angle(330 * DEGREES)
        tiny_circle_0_dot_0 = Dot().move_to(tiny_circle_0_p0)
        tiny_circle_0_dot_1 = Dot().move_to(tiny_circle_0_p1)

        tiny_circle_1 = Circle(radius=0.3, color=ORANGE).move_to(p3)
        tiny_circle_1_p0 = tiny_circle_1.point_at_angle(150 * DEGREES)
        tiny_circle_1_p1 = tiny_circle_1.point_at_angle(270 * DEGREES)
        tiny_circle_1_dot_0 = Dot().move_to(tiny_circle_1_p0)
        tiny_circle_1_dot_1 = Dot().move_to(tiny_circle_1_p1)

        polygon_0 = Polygon(p0,
                            tiny_circle_0_p0,
                            tiny_circle_1_p0,
                            p3,
                            tiny_circle_1_p1,
                            tiny_circle_0_p1,
                            color=BLUE)

        tiny_circle_2 = Circle(radius=0.3,
                               color=ORANGE).move_to(tiny_circle_0_p1)
        tiny_circle_2_p0 = tiny_circle_2.point_at_angle(30 * DEGREES)
        tiny_circle_2_dot_0 = Dot().move_to(tiny_circle_2_p0)
        tiny_circle_2_p1 = tiny_circle_2_p0 + 0.6 * UP
        tiny_circle_2_dot_1 = Dot().move_to(tiny_circle_2_p1)

        line_p0 = tiny_circle_2_p0 + 3.3 * UP
        line_0 = Line(tiny_circle_2_dot_0, line_p0)

        tiny_circle_3 = Circle(radius=0.3,
                               color=ORANGE).move_to(tiny_circle_1_p0)
        tiny_circle_3_p0 = tiny_circle_3.point_at_angle(210 * DEGREES)
        tiny_circle_3_dot_0 = Dot().move_to(tiny_circle_3_p0)
        tiny_circle_3_p1 = tiny_circle_3_p0 + 0.6 * DOWN
        tiny_circle_3_dot_1 = Dot().move_to(tiny_circle_3_p1)

        line_p1 = tiny_circle_3_p0 + 3.3 * DOWN
        line_1 = Line(tiny_circle_3_p0, line_p1)

        small_circle_0 = Circle(radius=0.6, color=GREEN).move_to(p1)
        small_circle_0_p1 = small_circle_0.point_at_angle(270 * DEGREES)
        small_circle_0_p2 = small_circle_0.point_at_angle(330 * DEGREES)
        small_circle_0_dot_0 = Dot().move_to(line_p0)
        small_circle_0_dot_1 = Dot().move_to(small_circle_0_p1)
        small_circle_0_dot_2 = Dot().move_to(small_circle_0_p2)

        small_circle_1 = Circle(radius=0.6, color=GREEN).move_to(p4)
        small_circle_1_p1 = small_circle_1.point_at_angle(90 * DEGREES)
        small_circle_1_p2 = small_circle_1.point_at_angle(150 * DEGREES)
        small_circle_1_dot_0 = Dot().move_to(line_p1)
        small_circle_1_dot_1 = Dot().move_to(small_circle_1_p1)
        small_circle_1_dot_2 = Dot().move_to(small_circle_1_p2)

        polygon_1 = Polygon(tiny_circle_0_p0,
                            tiny_circle_2_p1,
                            small_circle_0_p2,
                            small_circle_0_p1,
                            color=BLUE)

        polygon_2 = Polygon(tiny_circle_1_p1,
                            tiny_circle_3_p1,
                            small_circle_1_p2,
                            small_circle_1_p1,
                            color=BLUE)

        line_p2 = p2 + 0.3 * DOWN + 0.3 * np.sqrt(3) * RIGHT
        line_2 = Line(small_circle_0_dot_1, line_p2)
        line_2_dot_0 = Dot().move_to(line_p2)

        line_p3 = p5 + 0.3 * UP + 0.3 * np.sqrt(3) * LEFT
        line_3 = Line(small_circle_1_dot_1, line_p3)
        line_3_dot_0 = Dot().move_to(line_p3)

        polygon_3 = Polygon(small_circle_0_p1, line_p2, p2, p1, color=BLUE)
        polygon_4 = Polygon(small_circle_1_p1, line_p3, p5, p4, color=BLUE)

        line_p4 = p0 + 1.35 * UP
        line_p5 = p3 + 1.35 * DOWN

        tiny_circle_4 = Circle(radius=0.3, color=ORANGE).move_to(line_p4)
        tiny_circle_5 = Circle(radius=0.3, color=ORANGE).move_to(line_p5)

        tiny_circle_4_p0 = tiny_circle_4.point_at_angle(90 * DEGREES)
        tiny_circle_4_p1 = tiny_circle_4.point_at_angle(270 * DEGREES)

        tiny_circle_5_p0 = tiny_circle_5.point_at_angle(90 * DEGREES)
        tiny_circle_5_p1 = tiny_circle_5.point_at_angle(270 * DEGREES)

        tiny_circle_4_p0 = Dot().move_to(tiny_circle_4_p0)
        tiny_circle_4_p1 = Dot().move_to(tiny_circle_4_p1)

        tiny_circle_5_p0 = Dot().move_to(tiny_circle_5_p0)
        tiny_circle_5_p1 = Dot().move_to(tiny_circle_5_p1)

        line_p6 = line_p2 + 0.375 * DOWN + 0.375 * np.sqrt(3) * RIGHT
        line_p7 = line_p6 + 0.3 * DOWN + 0.3 * np.sqrt(3) * RIGHT
        line_p8 = line_p4 + 0.6 * np.sqrt(3) * RIGHT + 0.3 * UP
        line_p9 = line_p8 + 0.6 * UP

        line_p10 = line_p3 + 0.375 * UP + 0.375 * np.sqrt(3) * LEFT
        line_p11 = line_p10 + 0.3 * UP + 0.3 * np.sqrt(3) * LEFT
        line_p12 = line_p5 + 0.6 * np.sqrt(3) * LEFT + 0.3 * DOWN
        line_p13 = line_p12 + 0.6 * DOWN

        line_4 = Line(tiny_circle_4_p0, line_p6)
        line_5 = Line(tiny_circle_4_p1, line_p7)

        line_6 = Line(tiny_circle_5_p0, line_p11)
        line_7 = Line(tiny_circle_5_p1, line_p10)

        polygon_5 = Polygon(line_p6, line_p7, line_p8, line_p9, color=BLUE)
        polygon_6 = Polygon(line_p10, line_p11, line_p12, line_p13, color=BLUE)

        line_p4 = Dot().move_to(line_p4)
        line_p5 = Dot().move_to(line_p5)
        line_p6 = Dot().move_to(line_p6)
        line_p7 = Dot().move_to(line_p7)
        line_p8 = Dot().move_to(line_p8)
        line_p9 = Dot().move_to(line_p9)
        line_p10 = Dot().move_to(line_p10)
        line_p11 = Dot().move_to(line_p11)
        line_p12 = Dot().move_to(line_p12)
        line_p13 = Dot().move_to(line_p13)

        eesast = Tex(
            r"\textbf{E\quad E\quad S\quad $\Lambda$\quad S\quad T}")\
            .scale(1.5).shift(3 * DOWN)

        # self.play(Create(base_circle))

        # self.play(GrowFromCenter(big_circle_0), GrowFromCenter(big_circle_1),
        #           GrowFromCenter(big_circle_2), GrowFromCenter(big_circle_3),
        #           GrowFromCenter(big_circle_4), GrowFromCenter(big_circle_5))

        # self.play(FadeIn(dot0), FadeIn(dot1), FadeIn(dot2), FadeIn(dot3),
        #           FadeIn(dot4), FadeIn(dot5))

        # self.play(FadeOut(big_circle_0), FadeOut(big_circle_1),
        #           FadeOut(big_circle_2), FadeOut(big_circle_3),
        #           FadeOut(big_circle_4), FadeOut(big_circle_5))

        # self.play(GrowFromPoint(frame_0, dot0), GrowFromPoint(frame_1, dot1),
        #           GrowFromPoint(frame_2, dot2), GrowFromPoint(frame_3, dot3),
        #           GrowFromPoint(frame_4, dot4), GrowFromPoint(frame_5, dot5))

        # self.play(FadeOut(base_circle))

        # self.play(Create(tiny_circle_0), Create(tiny_circle_1))
        # self.play(FadeIn(tiny_circle_0_dot_0), FadeIn(tiny_circle_0_dot_1),
        #           FadeIn(tiny_circle_1_dot_0), FadeIn(tiny_circle_1_dot_1))

        self.play(GrowFromCenter(polygon_0))

        # self.play(Create(tiny_circle_2), Create(tiny_circle_3))
        # self.play(FadeIn(tiny_circle_2_dot_0), FadeIn(tiny_circle_3_dot_0))

        # self.play(GrowFromPoint(line_0, tiny_circle_2_dot_0),
        #           GrowFromPoint(line_1, tiny_circle_3_dot_0))
        # self.play(FadeIn(tiny_circle_2_dot_1), FadeIn(small_circle_0_dot_0),
        #           FadeIn(tiny_circle_3_dot_1), FadeIn(small_circle_1_dot_0))

        # self.play(GrowFromCenter(small_circle_0),
        #           GrowFromCenter(small_circle_1))
        # self.play(FadeIn(small_circle_0_dot_1), FadeIn(small_circle_0_dot_2),
        #           FadeIn(small_circle_1_dot_1), FadeIn(small_circle_1_dot_2))

        self.play(GrowFromPoint(polygon_1, tiny_circle_0_p0),
                  GrowFromPoint(polygon_2, tiny_circle_1_p1))

        # self.play(GrowFromPoint(line_2, small_circle_0_dot_1),
        #           GrowFromPoint(line_3, small_circle_1_dot_1))
        # self.play(FadeIn(line_2_dot_0), FadeIn(line_3_dot_0),
        #           FadeOut(tiny_circle_0), FadeOut(tiny_circle_1),
        #           FadeOut(tiny_circle_2),
        #           FadeOut(tiny_circle_3), FadeOut(dot0), FadeOut(dot3),
        #           FadeOut(tiny_circle_0_dot_0), FadeOut(tiny_circle_0_dot_1),
        #           FadeOut(tiny_circle_1_dot_0), FadeOut(tiny_circle_1_dot_1),
        #           FadeOut(tiny_circle_2_dot_0), FadeOut(tiny_circle_2_dot_1),
        #           FadeOut(tiny_circle_3_dot_0), FadeOut(tiny_circle_3_dot_1),
        #           FadeOut(line_0), FadeOut(line_1))

        self.play(GrowFromPoint(polygon_3, small_circle_0_p1),
                  GrowFromPoint(polygon_4, small_circle_1_p1))

        # self.play(FadeOut(small_circle_0), FadeOut(small_circle_1),
        #           FadeOut(small_circle_0_dot_0), FadeOut(small_circle_0_dot_1),
        #           FadeOut(small_circle_0_dot_2), FadeOut(small_circle_1_dot_0),
        #           FadeOut(small_circle_1_dot_1), FadeOut(small_circle_1_dot_2),
        #           FadeOut(line_2),
        #           FadeOut(line_3), FadeOut(dot1), FadeOut(dot2), FadeOut(dot4),
        #           FadeOut(dot5), FadeOut(line_2_dot_0), FadeOut(line_3_dot_0),
        #           FadeOut(frame_1), FadeOut(frame_4))

        # self.play(FadeIn(line_p4), FadeIn(line_p5))
        # self.play(GrowFromCenter(tiny_circle_4), GrowFromCenter(tiny_circle_5))
        # self.play(
        #     FadeIn(tiny_circle_4_p0),
        #     FadeIn(tiny_circle_4_p1),
        #     FadeIn(tiny_circle_5_p0),
        #     FadeIn(tiny_circle_5_p1),
        # )

        # self.play(
        #     GrowFromPoint(line_4, tiny_circle_4_p0),
        #     GrowFromPoint(line_5, tiny_circle_4_p1),
        #     GrowFromPoint(line_6, tiny_circle_5_p0),
        #     GrowFromPoint(line_7, tiny_circle_5_p1),
        # )

        # self.play(
        #     FadeIn(line_p6),
        #     FadeIn(line_p7),
        #     FadeIn(line_p10),
        #     FadeIn(line_p11),
        # )

        # self.play(
        #     FadeOut(tiny_circle_4),
        #     FadeOut(tiny_circle_5),
        #     FadeOut(line_p4),
        #     FadeOut(line_p5),
        #     FadeOut(tiny_circle_4_p0),
        #     FadeOut(tiny_circle_4_p1),
        #     FadeOut(tiny_circle_5_p0),
        #     FadeOut(tiny_circle_5_p1),
        # )

        # self.play(frame_0.animate.shift(0.6 * np.sqrt(3) * RIGHT),
        #           frame_3.animate.shift(0.6 * np.sqrt(3) * LEFT))

        # self.play(FadeIn(line_p8), FadeIn(line_p9), FadeIn(line_p12),
        #           FadeIn(line_p13))

        self.play(GrowFromPoint(polygon_5, line_p6),
                  GrowFromPoint(polygon_6, line_p10))

        # self.play(
        #     FadeOut(line_4),
        #     FadeOut(line_5),
        #     FadeOut(line_6),
        #     FadeOut(line_7),
        #     FadeOut(frame_0),
        #     FadeOut(frame_2),
        #     FadeOut(frame_3),
        #     FadeOut(frame_5),
        #     FadeOut(line_p6),
        #     FadeOut(line_p7),
        #     FadeOut(line_p8),
        #     FadeOut(line_p9),
        #     FadeOut(line_p10),
        #     FadeOut(line_p11),
        #     FadeOut(line_p12),
        #     FadeOut(line_p13),
        # )

        self.play(polygon_0.animate.set_fill(BLUE, opacity=1.0),
                  polygon_1.animate.set_fill(BLUE, opacity=1.0),
                  polygon_2.animate.set_fill(BLUE, opacity=1.0),
                  polygon_3.animate.set_fill(BLUE, opacity=1.0),
                  polygon_4.animate.set_fill(BLUE, opacity=1.0),
                  polygon_5.animate.set_fill(BLUE, opacity=1.0),
                  polygon_6.animate.set_fill(BLUE, opacity=1.0))

        up = 0.8 * UP

        self.play(polygon_0.animate.shift(up), polygon_1.animate.shift(up),
                  polygon_2.animate.shift(up), polygon_3.animate.shift(up),
                  polygon_4.animate.shift(up), polygon_5.animate.shift(up),
                  polygon_6.animate.shift(up))

        self.play(FadeIn(eesast))