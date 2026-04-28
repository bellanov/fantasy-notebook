import marimo

__generated_with = "0.23.3"
app = marimo.App(width="medium")


@app.cell
def _():  # type: ignore
    import httpx
    import marimo as mo
    from dotenv import dotenv_values

    from notebooks.domain.environment import registry  # type: ignore

    return httpx, mo, registry


@app.cell
def _(registry):  # type: ignore
    ENV = registry.get_service(".env").get_config()
    return (ENV,)


@app.cell
def _(ENV, httpx):  # type: ignore
    sports = httpx.get(
        f"https://api.the-odds-api.com/v4/sports/?apiKey={ENV['THE_ODDS_API']}"
    ).json()
    sports
    return


@app.cell
def _(mo):  # type: ignore
    # TODO: Integrate TheOddsAPI and query for Sports data
    sport = mo.ui.dropdown(["ncaa", "nba", "nfl"], value="ncaa")
    return (sport,)


@app.cell
def _(mo, sport):  # type: ignore
    mo.md(f"""
    # Sports

    Notebook to study **Sports** data.

    **Sport**

    {sport}
    """)
    return


@app.cell
def _():  # type: ignore
    return


if __name__ == "__main__":
    app.run()
