from manimlib.imports import *

class A_TitleScene(Scene):
    # Displays the title of the manim.
    def construct(self):
        title_text = TextMobject("Movement With SPIKE Prime")

        self.play(Write(title_text))
        self.wait(2)
        self.play(FadeOut(title_text))

class B_ControllingMovement(Scene):
    # Displays the methods of controlling a motor.
    def construct(self):
        title_text = TextMobject("Controlling Movement")

        time_text = TextMobject("Time")
        time_text.shift(3*UP)

        rotation_text = TextMobject("Rotations")
        rotation_text.shift(UP)

        degree_text = TextMobject("Degrees")
        degree_text.shift(DOWN)

        distance_text = TextMobject("Distance")
        distance_text.shift(3*DOWN)

        methods_text = VGroup(time_text, rotation_text, degree_text, distance_text)

        self.play(Write(title_text))
        self.wait(2)
        self.play(ReplacementTransform(title_text, methods_text))
        self.wait(2)
        self.play(ApplyMethod(time_text.move_to, ORIGIN), FadeOut(rotation_text), FadeOut(degree_text), FadeOut(distance_text))

class C_TimeScene(Scene):
    # Demonstrates how controlling a motor by time works.
    def construct(self):
        time_text = TextMobject("Time")

        circle_25 = Circle()
        circle_25.shift(3*LEFT)
        line_25 = Line(3*LEFT, 2*LEFT)
        wheel_25 = VGroup(circle_25, line_25)

        circle_50 = Circle()
        line_50 = Line(ORIGIN, RIGHT)
        wheel_50 = VGroup(circle_50, line_50)

        circle_100 = Circle()
        circle_100.shift(3*RIGHT)
        line_100 = Line(3*RIGHT, 4*RIGHT)
        wheel_100 = VGroup(circle_100, line_100)

        wheels = VGroup(wheel_25, wheel_50, wheel_100)

        power_25_text = TextMobject("25\%")
        power_25_text.next_to(wheel_25, DOWN)
        power_50_text = TextMobject("50\%")
        power_50_text.next_to(wheel_50, DOWN)
        power_100_text = TextMobject("100\%")
        power_100_text.next_to(wheel_100, DOWN)

        power_texts = VGroup(power_25_text, power_50_text, power_100_text)
        
        timer_tracker = ValueTracker(3)
        timer = DecimalNumber(2, num_decimal_places=3, edge_to_fix=RIGHT)
        timer.add_updater(lambda x: x.set_value(timer_tracker.get_value()))

        seconds_label = TextMobject("sec")
        seconds_label.next_to(timer, RIGHT)
        seconds_label.align_to(timer, DOWN)

        timer_label = VGroup(timer, seconds_label)
        timer_label.move_to(2*UP)


        self.add(time_text)
        self.wait(2)
        self.play(ReplacementTransform(time_text, wheels), Write(timer_label))
        self.play(FadeInFromDown(power_texts))
        self.wait(2)
        self.play(Rotating(wheel_25, radians=-PI/2), 
            Rotating(wheel_50, radians=-PI), 
            Rotating(wheel_100, radians=-TAU), 
            timer_tracker.increment_value, -3, run_time=3, rate_func=linear)
        self.wait(2)
        self.play(FadeOut(wheels), FadeOut(timer_label), FadeOut(power_texts))

