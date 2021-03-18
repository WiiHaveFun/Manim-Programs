from manimlib.imports import *

class A_TitleScene(Scene):
    # Displays the title of the manim.
    CONFIG={
		"camera_config":{"background_color":"#6C935C"}
	}

    def construct(self):
        title_text = Text("How to Play Tennis", color=BLACK)

        gameplay_text = Text("Gameplay", color=BLACK)
        gameplay_text.shift(0.5*UP)

        strokes_text = Text("Shots", color=BLACK)
        strokes_text.shift(0.5*DOWN)

        sections = VGroup(gameplay_text, strokes_text)

        self.play(Write(title_text))
        self.wait(1)
        self.play(ReplacementTransform(title_text, sections))
        self.wait(1)
        self.play(ApplyMethod(gameplay_text.move_to, ORIGIN), FadeOutAndShiftDown(strokes_text))
        self.wait(1)
        self.play(FadeOut(gameplay_text))

class B_ObjectiveScene(Scene):
    CONFIG={
		"camera_config":{"background_color":"#6C935C"}
	}
    
    # Displays a short title.
    def construct(self):
        objective_text = Text("Objective", color=BLACK)

        self.play(Write(objective_text))
        self.wait(1)
        self.play(FadeOut(objective_text))

court_SF = 0.15

