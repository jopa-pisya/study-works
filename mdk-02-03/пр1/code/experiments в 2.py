# Серии компьютерного эксперимента с дискретной логистической моделью
# Практическая работа 1 — вариант 2: a = 1.8, K = 120 000, N0 = 10 000, T = 36
# Серии: 1 — коэффициент прироста a, 2 — начальное состояние N0, 3 — ёмкость рынка K.
# Меняется всегда ровно один параметр, остальные остаются базовыми.
import numpy as np
import matplotlib.pyplot as plt

A, K, N0, T = 1.8, 120_000.0, 10_000.0, 36
SERIES = {
    "a":  [1.2, 1.5, 1.8, 2.1, 2.5, 2.7, 2.9],
    "N0": [500, 10_000, 40_000, 90_000, 130_000],
    "K":  [60_000, 120_000, 200_000],
}


def model(a, K, N0, T):
    """Та же рекуррентная формула, что в Excel и в population.py."""
    N = np.zeros(T + 1)
    N[0] = N0
    for t in range(T):
        N[t + 1] = N[t] + a * N[t] * (1.0 - N[t] / K)
    return N


def observe(a, K, N0, T):
    N = model(a, K, N0, T)
    hit = np.nonzero(N >= 0.95 * K)[0]
    t_star = int(hit[0]) if hit.size else None
    s = np.sign(N - K)
    crossings = int(np.sum(s[1:] * s[:-1] < 0))
    tail = N[-20:]
    ev, od = tail[0::2], tail[1::2]
    p1, p2 = float(np.mean(ev)), float(np.mean(od))
    dev = max(float(np.max(np.abs(ev - p1))), float(np.max(np.abs(od - p2))))
    swing = abs(p2 - p1)
    two_cycle = swing > 0.005 * K and dev < 0.02 * swing
    n_vals = len(set(int(round(x / (0.02 * K))) for x in tail))
    lo, hi = float(np.min(tail)), float(np.max(tail))
    amp = float(np.max(np.abs(tail - K)) / K * 100)

    if N0 > K:
        reg = "старт выше ёмкости (N0 > K)"
        char = ("N0 = %.0f > K: первый шаг уменьшает N до %.0f (убывающая ветвь), "
                "затем перелётов через K: %d; установившихся значений ≈ %d, "
                "диапазон %.0f…%.0f (размах %.1f%% K)"
                % (N0, float(N[1]), crossings, n_vals, lo, hi, (hi - lo) / K * 100))
    elif a <= 1:
        reg = "монотонный выход"
        char = "кривая прилипает к уровню K снизу, перелётов через K нет"
    elif a <= 2:
        idx = np.nonzero(s[1:] * s[:-1] < 0)[0]
        first = abs(float(N[idx[0] + 1]) - K) / K * 100 if idx.size else 0.0
        reg = "затухающие колебания через K"
        char = ("перелётов через K: %d; амплитуда затухает: первый перелёт ±%.1f%% K, "
                "к концу горизонта %.1f%% K" % (crossings, first, amp))
    elif a <= 2.6:
        reg = "устойчивый цикл"
        if two_cycle:
            char = ("два чередующихся значения ≈ %.0f и ≈ %.0f, размах ≈ %.1f%% K; "
                    "перелётов через K: %d, амплитуда не затухает"
                    % (p1, p2, swing / K * 100, crossings))
        else:
            char = ("колебания без затухания: установившихся значений ≈ %d, "
                    "размах ≈ %.1f%% K (диапазон %.0f…%.0f)"
                    % (n_vals, (hi - lo) / K * 100, lo, hi))
    else:
        reg = "нерегулярное поведение"
        char = ("значения заполняют диапазон %.0f…%.0f (%.0f…%.0f%% K), "
                "периодичности нет, размах ≈ %.1f%% K"
                % (lo, hi, lo / K * 100, hi / K * 100, (hi - lo) / K * 100))
    return t_star, reg, char


def run():
    num = 0
    print("№\tСерия\ta\tK\tN0\tt*\tРежим\tНаблюдение")
    for key, values in SERIES.items():
        for val in values:
            a, Kk, Nn = A, K, N0
            if key == "a":
                a = float(val)
            elif key == "K":
                Kk = float(val)
            else:
                Nn = float(val)
            num += 1
            t_star, reg, char = observe(a, Kk, Nn, T)
            print("%d\t%s\t%g\t%.0f\t%.0f\t%s\t%s\t%s"
                  % (num, key, a, Kk, Nn, "-" if t_star is None else t_star, reg, char))


def plot_series(key, title, fname):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for val in SERIES[key]:
        a, Kk, Nn = A, K, N0
        if key == "a":
            a = float(val); lbl = "a = %g" % val
        elif key == "K":
            Kk = float(val); lbl = "K = %.0f" % val
        else:
            Nn = float(val); lbl = "N0 = %.0f" % val
        ax.plot(range(T + 1), model(a, Kk, Nn, T), lw=1.4, label=lbl)
    ax.axhline(K, color="gray", ls="--", lw=0.9, label="уровень K")
    ax.set_title(title)
    ax.set_xlabel("Месяц t")
    ax.set_ylabel("N(t)")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(fname, dpi=130)


if __name__ == "__main__":
    run()
    plot_series("a", "Серия 1 — влияние коэффициента прироста a (вариант 2)", "series1_v2.png")
    plot_series("N0", "Серия 2 — влияние начального состояния N0 (вариант 2)", "series2_v2.png")
    plot_series("K", "Серия 3 — влияние ёмкости рынка K (вариант 2)", "series3_v2.png")
    print("\nСохранены рисунки: series1_v2.png, series2_v2.png, series3_v2.png")
