import sys, os
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1])) # Modify the path dynamically
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
