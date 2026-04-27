import marimo

__generated_with = "0.23.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    # TODO: Integrate TheOddsAPI and query for Sports data
    sport = mo.ui.dropdown(["ncaa", "nba", "nfl"], value="ncaa")
    return (sport,)


@app.cell
def _(mo, sport):
    mo.md(f"""
    # Sports

    Notebook to study **Sports** data.

    **Sport**

    {sport}

    """)
    return


if __name__ == "__main__":
    app.run()
