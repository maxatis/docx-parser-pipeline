import logging
from pathlib import Path

from markitdown import MarkItDown

logger = logging.getLogger(__name__)


class DocxConverter:
    def __init__(self) -> None:
        # Инициализируем движок
        self._engine = MarkItDown()

    def process_file(self, input_path: Path, output_path: Path) -> bool:
        """
        Конвертирует один файл с перехватом всех возможных исключений.
        Возвращает True в случае успеха, False при ошибке.
        """
        if input_path.suffix.lower() != ".docx":
            logger.warning(f"Пропущен файл {input_path.name}: неверное расширение.")
            return False

        try:
            logger.info(f"Начало конвертации: {input_path.name}")

            # Парсинг через MarkItDown
            result = self._engine.convert_local(str(input_path))

            # Сохранение результата
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result.text_content)

            logger.info(f"Успешно конвертирован: {input_path.name} -> {output_path.name}")
            return True

        except Exception:
            logger.exception(f"Критическая ошибка при конвертации {input_path.name}")
            return False
