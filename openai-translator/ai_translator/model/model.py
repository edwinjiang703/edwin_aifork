from book import ContentType


class Model:
    def make_text_prompt(self, text: str, target_language: str) -> str:

        return f"请按照如下要求保持原文本里面内容的格式,保证原文本里面内容的排版,比如保持换行符,对齐方式等.  例如如下格式：  aaaaaaaaa   bbbbbbbbb \n  bbbbbbbb  ccccccccc  \n  vvvvvvvvvvvvvvvv   \n ccccccccccccccc   文本如下：{target_language}：{text}"

    def make_table_prompt(self, table: str, target_language: str) -> str:
        return f"翻译为{target_language}，保持间距（空格，分隔符），以表格形式返回：\n{table}"

    def translate_prompt(self, content, target_language: str) -> str:
        if content.content_type == ContentType.TEXT:
            return self.make_text_prompt(content.original, target_language)
        elif content.content_type == ContentType.TABLE:
            return self.make_table_prompt(content.get_original_as_str(), target_language)

    def make_request(self, prompt):
        raise NotImplementedError("子类必须实现 make_request 方法")
