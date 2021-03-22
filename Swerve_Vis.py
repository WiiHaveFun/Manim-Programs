from manimlib.imports import *
import math

class A_Swerve(Scene):
  def construct(self):
    chassis = Square(side_length=2, stroke_width=0, fill_color=GRAY, fill_opacity=1).shift(2*RIGHT)

    fr = Dot().shift(UP+3*RIGHT)
    fl = Dot().shift(UP+RIGHT)
    rl = Dot().shift(DOWN+RIGHT)
    rr = Dot().shift(DOWN+3*RIGHT)

    x_tracker = ValueTracker(0)
    y_tracker = ValueTracker(0.001)
    rot_tracker = ValueTracker(0)

    def updateFRArrow(arrow):
      vector = calculateVectors(y_tracker.get_value(), x_tracker.get_value(), rot_tracker.get_value(), 0)[0]
      arrow.put_start_and_end_on(UP+3*RIGHT, np.array(UP+3*RIGHT+vector[0]*np.cos(np.radians(vector[1]))*UP+(vector[0]*np.sin(np.radians(vector[1]))*RIGHT)))
    
    def updateFLArrow(arrow):
      vector = calculateVectors(y_tracker.get_value(), x_tracker.get_value(), rot_tracker.get_value(), 0)[1]
      arrow.put_start_and_end_on(UP+RIGHT, np.array(UP+RIGHT+vector[0]*np.cos(np.radians(vector[1]))*UP+(vector[0]*np.sin(np.radians(vector[1]))*RIGHT)))

    def updateRLArrow(arrow):
      vector = calculateVectors(y_tracker.get_value(), x_tracker.get_value(), rot_tracker.get_value(), 0)[2]
      arrow.put_start_and_end_on(DOWN+RIGHT, np.array(DOWN+RIGHT+vector[0]*np.cos(np.radians(vector[1]))*UP+(vector[0]*np.sin(np.radians(vector[1]))*RIGHT)))

    def updateRRArrow(arrow):
      vector = calculateVectors(y_tracker.get_value(), x_tracker.get_value(), rot_tracker.get_value(), 0)[3]
      arrow.put_start_and_end_on(DOWN+3*RIGHT, np.array(DOWN+3*RIGHT+vector[0]*np.cos(np.radians(vector[1]))*UP+(vector[0]*np.sin(np.radians(vector[1]))*RIGHT)))

    fr_vector = Arrow()
    fr_vector.add_updater(updateFRArrow)
    fl_vector = Arrow()
    fl_vector.add_updater(updateFLArrow)
    rl_vector = Arrow()
    rl_vector.add_updater(updateRLArrow)
    rr_vector = Arrow()
    rr_vector.add_updater(updateRRArrow)

    left_pad = Circle(radius=0.5).move_to(3*LEFT)
    left_stick = Circle(radius=0.25, fill_color=WHITE, fill_opacity=1).move_to(3*LEFT)
    left_stick.add_updater(lambda x: x.move_to(3*LEFT+0.4*x_tracker.get_value()*RIGHT+0.4*y_tracker.get_value()*UP))

    right_pad = Circle(radius=0.5).move_to(1*LEFT)
    right_stick = Circle(radius=0.25, fill_color=WHITE, fill_opacity=1).move_to(1*LEFT)
    right_stick.add_updater(lambda x: x.move_to(1*LEFT+0.4*rot_tracker.get_value()*RIGHT))

    self.play(FadeIn(chassis), ShowCreation(fr), ShowCreation(fl), ShowCreation(rl), ShowCreation(rr))
    self.play(ShowCreation(left_pad), ShowCreation(left_stick), ShowCreation(right_pad), ShowCreation(right_stick))
    self.play(ShowCreation(fr_vector), ShowCreation(fl_vector), ShowCreation(rl_vector), ShowCreation(rr_vector))
    self.wait(1)
    # Full forward
    self.play(ApplyMethod(y_tracker.set_value, 1, run_time=1, rate_func=smooth))
    # Semi circle
    self.play(ApplyMethod(x_tracker.set_value, -1, run_time=2, rate_func=there_and_back), 
              ApplyMethod(y_tracker.set_value, -1, run_time=2, rate_func=smooth))
    # Semi circle
    self.play(ApplyMethod(x_tracker.set_value, 1, run_time=2, rate_func=there_and_back), 
              ApplyMethod(y_tracker.set_value, 1, run_time=2, rate_func=smooth))
    # Neutral
    self.play(ApplyMethod(y_tracker.set_value, 0.001, run_time=1, rate_func=smooth))
    # Pure rotation
    self.play(ApplyMethod(rot_tracker.set_value, -1, run_time=1, rate_func=smooth))
    self.play(ApplyMethod(rot_tracker.set_value, 1, run_time=2, rate_func=smooth))
    self.play(ApplyMethod(rot_tracker.set_value, 0, run_time=1, rate_func=smooth))
    # Full forward plus rotation
    self.play(ApplyMethod(y_tracker.set_value, 1, run_time=1, rate_func=smooth))
    self.play(ApplyMethod(rot_tracker.set_value, -1, run_time=1, rate_func=smooth))
    self.play(ApplyMethod(rot_tracker.set_value, 1, run_time=2, rate_func=smooth))
    self.play(ApplyMethod(rot_tracker.set_value, 0, run_time=1, rate_func=smooth))
    # Neutral
    self.play(ApplyMethod(y_tracker.set_value, 0.001, run_time=1, rate_func=smooth))
    # Move FR
    self.wait(1)
    self.play(ApplyMethod(rot_tracker.set_value, -1, run_time=1, rate_func=smooth))
    fr_vector.remove_updater(updateFRArrow)
    self.play(ApplyMethod(fr.shift, 0.3*DOWN), ApplyMethod(fr_vector.shift, 0.3*DOWN))
    self.play(ApplyMethod(fr.set_color, RED), ApplyMethod(fr_vector.set_color, RED))
    self.wait(1)
    self.play(ApplyMethod(fr.set_color, WHITE), ApplyMethod(fr_vector.set_color, WHITE))
    self.play(ApplyMethod(fr.shift, 0.3*UP), ApplyMethod(fr_vector.shift, 0.3*UP))
    fr_vector.add_updater(updateFRArrow)
    # Neutral
    self.play(ApplyMethod(rot_tracker.set_value, 0, run_time=1, rate_func=smooth))
    # Fade out
    self.wait(1)
    self.play(FadeOut(fr), FadeOut(fl), FadeOut(rl), FadeOut(rr), FadeOut(chassis),
              FadeOut(left_pad), FadeOut(left_stick), FadeOut(right_pad), FadeOut(right_stick),
              FadeOut(fr_vector), FadeOut(fl_vector), FadeOut(rl_vector), FadeOut(rr_vector))

