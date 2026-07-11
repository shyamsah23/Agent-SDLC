from pathlib import Path


class FileTools:

    @staticmethod
    def create_file(
        path: str,
        content: str
    ):

        Path(path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        Path(path).write_text(
            content,
            encoding="utf-8"
        )

        print(
            f"Created: {path}"
        )