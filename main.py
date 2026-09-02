import logging
import sys

from src.config import config
from src.converter import DocxConverter


def setup_logger() -> logging.Logger:
    """Настраивает форматированный логгер с выводом в консоль и в файл."""
    log_file = config.LOG_DIR / "parser.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(module)s | %(message)s",
        handlers=[logging.FileHandler(log_file, encoding="utf-8"), logging.StreamHandler(sys.stdout)],
    )
    return logging.getLogger("Pipeline")


def main() -> None:
    # 1. Инициализация инфраструктуры
    config.setup_directories()
    logger = setup_logger()
    logger.info("Запуск пайплайна конвертации DOCX -> MD")

    # 2. Инициализация конвертера
    converter = DocxConverter()

    # 3. Получение списка файлов (только .docx)
    files_to_process = list(config.INPUT_DIR.glob("*.docx"))

    if not files_to_process:
        logger.warning(f"Папка {config.INPUT_DIR} пуста. Завершение работы.")
        return

    logger.info(f"Найдено документов для обработки: {len(files_to_process)}")

    # 4. Пакетная обработка
    success_count = 0
    for input_file in files_to_process:
        output_file = config.OUTPUT_DIR / f"{input_file.stem}.md"

        is_success = converter.process_file(input_file, output_file)
        if is_success:
            success_count += 1

    # 5. Отчет
    logger.info("Пайплайн завершен.")
    logger.info(f"Успешно: {success_count} / {len(files_to_process)}. Ошибок: {len(files_to_process) - success_count}")


if __name__ == "__main__":
    main()
