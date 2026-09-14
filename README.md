# ORD Airport Delays

A personal data science project analyzing and predicting flight delays at Chicago O'Hare International Airport (ORD), built as a way to explore the traveler experience side of aviation — delays, pricing, and passenger impact.

## Project Status

Work in progress. Currently at the exploratory data analysis stage; prediction model not yet built.

## What's Done So Far

- Loaded and cleaned BTS on-time performance data for ORD (June 2026, ~607K rows)
- Aggregated average departure delay by carrier
- Visualized carrier-level delay comparisons with Seaborn

## Roadmap

- [ ] Aggregate delays by day of week
- [ ] Define binary prediction target (delayed >15 min: yes/no)
- [ ] Feature engineering
- [ ] Baseline classification model (scikit-learn: Logistic Regression / Decision Tree)
- [ ] Evaluate with precision/recall metrics
- [ ] Build a Streamlit front-end
- [ ] Explore hosting options

## Data Source

This project uses the [Bureau of Transportation Statistics (BTS) Reporting Carrier On-Time Performance dataset](https://transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ), filtered to ORD.

**The raw data is not included in this repository.** To reproduce:
1. Download the June 2026 on-time performance data from BTS Transtats (Reporting Carrier On-Time Performance dataset).
2. Place the CSV in a `data/` folder at the project root.
3. Run `Main.py`.

## Setup

```bash
git clone https://github.com/<your-username>/ord-airport-delays.git
cd ord-airport-delays
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Tech Stack

- Python 3.12
- pandas
- matplotlib / seaborn
- scikit-learn (planned)
- Streamlit (planned)

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.