""" Populate the database with some data at the start of the application"""

from src.persistence.repository import Repository


def populate_db(repo: Repository) -> None:
    """Populates the db with a dummy country"""
    from src.models.country import Country

    countries = [
        Country(name="Uruguay", code="UY"),
        Country(name="Brazil", code="BR"),
        Country(name="Chile", code="CL"),
        Country(name="Paraguay", code="PY"),
        Country(name="Bolivia", code="BO"),
        Country(name="Peru", code="PE"),
        Country(name="Ecuador", code="EC"),
        Country(name="Colombia", code="CO"),
        Country(name="Venezuela", code="VE"),
        Country(name="Guyana", code="GY"), 
    ]

    for country in countries:
        repo.save(country)

    print("Memory DB populated")