class C_Court(Scene):
    CONFIG={
		"camera_config":{"background_color":"#6C935C"}
	}

    # Displays the tennis court and explains the lines and areas of the court.
    def construct(self):
        court_text = Text("The Court", color=BLACK)

        doubles_court = Rectangle(height=36*court_SF, width=78*court_SF, fill_color="#3C638E", fill_opacity=1)
        net_line = Line(start=21*court_SF*UP, end=21*court_SF*DOWN, stroke_width=10)
        center_line = Line(start=21*court_SF*LEFT, end=21*court_SF*RIGHT)
        singles_court = Rectangle(height=27*court_SF, width=78*court_SF)
        service_boxes = Rectangle(height=27*court_SF, width=42*court_SF)
        hash_left = Line(start=39*court_SF*LEFT, end=39*court_SF*LEFT+(2/3)*court_SF*RIGHT)
        hash_right = Line(start=39*court_SF*RIGHT, end=39*court_SF*RIGHT+(2/3)*court_SF*LEFT)

        court = VGroup(doubles_court, net_line, center_line, singles_court, service_boxes, hash_left, hash_right)

        height_brace = Brace(doubles_court, LEFT)
        height_text = Text("36 ft", color=BLACK).rotate(PI/2).next_to(height_brace, LEFT)

        height_brace_2 = Brace(singles_court, RIGHT)
        height_text_2 = Text("27 ft", color=BLACK).rotate(-PI/2).next_to(height_brace_2, RIGHT)

        width_brace = Brace(doubles_court)
        width_text = Text("78 ft", color=BLACK).next_to(width_brace, DOWN)

        baseline_text = Text("Baseline", color=BLACK).scale(0.75).rotate(PI/2).next_to(doubles_court, LEFT)
        service_line_text = Text("Service Line", color=BLACK).scale(0.75).rotate(PI/2).next_to(service_boxes, LEFT)
        center_line_text = Text("Center Line", color=BLACK).scale(0.75).next_to(center_line, UP).shift(10.5*court_SF*LEFT)
        ssl_text = Text("Singles Side Line", color=BLACK).scale(0.75).next_to(singles_court, UP).shift(19.5*court_SF*LEFT+0.2*DOWN)
        dsl_text = Text("Doubles Side Line", color=BLACK).scale(0.75).next_to(doubles_court, UP).shift(19.5*court_SF*LEFT+0.2*DOWN)
        net_text = Text("Net", color=BLACK).scale(0.75).next_to(net_line, UP)

        line_text_group = VGroup(baseline_text, service_line_text, center_line_text, ssl_text, dsl_text, net_text)

        out_text = Text("Out of Bounds", color=BLACK).next_to(net_line, UP).align_to(doubles_court, LEFT)
        doubles_text = Text("Doubles Court", color=BLACK).align_to(doubles_court, TOP+LEFT)
        doubles_high = Rectangle(height=36*court_SF, width=78*court_SF, fill_color=RED, fill_opacity=0.5, stroke_width=0)
        singles_text = Text("Singles Court", color=BLACK).align_to(singles_court, TOP+LEFT)
        singles_high = Rectangle(height=27*court_SF, width=78*court_SF, fill_color=BLUE, fill_opacity=0.5, stroke_width=0)

        deuce_text = Text("Deuce Court", color=BLACK).align_to(doubles_court, BOTTOM+LEFT)
        deuce_high_1 = Rectangle(height=18*court_SF, width=39*court_SF, fill_color=RED, fill_opacity=0.5, stroke_width=0).align_to(doubles_court, BOTTOM+LEFT)
        deuce_high_2 = Rectangle(height=18*court_SF, width=39*court_SF, fill_color=RED, fill_opacity=0.5, stroke_width=0).align_to(doubles_court, TOP+RIGHT)
        ad_text = Text("Ad Court", color=BLACK).align_to(doubles_court, TOP+LEFT)
        ad_high_1 = Rectangle(height=18*court_SF, width=39*court_SF, fill_color=PURPLE, fill_opacity=0.5, stroke_width=0).align_to(doubles_court, TOP+LEFT)
        ad_high_2 = Rectangle(height=18*court_SF, width=39*court_SF, fill_color=PURPLE, fill_opacity=0.5, stroke_width=0).align_to(doubles_court, BOTTOM+RIGHT)

        service_text = Text("Service Boxes", color=BLACK).align_to(service_boxes, TOP+LEFT)
        service_high = Rectangle(height=27*court_SF, width=42*court_SF, fill_color=RED, fill_opacity=0.5, stroke_width=0)
        alley_text = Text("Doubles Alley", color=BLACK).align_to(doubles_court, TOP+LEFT)
        alley_high_1 = Rectangle(height=4.5*court_SF, width=78*court_SF, fill_color=PURPLE, fill_opacity=0.5, stroke_width=0).align_to(doubles_court, TOP)
        alley_high_2 = Rectangle(height=4.5*court_SF, width=78*court_SF, fill_color=PURPLE, fill_opacity=0.5, stroke_width=0).align_to(doubles_court, BOTTOM)

        self.play(Write(court_text))
        self.wait(1)
        self.play(FadeOut(court_text))
        self.wait(1)
        self.play(ShowCreation(doubles_court), 
            ShowCreation(net_line), 
            ShowCreation(center_line), 
            ShowCreation(singles_court), 
            ShowCreation(service_boxes), 
            ShowCreation(hash_left),
            ShowCreation(hash_right))
        self.wait(1)
        self.play(ShowCreation(height_brace), Write(height_text), ShowCreation(height_brace_2), Write(height_text_2), ShowCreation(width_brace), Write(width_text))
        self.wait(1)
        self.play(FadeOut(height_brace), FadeOut(height_text), FadeOut(height_brace_2), FadeOut(height_text_2), FadeOut(width_brace), FadeOut(width_text))
        self.wait(1),
        self.play(Write(baseline_text))
        self.wait(0.5)
        self.play(Write(service_line_text))
        self.wait(0.5)
        self.play(Write(center_line_text))
        self.wait(0.5)
        self.play(Write(ssl_text))
        self.wait(0.5)
        self.play(Write(dsl_text))
        self.wait(0.5)
        self.play(Write(net_text))
        self.wait(1)
        self.play(FadeOut(line_text_group))
        self.wait(1)
        self.play(Write(out_text))
        self.wait(0.5)
        self.play(FadeIn(doubles_high), Write(doubles_text))
        self.wait(0.5)
        self.play(FadeIn(singles_high), Write(singles_text))
        self.wait(1)
        self.play(FadeOut(out_text), FadeOut(doubles_high), FadeOut(doubles_text), FadeOut(singles_high), FadeOut(singles_text))
        self.wait(1)
        self.play(FadeIn(deuce_high_1), FadeIn(deuce_high_2), Write(deuce_text))
        self.wait(0.5)
        self.play(FadeIn(ad_high_1), FadeIn(ad_high_2), Write(ad_text))
        self.wait(1)
        self.play(FadeOut(deuce_high_1), FadeOut(deuce_high_2), FadeOut(deuce_text), FadeOut(ad_high_1), FadeOut(ad_high_2), FadeOut(ad_text))
        self.wait(1)
        self.play(FadeIn(service_high), Write(service_text))
        self.wait(0.5)
        self.play(FadeIn(alley_high_1), FadeIn(alley_high_2), Write(alley_text))
        self.wait(1)
        self.play(FadeOut(service_high), FadeOut(service_text), FadeOut(alley_high_1), FadeOut(alley_high_2), FadeOut(alley_text))
        self.play(FadeOut(court))

