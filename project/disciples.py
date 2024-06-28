from os import path
from typing import Optional
import csv


class Disciples:
    def __init__(self) -> None:
        self._name: Optional[str] = None
        self._disciple_type: Optional[str] = None
        self._level: Optional[str] = None
        self._profession: Optional[str] = None
        self._department: Optional[str] = None
        self._cultivation_law: Optional[str] = None

    def add_data(
        self,
        name: str,
        disciple_type: str,
        level: str,
        profession: str,
        department: str,
        cultivation_law: str,
    ) -> None:
        self._name = name
        self._disciple_type = disciple_type
        self._level = level
        self._profession = profession
        self._department = department
        self._cultivation_law = cultivation_law
        row = {
            "Name": self._name,
            "Disciple_type": self._disciple_type,
            "Level": self._level,
            "Profession": self._profession,
            "Department": self._department,
            "Cultivation_law": self._cultivation_law,
        }
        if path.isfile("disciples.csv"):
            with open("disciples.csv", "a") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=[
                        "Name",
                        "Disciple_type",
                        "Level",
                        "Profession",
                        "Department",
                        "Cultivation_law",
                    ],
                )
                writer.writerow(row)
        else:
            with open("disciples.csv", "a") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=[
                        "Name",
                        "Disciple_type",
                        "Level",
                        "Profession",
                        "Department",
                        "Cultivation_law",
                    ],
                )
                writer.writeheader()
                writer.writerow(row)

    @staticmethod
    def file_reader() -> list:
        with open("disciples.csv") as file:
            reader = csv.DictReader(file)
            table: list = []
            for row in reader:
                table.append(
                    {
                        "Name": row["Name"],
                        "Disciple_type": row["Disciple_type"],
                        "Level": row["Level"],
                        "Profession": row["Profession"],
                        "Department": row["Department"],
                        "Cultivation_law": row["Cultivation_law"],
                    }
                )
        return table

    # test function for unit testing
    def check_add_data(
        self,
        name: str,
        disciple_type: str,
        level: str,
        profession: str,
        department: str,
        cultivation_law: str,
    ) -> bool:
        self._name = name
        self._disciple_type = disciple_type
        self._level = level
        self._profession = profession
        self._department = department
        self._cultivation_law = cultivation_law

        if (
            not self._disciple_type in ["Outer", "Inner", "Core"]
            or not self._level
            in [
                "Qi refinement",
                "Body refinement",
                "Foundation establishment",
                "Core formation",
                "Nascent soul",
                "Soul transformation",
                "Mahayana",
                "Tribulation",
            ]
            or not self._profession
            in [
                "Alchemist",
                "Weapon master",
                "Blacksmith",
                "Formation master",
                "Array master",
                "Tailsman master",
                "Pure combat",
                "Warrior",
            ]
            or not self._department
            in [
                "Alchemy",
                "Weapons",
                "Array",
                "Tailsman",
                "Combat",
            ]
        ):
            return False

        else:
            row = {
                "Name": self._name,
                "Disciple_type": self._disciple_type,
                "Level": self._level,
                "Profession": self._profession,
                "Department": self._department,
                "Cultivation_law": self._cultivation_law,
            }
            with open("test_disciples.csv", "a") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=[
                        "Name",
                        "Disciple_type",
                        "Level",
                        "Profession",
                        "Department",
                        "Cultivation_law",
                    ],
                )
                writer.writeheader()
                writer.writerow(row)
            return True

    # test function for unit testing
    @staticmethod
    def check_file_reader() -> list:
        with open("test_disciples.csv") as file:
            reader = csv.DictReader(file)
            table: list = []
            for row in reader:
                table.append(
                    {
                        "Name": row["Name"],
                        "Disciple_type": row["Disciple_type"],
                        "Level": row["Level"],
                        "Profession": row["Profession"],
                        "Department": row["Department"],
                        "Cultivation_law": row["Cultivation_law"],
                    }
                )
        return table
