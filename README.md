# Demographic Multipliers Database — ACS 2018–2022

> A queryable MySQL + Python database of U.S. residential demographic multipliers built from American Community Survey (ACS) 2018–2022 data — how household size, age composition, school-age children (SAC) and public-school children (PSC) vary by housing type, tenure, year built, and home value, for every state.

## What this is

Demographic multipliers translate new housing into people: how many residents, by age group, and how many school children a given type of home is expected to generate. Planners, municipalities, and developers use them for fiscal impact analysis, school planning, and infrastructure decisions.

This repo contains the database (8 CSV tables), Python/MySQL query tools, SQL, a worked notebook (including 90% confidence-interval calculations), and the original construction documentation.

## The data — 8 tables

Each table: 46–48 variables, 1,000–5,900 rows, by state (`st`).

| File | Cut |
|---|---|
| `database_sel_typ.csv` | By unit type (SFD, SFA, multifamily…) |
| `database_sel_typ_yr.csv` | By unit type × year built (pre-2000 / 2000–2021) |
| `database_sel_ALLtyp.csv` | All unit types combined |
| `database_sel_ALLtyp_yr.csv` | All types × year built |
| `database_val_sel_typ_yr.csv` | By unit type × year built × value vs. median |
| `database_val_sel_ALLtyp_yr.csv` | All types × year built × value vs. median |
| `database_valTRC_sel_typ.csv` | By unit type × value tercile |
| `database_valTRC_sel_ALLtyp.csv` | All types × value tercile |

Variables include weighted/unweighted units, people, age bands (0–4, 5–17, 18–34, 35–44, 45–54, 55–64, 65–74, 75+), SAC and PSC by grade band (K–5, 6–8, 9–12). File naming and construction are documented in `docs/database-construction.docx`.

## Query tools (`src/`)

Interactive Python + MySQL scripts (credentials via environment variables — see `.env.example`):

- `query_by_unit_type.py` — units and age profile by unit type for a chosen state
- `query_by_tenure.py` — tenure cuts: units, people by age, SAC/PSC ingredients
- `query_by_year_built.py` — older vs. newer (2000–2021) housing comparisons
- `state_summary.py` — state-level totals across all cuts

Notebooks: `17_all_housing_units.ipynb` (queries + 90% CIs) and `DM_tables.ipynb` (the processing pipeline that builds the DM tables — population by age, SAC by grade — from the source workbooks). An early Streamlit + pydeck map app is in `app/streamlit_map_app.py`, and the project presentation *Multipliers and Municipalities* is in `docs/`.

Plus `notebooks/17_all_housing_units.ipynb` — housing-unit queries with demographic multiplier extraction and 90% confidence intervals, and example SQL in `sql/`.

## How to run

```bash
pip install -r requirements.txt
cp .env.example .env   # fill in your local MySQL credentials
# load any data/*.csv into a MySQL database named `demographics`, then:
python src/query_by_unit_type.py
```

## Credit

Demographic multipliers derived from ACS microdata by **Professor Alexandru Voicu, College of Staten Island (CUNY)**; database construction documented in `docs/`. Query tools, notebook, and this repository structure by **Umer Farooq** (Center for Urban Policy Research, Rutgers University). This work underpins the interactive [US Housing & Demographics Explorer](https://github.com/umerfarooq7424/Job-Sample-Code).

## Author

**Umer Farooq** — Economic & Climate Risk Analyst · [LinkedIn](https://www.linkedin.com/in/umer-farooq-gojra/) · [GitHub](https://github.com/umerfarooq7424)

## License

MIT — see LICENSE. ACS data is public (U.S. Census Bureau).
