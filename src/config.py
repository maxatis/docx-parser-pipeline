from pathlib import Path

from pydantic import BaseModel


class PipelineConfig(BaseModel):
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    INPUT_DIR: Path = BASE_DIR / "input_docs"
    OUTPUT_DIR: Path = BASE_DIR / "output_md"
    LOG_DIR: Path = BASE_DIR / "logs"

    def setup_directories(self) -> None:
        """Creates necessary directories if they do not exist."""
        self.INPUT_DIR.mkdir(parents=True, exist_ok=True)
        self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        self.LOG_DIR.mkdir(parents=True, exist_ok=True)


config = PipelineConfig()
