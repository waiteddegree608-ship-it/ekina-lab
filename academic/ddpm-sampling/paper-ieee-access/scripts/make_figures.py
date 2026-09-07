"""Editorial figures for IEEE Access submission. No invented numbers."""
from pathlib import Path
from fig_gamma_sensitivity import make_figure as gamma_sensitivity

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)


def main():
    gamma_sensitivity(FIG / "fig_gamma_sensitivity.pdf", FIG / "fig_gamma_sensitivity.png")
    print("wrote gamma sensitivity figure")


if __name__ == "__main__":
    main()
