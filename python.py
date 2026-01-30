from manim import *

class QuadraticGraph(Scene):
    def construct(self):
        # 創建坐標軸
        axes = Axes(
            x_range=[-5, 5, 1],  # x 軸範圍
            y_range=[-5, 25, 5], # y 軸範圍
            axis_config={"include_numbers": True}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # 定義二次函數
        quadratic = axes.plot(lambda x: x**2, color=BLUE, x_range=[-5, 5])

        # 添加標籤
        quadratic_label = axes.get_graph_label(quadratic, label="x^2")

        # 動畫效果：繪製函數
        self.play(Create(axes), Write(labels))
        self.play(Create(quadratic), Write(quadratic_label))
        self.wait(2)

        # 動畫效果：改變函數形狀
        new_quadratic = axes.plot(lambda x: 0.5 * x**2, color=GREEN, x_range=[-5, 5])
        new_label = axes.get_graph_label(new_quadratic, label="0.5x^2")

        self.play(Transform(quadratic, new_quadratic), Transform(quadratic_label, new_label))
        self.wait(2)

# Entry point
if __name__ == "__main__":
    import os
    os.system(f"manim -pql {__file__} QuadraticGraph")