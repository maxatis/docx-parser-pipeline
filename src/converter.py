import logging
from pathlib import Path

from markitdown import MarkItDown

logger = logging.getLogger(__name__)


class DocumentConverter:
    def __init__(self) -> None:
        # Initialize engine
        self._engine = MarkItDown()

    def process_file(self, input_path: Path, output_path: Path) -> bool:
        allowed_extensions = {".docx", ".pdf"}
        if input_path.suffix.lower() not in allowed_extensions:
            logger.warning(f"Skipped file {input_path.name}: invalid extension.")
            return False

        try:
            logger.info(f"Starting conversion: {input_path.name}")

            # Parsing via MarkItDown
            result = self._engine.convert_local(str(input_path))

            # Save result
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result.text_content)

            logger.info(f"Successfully converted: {input_path.name} -> {output_path.name}")
            return True

        except Exception:
            logger.exception(f"Critical error during conversion of {input_path.name}")
            return False
