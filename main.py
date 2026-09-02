import logging
import sys

from src.config import config
from src.converter import DocxConverter


def setup_logger() -> logging.Logger:
    """Configures a formatted logger outputting to console and file."""
    log_file = config.LOG_DIR / "parser.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(module)s | %(message)s",
        handlers=[logging.FileHandler(log_file, encoding="utf-8"), logging.StreamHandler(sys.stdout)],
    )
    return logging.getLogger("Pipeline")


def main() -> None:
    # 1. Initialize infrastructure
    config.setup_directories()
    logger = setup_logger()
    logger.info("Starting DOCX to MD conversion pipeline")

    # 2. Initialize converter
    converter = DocxConverter()

    # 3. Получение списка файлов (только .docx)
    files_to_process = list(config.INPUT_DIR.glob("*.docx"))

    if not files_to_process:
        logger.warning(f"Directory {config.INPUT_DIR} is empty. Exiting.")
        return

    logger.info(f"Found documents to process: {len(files_to_process)}")

    # 4. Batch processing
    success_count = 0
    for input_file in files_to_process:
        output_file = config.OUTPUT_DIR / f"{input_file.stem}.md"

        is_success = converter.process_file(input_file, output_file)
        if is_success:
            success_count += 1

    # 5. Report
    logger.info("Pipeline finished.")
    logger.info(f"Success: {success_count} / {len(files_to_process)}. Errors: {len(files_to_process) - success_count}")


if __name__ == "__main__":
    main()