class D_Point(Scene):
    CONFIG={
		"camera_config":{"background_color":"#6C935C"}
	}

    # Displays the tennis court.
    def construct(self):
        gameplay_text = Text("Playing a Point", color=BLACK)

        doubles_court = Rectangle(height=36*court_SF, width=78*court_SF, fill_color="#3C638E", fill_opacity=1)
        net_line = Line(start=21*court_SF*UP, end=21*court_SF*DOWN, stroke_width=10)
        center_line = Line(start=21*court_SF*LEFT, end=21*court_SF*RIGHT)
        singles_court = Rectangle(height=27*court_SF, width=78*court_SF)
        service_boxes = Rectangle(height=27*court_SF, width=42*court_SF)
        hash_left = Line(start=39*court_SF*LEFT, end=39*court_SF*LEFT+(2/3)*court_SF*RIGHT)
        hash_right = Line(start=39*court_SF*RIGHT, end=39*court_SF*RIGHT+(2/3)*court_SF*LEFT)

        court = VGroup(doubles_court, net_line, center_line, singles_court, service_boxes, hash_left, hash_right)

        player_1 = Circle(radius=1.5*court_SF, fill_color="#D2B4AC", fill_opacity=1, stroke_width=0).next_to(singles_court, LEFT).shift(3*court_SF*DOWN)
        player_2 = Circle(radius=1.5*court_SF, fill_color="#D2B4AC", fill_opacity=1, stroke_width=0).next_to(singles_court, RIGHT).shift(10*court_SF*UP)

        h_tracker = ValueTracker(0)

        ball = Circle(radius=0.5*court_SF, fill_color="#CCFF00", fill_opacity=1, stroke_width=0).next_to(player_1, RIGHT)
        shadow = Circle(radius=0.5*court_SF, fill_color="#ABABAB", fill_opacity=0.5, stroke_width=0)

        bounce_param=4
        second_scale=4

        def bounceBall(shadow):
            if h_tracker.get_value() <= 2:
                shadow.move_to([ball.get_x(), (ball.get_y()/court_SF-(-7*h_tracker.get_value()*(h_tracker.get_value()-2)))*court_SF, 0])
            else:
                shadow.move_to([ball.get_x(), (ball.get_y()/court_SF-(-second_scale*(h_tracker.get_value()-2)*(h_tracker.get_value()-bounce_param)))*court_SF, 0])

        shadow.add_updater(bounceBall)
        h_tracker.set_value(0.2)

        cross_arm_1 = Line(start=0.25*LEFT, end=0.25*RIGHT, color=RED).rotate(PI/4)
        cross_arm_2 = Line(start=0.25*LEFT, end=0.25*RIGHT, color=RED).rotate(-PI/4)

        cross = VGroup(cross_arm_1, cross_arm_2)

        self.play(Write(gameplay_text))
        self.wait(1)
        self.play(FadeOut(gameplay_text))
        self.wait(1)
        self.play(FadeIn(court),
            FadeIn(player_1),
            FadeIn(player_2),
            FadeIn(shadow),
            FadeIn(ball))
        self.wait(1)
        self.play(ApplyMethod(ball.move_to, [40*court_SF, 10*court_SF, 0]), 
            ApplyMethod(player_2.move_to, [player_2.get_x(), 7*court_SF, 0]), 
            h_tracker.set_value, 3.5, run_time=2, rate_func=linear)
        h_tracker.set_value(0.2)
        bounce_param=3
        second_scale=10
        self.play(ApplyMethod(ball.move_to, [-40*court_SF, 5*court_SF, 0]), 
            ApplyMethod(player_1.move_to, [player_1.get_x(), 3*court_SF, 0]), 
            ApplyMethod(player_2.move_to, [player_2.get_x(), 0, 0]), 
            h_tracker.set_value, 2.5, run_time=2, rate_func=linear)
        h_tracker.set_value(0.198)
        self.play(ApplyMethod(ball.move_to, [40*court_SF, -13*court_SF, 0]), 
            ApplyMethod(player_1.move_to, [player_1.get_x(), 0, 0]), 
            ApplyMethod(player_2.move_to, [player_2.get_x(), -10*court_SF, 0]), 
            h_tracker.set_value, 2.5, run_time=2, rate_func=linear)
        h_tracker.set_value(0.198)
        self.play(ApplyMethod(ball.move_to, [-20*court_SF, -17*court_SF, 0]), 
            ApplyMethod(player_1.move_to, [player_1.get_x(), -10*court_SF, 0]), 
            ApplyMethod(player_2.move_to, [player_2.get_x(), -7*court_SF, 0]), 
            h_tracker.set_value, 2, run_time=1.5, rate_func=linear)
        cross.move_to(ball)
        self.play(ShowCreation(cross))
        self.wait(1)
        self.play(FadeOut(ball), FadeOut(shadow), FadeOut(cross), FadeOut(player_1), FadeOut(player_2))
        player_1.next_to(singles_court, LEFT).shift(3*court_SF*UP)
        player_2.next_to(singles_court, RIGHT).shift(10*court_SF*DOWN)
        ball.next_to(player_1, RIGHT)
        h_tracker.set_value(0.2)
        self.play(FadeIn(ball), FadeIn(shadow), FadeIn(player_1), FadeIn(player_2))
        self.wait(1)
        #fade all
        self.play(FadeOut(court), FadeOut(player_1), FadeOut(player_2), FadeOut(ball), FadeOut(shadow))

