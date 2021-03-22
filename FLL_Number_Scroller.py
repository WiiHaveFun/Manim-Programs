from manimlib.imports import *

class A_Scroller(Scene):
  CONFIG={
    "camera_config":{"background_color":"#FFFFFF"}
  }
  def construct(self):
    text_1 = Text("3493", color="#DC3832")
    text_2 = Text("3646", color="#221F20").shift(2*RIGHT)
    text_3 = Text("4182", color="#2566AD").shift(4*RIGHT)
    text_4 = Text("16417", color="#DC3832").shift(6*RIGHT)
    text_5 = Text("18209", color="#221F20").shift(8*RIGHT)
    text_6 = Text("18569", color="#2566AD").shift(10*RIGHT)
    text_7 = Text("22229", color="#DC3832").shift(12*RIGHT)
    text_8 = Text("24928", color="#221F20").shift(14*RIGHT)
    text_9 = Text("26827", color="#2566AD").shift(16*RIGHT)
    text_10 = Text("29779", color="#DC3832").shift(18*RIGHT)
    line_1 = VGroup(text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9, text_10)

    text_11 = Text("30898", color="#221F20").shift(DOWN)
    text_12 = Text("31568", color="#2566AD").shift(2*RIGHT+DOWN)
    text_13 = Text("32075", color="#DC3832").shift(4*RIGHT+DOWN)
    text_14 = Text("32777", color="#221F20").shift(6*RIGHT+DOWN)
    text_15 = Text("33959", color="#2566AD").shift(8*RIGHT+DOWN)
    text_16 = Text("35450", color="#DC3832").shift(10*RIGHT+DOWN)
    text_17 = Text("37680", color="#221F20").shift(12*RIGHT+DOWN)
    text_18 = Text("38268", color="#2566AD").shift(14*RIGHT+DOWN)
    text_19 = Text("38269", color="#DC3832").shift(16*RIGHT+DOWN)
    text_20 = Text("38849", color="#221F20").shift(18*RIGHT+DOWN)
    line_2 = VGroup(text_11, text_12, text_13, text_14, text_15, text_16, text_17, text_18, text_19, text_20)

    text_21 = Text("44204", color="#2566AD").shift(2*DOWN)
    text_22 = Text("44798", color="#DC3832").shift(2*RIGHT+2*DOWN)
    text_23 = Text("44814", color="#221F20").shift(4*RIGHT+2*DOWN)
    text_24 = Text("45084", color="#2566AD").shift(6*RIGHT+2*DOWN)
    text_25 = Text("45252", color="#DC3832").shift(8*RIGHT+2*DOWN)
    text_26 = Text("46041", color="#221F20").shift(10*RIGHT+2*DOWN)
    text_27 = Text("46380", color="#2566AD").shift(12*RIGHT+2*DOWN)
    text_28 = Text("47891", color="#DC3832").shift(14*RIGHT+2*DOWN)
    text_29 = Text("51126", color="#221F20").shift(16*RIGHT+2*DOWN)
    text_30 = Text("51599", color="#2566AD").shift(18*RIGHT+2*DOWN)
    line_3 = VGroup(text_21, text_22, text_23, text_24, text_25, text_26, text_27, text_28, text_29, text_30)

    all_numbers_1 = VGroup(line_1, line_2, line_3)
    all_numbers_2 = all_numbers_1.copy()
    all_numbers_1.move_to(2*UP).shift(20*RIGHT)
    all_numbers_2.move_to(2*UP)
    all_numbers = VGroup(all_numbers_1, all_numbers_2).to_edge(LEFT)

    self.add(all_numbers)
    self.play(ApplyMethod(all_numbers.to_edge, RIGHT), run_time=10, rate_func=linear)















