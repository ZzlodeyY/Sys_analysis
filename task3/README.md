# Задание

## Постановка задачи

Программа должна обработать JSON-строку, описывающую граф. На основе этой строки необходимо:  

1. Построить матрицу, содержащую количество различных типов связей управления для каждой вершины графа.  
2. Рассчитать энтропию системы, используя значения из полученной матрицы.  

---

## Входные данные

На вход программы подается JSON-строка, представляющая граф.  

Пример входных данных:  

```json
{
    "1": {
        "2": {
            "3": {
                "5": {},
                "6": {}
            },
            "4": {
                "7": {},
                "8": {}
            }
        }
    }
}