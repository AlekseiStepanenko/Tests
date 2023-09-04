from unittest import TestCase
from main import search_popular_name, unique_names, duration_courses
from YD_API import create_folder
from Auth_Yandex import auth_yandex





class TestPopularName(TestCase):

    def test_accurate_result(self):
        name = [
            ["Игорь Шмаргунов", "Олег Булыгин", "Игорь Демидов", "Кирилл Табельский", "Игорь Ульянцев",
             "Роман Гордиенко"],
            ["Игорь Воронов", "Павел Дерендяев"],
            ["Игорь Нуруллин", "Олег Шек", "Максим Филипенко", "Елена Никитина"],
            ["Олег Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
        ]
        res = search_popular_name(name)
        expected = f'Игорь: 5 раз(а), Олег: 3 раз(а), Александр: 2 раз(а)'
        self.assertEquals(res,expected)

    def test_element_insertion(self):
        name = [
            ["Игорь Шмаргунов", "Олег Булыгин", "Игорь Демидов", "Кирилл Табельский", "Игорь Ульянцев",
             "Роман Гордиенко"],
            ["Игорь Воронов", "Павел Дерендяев"],
            ["Игорь Нуруллин", "Олег Шек", "Максим Филипенко", "Елена Никитина"],
            ["Олег Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
        ]
        res = search_popular_name(name)
        expected = 'Игорь'
        self.assertIn(expected, res)

class TestSearchUniqueNames(TestCase):

    def test_empty_value1(self):
        name = [
            ["Игорь Шмаргунов", "Олег Булыгин", "Игорь Демидов", "Кирилл Табельский", "Игорь Ульянцев",
             "Роман Гордиенко"],
            ["Игорь Воронов", "Павел Дерендяев"],
            ["Игорь Нуруллин", "Олег Шек", "Максим Филипенко", "Елена Никитина"],
            ["Олег Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
        ]
        res = unique_names(name)
        self.assertIsNotNone(res)


    def test_empty_value2(self):
        name = [
            ["Игорь Шмаргунов", "Олег Булыгин", "Игорь Демидов", "Кирилл Табельский", "Игорь Ульянцев",
             "Роман Гордиенко"],
            ["Игорь Воронов", "Павел Дерендяев"],
            ["Игорь Нуруллин", "Олег Шек", "Максим Филипенко", "Елена Никитина"],
            ["Олег Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
        ]
        res = unique_names(name)
        expected = 'Шмаргунов'
        self.assertNotIn(expected, res)

class TestDurationCourses(TestCase):
    def test_insertion_of_name(self):
        name = [
            ["Игорь Шмаргунов", "Олег Булыгин", "Игорь Демидов", "Кирилл Табельский", "Игорь Ульянцев",
             "Роман Гордиенко"],
            ["Игорь Воронов", "Павел Дерендяев"],
            ["Игорь Нуруллин", "Олег Шек", "Максим Филипенко", "Елена Никитина"],
            ["Олег Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
        ]
        a = 'Fullstack-разработчик на Python'
        res = duration_courses(name)
        self.assertIn(a, res)

class TestCreateFolder(TestCase):

    def test_status_code1(self):
        a = 201
        res = create_folder('Tes Folder', 'AAAAAAAA')
        self.assertEqual(a, res)

    def test_status_code2(self):
        a = 409
        res = create_folder('Test Folder', 'AAAAAA')
        self.assertEqual(a, res)

    def test_status_code3(self):
        a = 401
        res = create_folder('Test Folder', 'AA')
        self.assertEqual(a, res)

class TestAuthYandex(TestCase):
    def test_login(self):
        log = 'AAAA'
        pas = 'AAAA'
        res = auth_yandex(log, pas)
        self.assertIsNotNone(res)