class E_Serves(Scene):
    CONFIG={
		"camera_config":{"background_color":"#6C935C"}
	}

    # Displays the tennis court.
    def construct(self):
        gameplay_text = Text("Legal and Illegal Serves", color=BLACK)

        doubles_court = Rectangle(height=36*court_SF, width=78*court_SF, fill_color="#3C638E", fill_opacity=1)
        net_line = Line(start=21*court_SF*UP, end=21*court_SF*DOWN, stroke_width=10)
        center_line = Line(start=21*court_SF*LEFT, end=21*court_SF*RIGHT)
        singles_court = Rectangle(height=27*court_SF, width=78*court_SF)
        service_boxes = Rectangle(height=27*court_SF, width=42*court_SF)
        hash_left = Line(start=39*court_SF*LEFT, end=39*court_SF*LEFT+(2/3)*court_SF*RIGHT)
        hash_right = Line(start=39*court_SF*RIGHT, end=39*court_SF*RIGHT+(2/3)*court_SF*LEFT)

        court = VGroup(doubles_court, net_line, center_line, singles_court, service_boxes, hash_left, hash_right)

        player_1 = Circle(radius=1.5*court_SF, fill_color="#D2B4AC", fill_opacity=1, stroke_width=0).next_to(singles_court, LEFT).shift(3*court_SF*DOWN)
        player_2 = Circle(radius=1.5*court_SF, fill_color="#D2B4AC", fill_opacity=1, stroke_width=0).next_to(singles_court, RIGHT).shift(10*court_SF*UP)

        h_tracker = ValueTracker(0)

        ball = Circle(radius=0.5*court_SF, fill_color="#CCFF00", fill_opacity=1, stroke_width=0).next_to(player_1, RIGHT)
        shadow = Circle(radius=0.5*court_SF, fill_color="#ABABAB", fill_opacity=0.5, stroke_width=0)

        bounce_param=4
        second_scale=4

        def bounceBall(shadow):
            if h_tracker.get_value() <= 2:
                shadow.move_to([ball.get_x(), (ball.get_y()/court_SF-(-7*h_tracker.get_value()*(h_tracker.get_value()-2)))*court_SF, 0])
            else:
                shadow.move_to([ball.get_x(), (ball.get_y()/court_SF-(-second_scale*(h_tracker.get_value()-2)*(h_tracker.get_value()-bounce_param)))*court_SF, 0])

        shadow.add_updater(bounceBall)
        h_tracker.set_value(0.2)

        h_tracker_2 = ValueTracker(0)

        ball_2 = Circle(radius=0.5*court_SF, fill_color="#CCFF00", fill_opacity=1, stroke_width=0).next_to(player_1, RIGHT)
        shadow_2 = Circle(radius=0.5*court_SF, fill_color="#ABABAB", fill_opacity=0.5, stroke_width=0)

        def bounceBall_2(shadow):
            if h_tracker_2.get_value() <= 2:
                shadow.move_to([ball_2.get_x(), (ball_2.get_y()/court_SF-(-7*h_tracker_2.get_value()*(h_tracker_2.get_value()-2)))*court_SF, 0])
            else:
                shadow.move_to([ball_2.get_x(), (ball_2.get_y()/court_SF-(-second_scale*(h_tracker_2.get_value()-2)*(h_tracker_2.get_value()-bounce_param)))*court_SF, 0])

        shadow_2.add_updater(bounceBall_2)
        h_tracker_2.set_value(0.2)

        h_tracker_3 = ValueTracker(0)

        ball_3 = Circle(radius=0.5*court_SF, fill_color="#CCFF00", fill_opacity=1, stroke_width=0).next_to(player_1, RIGHT)
        shadow_3 = Circle(radius=0.5*court_SF, fill_color="#ABABAB", fill_opacity=0.5, stroke_width=0)

        def bounceBall_3(shadow):
            if h_tracker_3.get_value() <= 2:
                shadow.move_to([ball_3.get_x(), (ball_3.get_y()/court_SF-(-7*h_tracker_3.get_value()*(h_tracker_3.get_value()-2)))*court_SF, 0])
            else:
                shadow.move_to([ball_3.get_x(), (ball_3.get_y()/court_SF-(-second_scale*(h_tracker_3.get_value()-2)*(h_tracker_3.get_value()-bounce_param)))*court_SF, 0])

        shadow_3.add_updater(bounceBall_3)
        h_tracker_3.set_value(0.2)

        h_tracker_4 = ValueTracker(0)

        ball_4 = Circle(radius=0.5*court_SF, fill_color="#CCFF00", fill_opacity=1, stroke_width=0).next_to(player_1, RIGHT)
        shadow_4 = Circle(radius=0.5*court_SF, fill_color="#ABABAB", fill_opacity=0.5, stroke_width=0)

        def bounceBall_4(shadow):
            if h_tracker_4.get_value() <= 2:
                shadow.move_to([ball_4.get_x(), (ball_4.get_y()/court_SF-(-7*h_tracker_4.get_value()*(h_tracker_4.get_value()-2)))*court_SF, 0])
            else:
                shadow.move_to([ball_4.get_x(), (ball_4.get_y()/court_SF-(-second_scale*(h_tracker_4.get_value()-2)*(h_tracker_4.get_value()-bounce_param)))*court_SF, 0])

        shadow_4.add_updater(bounceBall_4)
        h_tracker_4.set_value(0.2)

        cross_arm_1 = Line(start=0.25*LEFT, end=0.25*RIGHT, color=RED).rotate(PI/4)
        cross_arm_2 = Line(start=0.25*LEFT, end=0.25*RIGHT, color=RED).rotate(-PI/4)

        cross = VGroup(cross_arm_1, cross_arm_2)
        fault_text = Text("Fault", color=RED)

        cross_2 = VGroup(cross_arm_1, cross_arm_2)
        fault_text_2 = Text("Fault", color=RED)

        let_text = Text("Let", color=GRAY)

        in_text = Text("In", color=GREEN)

        self.play(Write(gameplay_text))
        self.wait(1)
        self.play(FadeOut(gameplay_text))
        self.wait(1)
        self.play(FadeIn(court),
            FadeIn(player_1),
            FadeIn(player_2),
            FadeIn(shadow),
            FadeIn(ball))
        self.wait(1)
        self.play(ApplyMethod(ball.move_to, [30*court_SF, 10*court_SF, 0]), 
            h_tracker.set_value, 2, run_time=1.5, rate_func=linear)
        cross.move_to(ball)
        fault_text.next_to(ball, DOWN)
        self.play(ShowCreation(cross), Write(fault_text), FadeIn(shadow_2), FadeIn(ball_2))
        self.play(ApplyMethod(ball_2.move_to, [0, 5*court_SF, 0]), 
            h_tracker_2.set_value, 1.8, run_time=1, rate_func=linear)
        self.play(ApplyMethod(ball_2.move_to, [-3*court_SF, 6*court_SF, 0]), 
            h_tracker_2.set_value, 2, run_time=0.25, rate_func=linear)
        cross_2.move_to(ball_2)
        fault_text_2.next_to(ball_2, LEFT)
        self.play(ShowCreation(cross_2), Write(fault_text_2), FadeIn(shadow_3), FadeIn(ball_3))
        self.play(ApplyMethod(ball_3.move_to, [0, 5*court_SF, 0]), 
            h_tracker_3.set_value, 1.756, run_time=1, rate_func=linear)
        self.play(ApplyMethod(ball_3.move_to, [10*court_SF, 10*court_SF, 0]), 
            h_tracker_3.set_value, 0, run_time=1, rate_func=linear)
        let_text.next_to(ball_3, RIGHT)
        self.play(Write(let_text), FadeIn(shadow_4), FadeIn(ball_4))
        self.play(ApplyMethod(ball_4.move_to, [12*court_SF, 5*court_SF, 0]), 
            h_tracker_4.set_value, 2, run_time=1, rate_func=linear)
        in_text.next_to(ball_4, RIGHT)
        self.play(Write(in_text))
        self.wait(1)
        self.play(FadeOut(court), FadeOut(player_1), FadeOut(player_2), 
            FadeOut(ball), FadeOut(ball_2), FadeOut(ball_3), FadeOut(ball_4), FadeOut(shadow), FadeOut(shadow_2), FadeOut(shadow_3), FadeOut(shadow_4), \
            FadeOut(cross), FadeOut(cross_2), FadeOut(fault_text), FadeOut(fault_text_2), FadeOut(let_text), FadeOut(in_text))

