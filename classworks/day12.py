#<<<<<<<<<<<<<<mini library system>>>>>>>>
import re
def valid_book(book):
   return bool(re.fullmatch(r"[A-Za-z ]+", book))
def valid_year(year):
    return bool(re.fullmatch(r"(19|20)\d{2}", year))

def Validate():
    try:
        title = input(" Enter the book title: ").strip()
        if not valid_book(title):
            raise ValueError("Invalid title. Use only letters and spaces.")

        year = input("Enter the publication year (e.g., 2001): ").strip()
        if not valid_year(year):
            raise ValueError("Invalid year. Must be a 4-digit year starting with '19' or '20'.")
        print(f"\n Book accepted:Name of the book: '{title}'published on : ({year})")

    except ValueError as error:
        print(f"\n{error}")

    finally:
        print("\n Library system process completed.")
Validate()