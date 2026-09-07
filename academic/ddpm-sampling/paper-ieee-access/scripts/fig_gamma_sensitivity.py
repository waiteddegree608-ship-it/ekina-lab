"""γ sensitivity for ρ=100 class-frequency-adaptive CFG.

Data source (read-only): opencode-deliverables/task_798bbf2783/
No invented numbers.
"""
from pathlib import Path
import csv
import json
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties
from matplotlib.lines import Line2D
import numpy as np

INK = "#1a1814"
SLATE = "#5c564c"
DOT = "#8a8376"

# Colorblind-friendly blue / orange (Okabe-Ito inspired, not red-green).
BLUE = "#0072B2"
ORANGE = "#D55E00"

DATA_DELIVERABLE = Path(
    r"E:\workspace\Ekina\AgentHome\workspace\opencode-deliverables\task_798bbf2783"
)

GAMMAS = np.array([0.15, 0.30, 0.50])


def load_baseline_csv(path: Path):
    """Return tail/all FID for the cfg1.5 eta1.0 row."""
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if float(row["cfg"]) == 1.5 and float(row["eta"]) == 1.0:
                if row["bucket"] == "tail":
                    tail = float(row["FID"])
                elif row["bucket"] == "all":
                    all_ = float(row["FID"])
    return {"tail": tail, "all": all_}


def load_adaptive_summary(path: Path):
    """Read the master summary.json and pivot by (omega0, gamma)."""
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    grid = {}
    for entry in data["results"]:
        w = float(entry["omega0"])
        g = float(entry["gamma"])
        grid[(w, g)] = {
            "head": float(entry["head"]),
            "mid": float(entry["mid"]),
            "tail": float(entry["tail"]),
            "all": float(entry["all"]),
        }
    return grid


def configure_mpl():
    mpl.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "SimSun", "Times", "Nimbus Roman", "DejaVu Serif"],
        "mathtext.fontset": "stix",
        "font.size": 8,
        "axes.labelsize": 8,
        "axes.titlesize": 8.5,
        "axes.labelcolor": INK,
        "axes.edgecolor": INK,
        "axes.linewidth": 0.55,
        "xtick.color": INK,
        "ytick.color": INK,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "figure.dpi": 200,
        "savefig.dpi": 360,
        "pdf.fonttype": 42,
        "legend.frameon": False,
        "legend.fontsize": 7,
        "axes.spines.top": False,
        "axes.spines.right": False,
    })


def plot_panel(ax, grid, baseline, bucket: str, ylabel: str, letter: str):
    for omega0, color, marker in [(1.5, ORANGE, "s"), (1.0, BLUE, "o")]:
        vals = [grid[(omega0, g)][bucket] for g in GAMMAS]
        ax.plot(
            GAMMAS, vals, marker=marker, ms=5, lw=1.5, color=color,
            markerfacecolor="white", markeredgewidth=1.1, zorder=3,
            label=rf"$\omega_0={omega0:g}$",
        )
        # annotate numeric values
        for g, v in zip(GAMMAS, vals):
            ax.annotate(
                f"{v:.1f}", xy=(g, v), xytext=(0, 7),
                textcoords="offset points", ha="center", va="bottom",
                fontsize=6.2, color=color,
            )

    ax.axhline(baseline[bucket], color=DOT, lw=0.9, ls="--", zorder=1, label="global baseline")
    ax.text(
        GAMMAS[-1] + 0.02, baseline[bucket], f" {baseline[bucket]:.1f}",
        va="center", ha="left", fontsize=6.5, color=DOT,
    )

    ax.set_xscale("linear")
    ax.set_xticks(GAMMAS, [f"{g:g}" for g in GAMMAS])
    ax.set_xlabel(r"Adaptive exponent $\gamma$")
    ax.set_ylabel(ylabel)
    ax.yaxis.grid(True, ls=":", lw=0.4, color="#d8d2c4")
    ax.set_axisbelow(True)
    ax.set_title(rf"{letter}   {bucket.capitalize()} FID", loc="left", fontsize=8, pad=5, color=INK)
    ax.legend(loc="best", handletextpad=0.35, borderaxespad=0.2)


def make_figure(out_pdf: Path, out_png: Path | None = None):
    configure_mpl()
    baseline = load_baseline_csv(DATA_DELIVERABLE / "gate_rho100_200k.csv")
    grid = load_adaptive_summary(DATA_DELIVERABLE / "summary.json")

    fig, axes = plt.subplots(1, 2, figsize=(7.05, 2.75), constrained_layout=True)
    plot_panel(axes[0], grid, baseline, "tail", "FID ↓", "a")
    plot_panel(axes[1], grid, baseline, "all", "FID ↓", "b")

    fig.text(
        0.5, -0.02,
        r"Class-frequency-adaptive CFG: $\omega_c = \omega_0 \exp(\gamma \cdot \rho_c)$",
        ha="center", va="top", fontsize=7, color=SLATE,
    )
    chinese_font = FontProperties(family="SimSun", size=7)
    fig.text(
        0.5, -0.06,
        "图注：温和提权有效，过大则崩坏。",
        ha="center", va="top", fontproperties=chinese_font, color=SLATE,
    )

    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_pdf, bbox_inches="tight", pad_inches=0.06)
    if out_png:
        out_png.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_png, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return grid, baseline


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    grid, baseline = make_figure(
        root / "figures" / "fig_gamma_sensitivity.pdf",
        root / "figures" / "fig_gamma_sensitivity.png",
    )
    print("wrote fig_gamma_sensitivity")
    print(f"baseline  tail={baseline['tail']:.3f} all={baseline['all']:.3f}")
    for omega0 in (1.0, 1.5):
        for g in GAMMAS:
            row = grid[(omega0, g)]
            print(f"omega0={omega0:g} gamma={g:g}  "
                  f"head={row['head']:.3f} mid={row['mid']:.3f} "
                  f"tail={row['tail']:.3f} all={row['all']:.3f}")
