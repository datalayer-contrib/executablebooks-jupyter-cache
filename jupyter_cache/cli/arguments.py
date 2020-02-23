import click

NB_PATH = click.argument(
    "nbpath",
    metavar="NBPATH",
    type=click.Path(dir_okay=False, exists=True, readable=True, resolve_path=True),
)

NB_PATHS = click.argument(
    "nbpaths",
    metavar="NBPATHS",
    nargs=-1,
    type=click.Path(dir_okay=False, exists=True, readable=True, resolve_path=True),
)

PK = click.argument("pk", metavar="PK", type=int)

PKS = click.argument("pks", metavar="PKs", nargs=-1, type=int)