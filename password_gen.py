import random
import string
import pyperclip
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

console = Console()

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        console.print("[red]Error: You must select at least one character type![/red]")
        return None

    # Ensure security rules
    if length < 8:
        console.print("[yellow]Warning: Password length is less than 8 (less secure).[/yellow]")

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    console.print(Panel.fit("🔐 [bold cyan]Random Password Generator[/bold cyan] 🔐", style="bold green"))

    try:
        length = int(Prompt.ask("[bold white]Enter password length[/bold white]", default="12"))
    except ValueError:
        console.print("[red]Invalid number![/red]")
        return

    use_upper = Confirm.ask("Include uppercase letters? (A-Z)")
    use_lower = Confirm.ask("Include lowercase letters? (a-z)")
    use_digits = Confirm.ask("Include numbers? (0-9)")
    use_symbols = Confirm.ask("Include symbols? (!@#$ etc.)")

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    if password:
        console.print(Panel.fit(f"[bold green]Generated Password:[/bold green] [bold yellow]{password}[/bold yellow]", title="Success"))
        pyperclip.copy(password)
        console.print("[cyan]Password copied to clipboard![/cyan]")

if __name__ == "__main__":
    main()