class D_RotationsScene(Scene):
    # Demonstrates how controlling a motor by rotations works.
    def construct(self):
        rotations_text = TextMobject("Rotations")

        circle_25 = Circle()
        circle_25.shift(3*LEFT)
        line_25 = Line(3*LEFT, 2*LEFT)
        wheel_25 = VGroup(circle_25, line_25)

        circle_05 = Circle()
        line_05 = Line(ORIGIN, RIGHT)
        wheel_05 = VGroup(circle_05, line_05)

        circle_1 = Circle()
        circle_1.shift(3*RIGHT)
        line_1 = Line(3*RIGHT, 4*RIGHT)
        wheel_1 = VGroup(circle_1, line_1)

        wheels = VGroup(wheel_25, wheel_05, wheel_1)

        tracker_25 = DecimalNumber(0, num_decimal_places=2, edge_to_fix=RIGHT)
        tracker_25.add_updater(lambda x: x.set_value(-line_25.get_angle() / TAU))

        rotation_label_25 = TextMobject("rot")
        rotation_label_25.next_to(tracker_25, RIGHT)
        rotation_label_25.align_to(tracker_25, DOWN)

        rotation_tracker_25 = VGroup(tracker_25, rotation_label_25)
        rotation_tracker_25.move_to(3*LEFT+2*UP)

        tracker_05 = DecimalNumber(0, num_decimal_places=2, edge_to_fix=RIGHT)
        tracker_05.add_updater(lambda x: x.set_value(-line_05.get_angle() / TAU))

        rotation_label_05 = TextMobject("rot")
        rotation_label_05.next_to(tracker_05, RIGHT)
        rotation_label_05.align_to(tracker_05, DOWN)

        rotation_tracker_05 = VGroup(tracker_05, rotation_label_05)
        rotation_tracker_05.move_to(2*UP)

        tracker_1 = DecimalNumber(0, num_decimal_places=2, edge_to_fix=RIGHT)
        tracker_1.add_updater(lambda x: x.set_value(-line_1.get_angle() / TAU) if line_1.get_angle() < 0 
            else x.set_value((2 * (PI - line_1.get_angle()) + line_1.get_angle()) / TAU) if line_1.get_angle() > 0 
            else x.set_value(0))

        rotation_label_1 = TextMobject("rot")
        rotation_label_1.next_to(tracker_1, RIGHT)
        rotation_label_1.align_to(tracker_1, DOWN)

        rotation_tracker_1 = VGroup(tracker_1, rotation_label_1)
        rotation_tracker_1.move_to(3*RIGHT+2*UP)

        self.play(Write(rotations_text))
        self.wait(2)
        self.play(ReplacementTransform(rotations_text, wheels), Write(rotation_tracker_25), Write(rotation_tracker_05), Write(rotation_tracker_1))
        self.wait(2)
        self.play(Rotating(wheel_25, radians=-PI/2, run_time=1), 
            Rotating(wheel_05, radians=-PI, run_time=2), 
            Rotating(wheel_1, radians=-TAU, run_time=4))
        self.wait(2)
        self.play(FadeOut(wheels), FadeOut(rotation_tracker_25), FadeOut(rotation_tracker_05), FadeOut(rotation_tracker_1))

class E_DegreesScene(Scene):
    # Demonstrates how controlling a motor by degrees works.
    def construct(self):
        degrees_text = TextMobject("Degrees")

        circle_25 = Circle()
        circle_25.shift(3*LEFT)
        line_25 = Line(3*LEFT, 2*LEFT)
        wheel_25 = VGroup(circle_25, line_25)

        circle_05 = Circle()
        line_05 = Line(ORIGIN, RIGHT)
        wheel_05 = VGroup(circle_05, line_05)

        circle_1 = Circle()
        circle_1.shift(3*RIGHT)
        line_1 = Line(3*RIGHT, 4*RIGHT)
        wheel_1 = VGroup(circle_1, line_1)

        wheels = VGroup(wheel_25, wheel_05, wheel_1)

        tracker_25 = DecimalNumber(0, num_decimal_places=0, edge_to_fix=RIGHT)
        tracker_25.add_updater(lambda x: x.set_value(-line_25.get_angle() / DEGREES))

        degree_label_25 = TextMobject(u'\N{DEGREE SIGN}')
        degree_label_25.next_to(tracker_25, RIGHT)
        degree_label_25.align_to(tracker_25, UP)
        degree_label_25.shift(0.2*LEFT)

        degree_tracker_25 = VGroup(tracker_25, degree_label_25)
        degree_tracker_25.move_to(3*LEFT+2*UP)

        tracker_05 = DecimalNumber(0, num_decimal_places=0, edge_to_fix=RIGHT)
        tracker_05.add_updater(lambda x: x.set_value(-line_05.get_angle() / DEGREES))

        degree_label_05 = TextMobject(u'\N{DEGREE SIGN}')
        degree_label_05.next_to(tracker_05, RIGHT)
        degree_label_05.align_to(tracker_05, UP)
        degree_label_05.shift(0.2*LEFT)

        degree_tracker_05 = VGroup(tracker_05, degree_label_05)
        degree_tracker_05.move_to(2*UP)

        tracker_1 = DecimalNumber(0, num_decimal_places=0, edge_to_fix=RIGHT)
        tracker_1.add_updater(lambda x: x.set_value(-line_1.get_angle() / DEGREES) if line_1.get_angle() < 0 
            else x.set_value((2 * (PI - line_1.get_angle()) + line_1.get_angle()) / DEGREES) if line_1.get_angle() > 0 
            else x.set_value(0))

        degree_label_1 = TextMobject(u'\N{DEGREE SIGN}')
        degree_label_1.next_to(tracker_1, RIGHT)
        degree_label_1.align_to(tracker_1, UP)
        degree_label_1.shift(0.2*LEFT)

        degree_tracker_1 = VGroup(tracker_1, degree_label_1)
        degree_tracker_1.move_to(3*RIGHT+2*UP)

        self.play(Write(degrees_text))
        self.wait(2)
        self.play(ReplacementTransform(degrees_text, wheels), Write(degree_tracker_25), Write(degree_tracker_05), Write(degree_tracker_1))
        self.wait(2)
        self.play(Rotating(wheel_25, radians=-PI/2, run_time=1), 
            Rotating(wheel_05, radians=-PI, run_time=2), 
            Rotating(wheel_1, radians=-TAU, run_time=4))
        self.wait(2)
        self.play(FadeOut(wheels), FadeOut(degree_tracker_25), FadeOut(degree_tracker_05), FadeOut(degree_tracker_1))

