from __future__ import annotations

from collections.abc import Sequence

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class ChartCanvas(FigureCanvasQTAgg):
    def __init__(self, minimum_height: int = 255) -> None:
        self.figure = Figure(figsize=(5, 3), tight_layout=True, facecolor="#111a2c")
        super().__init__(self.figure)
        self.setMinimumHeight(minimum_height)
        self.axes = self.figure.add_subplot(111)
        self._prepare_axes()

    def _prepare_axes(self) -> None:
        self.axes.clear()
        self.axes.set_facecolor("#111a2c")
        self.axes.tick_params(colors="#aebbd0", labelsize=8)
        for spine in self.axes.spines.values():
            spine.set_color("#334563")
        self.axes.grid(alpha=0.2, color="#9baac2")

    def empty(self, message: str) -> None:
        self._prepare_axes()
        self.axes.text(0.5, 0.5, message, ha="center", va="center", color="#9baac2", transform=self.axes.transAxes)
        self.axes.set_xticks([])
        self.axes.set_yticks([])
        self.draw_idle()

    def draw_pie(self, labels: Sequence[str], values: Sequence[float], title: str) -> None:
        self._prepare_axes()
        if not values or sum(values) <= 0:
            self.empty(title)
            return
        palette = ["#c2384f", "#dc6b35", "#d6a934", "#3989c6", "#5c708d"]
        self.axes.pie(
            values,
            labels=labels,
            autopct=lambda value: f"{value:.0f}%" if value >= 4 else "",
            startangle=90,
            colors=palette[: len(values)],
            textprops={"color": "#dce6f5", "fontsize": 8},
            wedgeprops={"width": 0.55, "edgecolor": "#111a2c"},
        )
        self.axes.set_title(title, color="#f5f8ff", fontsize=11, fontweight="bold")
        self.draw_idle()

    def draw_bar(self, labels: Sequence[str], values: Sequence[float], title: str) -> None:
        self._prepare_axes()
        if not labels:
            self.empty(title)
            return
        positions = list(range(len(labels)))
        self.axes.barh(positions, values, color="#2f84c6")
        self.axes.set_yticks(positions, labels=[label[:30] for label in labels])
        self.axes.invert_yaxis()
        self.axes.set_title(title, color="#f5f8ff", fontsize=11, fontweight="bold")
        self.axes.set_xlabel("Count", color="#aebbd0")
        self.draw_idle()

    def draw_line(self, labels: Sequence[str], values: Sequence[float], title: str, unit: str = "") -> None:
        self._prepare_axes()
        if not values:
            self.empty(title)
            return
        x = list(range(1, len(values) + 1))
        self.axes.plot(x, values, marker="o", linewidth=2, color="#4da3ff")
        if labels and len(labels) <= 12:
            self.axes.set_xticks(x, labels=labels, rotation=30 if len(labels) > 5 else 0)
        else:
            self.axes.set_xlabel("Sample", color="#aebbd0")
        self.axes.set_ylabel(unit, color="#aebbd0")
        self.axes.set_title(title, color="#f5f8ff", fontsize=11, fontweight="bold")
        self.draw_idle()
