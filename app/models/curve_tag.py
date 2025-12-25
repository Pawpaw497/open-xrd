from matplotlib import color_sequences

built_in_color_sequences = [
    'tab10', 'tab20', 'tab20b', 'tab20c', 'Pastel1', 'Pastel2', 'Paired',
    'Accent', 'Dark2', 'Set1', 'Set2', 'Set3', 'petroff10']

built_in_colors = []
for s in built_in_color_sequences:
    built_in_colors.extend(color_sequences[s])


class CurveTag:
    def __init__(self, tag_name: str) -> None:
        self.tag_name = tag_name


class CurveTagManager:
    def __init__(self, default_tags: list[CurveTag] = []) -> None:
        self.tags = default_tags

    def get_style(self, tag_or_str):
        if isinstance(tag_or_str, CurveTag):
            tag = tag_or_str
        else:
            tag = CurveTag(tag_or_str)

        if tag in self.tags:
            return self.tags[tag]
        else:
            return None

    def add_tag(self, tag_name: str):
        new_tag = CurveTag(tag_name)
        self.tags.append(new_tag)


default_tags = [


]

curve_tag_manager = CurveTagManager()
