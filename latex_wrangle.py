import re
import uuid
from typing import Dict, List, Match, Any
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
from markdown import Markdown

class LatexPreprocessor(Preprocessor):
    def __init__(self) -> None:
        self.latex_blocks: Dict[str, str] = {}

    def run(self, lines: List[str]) -> List[str]:
        text = '\n'.join(lines)
        processed_text = self._process_latex(text)
        return processed_text.split('\n')

    def _process_latex(self, text: str) -> str:
        def replace_latex(match: Match[str]) -> str:
            placeholder: str = f'LATEXBLOCK{uuid.uuid4().hex}'
            self.latex_blocks[placeholder] = match.group(0)
            return placeholder

        # Replace display ($$...$$) LaTeX
        text = re.sub(r'\$\$((?:.|\n)+?)\$\$', replace_latex, text, flags=re.DOTALL)
        
        # Replace inline ($...$) LaTeX (single-line only) (note that this will not work for multi-line inline LaTeX)
        text = re.sub(r'\$([^$\n]+?)\$', replace_latex, text)
        
        return text

    def restore_latex(self, html: str) -> str:
        
        for placeholder, latex in self.latex_blocks.items():
            html = html.replace(placeholder, latex)
        
        return html

class LatexExtension(Extension):
    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        self.preprocessor: LatexPreprocessor = LatexPreprocessor()
        super().__init__(**kwargs)

    def extendMarkdown(self, md: Markdown) -> None:
        md.preprocessors.register(self.preprocessor, 'latex', 175)

    def restore_latex(self, html: str) -> str:
        return self.preprocessor.restore_latex(html)
