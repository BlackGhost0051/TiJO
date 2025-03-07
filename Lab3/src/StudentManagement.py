class StudentManagement:
    """
    Klasa zarzadzajaca studentami i ich ocenami.
    """

    def __init__(self):
        self.students = {}
        self.grades = {}

    def add_student(self, id: str, name: str, age: int) -> bool:
        """
        Dodaje nowego studenta do bazy danych.

        Args:
            name: Imie studenta.
            age: Wiek studenta.
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli dodanie zakonczylo sie sukcesem.
            False w przeciwnym wypadku.
        """
        if id in self.students:
            return False
        self.students[id] = {"name": name, "age": age}
        self.grades[id] = {}
        return True


    def update_student(self, id: str, name: str, age: int) -> bool:
        """
        Aktualizuje dane istniejacego studenta na podstawie identyfikatora.

        Args:
            name: Imie studenta.
            age: Wiek studenta.
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli aktualizacja zakonczyla sie sukcesem.
            False w przeciwnym wypadku.
        """
        if id not in self.students:
            return False
        self.students[id] = {"name": name, "age": age}
        return True

    def remove_student(self, id: str) -> bool:
        """
        Usuwa studenta z bazy danych na podstawie jego identyfikatora.

        Args:
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli usuniecie zakonczylo sie sukcesem.
            False w przeciwnym wypadku.
        """
        if id in self.students:
            del self.students[id]
            del self.grades[id]
            return True
        return False

    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        """
        Dodaje ocene z danego przedmiotu dla okreslonego studenta.

        Args:
            student_id: Unikalny identyfikator studenta.
            subject: Nazwa przedmiotu.
            grade: Ocena.

        Returns:
            True, jesli dodanie oceny zakonczylo sie sukcesem (2.0, 3.0, 3.5, 4.0, 4.5, 5.0),
            False w przeciwnym razie.
        """
        valid_grades = {2.0, 3.0, 3.5, 4.0, 4.5, 5.0}
        if student_id not in self.students or grade not in valid_grades:
            return False

        if subject not in self.grades[student_id]:
            self.grades[student_id][subject] = []

        self.grades[student_id][subject].append(grade)
        return True

    def avg_grades(self, subject: str) -> float:
        """
        Oblicza srednia ocen z danego przedmiotu dla wszystkich studentow.

        Args:
            subject: Nazwa przedmiotu.

        Returns:
            Srednia ocen z przedmiotu jako liczba zmiennoprzecinkowa.
        """
        all_grades = []

        for student_id in self.grades:
            if subject in self.grades[student_id]:
                all_grades.extend(self.grades[student_id][subject])

        if not all_grades:
            return 0.0

        return sum(all_grades) / len(all_grades)\

    def avg_all_grades(self, student_id: str) -> float:
        all_grades = []

        for subject in self.grades[student_id]:
            all_grades.extend(self.grades[student_id][subject])

        if not all_grades:
            return 0.0

        return sum(all_grades) / len(all_grades)