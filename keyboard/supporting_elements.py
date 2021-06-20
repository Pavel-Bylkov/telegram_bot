from .common import keyboard, answer, get_keyboard

keyboard = {**keyboard, **{

    '/Несущие элементы/': get_keyboard(['Капитальные стены',
                                        'Фундаменты',
                                        'Перекрытия',
                                        'Покрытие',
                                        'Перемычки',
                                        'Подвал',
                                        'Система стропил']),
    '/Несущие элементы/Капитальные стены/': get_keyboard(['Материал',
                                                          'Толщина кладки наружных стен',
                                                          'Система перевязки',
                                                          'Наличие карнизов']),
    '/Несущие элементы/Капитальные стены/Материал/': get_keyboard(['Камень',
                                                                'Кирпич',
                                                                'Блоки',
                                                                'Дерево',
                                                                'Другое',]),
    '/Несущие элементы/Капитальные стены/Материал/Кирпич/': get_keyboard(['Система кладки']),
    '/Несущие элементы/Капитальные стены/Материал/Кирпич/Система кладки/': get_keyboard(['Рядовая', 'Нет']),
     '/Несущие элементы/Капитальные стены/Материал/Блоки/': get_keyboard(['Система кладки']),
    '/Несущие элементы/Капитальные стены/Материал/Блоки/Система кладки/': get_keyboard(['Рядовая', 'Нет']),
    '/Несущие элементы/Капитальные стены/Толщина кладки наружных стен/': get_keyboard(['Без учета отделки', 'С учетом отделки']),
    '/Несущие элементы/Капитальные стены/Система перевязки/': get_keyboard(['Однорядная', 'Нет']),
    '/Несущие элементы/Капитальные стены/Наличие карнизов/': get_keyboard(['Нет', 'Да']),
    '/Несущие элементы/Капитальные стены/Наличие карнизов/Да/': get_keyboard(['Размер вылета', 'Каким образом сделаны?']),
    '/Несущие элементы/Фундаменты/': get_keyboard(['Ленточные', 'Другое']),
    '/Несущие элементы/Фундаменты/Ленточные/': get_keyboard(['Из чего выполнены?']),
    '/Несущие элементы/Фундаменты/Ленточные/Из чего выполнены?/': get_keyboard(['Бутовая кладка', 'Другое']),
    '/Несущие элементы/Перекрытия/': get_keyboard(['Деревянные', 'Бетонные']),
    '/Несущие элементы/Перекрытия/Деревянные/': get_keyboard(['Опирание']),
    '/Несущие элементы/Перекрытия/Бетонные/': get_keyboard(['Опирание']),
    '/Несущие элементы/Перекрытия/Деревянные/Опирание/': get_keyboard(['На наружные и внутренние стены', 'Свой вариант']),
    '/Несущие элементы/Перекрытия/Бетонные/Опирание/': get_keyboard(['На наружные и внутренние стены', 'Свой вариант']),
    '/Несущие элементы/Покрытие/': get_keyboard(['Деревянная стропильная система', 'Свой вариант']),
    '/Несущие элементы/Перемычки/': get_keyboard(['Стальные', 'Деревянные']),
    '/Несущие элементы/Подвал/': get_keyboard(['Наличие колонн', 'Материал стен', 'Материал отделки', 'Перекрытие', 'Полы']),
    '/Несущие элементы/Подвал/Наличие колонн/': get_keyboard(['Нет', 'Да']),
    '/Несущие элементы/Подвал/Перекрытие/': get_keyboard(['Деревянное', 'Другое']),
    '/Несущие элементы/Подвал/Перекрытие/Деревянное/': get_keyboard(['Опирание']),
    '/Несущие элементы/Подвал/Наличие колонн/Перекрытие/Другое/': get_keyboard(['Опирание']),
    '/Несущие элементы/Подвал/Полы/': get_keyboard(['Цементная стяжка', 'Плитка', 'Другое']),
    '/Несущие элементы/Система стропил/': get_keyboard(['Деревянная стропильная система', 'Шаг стропил', 'Другое', 'Нет']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/': get_keyboard(['Материал ног',
                                                                                       'Мауэрлат',
                                                                                       'Стойки',
                                                                                       'Раскосы',
                                                                                       'Ригель',
                                                                                       'Затяжка',
                                                                                       'Накостная нога вальмы',
                                                                                       'Кобылки',
                                                                                       'Обрешетка']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Материал ног/': get_keyboard(['Бревно', 'Доска', 'Брус']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Материал ног/Доска/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Материал ног/Брус/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Мауэрлат/': get_keyboard(['Материал',
                                                                                                'Состояние',
                                                                                                'Влажность',
                                                                                                'Крепление к стене',
                                                                                                'Гидроизоляция',
                                                                                                'Шаг']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Мауэрлат/Материал/': get_keyboard(['Бревно', 'Доска', 'Брус']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Мауэрлат/Материал/Доска/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Мауэрлат/Материал/Брус/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Мауэрлат/Влажность/': get_keyboard(['Показатель', 'Фото с прибором']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Мауэрлат/Крепление к стене/': get_keyboard(['Скоба', 'Проволока', 'Анкер', 'Другое']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Мауэрлат/Гидроизоляция/': get_keyboard(['Да', 'Нет']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Мауэрлат/Гидроизоляция/Да/': get_keyboard(['Обмазочная', 'Рулонная']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Стойки/': get_keyboard(['Бревно', 'Доска', 'Брус', 'Шаг']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Стойки/Доска/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Стойки/Брус/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Раскосы/': get_keyboard(['Нет', 'Да']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Раскосы/Да/':  get_keyboard(['Бревно', 'Доска', 'Брус']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Раскосы/Да/Бревно/':  get_keyboard(['Бревно', 'Доска', 'Брус']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Раскосы/Да/Доска/':  get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Раскосы/Да/Брус/':  get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Ригель/': get_keyboard(['Верхний', 'Нижний']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Ригель/Верхний/': get_keyboard(['Бревно', 'Доска', 'Брус']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Ригель/Верхний/Доска/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Ригель/Верхний/Брус/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Ригель/Нижний/': get_keyboard(['Бревно', 'Доска', 'Брус']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Ригель/Нижний/Доска/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Ригель/Нижний/Брус/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Затяжка/': get_keyboard(['Нет', 'Да']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Затяжка/Да/': get_keyboard(['Материал', 'Размеры']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Затяжка/Да/Материал/': get_keyboard(['Металл', 'Трос', 'Полоса', 'Другое']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Затяжка/Да/Размеры/': get_keyboard(['Ширина', 'Высота', 'Длина', 'Диаметр']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Накостная нога вальмы/': get_keyboard(['Нет', 'Да']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Накостная нога вальмы/Да/': get_keyboard(['Бревно', 'Доска', 'Брус']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Накостная нога вальмы/Да/Доска/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Накостная нога вальмы/Да/Брус/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Кобылки/': get_keyboard(['Нет', 'Да']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Обрешетка/': get_keyboard(['Доска', 'Брус', 'Шаг', 'Наличие в коньке']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Обрешетка/Доска/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Обрешетка/Брус/': get_keyboard(['Ширина', 'Высота']),
    '/Несущие элементы/Система стропил/Деревянная стропильная система/Обрешетка/Наличие в коньке/': get_keyboard(['Да', 'Нет']),

}}