class F_Returns(Scene):
    CONFIG={
		"camera_config":{"background_color":"#6C935C"}
	}

    # Displays the tennis court.
    def construct(self):
        gameplay_text = Text("Legal and Illegal Returns", color=BLACK)

        doubles_court = Rectangle(height=36*court_SF, width=78*court_SF, fill_color="#3C638E", fill_opacity=1)
        net_line = Line(start=21*court_SF*UP, end=21*court_SF*DOWN, stroke_width=10)
        center_line = Line(start=21*court_SF*LEFT, end=21*court_SF*RIGHT)
        singles_court = Rectangle(height=27*court_SF, width=78*court_SF)
        service_boxes = Rectangle(height=27*court_SF, width=42*court_SF)
        hash_left = Line(start=39*court_SF*LEFT, end=39*court_SF*LEFT+(2/3)*court_SF*RIGHT)
        hash_right = Line(start=39*court_SF*RIGHT, end=39*court_SF*RIGHT+(2/3)*court_SF*LEFT)

        court = VGroup(doubles_court, net_line, center_line, singles_court, service_boxes, hash_left, hash_right)

        player_1 = Circle(radius=1.5*court_SF, fill_color="#D2B4AC", fill_opacity=1, stroke_width=0).next_to(singles_court, LEFT)
        player_2 = Circle(radius=1.5*court_SF, fill_color="#D2B4AC", fill_opacity=1, stroke_width=0).next_to(singles_court, RIGHT)

        h_tracker = ValueTracker(0)

        ball = Circle(radius=0.5*court_SF, fill_color="#CCFF00", fill_opacity=1, stroke_width=0).next_to(player_1, RIGHT+DOWN)
        shadow = Circle(radius=0.5*court_SF, fill_color="#ABABAB", fill_opacity=0.5, stroke_width=0)

        bounce_param=4
        second_scale=4

        def bounceBall(shadow):
            if h_tracker.get_value() <= 2:
                shadow.move_to([ball.get_x(), (ball.get_y()/court_SF-(-7*h_tracker.get_value()*(h_tracker.get_value()-2)))*court_SF, 0])
            else:
                shadow.move_to([ball.get_x(), (ball.get_y()/court_SF-(-second_scale*(h_tracker.get_value()-2)*(h_tracker.get_value()-bounce_param)))*court_SF, 0])

        shadow.add_updater(bounceBall)
        h_tracker.set_value(0.2)

        h_tracker_2 = ValueTracker(0)

        ball_2 = Circle(radius=0.5*court_SF, fill_color="#CCFF00", fill_opacity=1, stroke_width=0).next_to(player_1, RIGHT+DOWN)
        shadow_2 = Circle(radius=0.5*court_SF, fill_color="#ABABAB", fill_opacity=0.5, stroke_width=0)

        def bounceBall_2(shadow):
            if h_tracker_2.get_value() <= 2:
                shadow.move_to([ball_2.get_x(), (ball_2.get_y()/court_SF-(-7*h_tracker_2.get_value()*(h_tracker_2.get_value()-2)))*court_SF, 0])
            else:
                shadow.move_to([ball_2.get_x(), (ball_2.get_y()/court_SF-(-second_scale*(h_tracker_2.get_value()-2)*(h_tracker_2.get_value()-bounce_param)))*court_SF, 0])

        shadow_2.add_updater(bounceBall_2)
        h_tracker_2.set_value(0.2)

        h_tracker_3 = ValueTracker(0)

        ball_3 = Circle(radius=0.5*court_SF, fill_color="#CCFF00", fill_opacity=1, stroke_width=0).next_to(player_2, LEFT+DOWN)
        shadow_3 = Circle(radius=0.5*court_SF, fill_color="#ABABAB", fill_opacity=0.5, stroke_width=0)

        def bounceBall_3(shadow):
            if h_tracker_3.get_value() <= 2:
                shadow.move_to([ball_3.get_x(), (ball_3.get_y()/court_SF-(-7*h_tracker_3.get_value()*(h_tracker_3.get_value()-2)))*court_SF, 0])
            else:
                shadow.move_to([ball_3.get_x(), (ball_3.get_y()/court_SF-(-second_scale*(h_tracker_3.get_value()-2)*(h_tracker_3.get_value()-bounce_param)))*court_SF, 0])

        shadow_3.add_updater(bounceBall_3)
        h_tracker_3.set_value(0.2)

        h_tracker_4 = ValueTracker(0)

        ball_4 = Circle(radius=0.5*court_SF, fill_color="#CCFF00", fill_opacity=1, stroke_width=0).next_to(player_1, RIGHT+UP)
        shadow_4 = Circle(radius=0.5*court_SF, fill_color="#ABABAB", fill_opacity=0.5, stroke_width=0)

        def bounceBall_4(shadow):
            if h_tracker_4.get_value() <= 2:
                shadow.move_to([ball_4.get_x(), (ball_4.get_y()/court_SF-(-7*h_tracker_4.get_value()*(h_tracker_4.get_value()-2)))*court_SF, 0])
            else:
                shadow.move_to([ball_4.get_x(), (ball_4.get_y()/court_SF-(-second_scale*(h_tracker_4.get_value()-2)*(h_tracker_4.get_value()-bounce_param)))*court_SF, 0])

        shadow_4.add_updater(bounceBall_4)
        h_tracker_4.set_value(0.2)

        cross_arm_1 = Line(start=0.25*LEFT, end=0.25*RIGHT, color=RED).rotate(PI/4)
        cross_arm_2 = Line(start=0.25*LEFT, end=0.25*RIGHT, color=RED).rotate(-PI/4)

        cross = VGroup(cross_arm_1, cross_arm_2)
        out_text = Text("Out", color=RED)

        cross_2 = VGroup(cross_arm_1, cross_arm_2)
        net_text = Text("In the Net", color=RED)

        double_text = Text("Double Bounce", color=RED)

        in_text = Text("In", color=GREEN)

        self.play(Write(gameplay_text))
        self.wait(1)
        self.play(FadeOut(gameplay_text))
        self.wait(1)
        self.play(FadeIn(court),
            FadeIn(player_1),
            FadeIn(player_2),
            FadeIn(shadow),
            FadeIn(ball))
        self.wait(1)
        self.play(ApplyMethod(ball.move_to, [43*court_SF, 10*court_SF, 0]), 
            h_tracker.set_value, 2, run_time=1.5, rate_func=linear)
        cross.move_to(ball)
        out_text.next_to(ball, UP)
        self.play(ShowCreation(cross), Write(out_text), FadeIn(shadow_2), FadeIn(ball_2))
        self.play(ApplyMethod(ball_2.move_to, [0, -5*court_SF, 0]), 
            h_tracker_2.set_value, 1.8, run_time=1, rate_func=linear)
        self.play(ApplyMethod(ball_2.move_to, [-3*court_SF, -6*court_SF, 0]), 
            h_tracker_2.set_value, 2, run_time=0.25, rate_func=linear)
        cross_2.move_to(ball_2)
        net_text.next_to(ball_2, LEFT)
        self.play(ShowCreation(cross_2), Write(net_text), FadeIn(shadow_3), FadeIn(ball_3))
        bounce_param=3
        second_scale=10
        self.play(ApplyMethod(ball_3.move_to, [-35*court_SF, 10*court_SF, 0]), 
            h_tracker_3.set_value, 3, run_time=2, rate_func=linear)
        double_text.next_to(ball_3, RIGHT)
        self.play(Write(double_text), FadeIn(shadow_4), FadeIn(ball_4))
        self.play(ApplyMethod(ball_4.move_to, [30*court_SF, -13*court_SF, 0]), 
            h_tracker_4.set_value, 2, run_time=1.5, rate_func=linear)
        in_text.next_to(ball_4, UP)
        self.play(Write(in_text))
        self.wait(1)
        self.play(FadeOut(court), FadeOut(player_1), FadeOut(player_2), 
            FadeOut(ball), FadeOut(ball_2), FadeOut(ball_3), FadeOut(ball_4), FadeOut(shadow), FadeOut(shadow_2), FadeOut(shadow_3), FadeOut(shadow_4),
            FadeOut(cross), FadeOut(cross_2), FadeOut(out_text), FadeOut(net_text), FadeOut(double_text), FadeOut(in_text))