wheelBase = 10
trackWidth = 10

def calculateVectors(FWD, STR, RCW, gyroAngle):

  # Makes the command field-centric.
  temp = FWD * math.cos(gyroAngle) + STR * math.sin(gyroAngle)
  STR = -FWD * math.sin(gyroAngle) + STR * math.cos(gyroAngle)
  FWD = temp

  # Uses inverse kinematics to derive wheel speeds and angles.
  R = math.hypot(wheelBase, trackWidth)

  A = STR - RCW * (wheelBase / R)
  B = STR + RCW * (wheelBase / R)
  C = FWD - RCW * (trackWidth / R)
  D = FWD + RCW * (trackWidth / R)

  fr_ws = math.hypot(B, C)
  fl_ws = math.hypot(B, D)
  bl_ws = math.hypot(A, D)
  br_ws = math.hypot(A, C)

  fr_wa = math.atan2(B, C) * 180 / math.pi
  fl_wa = math.atan2(B, D) * 180 / math.pi
  bl_wa = math.atan2(A, D) * 180 / math.pi
  br_wa = math.atan2(A, C) * 180 / math.pi

  # Normalize wheel speeds.
  max = fr_ws
  if fl_ws > max:
    max = fl_ws
  if bl_ws > max:
    max = bl_ws
  if br_ws > max:
    max = br_ws

  if max > 1:
    fr_ws /= max
    fl_ws /= max
    bl_ws /= max
    br_ws /= max

  return np.array([[fr_ws, fr_wa], 
    [fl_ws, fl_wa], 
    [bl_ws, bl_wa], 
    [br_ws, br_wa]])


