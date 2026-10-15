from rassler_py.generator import Generator


class Renderer:
    @staticmethod
    def render(generator: Generator, start: int, count: int) -> tuple[list[float], int]:
        return generator.generate_block(start, count)