class G_Scoring(Scene):
    CONFIG={
		"camera_config":{"background_color":"#6C935C"}
	}

    # Displays the tennis court.
    def construct(self):
        scoring_text = Text("Scoring", color=BLACK)

        match_text = Text("Match", color=BLACK).shift(UP)
        set_text = Text("Set", color=BLACK)
        game_text = Text("Game", color=BLACK).shift(DOWN)

        one_server_text = Text("One Server", color=BLACK).shift(2.5*UP)
        win_by_4_text = Text("Win at least 4 points and by 2 points", color=BLACK).shift(1.5*UP)
        point_text = Text("Points", color=BLACK).shift(0.5*UP+LEFT)
        zero_text = Text("0", color=BLACK).shift(0.5*UP+RIGHT)
        one_text = Text("1", color=BLACK).shift(0.5*UP+2*RIGHT)
        two_text = Text("2", color=BLACK).shift(0.5*UP+3*RIGHT)
        three_text = Text("3", color=BLACK).shift(0.5*UP+4*RIGHT)
        score_text = Text("Score", color=BLACK).shift(LEFT)
        love_text = Text("Love", color=BLACK).shift(RIGHT)
        text_15 = Text("15", color=BLACK).shift(2*RIGHT)
        text_30 = Text("30", color=BLACK).shift(3*RIGHT)
        text_40 = Text("40", color=BLACK).shift(4*RIGHT)

        score_group = VGroup(point_text, zero_text, one_text, two_text, three_text, score_text, love_text, text_15, text_30, text_40).move_to(0.25*UP)

        deuce_text = Text("40-40 is called Deuce", color=BLACK).shift(DOWN)

        alt_text = Text("Alternate Servers", color=BLACK).shift(2.5*UP)
        win_by_6_text = Text("Win at least 6 games and by 2 games", color=BLACK).shift(1.5*UP)
        five_text = Text("5-5 First to 7", color=BLACK).shift(0.5*UP)
        six_text = Text("6-6 Play a tiebreaker", color=BLACK).shift(0.5*DOWN)
        tie_text = Text("Tiebreaker: Win at least 7 points and by 2 points", color=BLACK).shift(1.5*DOWN)

        best_of_3 = Text("Best of 3 sets", color=BLACK).shift(2.5*UP)
        or_text = Text("or", color=BLACK).shift(1.5*UP)
        best_of_5 = Text("Best of 5 sets", color=BLACK).shift(0.5*UP)

        self.play(Write(scoring_text))
        self.wait(1)
        self.play(FadeOut(scoring_text))
        self.wait(1)
        self.play(Write(match_text))
        self.wait(0.5)
        self.play(TransformFromCopy(match_text, set_text))
        self.wait(0.5)
        self.play(TransformFromCopy(set_text, game_text))
        self.wait(1)
        self.play(FadeOut(match_text), FadeOut(set_text), ApplyMethod(game_text.move_to, 3.5*UP))
        self.wait(1)
        self.play(Write(one_server_text))
        self.wait(1)
        self.play(Write(win_by_4_text))
        self.wait(1)
        self.play(Write(point_text), Write(score_text))
        self.wait(0.5)
        self.play(Write(zero_text), Write(love_text))
        self.wait(0.5)
        self.play(Write(one_text), Write(text_15))
        self.wait(0.5)
        self.play(Write(two_text), Write(text_30))
        self.wait(0.5)
        self.play(Write(three_text), Write(text_40))
        self.wait(1)
        self.play(Write(deuce_text))
        set_text.move_to(3.5*UP)
        self.wait(1)
        self.play(ReplacementTransform(game_text, set_text), FadeOut(one_server_text), FadeOut(win_by_4_text), FadeOut(score_group), FadeOut(deuce_text))
        self.wait(1)
        self.play(Write(alt_text))
        self.wait(1)
        self.play(Write(win_by_6_text))
        self.wait(1)
        self.play(Write(five_text))
        self.wait(1)
        self.play(Write(six_text))
        self.wait(1)
        self.play(Write(tie_text))
        self.wait(1)
        match_text.move_to(3.5*UP)
        self.play(ReplacementTransform(set_text, match_text), FadeOut(alt_text), FadeOut(win_by_6_text), FadeOut(five_text), FadeOut(six_text), FadeOut(tie_text))
        self.wait(1)
        self.play(Write(best_of_3), Write(or_text), Write(best_of_5))
        self.wait(1)
        self.play(FadeOut(match_text), FadeOut(best_of_3), FadeOut(or_text), FadeOut(best_of_5))

