"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Telegram Hq Builder."""


if __name__ == "__main__":
    main(prog_name="telegram-hq-builder")  # pragma: no cover
