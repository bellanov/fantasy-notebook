import marimo

__generated_with = "0.23.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import httpx
    import marimo as mo

    from dotenv import dotenv_values
    from notebooks.domain.environment import registry

    return httpx, mo, registry


@app.cell
def _(registry):
    # Define Global Variables
    ENV = registry.get_service(".env").get_config()
    return (ENV,)


@app.cell
def _(ENV, httpx, mo):
    # Define UI Elements
    sports = httpx.get(f"https://api.the-odds-api.com/v4/sports/?apiKey={ENV['THE_ODDS_API']}").json()

    sports_ui_options = [sport["group"] for sport in sports]
    leagues_ui_options = [sport["key"] for sport in sports]

    sport = mo.ui.dropdown(sports_ui_options, value=f"{sports_ui_options[0]}")
    league = mo.ui.dropdown(leagues_ui_options, value=f"{leagues_ui_options[0]}")

    return league, sport


@app.cell
def _(league, mo, sport):
    mo.md(f"""
    # Sports

    Notebook to study **Sports** data.


    | Sport   |  League  |
    | :----   | :------- |
    | {sport} | {league} |

    """)
    return


@app.cell
def _(league, sport):
    sport.value, league.value
    return


if __name__ == "__main__":
    app.run()