class H_Shots(Scene):
    CONFIG={
		"camera_config":{"background_color":"#6C935C"}
	}

    def construct(self):
        shots_text = Text("Shots", color=BLACK)

        serve_text = Text("Serves", color=BLACK).move_to(3*UP)
        ground_text = Text("Groundstrokes", color=BLACK).move_to(2*UP)
        fore_text = Text("Forehand", color=BLACK).move_to(2*LEFT+1*UP)
        back_text = Text("Backhand", color=BLACK).move_to(2*RIGHT+1*UP)
        volley_text = Text("Volleys", color=BLACK)
        over_text = Text("Overhead Smashes", color=BLACK).move_to(DOWN)

        line_1 = Line(start=1.75*UP, end=2*LEFT+1.25*UP)
        line_2 = Line(start=1.75*UP, end=2*RIGHT+1.25*UP)

        shot_group = VGroup(serve_text, ground_text, fore_text, back_text, volley_text, over_text, line_1, line_2).move_to(ORIGIN)

        self.play(Write(shots_text))
        self.wait(1)
        self.play(FadeOut(shots_text))
        self.wait(1)
        self.play(Write(serve_text), Write(ground_text), Write(fore_text), Write(back_text), Write(volley_text), Write(over_text), ShowCreation(line_1), ShowCreation(line_2))
        self.wait(1)
        self.play(FadeOut(serve_text), FadeOut(ground_text), FadeOut(fore_text), FadeOut(back_text), FadeOut(volley_text), FadeOut(over_text), FadeOut(line_1), FadeOut(line_2))