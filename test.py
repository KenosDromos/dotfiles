import logging
import functools

# Настройка логгера для записи в файл
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def dynamic_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Определяем информацию о вызывающем контексте
        func_name = func.__name__
        module_name = func.__module__
        class_name = func.__qualname__.split('.')[0] if '.' in func.__qualname__ else None

        # Создаем логгер с динамическим именем
        if class_name:
            logger_name = f"{module_name}.{class_name}.{func_name}"
        else:
            logger_name = f"{module_name}.{func_name}"

        logger = logging.getLogger(logger_name)
        
        # Логгирование перед вызовом функции
        logger.debug("Calling function/method")

        # Изменение поведения в зависимости от контекста
        if func_name == "special_function":
            logger.warning("Special handling for special_function")
        elif class_name == "SpecialClass":
            logger.warning("Special handling for SpecialClass")

        # Вызов функции
        result = func(*args, **kwargs)

        # Логгирование после вызова функции
        logger.info("Function/method completed")

        return result

    return wrapper

# Пример использования декоратора
@dynamic_logger
def example_function():
    print("Executing example_function")

class ExampleClass:
    @dynamic_logger
    def example_method(self):
        print("Executing example_method")

@dynamic_logger
def special_function():
    print("Executing special_function")

class SpecialClass:
    @dynamic_logger
    def special_method(self):
        print("Executing special_method")

# Тестовые вызовы
example_function()
ec = ExampleClass()
ec.example_method()
special_function()
sc = SpecialClass()
sc.special_method()