class F_IntroToDistance(GraphScene):
    # Animates a wheel rolling a set distance and introduces the idea of converting rotations to distance.
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "y_min": 0,
        "y_max": 1,
        "graph_origin": [-5, -1, 0],
        "x_labeled_nums": range(0, 11, 1),
        "x_axis_width": 10,
        "y_axis_height": 0,
        "x_axis_label": None,
        "y_axis_label": None,
        "exclude_zero_label": False
    }
    def construct(self):
        distance_text = TextMobject("Distance")

        distance_tracker = ValueTracker(0)

        circle = Circle()
        circle.shift(5*LEFT)
        line = Line(5*LEFT, 4*LEFT)
        wheel = VGroup(circle, line)

        circle.add_updater(lambda x: x.move_to([distance_tracker.get_value() - 5, 0, 0]))
        line.add_updater(lambda x: line.move_to([distance_tracker.get_value() - 5 + np.cos(distance_tracker.get_value()) / 2, -np.sin(distance_tracker.get_value()) / 2, 0]))
        line.add_updater(lambda x: x.set_angle(-distance_tracker.get_value()))

        arrow = Arrow(5*LEFT+2*DOWN, 5*RIGHT+2*DOWN, buff=0)

        text_1 = TextMobject("Control using:")
        text_1.shift(3*UP)

        time_text = TextMobject("Time")
        time_text.shift(2*UP)

        rotations_text = TextMobject("Rotations")
        rotations_text.shift(1*UP)

        degrees_text = TextMobject("Degrees")

        text_group = VGroup(text_1, time_text, rotations_text, degrees_text)

        conversion_text = TextMobject(chr(8594) + " Distance")

        conversion_group = VGroup(rotations_text, conversion_text)

        def update_line_1(line):
            line.set_start_and_end_attrs(5*LEFT+2*DOWN, [distance_tracker.get_value() - 5, -2, 0])
            line.generate_points()

        line_1 = Line(5*LEFT+2*DOWN, 5*LEFT+2*DOWN, color=RED_A)
        line_1.add_updater(update_line_1)

        def update_line_2(line):
            line.set_start_and_end_attrs((5-2*PI)*LEFT+2*DOWN, [distance_tracker.get_value() - 5, -2, 0])
            line.generate_points()

        line_2 = Line((5-2*PI)*LEFT+2*DOWN, (5-2*PI)*LEFT+2*DOWN, color=GREEN_A)
        line_2.add_updater(update_line_2)

        unroll_tracker = ValueTracker(0)

        def update_unrolling_circle(circle):
            circle.become(Arc(start_angle=-PI/2, angle=TAU-unroll_tracker.get_value(), color=RED))
            circle.move_arc_center_to((-PI + unroll_tracker.get_value())*RIGHT+UP)

        unrolling_circle = Circle()
        unrolling_circle.shift(PI*LEFT+UP)
        unrolling_circle.add_updater(update_unrolling_circle)

        def update_unrolling_line(line):
            line.set_start_and_end_attrs(PI*LEFT, (-PI + unroll_tracker.get_value())*RIGHT)
            line.generate_points()

        unrolling_line = Line(PI*LEFT+UP, PI*LEFT+UP, color=RED)
        unrolling_line.add_updater(update_unrolling_line)

        circumference_arc = Arc(start_angle=PI/3, angle=-TAU+PI/6, radius=1.5)
        circumference_arc.shift(UP)

        arrow_tip = ArrowTip(color=WHITE, start_angle=0)
        arrow_tip.shift(2.5*UP+0.1*LEFT)

        circumference_arrow = VGroup(circumference_arc, arrow_tip)

        circumference_text = TextMobject("Circumference")
        circumference_text.shift(3.5*UP)

        self.play(Write(distance_text))
        self.wait(2)
        self.play(FadeOut(distance_text))
        self.setup_axes(animate=True)
        self.play(ShowCreation(wheel))
        self.wait(2)
        self.play(GrowArrow(arrow))
        self.wait(2)
        self.play(FadeOut(arrow))
        self.play(distance_tracker.increment_value, 10, run_time=5)
        self.wait(2)
        self.play(Write(text_group))
        self.wait(2)
        self.play(FadeOut(time_text), FadeOut(degrees_text), ApplyMethod(rotations_text.shift, UP))
        self.wait(2)
        conversion_text.next_to(rotations_text, RIGHT)
        self.play(Write(conversion_text), FadeOut(text_1))
        self.play(ApplyMethod(conversion_group.move_to, [0, 2, 0]))
        self.wait(2)
        self.play(distance_tracker.increment_value, -10, run_time=2)
        self.wait(2)
        self.add(line_1)
        self.play(distance_tracker.increment_value, 2*PI, run_time=2)
        line_1.remove_updater(update_line_1)
        self.add(line_2)
        self.play(distance_tracker.increment_value, 10-2*PI, run_time=2)
        self.wait(2)
        self.play(FadeOut(self.axes), FadeOut(wheel), FadeOut(conversion_group), FadeOut(line_2), ApplyMethod(line_1.move_to, ORIGIN+DOWN))
        self.play(ShowCreation(unrolling_circle))
        self.wait(1)
        self.add(unrolling_line)
        self.play(unroll_tracker.increment_value, TAU, run_time=4)
        self.wait(2)
        self.play(unroll_tracker.increment_value, -TAU, run_time=2)
        self.remove(unrolling_line)
        unrolling_circle.remove_updater(update_unrolling_circle)
        unrolling_line.remove_updater(update_unrolling_line)
        self.play(ApplyMethod(unrolling_circle.move_arc_center_to, UP))
        self.play(ShowCreation(circumference_arrow), run_time=2)
        self.play(Write(circumference_text))
        self.play(FadeOut(line_1), ApplyMethod(unrolling_circle.shift, DOWN), ApplyMethod(circumference_arrow.shift, DOWN), ApplyMethod(circumference_text.shift, DOWN))
        self.wait(2)
        self.play(FadeOut(unrolling_circle), FadeOut(circumference_arrow), FadeOut(circumference_text))

