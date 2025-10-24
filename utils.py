from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule
from rich.prompt import Prompt
from os.path import expanduser


console = Console()


def main_heading(title_name, description):
    styled_text = Text(description, justify="center", style="bold white on grey15")
    panel = Panel(
        styled_text,
        border_style="#13DAF9",
        padding=(1, 4),
        title=title_name,
        title_align="center",
    )
    console.print(panel)


def lined_input(input_prompt, default_option="eg: downloads"):
    console.print(Rule(style="#FCED1A"))
    input_text = Prompt.ask(f"{input_prompt}>>>", default=default_option)
    console.print(Rule(style="#FCED1A"))
    return input_text


def error_print(text, type="error"):
    
    if type == "warning":
        console.print(
            Panel(
                f"[bold #FB7A1D]{text}[/]",
                title="⚠️ Warning",
                border_style="#F8C733",
                title_align="left",
            )
        )
    else:
        console.print(
            Panel(
                f"[bold red]{text}[/]",
                title="❌ Error",
                border_style="red",
                title_align="left",
            )
        )

def lined_print(text,line_style="─", color="cyan"):
    console.print(Rule(f"[bold]{text}",style=color,align="center",characters=line_style))

def color_print(text, color="white"):
    console.print(f"[{color}]{text}")

def default_directory_paths():
    home_dir = expanduser("~")
    desktop_path = home_dir + "\\Desktop"
    downloads_path = home_dir + "\\Downloads"
    return desktop_path, downloads_path


def optional_input(
    input_text: str = "Your input here",
    options: list = ["op1", "op2"],
    default: str = "op1(say)",
    title: str = "options",
) -> str:
    option_text = "\n".join(
        f"[bold cyan]{i+1}.[/bold cyan] {option}" for i, option in enumerate(options)
    )
    console.print(
        Panel(option_text, title=title, subtitle=f"def: {default}", expand=False)
    )
    choice = Prompt.ask(input_text, default=default)
    return choice


if __name__ == "__main__":
    main_heading("Main Heading", "This is the description")
    lined_input("Thsi is input prompt", "this is suggestion")
    error_print("This is a warning", type="warning")
    error_print("This is an error", type="error")
    lined_print("This is a lined print", color="#8E16FF")
    color_print("This is colored print")
    desktop, download = default_directory_paths()
    print(desktop, download)
    print(optional_input())
