# Men vs Women FIFA World Cup Goal Comparison

This project analyzes the **total goals scored per match** in FIFA World Cup tournaments (post-2002) for both men’s and women’s matches, using statistical tests and visualization.

---

## Files Included

- `men_results.csv`: Historical match results from men's international matches.
- `women_results.csv`: Historical match results from women's international matches.
- `men_vs_women_soccer_score.py`: Python script containing all the code for data processing, visualization, and hypothesis testing.
- `README.md`: You're reading it! 😉

---

## Objective

To determine whether **women's FIFA World Cup matches** have significantly more total goals than **men's**, based on data since 2002.

---

## Dependencies

Make sure the following Python libraries are installed:

```bash
pip install pandas matplotlib seaborn scipy pingouin
```

---

## How to Run

1. Place `men_results.csv` and `women_results.csv` in the same directory as the script.
2. Run the script using Python:

```bash
python men_vs_women_soccer_score.py
```

---

## Statistical Analysis

- **Test Used**: Mann-Whitney U Test (non-parametric)
- **Libraries**:
  - `pingouin` – for a more readable statistical output
  - `scipy.stats` – for a standard implementation
- **Hypothesis**:
  - **Null Hypothesis (H₀)**: Women's matches do *not* have more total goals than men's.
  - **Alternative Hypothesis (H₁)**: Women's matches *do* have more total goals than men's.
- **Significance Level**: α = 0.01

---

## Visualization

A combined **boxplot + stripplot** is generated to visually compare goal distributions between men’s and women’s World Cup matches.

#### Example Output:
```
{'p-val': 0.0004, 'Result': 'Null Hypothesis Rejected'}
```

---

## Insights

If the **p-value is ≤ 0.01**, we reject the null hypothesis and conclude that **women's matches tend to have significantly more goals per match** than men's in the given period.

---

## Notes

- Only matches from **FIFA World Cup tournaments** after **January 1, 2002** are considered.
- The script uses `.copy()` during filtering to avoid `SettingWithCopyWarning`.
- The plot uses `hue='group'` with `palette='Set2'` to avoid future seaborn warnings.

---

## Author

**Nitin Yadav**  
_Data Analyst | Python Enthusiast