class G_CalculatingCircumference(Scene):
    # Explains how to calculate the circumference of a wheel
    def construct(self):
        calculating_circumference_text = TextMobject("Calculating Circumference")

        equation = TexMobject(r"\text{Circumference} = 2 \pi r")

        pi_text = TextMobject("Pi")
        pi = TexMobject(r"\pi")
        pi.next_to(pi, DOWN)

        pi_group = VGroup(pi_text, pi)
        pi_group.move_to(ORIGIN)

        pi_written = VGroup(
            TextMobject("3.14159265358979323846264338327950288419716939937510"),
            TextMobject("58209749445923078164062862089986280348253421170679"),
            TextMobject("82148086513282306647093844609550582231725359408128"),
            TextMobject("48111745028410270193852110555964462294895493038196"),
            TextMobject("44288109756659334461284756482337867831652712019091"),
            TextMobject("45648566923460348610454326648213393607260249141273"),
            TextMobject("72458700660631558817488152092096282925409171536436"),
            TextMobject("78925903600113305305488204665213841469519415116094"),
            TextMobject("33057270365759591953092186117381932611793105118548"),
            TextMobject("07446237996274956735188575272489122793818301194912")
        ).arrange(DOWN, aligned_edge=RIGHT)

        pi_written = VGroup(pi_written, TextMobject("...")).arrange(RIGHT, aligned_edge=DOWN, buff=SMALL_BUFF)

        radius_text = TextMobject("Radius")
        radius = TexMobject(r"r")
        radius.next_to(radius_text, DOWN)

        radius_group = VGroup(radius_text, radius)
        radius_group.move_to(ORIGIN)

        circle = Circle(radius=2)
        line = Line(ORIGIN, 2*RIGHT)
        wheel = VGroup(circle, line)

        r_and_line = VGroup(radius, line)

        equation_2 = TexMobject(r"2 \pi")
        equation_3 = TexMobject(r"2 \times 3.14... \times")
        equation_4 = TexMobject(r"6.28... \times")

        equation_group = VGroup(equation_2, r_and_line)

        line_2 = Line(LEFT+2*UP, RIGHT+2*UP)
        line_3 = Line(LEFT+1*UP, RIGHT+1*UP)
        line_4 = Line(LEFT, RIGHT)
        line_5 = Line(LEFT+1*DOWN, RIGHT+1*DOWN)
        line_6 = Line(LEFT+2*DOWN, RIGHT+2*DOWN)
        line_7 = Line(LEFT+3*DOWN, (TAU-6)*LEFT+3*DOWN)

        lines = VGroup(line_2, line_3, line_4, line_5, line_6, line_7)

        rotate_counter = ValueTracker(0)

        arc = Arc(start_angle=PI/2+0.5, angle=-1, arc_center=UP, radius=2)
        arc_2 = Arc(start_angle=PI/2+0.5, angle=-1, radius=2)
        arc_3 = Arc(start_angle=PI/2+0.5, angle=-1, arc_center=DOWN, radius=2)
        arc_4 = Arc(start_angle=PI/2+0.5, angle=-1, arc_center=2*DOWN, radius=2)
        arc_5 = Arc(start_angle=PI/2+0.5, angle=-1, arc_center=3*DOWN, radius=2)
        arc_6 = Arc(start_angle=PI/2+0.5, angle=-1, arc_center=4*DOWN, radius=2)
        arc_7 = Arc(start_angle=PI/2+PI-3, angle=-TAU+6, arc_center=5*DOWN, radius=2)

        arcs = VGroup(arc, arc_2, arc_3, arc_4, arc_5, arc_6, arc_7)

        self.play(Write(calculating_circumference_text))
        self.wait(2)
        self.play(ReplacementTransform(calculating_circumference_text, equation))
        self.wait(2)
        self.play(FadeOut(equation))
        self.play(Write(pi_group))
        self.wait(2)
        self.play(ReplacementTransform(pi_group, pi_written))
        self.wait(2)
        self.play(FadeOut(pi_written))
        self.play(Write(radius_group))
        self.wait(2)
        self.play(ShowCreation(wheel), FadeOut(radius_text), ApplyMethod(radius.next_to, RIGHT, UP))
        self.wait(2)
        equation_2.next_to(r_and_line, LEFT, buff=SMALL_BUFF)
        self.play(Write(equation_2), FadeOut(circle))
        self.play(ApplyMethod(equation_group.move_to, ORIGIN))
        self.wait(2)
        equation_3.next_to(r_and_line, LEFT, buff=SMALL_BUFF)
        self.play(Transform(equation_2, equation_3))
        self.play(ApplyMethod(equation_group.move_to, ORIGIN))
        self.wait(2)
        equation_4.next_to(r_and_line, LEFT, buff=SMALL_BUFF)
        self.play(Transform(equation_2, equation_4))
        self.play(ApplyMethod(equation_group.move_to, ORIGIN))
        self.wait(2)
        self.play(FadeOut(equation_2), FadeOut(radius), ApplyMethod(line.move_to, 3*UP))
        self.play(TransformFromCopy(line, lines))
        self.wait(1)
        self.play(ReplacementTransform(line, arc), 
            ReplacementTransform(line_2, arc_2), 
            ReplacementTransform(line_3, arc_3), 
            ReplacementTransform(line_4, arc_4), 
            ReplacementTransform(line_5, arc_5), 
            ReplacementTransform(line_6, arc_6), 
            ReplacementTransform(line_7, arc_7))
        self.wait(1)
        self.play(ApplyMethod(arc.move_arc_center_to, 3*RIGHT),
            ApplyMethod(arc_2.move_arc_center_to, ORIGIN),
            ApplyMethod(arc_3.move_arc_center_to, 3*LEFT),
            ApplyMethod(arc_4.move_arc_center_to, 4.5*LEFT+4*DOWN),
            ApplyMethod(arc_5.move_arc_center_to, 1.5*LEFT+4*DOWN),
            ApplyMethod(arc_6.move_arc_center_to, 1.5*RIGHT+4*DOWN),
            ApplyMethod(arc_7.move_arc_center_to, 4.5*RIGHT+4*DOWN))
        self.wait(1)

        arc.add_updater(lambda x: x.become(Arc(start_angle=PI/2+0.5-rotate_counter.get_value()*(PI/2-0.5), angle=-1, 
            arc_center=(2*np.cos(PI/2-rotate_counter.get_value()*(PI/2-0.5))-3)*LEFT+
                        (2-2*np.sin(PI/2-rotate_counter.get_value()*(PI/2-0.5)))*UP, radius=2)))
        arc_2.add_updater(lambda x: x.become(Arc(start_angle=PI/2+0.5-rotate_counter.get_value()*(PI/2-1.5), angle=-1, 
            arc_center=(2*np.cos(PI/2-rotate_counter.get_value()*(PI/2-1.5)))*LEFT+
                        (2-2*np.sin(PI/2-rotate_counter.get_value()*(PI/2-1.5)))*UP, radius=2)))
        arc_3.add_updater(lambda x: x.become(Arc(start_angle=PI/2+0.5-rotate_counter.get_value()*(PI/2-2.5), angle=-1, 
            arc_center=(2*np.cos(PI/2-rotate_counter.get_value()*(PI/2-2.5))+3)*LEFT+
                        (2-2*np.sin(PI/2-rotate_counter.get_value()*(PI/2-2.5)))*UP, radius=2)))
        arc_4.add_updater(lambda x: x.become(Arc(start_angle=PI/2+0.5-rotate_counter.get_value()*(PI/2-3.5), angle=-1, 
            arc_center=(2*np.cos(PI/2-rotate_counter.get_value()*(PI/2-3.5))+4.5)*LEFT+
                        (2-2*np.sin(PI/2-rotate_counter.get_value()*(PI/2-3.5))-4)*UP, radius=2)))
        arc_5.add_updater(lambda x: x.become(Arc(start_angle=PI/2+0.5-rotate_counter.get_value()*(PI/2-4.5), angle=-1, 
            arc_center=(2*np.cos(PI/2-rotate_counter.get_value()*(PI/2-4.5))+1.5)*LEFT+
                        (2-2*np.sin(PI/2-rotate_counter.get_value()*(PI/2-4.5))-4)*UP, radius=2)))
        arc_6.add_updater(lambda x: x.become(Arc(start_angle=PI/2+0.5-rotate_counter.get_value()*(PI/2-5.5), angle=-1, 
            arc_center=(2*np.cos(PI/2-rotate_counter.get_value()*(PI/2-5.5))-1.5)*LEFT+
                        (2-2*np.sin(PI/2-rotate_counter.get_value()*(PI/2-5.5))-4)*UP, radius=2)))
        arc_7.add_updater(lambda x: x.become(Arc(start_angle=PI/2+PI-3-rotate_counter.get_value()*(PI/2-(3+PI)), angle=-TAU+6, 
            arc_center=(2*np.cos(PI/2-rotate_counter.get_value()*(PI/2-(3+PI)))-4.5)*LEFT+
                        (2-2*np.sin(PI/2-rotate_counter.get_value()*(PI/2-(3+PI)))-4)*UP, radius=2)))

        self.play(rotate_counter.increment_value, 1, run_time=2)
        self.wait(1)
        arc.clear_updaters()
        arc_2.clear_updaters()
        arc_3.clear_updaters()
        arc_4.clear_updaters()
        arc_5.clear_updaters()
        arc_6.clear_updaters()
        arc_7.clear_updaters()
        self.play(ApplyMethod(arc.move_arc_center_to, 0.5*np.cos(0.5)*RIGHT+0.5*np.sin(0.5)*UP),
            ApplyMethod(arc_2.move_arc_center_to, 0.5*np.cos(1.5)*RIGHT+0.5*np.sin(1.5)*UP),
            ApplyMethod(arc_3.move_arc_center_to, 0.5*np.cos(2.5)*RIGHT+0.5*np.sin(2.5)*UP),
            ApplyMethod(arc_4.move_arc_center_to, 0.5*np.cos(3.5)*RIGHT+0.5*np.sin(3.5)*UP),
            ApplyMethod(arc_5.move_arc_center_to, 0.5*np.cos(4.5)*RIGHT+0.5*np.sin(4.5)*UP),
            ApplyMethod(arc_6.move_arc_center_to, 0.5*np.cos(5.5)*RIGHT+0.5*np.sin(5.5)*UP),
            ApplyMethod(arc_7.move_arc_center_to, 0.5*np.cos(3+PI)*RIGHT+0.5*np.sin(3+PI)*UP))
        self.wait(1)
        self.play(ApplyMethod(arc.move_arc_center_to, ORIGIN),
            ApplyMethod(arc_2.move_arc_center_to, ORIGIN),
            ApplyMethod(arc_3.move_arc_center_to, ORIGIN),
            ApplyMethod(arc_4.move_arc_center_to, ORIGIN),
            ApplyMethod(arc_5.move_arc_center_to, ORIGIN),
            ApplyMethod(arc_6.move_arc_center_to, ORIGIN),
            ApplyMethod(arc_7.move_arc_center_to, ORIGIN))
        self.wait(2)
        self.play(FadeOut(arcs))

