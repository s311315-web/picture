
from manim import *
import numpy as np

class AMGMProof(Scene):
    def construct(self):
        # 1. Setup Parameters (a=4, b=1)
        a_val, b_val = 4, 1
        r = (a_val + b_val) / 2
        
        # Draw Semicircle and Diameter
        diameter = Line(LEFT * r, RIGHT * r, color=WHITE)
        semicircle = Arc(radius=r, start_angle=0, angle=PI, color=YELLOW)
        
        # 2. Geometric points
        split_x = -r + a_val
        split_point = [split_x, 0, 0]
        
        # Height of the altitude (GM)
        h_val = np.sqrt(a_val * b_val)
        top_curr = [split_x, h_val, 0]
        
        # Triangle and Altitude
        triangle = Polygon(
            diameter.get_start(), 
            top_curr,             
            diameter.get_end(),   
            color=BLUE
        )
        altitude = Line(split_point, top_curr, color=GREEN)
        
        # Labels using only MathTex
        gm_label = MathTex(r"\sqrt{ab}", color=GREEN).next_to(altitude, RIGHT, buff=0.1)
        am_radius = Line(ORIGIN, UP * r, color=RED)
        am_label = MathTex(r"\frac{a+b}{2}", color=RED).next_to(am_radius, LEFT, buff=0.1)

        # --- Animation Sequence ---
        
        # Step 1: Create Circle and Triangle
        self.play(Create(diameter), Create(semicircle))
        self.play(Create(triangle))
        self.play(Create(altitude), Write(gm_label))
        self.wait(1)

        # Step 2: Show the Radius (Arithmetic Mean)
        self.play(Create(am_radius), Write(am_label))
        self.wait(1)

        # Step 3: Transform to Isosceles (a=b)
        new_top = [0, r, 0]
        new_triangle = Polygon(
            diameter.get_start(),
            new_top,
            diameter.get_end(),
            color=BLUE
        )
        new_altitude = Line(ORIGIN, new_top, color=GREEN)

        self.play(
            Transform(triangle, new_triangle),
            Transform(altitude, new_altitude),
            gm_label.animate.next_to(new_top, RIGHT),
            run_time=2
        )
        
        # Step 4: Final Inequality
        final_formula = MathTex(r"\frac{a+b}{2} \ge \sqrt{ab}", color=YELLOW).to_edge(UP)
        self.play(Write(final_formula))
        self.play(Indicate(final_formula))
        self.wait(2)
# Entry point
if __name__ == "__main__":
    import os
    os.system(f"manim -pql {__file__} QuadraticGraph")