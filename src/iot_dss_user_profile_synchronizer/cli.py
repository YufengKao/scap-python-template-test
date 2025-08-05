"""Console script for iot_dss_user_profile_synchronizer."""

import typer
from rich.console import Console
import json

from iot_dss_user_profile_synchronizer import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for iot_dss_user_profile_synchronizer."""
    console.print("Replace this message by putting your code into "
               "iot_dss_user_profile_synchronizer.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()
if __name__ == "__main__":
    app()