class H_ConvertingUnits(Scene):
    # Explains how to convert from inches to rotations
    def construct(self):
        conversion_text = TextMobject("Converting Inches to Rotations")

        feet_to_inches_text = TextMobject("Feet " + chr(8594) + " Inches")

        eq_1 = TexMobject(r"\text{feet}", r"\times", r"\text{conversion factor}", r"=", r"\text{inches}")
        eq_1.set_color_by_tex_to_color_map({
            "{feet}": RED,
            "{conversion factor}": YELLOW,
            "{inches}": ORANGE
        })

        eq_2 = TexMobject(r"\text{feet}", r"\times", r"\text{inches per foot}", r"=", r"\text{inches}")
        eq_2.set_color_by_tex_to_color_map({
            "{feet}": RED,
            "{inches per foot}": YELLOW,
            "{inches}": ORANGE
        })

        eq_3 = TexMobject(r"\text{feet}", r"\times", r"\frac{\text{12 inches}}{\text{1 foot}}", r"=", r"\text{inches}")
        eq_3.set_color_by_tex_to_color_map({
            "{feet}": RED,
            "12": YELLOW,
            "text{inches}": ORANGE
        })

        inches_to_rot_text = TextMobject("Inches " + chr(8594) + " Rotations")

        eq_4 = TexMobject(r"\text{inches}", r"\times", r"\text{conversion factor}", r"=", r"\text{rotations}")
        eq_4.set_color_by_tex_to_color_map({
            "{inches}": RED,
            "{conversion factor}": YELLOW,
            "{rotations}": ORANGE
        })

        eq_5 = TexMobject(r"\text{inches}", r"\times", r"\text{inches per rotation}", r"=", r"\text{rotations}")
        eq_5.set_color_by_tex_to_color_map({
            "{inches}": RED,
            "{inches per rotation}": YELLOW,
            "{rotations}": ORANGE
        })

        eq_6 = TexMobject(r"\text{inches}", r"\times", r"\frac{\text{1 rotation}}{\text{circumference}}", r"=", r"\text{rotations}")
        eq_6.set_color_by_tex_to_color_map({
            "{inches}": RED,
            "{1 rotation}": YELLOW,
            "{rotations}": ORANGE
        })

        eq_7 = TexMobject(r"\text{inches}", r"\times", r"\frac{\text{1 rotation}}{2 \pi r \ \text{inches}}", r"=", r"\text{rotations}")
        eq_7.set_color_by_tex_to_color_map({
            "{inches}": RED,
            "{1 rotation}": YELLOW,
            "{rotations}": ORANGE
        })

        self.play(Write(conversion_text))
        self.wait(2)
        self.play(ReplacementTransform(conversion_text, feet_to_inches_text))
        self.wait(2)
        self.play(ReplacementTransform(feet_to_inches_text, eq_1))
        self.wait(2)
        self.play(ReplacementTransform(eq_1, eq_2))
        self.wait(2)
        self.play(ReplacementTransform(eq_2, eq_3))
        self.wait(2)
        self.play(FadeOut(eq_3))
        self.play(Write(inches_to_rot_text))
        self.wait(2)
        self.play(ReplacementTransform(inches_to_rot_text, eq_4))
        self.wait(2)
        self.play(ReplacementTransform(eq_4, eq_5))
        self.wait(2)
        self.play(ReplacementTransform(eq_5, eq_6))
        self.wait(2)
        self.play(ReplacementTransform(eq_6, eq_7))
        self.wait(2)
        self.play(FadeOut(eq_7))
